## resman（资源管理任务）

|参数|描述|可能值|默认值|示例|
|:----|:----|:----|:----|:----|
|title|任务标题，插件可见时显示|字符串|Resources management|`title;Resource Control`|
|taskplacement|任务在3x2画布中的位置|`topleft`, `topmid`, `topright`, `bottomleft`, `bottommid`, `bottomright`, `fullscreen`|bottommid|`taskplacement;topmid`|
|taskupdatetime|插件更新间隔（毫秒）|正整数|2000|`taskupdatetime;1500`|
|automaticsolver|是否自动设置目标频率|布尔值|False|`automaticsolver;True`|
|displayautomationstate|是否显示当前自动化状态|布尔值|True|`displayautomationstate;False`|
|toleranceradius| tolerance区域半径（0不显示）|整数|250|`toleranceradius;300`|
|tolerancecolor|体积在区域内时的颜色|`white`, `black`, `green`, `red`, `background`, `lightgrey`, `grey`, `blue`|black|`tolerancecolor;green`|
|tolerancecoloroutside|体积在区域外时的颜色|`white`, `black`, `green`, `red`, `background`, `lightgrey`, `grey`, `blue`|black|`tolerancecoloroutside;red`|
|pumpcoloroff|泵关闭时的颜色|`white`, `black`, `green`, `red`, `background`, `lightgrey`, `grey`, `blue`|white|`pumpcoloroff;grey`|
|pumpcoloron|泵开启时的颜色|`white`, `black`, `green`, `red`, `background`, `lightgrey`, `grey`, `blue`|green|`pumpcoloron;blue`|
|pumpcolorfailure|泵故障时的颜色|`white`, `black`, `green`, `red`, `background`, `lightgrey`, `grey`, `blue`|red|`pumpcolorfailure;lightgrey`|
|displaystatus|是否在特定面板显示泵状态|布尔值|True|`displaystatus;False`|
|statuslocation|泵状态显示位置|`topleft`, `topmid`, `topright`, `bottomleft`, `bottommid`, `bottomright`, `fullscreen`|bottomright|`statuslocation;topright`|
|tank-a-level|A tank当前液位|整数|2500|`tank-a-level;2000`|
|tank-a-max|A tank最大液位|整数|4000|`tank-a-max;5000`|
|tank-a-target|A tank目标液位|整数|2500|`tank-a-target;3000`|
|tank-a-depletable|A tank是否可耗尽|布尔值|True|`tank-a-depletable;False`|
|tank-a-lossperminute|A tank每分钟泄漏量|正整数|800|`tank-a-lossperminute;700`|
|tank-b-level|B tank当前液位|整数|2500|`tank-b-level;2200`|
|tank-b-max|B tank最大液位|整数|4000|`tank-b-max;4500`|
|tank-b-target|B tank目标液位|整数|2500|`tank-b-target;2800`|
|tank-b-depletable|B tank是否可耗尽|布尔值|True|`tank-b-depletable;False`|
|tank-b-lossperminute|B tank每分钟泄漏量|正整数|800|`tank-b-lossperminute;600`|
|tank-c-level|C tank当前液位|整数|1000|`tank-c-level;1200`|
|tank-c-max|C tank最大液位|整数|2000|`tank-c-max;2500`|
|tank-c-target|C tank目标液位|整数|（空）|`tank-c-target;1500`|
|tank-c-depletable|C tank是否可耗尽|布尔值|True|`tank-c-depletable;False`|
|tank-c-lossperminute|C tank每分钟泄漏量|正整数|0|`tank-c-lossperminute;100`|
|tank-d-level|D tank当前液位|整数|1000|`tank-d-level;1300`|
|tank-d-max|D tank最大液位|整数|2000|`tank-d-max;2200`|
|tank-d-target|D tank目标液位|整数|（空）|`tank-d-target;1600`|
|tank-d-depletable|D tank是否可耗尽|布尔值|True|`tank-d-depletable;False`|
|tank-d-lossperminute|D tank每分钟泄漏量|正整数|0|`tank-d-lossperminute;150`|
|tank-e-level|E tank当前液位|整数|3000|`tank-e-level;3200`|
|tank-e-max|E tank最大液位|整数|4000|`tank-e-max;4200`|
|tank-e-target|E tank目标液位|整数|（空）|`tank-e-target;3500`|
|tank-e-depletable|E tank是否可耗尽|布尔值|False|`tank-e-depletable;True`|
|tank-e-lossperminute|E tank每分钟泄漏量|正整数|0|`tank-e-lossperminute;50`|
|tank-f-level|F tank当前液位|整数|3000|`tank-f-level;3300`|
|tank-f-max|F tank最大液位|整数|4000|`tank-f-max;4300`|
|tank-f-target|F tank目标液位|整数|（空）|`tank-f-target;3600`|
|tank-f-depletable|F tank是否可耗尽|布尔值|False|`tank-f-depletable;True`|
|tank-f-lossperminute|F tank每分钟泄漏量|正整数|0|`tank-f-lossperminute;70`|
|pump-1-flow|泵1每分钟流量|正整数|800|`pump-1-flow;900`|
|pump-1-state|泵1当前状态|`on` 或 `off` 或 `failure`|off|`pump-1-state;on`|
|pump-1-key|切换泵1的键盘键|键盘键|NUM_1|`pump-1-key;1`|
|pump-2-flow|泵2每分钟流量|正整数|600|`pump-2-flow;700`|
|pump-2-state|泵2当前状态|`on` 或 `off` 或 `failure`|off|`pump-2-state;failure`|
|pump-2-key|切换泵2的键盘键|键盘键|NUM_2|`pump-2-key;2`|
|pump-3-flow|泵3每分钟流量|正整数|800|`pump-3-flow;850`|
|pump-3-state|泵3当前状态|`on` 或 `off` 或 `failure`|off|`pump-3-state;on`|
|pump-3-key|切换泵3的键盘键|键盘键|NUM_3|`pump-3-key;3`|
|pump-4-flow|泵4每分钟流量|正整数|600|`pump-4-flow;650`|
|pump-4-state|泵4当前状态|`on` 或 `off` 或 `failure`|off|`pump-4-state;off`|
|pump-4-key|切换泵4的键盘键|键盘键|NUM_4|`pump-4-key;4`|
|pump-5-flow|泵5每分钟流量|正整数|600|`pump-5-flow;550`|
|pump-5-state|泵5当前状态|`on` 或 `off` 或 `failure`|off|`pump-5-state;on`|
|pump-5-key|切换泵5的键盘键|键盘键|NUM_5|`pump-5-key;5`|
|pump-6-flow|泵6每分钟流量|正整数|600|`pump-6-flow;620`|
|pump-6-state|泵6当前状态|`on` 或 `off` 或 `failure`|off|`pump-6-state;failure`|
|pump-6-key|切换泵6的键盘键|键盘键|NUM_6|`pump-6-key;6`|
|pump-7-flow|泵7每分钟流量|正整数|400|`pump-7-flow;450`|
|pump-7-state|泵7当前状态|`on` 或 `off` 或 `failure`|off|`pump-7-state;on`|
|pump-7-key|切换泵7的键盘键|键盘键|NUM_7|`pump-7-key;7`|
|pump-8-flow|泵8每分钟流量|正整数|400|`pump-8-flow;380`|
|pump-8-state|泵8当前状态|`on` 或 `off` 或 `failure`|off|`pump-8-state;off`|
|pump-8-key|切换泵8的键盘键|键盘键|NUM_8|`pump-8-key;8`|