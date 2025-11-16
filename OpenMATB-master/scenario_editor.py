"""Simple GUI editor for OpenMATB scenario files with run support."""
from __future__ import annotations

import configparser
import queue
import subprocess
import sys
import threading
from collections.abc import Callable
from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

import markdown
from tkinterweb import HtmlFrame


class MarkdownViewer(ttk.Frame):
    """Simple markdown viewer with toggle buttons."""

    def __init__(
        self,
        master: tk.Misc,
        documents: dict[str, Path],
        status_callback: Callable[[str], None] | None = None,
    ) -> None:
        super().__init__(master, padding=(10, 10, 10, 10))
        self.documents = documents
        self.status_callback = status_callback
        self.current_key: str | None = None
        self.buttons: dict[str, ttk.Button] = {}

        control_frame = ttk.Frame(self)
        control_frame.pack(fill=tk.X, pady=(0, 10))

        for key in documents.keys():
            btn = ttk.Button(control_frame, text=key, command=lambda k=key: self.toggle_document(k))
            btn.pack(side=tk.LEFT, padx=4)
            self.buttons[key] = btn

        ttk.Button(control_frame, text="关闭", command=self.close_document).pack(side=tk.LEFT, padx=4)

        self.html_widget = HtmlFrame(self, horizontal_scrollbar="auto")
        self.html_widget.pack(fill=tk.BOTH, expand=True)
        self._set_html("<p>请选择一个任务文档。</p>")

    def toggle_document(self, key: str) -> None:
        if self.current_key == key:
            self.close_document()
        else:
            self.open_document(key)

    def open_document(self, key: str) -> None:
        path = self.documents.get(key)
        if not path or not path.exists():
            self._set_html(f"<p>未找到文档：{key}</p>")
            self.current_key = None
            self._notify(f"未找到 {key} 文档")
            return

        text = path.read_text(encoding="utf-8")
        html_body = markdown.markdown(text, extensions=["fenced_code", "tables"])
        html = f"<h2>{key}</h2>{html_body}"
        self._set_html(html)
        self.current_key = key
        self._notify(f"已打开 {key} 文档")
        self._update_button_states()

    def close_document(self) -> None:
        if not self.current_key:
            return
        self.current_key = None
        self._set_html("<p>文档已关闭。</p>")
        self._notify("文档已关闭")
        self._update_button_states()

    def _set_html(self, body_html: str) -> None:
        styles = """
            <style>
            body { font-family: 'Segoe UI', 'Microsoft YaHei', Arial, sans-serif; margin: 16px; }
            h1, h2, h3 { margin-top: 0; }
            table { border-collapse: collapse; width: 100%; margin-top: 12px; }
            th, td { border: 1px solid #999; padding: 6px 10px; text-align: left; }
            th { background-color: #f5f5f5; }
            code { background-color: #f0f0f0; padding: 2px 4px; border-radius: 4px; }
            pre { background-color: #272822; color: #f8f8f2; padding: 10px; border-radius: 6px; overflow-x: auto; }
            </style>
        """
        html = f"<html><head>{styles}</head><body>{body_html}</body></html>"
        self.html_widget.load_html(html)

    def _notify(self, message: str) -> None:
        if self.status_callback:
            self.status_callback(message)

    def _update_button_states(self) -> None:
        for key, btn in self.buttons.items():
            if key == self.current_key:
                btn.state(["pressed"])
            else:
                btn.state(["!pressed"])


class ScenarioEditorApp:
    """Tkinter-based editor for MATB scenario files."""

    def __init__(self) -> None:
        self.root_dir = Path(__file__).resolve().parent
        self.config_path = self.root_dir / "config.ini"
        self.scenario_dir = (self.root_dir / "includes" / "scenarios").resolve()
        self.docs_dir = (self.root_dir / "docs" / "tasks").resolve()
        self.docs_dir.mkdir(parents=True, exist_ok=True)
        self.doc_map = {
            "SYSMON": self.docs_dir / "SYSMON.md",
            "TARACK": self.docs_dir / "TARACK.md",
            "COM": self.docs_dir / "COM.md",
            "RESMAN": self.docs_dir / "RESMAN.md",
        }

        self.root = tk.Tk()
        self.root.title("OpenMATB Scenario Editor")
        self.root.geometry("1100x700")

        self.path_var = tk.StringVar()
        self.status_var = tk.StringVar(value="就绪")

        self.config = configparser.ConfigParser()
        self.config.optionxform = str  # 保留原有大小写
        self.current_file: Path | None = None
        self.scenario_rel_path = "default.txt"
        self.process: subprocess.Popen[str] | None = None
        self.output_queue: queue.Queue[str] = queue.Queue()
        self.dirty = False

        self._load_config()
        self._build_ui()
        self._bind_events()
        self._load_current_file()
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    # ------------------------------------------------------------------
    # UI construction
    def _build_ui(self) -> None:
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.editor_tab = ttk.Frame(self.notebook)
        self.docs_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.editor_tab, text="场景编辑器")
        self.notebook.add(self.docs_tab, text="任务文档")

        self._build_editor_tab()
        self._build_docs_tab()

    def _build_editor_tab(self) -> None:
        toolbar = ttk.Frame(self.editor_tab, padding=(10, 10, 10, 5))
        toolbar.pack(fill=tk.X)

        ttk.Label(toolbar, text="场景文件:").pack(side=tk.LEFT)
        path_entry = ttk.Entry(toolbar, textvariable=self.path_var, width=80, state="readonly")
        path_entry.pack(side=tk.LEFT, padx=6)

        ttk.Button(toolbar, text="打开...", command=self._choose_file).pack(side=tk.LEFT)
        ttk.Button(toolbar, text="保存", command=self._save_file).pack(side=tk.LEFT, padx=4)
        ttk.Button(toolbar, text="另存为...", command=self._save_as).pack(side=tk.LEFT)
        ttk.Button(toolbar, text="设为当前场景", command=self._set_active_scenario).pack(side=tk.LEFT, padx=4)
        ttk.Button(toolbar, text="重新加载", command=self._reload_file).pack(side=tk.LEFT)

        editor_frame = ttk.Frame(self.editor_tab, padding=(10, 0, 10, 5))
        editor_frame.pack(fill=tk.BOTH, expand=True)

        self.text_widget = tk.Text(editor_frame, wrap=tk.NONE, undo=True, font=("Consolas", 11))
        y_scroll = ttk.Scrollbar(editor_frame, orient=tk.VERTICAL, command=self.text_widget.yview)
        x_scroll = ttk.Scrollbar(editor_frame, orient=tk.HORIZONTAL, command=self.text_widget.xview)
        self.text_widget.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

        self.text_widget.grid(row=0, column=0, sticky="nsew")
        y_scroll.grid(row=0, column=1, sticky="ns")
        x_scroll.grid(row=1, column=0, sticky="ew")
        editor_frame.columnconfigure(0, weight=1)
        editor_frame.rowconfigure(0, weight=1)

        output_frame = ttk.LabelFrame(self.editor_tab, text="运行输出", padding=(10, 5))
        output_frame.pack(fill=tk.BOTH, expand=False, padx=10, pady=(0, 10))

        self.output_text = tk.Text(output_frame, height=10, state="disabled", font=("Consolas", 10))
        output_scroll = ttk.Scrollbar(output_frame, orient=tk.VERTICAL, command=self.output_text.yview)
        self.output_text.configure(yscrollcommand=output_scroll.set)
        self.output_text.grid(row=0, column=0, sticky="nsew")
        output_scroll.grid(row=0, column=1, sticky="ns")
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)

        action_frame = ttk.Frame(self.editor_tab, padding=(10, 0, 10, 10))
        action_frame.pack(fill=tk.X)

        ttk.Button(action_frame, text="启动 OpenMATB", command=self._run_matb).pack(side=tk.LEFT)
        ttk.Button(action_frame, text="停止", command=self._stop_matb).pack(side=tk.LEFT, padx=6)

        ttk.Label(action_frame, textvariable=self.status_var).pack(side=tk.RIGHT)

    def _build_docs_tab(self) -> None:
        viewer = MarkdownViewer(
            self.docs_tab,
            documents=self.doc_map,
            status_callback=self._update_status,
        )
        viewer.pack(fill=tk.BOTH, expand=True)
        self.markdown_viewer = viewer

    def _bind_events(self) -> None:
        self.text_widget.bind("<<Modified>>", self._on_text_modified)

    # ------------------------------------------------------------------
    # File handling
    def _load_config(self) -> None:
        if not self.config_path.exists():
            messagebox.showerror("缺少配置", f"未找到 config.ini ({self.config_path})")
            self.root.destroy()
            sys.exit(1)

        self.config.read(self.config_path, encoding="utf-8")
        section = self.config.get("Openmatb", "scenario_path", fallback="default.txt")
        self.scenario_rel_path = section
        try:
            resolved = self._resolve_scenario_path(section)
        except FileNotFoundError:
            resolved = (self.scenario_dir / section).resolve()
        self.current_file = resolved
        self.path_var.set(str(self.current_file))

    def _load_current_file(self) -> None:
        if not self.current_file:
            return
        try:
            text = self.current_file.read_text(encoding="utf-8")
        except FileNotFoundError:
            text = ""
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert("1.0", text)
        self.text_widget.edit_modified(False)
        self.dirty = False
        self._update_status(f"已加载 {self.current_file}")
        self.path_var.set(str(self.current_file))

    def _reload_file(self) -> None:
        if self.dirty and not self._confirm_discard_changes():
            return
        self._load_current_file()

    def _choose_file(self) -> None:
        initial_dir = self.current_file.parent if self.current_file else self.scenario_dir
        file_path = filedialog.askopenfilename(
            title="选择场景文件",
            initialdir=initial_dir,
            filetypes=[("Text", "*.txt"), ("All files", "*.*")],
        )
        if not file_path:
            return
        new_path = Path(file_path).resolve()
        self.current_file = new_path
        self.scenario_rel_path = self._relative_scenario_path(new_path)
        self._load_current_file()

    def _save_file(self) -> None:
        if not self.current_file:
            self._save_as()
            return
        text = self.text_widget.get("1.0", tk.END)
        if not self._validate_content(text):
            if not messagebox.askyesno("确认保存", "内容可能存在格式问题，仍要保存吗？"):
                return
        self.current_file.write_text(text.rstrip() + "\n", encoding="utf-8")
        self.dirty = False
        self.text_widget.edit_modified(False)
        self._update_status("已保存")

    def _save_as(self) -> None:
        initial_dir = self.current_file.parent if self.current_file else self.scenario_dir
        file_path = filedialog.asksaveasfilename(
            title="另存为",
            defaultextension=".txt",
            initialdir=initial_dir,
            filetypes=[("Text", "*.txt"), ("All files", "*.*")],
        )
        if not file_path:
            return
        self.current_file = Path(file_path)
        self.scenario_rel_path = self._relative_scenario_path(self.current_file)
        self._save_file()

    def _set_active_scenario(self) -> None:
        if not self.current_file:
            return
        rel = self._relative_scenario_path(self.current_file)
        self.config.set("Openmatb", "scenario_path", rel)
        with self.config_path.open("w", encoding="utf-8") as config_file:
            self.config.write(config_file, space_around_delimiters=False)
        self._update_status(f"已将 {rel} 设置为当前场景")

    # ------------------------------------------------------------------
    # Validation helpers
    def _validate_content(self, text: str) -> bool:
        lines = [line for line in text.splitlines() if line.strip() and not line.strip().startswith("#")]
        for number, line in enumerate(lines, start=1):
            if ";" not in line:
                return False
        return True

    def _confirm_discard_changes(self) -> bool:
        if not self.dirty:
            return True
        return messagebox.askyesno("丢弃修改", "当前修改尚未保存，确定要丢弃吗？")

    def _relative_scenario_path(self, path: Path) -> str:
        try:
            rel = path.relative_to(self.scenario_dir)
            return rel.as_posix()
        except ValueError:
            return str(path)

    def _resolve_scenario_path(self, value: str) -> Path:
        candidate = Path(value)
        if candidate.is_absolute() and candidate.exists():
            return candidate
        relative_candidate = (self.scenario_dir / value).resolve()
        if relative_candidate.exists():
            return relative_candidate
        raise FileNotFoundError(value)

    # ------------------------------------------------------------------
    # Text change handling
    def _on_text_modified(self, event: tk.Event) -> None:  # type: ignore[override]
        if self.text_widget.edit_modified():
            self.dirty = True
            self._update_status("已修改，记得保存")
            self.text_widget.edit_modified(False)

    def _update_status(self, message: str) -> None:
        self.status_var.set(message)

    # ------------------------------------------------------------------
    # Running OpenMATB
    def _run_matb(self) -> None:
        if self.process and self.process.poll() is None:
            messagebox.showinfo("已在运行", "OpenMATB 已经在运行中。")
            return
        if self.dirty:
            save = messagebox.askyesno("保存修改", "运行前需要保存修改，是否立即保存？")
            if save:
                self._save_file()
            else:
                return
        self._set_active_scenario()

        command = [sys.executable, "main.py"]
        try:
            self.process = subprocess.Popen(
                command,
                cwd=self.root_dir,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
            )
        except FileNotFoundError as exc:
            messagebox.showerror("启动失败", f"无法运行 main.py: {exc}")
            return

        self._append_output("===== OpenMATB started =====\n")
        threading.Thread(target=self._pipe_output, daemon=True).start()
        self.root.after(100, self._drain_output)
        self._update_status("OpenMATB 运行中…")

    def _stop_matb(self) -> None:
        if not self.process or self.process.poll() is not None:
            self._update_status("没有正在运行的进程")
            return
        self.process.terminate()
        self.process.wait(timeout=5)
        self._append_output("===== OpenMATB terminated by user =====\n")
        self._update_status("OpenMATB 已停止")

    def _pipe_output(self) -> None:
        if not self.process or not self.process.stdout:
            return
        for line in self.process.stdout:
            self.output_queue.put(line)
        self.process = None
        self.output_queue.put("===== OpenMATB finished =====\n")

    def _drain_output(self) -> None:
        updated = False
        while not self.output_queue.empty():
            line = self.output_queue.get()
            self._append_output(line)
            updated = True
        if self.process:
            self.root.after(200, self._drain_output)
        elif updated:
            self._update_status("OpenMATB 已结束")

    def _append_output(self, text: str) -> None:
        self.output_text.configure(state="normal")
        self.output_text.insert(tk.END, text)
        self.output_text.see(tk.END)
        self.output_text.configure(state="disabled")

    # ------------------------------------------------------------------
    def _on_close(self) -> None:
        if not self._confirm_discard_changes():
            return
        if self.process and self.process.poll() is None:
            if not messagebox.askyesno("退出", "OpenMATB 仍在运行，确认要退出并终止它吗？"):
                return
            self._stop_matb()
        self.root.destroy()

    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    app = ScenarioEditorApp()
    app.run()


if __name__ == "__main__":
    main()
