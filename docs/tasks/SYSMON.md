
## sysmon（系统监控任务）

|参数|描述|可能值|默认值|示例|
|:----|:----|:----|:----|:----|
|title|任务标题，插件可见时显示|字符串|System monitoring|`title;System Check`|
|taskplacement|任务在3x2画布中的位置|`topleft`, `topmid`, `topright`, `bottomleft`, `bottommid`, `bottomright`, `fullscreen`|topleft|`taskplacement;topright`|
|taskupdatetime|插件更新间隔（毫秒）|正整数|200|`taskupdatetime;250`|
|alerttimeout|故障最大持续时间（毫秒）|正整数|10000|`alerttimeout;15000`|
|automaticsolver|是否自动纠正故障|布尔值|False|`automaticsolver;True`|
|automaticsolverdelay|自动纠正延迟（毫秒）|正整数|1000|`automaticsolverdelay;1500`|
|displayautomationstate|是否显示当前自动化状态|布尔值|True|`displayautomationstate;False`|
|allowanykey|是否允许使用任何系统监控键|布尔值|False|`allowanykey;True`|
|feedbackduration|反馈持续时间（毫秒）|正整数|1500|`feedbackduration;2000`|
|feedbacks-positive-active|是否启用正确响应的正反馈|布尔值|True|`feedbacks-positive-active;False`|
|feedbacks-positive-color|正反馈颜色|`white`, `black`, `green`, `red`, `background`, `lightgrey`, `grey`, `blue`|green|`feedbacks-positive-color;white`|
|feedbacks-negative-active|是否启用错误响应的负反馈|布尔值|True|`feedbacks-negative-active;False`|
|feedbacks-negative-color|负反馈颜色|`white`, `black`, `green`, `red`, `background`, `lightgrey`, `grey`, `blue`|red|`feedbacks-negative-color;grey`|
|lights-1-name|第一个（左）灯的名称|字符串|F5|`lights-1-name;LightA`|
|lights-1-failure|是否触发故障|布尔值|False|`lights-1-failure;True`|
|lights-1-default|无故障时的默认状态|`on` 或 `off`|on|`lights-1-default;off`|
|lights-1-oncolor|灯亮时的颜色|`white`, `black`, `green`, `red`, `background`, `lightgrey`, `grey`, `blue`|green|`lights-1-oncolor;red`|
|lights-1-key|解决故障的键盘键|键盘键|F5|`lights-1-key;F7`|
|lights-1-on|灯的当前状态|布尔值|True|`lights-1-on;False`|
|lights-2-name|第二个（右）灯的名称|字符串|F6|`lights-2-name;LightB`|
|lights-2-failure|是否触发故障|布尔值|False|`lights-2-failure;True`|
|lights-2-default|无故障时的默认状态|`on` 或 `off`|off|`lights-2-default;on`|
|lights-2-oncolor|灯亮时的颜色|`white`, `black`, `green`, `red`, `background`, `lightgrey`, `grey`, `blue`|red|`lights-2-oncolor;green`|
|lights-2-key|解决故障的键盘键|键盘键|F6|`lights-2-key;F8`|
|lights-2-on|灯的当前状态|布尔值|False|`lights-2-on;True`|
|scales-1-name|量表1的名称|字符串|F1|`scales-1-name;Scale1`|
|scales-1-failure|是否触发故障|布尔值|False|`scales-1-failure;True`|
|scales-1-side|故障发生的方向（0随机，1上，-1下）|-1, 0, 1|0|`scales-1-side;1`|
|scales-1-key|解决故障的键盘键|键盘键|F1|`scales-1-key;F9`|
|scales-2-name|量表2的名称|字符串|F2|`scales-2-name;Scale2`|
|scales-2-failure|是否触发故障|布尔值|False|`scales-2-failure;True`|
|scales-2-side|故障发生的方向|-1, 0, 1|0|`scales-2-side;-1`|
|scales-2-key|解决故障的键盘键|键盘键|F2|`scales-2-key;F10`|
|scales-3-name|量表3的名称|字符串|F3|`scales-3-name;Scale3`|
|scales-3-failure|是否触发故障|布尔值|False|`scales-3-failure;True`|
|scales-3-side|故障发生的方向|-1, 0, 1|0|`scales-3-side;1`|
|scales-3-key|解决故障的键盘键|键盘键|F3|`scales-3-key;F11`|
|scales-4-name|量表4的名称|字符串|F4|`scales-4-name;Scale4`|
|scales-4-failure|是否触发故障|布尔值|False|`scales-4-failure;True`|
|scales-4-side|故障发生的方向|-1, 0, 1|0|`scales-4-side;-1`|
|scales-4-key|解决故障的键盘键|键盘键|F4|`scales-4-key;F12`|
