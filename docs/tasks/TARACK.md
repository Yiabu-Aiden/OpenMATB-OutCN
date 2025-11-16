## track（跟踪任务）

|参数|描述|可能值|默认值|示例|
|:----|:----|:----|:----|:----|
|title|任务标题，插件可见时显示|字符串|Tracking|`title;Cursor Tracking`|
|taskplacement|任务在3x2画布中的位置|`topleft`, `topmid`, `topright`, `bottomleft`, `bottommid`, `bottomright`, `fullscreen`|topmid|`taskplacement;bottommid`|
|taskupdatetime|插件更新间隔（毫秒）|正整数|20|`taskupdatetime;30`|
|cursorcolor|移动光标的颜色|`white`, `black`, `green`, `red`, `background`, `lightgrey`, `grey`, `blue`|black|`cursorcolor;green`|
|cursorcoloroutside|光标在目标区域外时的颜色|`white`, `black`, `green`, `red`, `background`, `lightgrey`, `grey`, `blue`|red|`cursorcoloroutside;blue`|
|automaticsolver|是否自动补偿光标移动至中心|布尔值|False|`automaticsolver;True`|
|displayautomationstate|是否显示当前自动化状态|布尔值|True|`displayautomationstate;False`|
|targetproportion|目标区域半径比例（0-1）|0到1之间的数值|0.25|`targetproportion;0.3`|
|joystickforce|操纵杆灵敏度因子|整数|1|`joystickforce;2`|
|inverseaxis|是否反转操纵杆动作|布尔值|False|`inverseaxis;True`|
