根据 0xfaskety 的代码魔改，加入

1 定时任务执行，可以设置每天刷一点，更健康
2 多账号执行逻辑
3 牛市币本位，刷量完后账号保留sol，防止爆拉


经测试磨损在0.3%-0.03%z之间

个人twitter https://twitter.com/crazytidy

通过requirements.txt文件安装依赖库，推荐在北京时间的下午刷量

pip install -r requirements.txt

使用方法：
1. 下载本库
2. 在终端中打开本库
3. 修改monitor中的api数组，以及每次刷的量
4. 运行pip install -r requirements.txt命令安装依赖库
5. 运行python monitor

原代码：https://github.com/yuankongzhe/backpack-faskety-auto-trade
