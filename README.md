### 项目名称：校园网自动登录脚本

### 用法：

* 下载login.py和main.py
* 首次打开main.py，并跟随要求按照必要是模组
* 输入密码和账户：
  * 可以跟随main.py输入账户和密码
  * 也可以在生成的information.json输入账户密码（请不要动login_success属性）
  * 当能验证密码账号正确后会记录成一个information.json的信息文件
* 输入正确后下次就可以直接登录，不用再次输入
* 如果有值守的需求也可以在成功登录以后直接运行 login.py文件达到快速登录

### 进阶用法：

* 所写的python代码都遵循最低引用的要求，这意味这可以打包一个较小的可执行程序。
* 打包不限于exe文件
* 打包所需要的模组：pyinstaller
* 所需的指令：pyinstaller -F login.py

> 打包后的文件依旧需要information.json文件

### 高阶用法：

* 在windows上可以通过计划任务**检测所连接的WIFI**来判断是否需要运行程序/脚本，从而实现自动登录
* 在linux上可以使用NetworkManager来检测网络变化，从而决定是否执行脚本
* 在安卓上，也有方法，不过一般用不到，就再没研究
* ios上同理

### 还想实现，但还没实现的功能：

1. 用户的信息都会储存再imformation.json中，造成的比较严重的安全风险。

   通过另一个脚本用pyinstaller打包成一个专属于用户的登录脚本，可以降低信息泄露风险

2. 想通过第三个脚本实现自动部署，能够自动再linux和windows上一键部署，实现上面的高阶用法



联系方式：libestor@qq.com
