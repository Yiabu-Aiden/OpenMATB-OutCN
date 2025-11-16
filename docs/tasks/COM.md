## communications（通信任务）

|参数|描述|可能值|默认值|示例|
|:----|:----|:----|:----|:----|
|title|任务标题，插件可见时显示|字符串|Communications|`title;Radio Communications`|
|taskplacement|任务在3x2画布中的位置|`topleft`, `topmid`, `topright`, `bottomleft`, `bottommid`, `bottomright`, `fullscreen`|bottomleft|`taskplacement;topright`|
|taskupdatetime|插件更新间隔（毫秒）|正整数|80|`taskupdatetime;100`|
|automaticsolver|是否启用自动解决功能|布尔值|False|`automaticsolver;True`|
|displayautomationstate|是否显示当前自动化状态|布尔值|True|`displayautomationstate;False`|
|callsignregex|呼号生成的正则表达式模式|正则表达式|[A-Z][A-Z][A-Z]\d\d\d|`callsignregex;[A-Z]\d[A-Z]\d\d`|
|owncallsign|受试者呼号，为空时按正则生成|字符串|（空）|`owncallsign;ABC123`|
|othercallsignnumber|无关干扰呼号的数量|正整数|5|`othercallsignnumber;3`|
|othercallsign|干扰呼号列表，为空时自动生成|字符串列表|（空）|`othercallsign;[XYZ789, DEF456]`|
|airbandminMhz|最小无线电频率（MHz）|正浮点数|108.0|`airbandminMhz;110.0`|
|airbandmaxMhz|最大无线电频率（MHz）|正浮点数|137.0|`airbandmaxMhz;135.0`|
|airbandminvariationMhz|目标无线电的最小频率变化|正整数|5|`airbandminvariationMhz;4`|
|airbandmaxvariationMhz|目标无线电的最大频率变化|正整数|6|`airbandmaxvariationMhz;7`|
|voiceidiom|语音方言，对应文件夹需在Sound目录|`english` 或 `french`|french|`voiceidiom;english`|
|voicegender|语音性别，对应文件夹需在所选方言目录|`male` 或 `female`|female|`voicegender;male`|
|radioprompt|触发目标或干扰提示|`own` 或 `other`|（空）|`radioprompt;own`|
|promptlist|无线电标签列表，按出现顺序|字符串列表|[NAV1, NAV2, COM1, COM2]|`promptlist;[COM3, COM4]`|
|maxresponsedelay|最大响应延迟（毫秒）|正整数|20000|`maxresponsedelay;15000`|
|feedbackduration|反馈持续时间（毫秒）|正整数|1500|`feedbackduration;2000`|
|feedbacks-positive-active|是否启用正确响应的正反馈|布尔值|False|`feedbacks-positive-active;True`|
|feedbacks-positive-color|正反馈颜色|`white`, `black`, `green`, `red`, `background`, `lightgrey`, `grey`, `blue`|green|`feedbacks-positive-color;blue`|
|feedbacks-negative-active|是否启用错误响应的负反馈|布尔值|False|`feedbacks-negative-active;True`|
|feedbacks-negative-color|负反馈颜色|`white`, `black`, `green`, `red`, `background`, `lightgrey`, `grey`, `blue`|red|`feedbacks-negative-color;lightgrey`|
