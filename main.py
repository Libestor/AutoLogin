try:
    from json import  dumps,loads
    from login import Login
    from re import fullmatch
    import requests
    import socket
except ModuleNotFoundError:
    print("亲，必要的模组还没安装呢，可以在控制台输入：\n"
          "pip install  re\n"
          "pip install requests\n"
          "pip install socket\n实现安装"
          "并且确保文件login.php 和主程序在同一个文件夹")
    exit()


class Table(Login):
    """
    用户互动界面
    """


    def __init__(self):
        super().__init__()
        self.filename= "information.json"
        self.user_info={
            "user_code":"id_code",
            "user_passwd":"password",
            "user_nat":"2",
            "login_success":0
        }


    def CheckID(self,id):
        pattern = "[0-9]{7}"
        if(fullmatch(pattern,id)):
            return 0
        else:return 1


    def Check_nat(self,nat):
        pattern = "1|2|3|4"
        if(fullmatch(pattern,nat)):
            return 0
        else:return 1


    def Choose(self):
        print("未检测到数据输入，您是打算现在输入,还是生成json文件手动输入/导入json文件")
        Choice = input("现在输入请打1，生成json文件请打2")
        if Choice != '1' and Choice != '2':
            flag = 1
        else:
            flag = 0
        while flag:
            Choice = input("输入有误，请重新输入：")
            if Choice != '1' and  Choice != '2' :
                flag = 1
            else : flag = 0
        if(Choice == '1'):
            self.InputData()
        elif(Choice == '2'):
            self.CreateJsonFile()


    def InputData(self):
        user_code = input("请输入唯一识别码")
        while(self.CheckID(user_code)):
            user_code = input("输入有误，请重新输入唯一识别码")
        user_passwd = input("请输入您的密码")
        user_nat = input("请输入您的网络类型，电信输入'1',移动输入'2'，教师输入'3'，临时输入'4'")
        while(self.Check_nat(user_nat)):
            user_nat = input("您输入的网络类型有误，请重新输入")
        self.user_info['user_code']=user_code
        self.user_info['user_passwd']=user_passwd
        self.user_info['user_nat']=user_nat


    def CreateJsonFile(self):
        self.DumpJson()
        print("请在已经生成的json文件中输入信息，然后重新运行文件")
        print("依次输入唯一识别码，密码，运营商（用1，2，3，4代替电信，移动，教师，临时）login_success勿动")
        exit()


    def FileCheck(self):
        try:
            with open(self.filename,"r") as f:
                self.user_info=loads(f.read())
        except FileNotFoundError: self.Choose()
        reason = self.send(self.user_info)
        if 'dr1003({"result":"1","msg":"\u8ba4\u8bc1\u6210\u529f"})' in reason :
            print("登录成功")
        elif 'dr1003({"result":"0","msg":"","ret_code":2})' in reason:
            print( "已经登录了")
            print("数据已记录")
            if(self.user_info["login_success"] != 1):
                self.user_info["login_success"] = 1
                self.DumpJson()
        elif 'dr1003({"result":"0","msg":"bGRhcCBhdXRoIGVycm9y","ret_code":1})' in reason:
            print("密码错误")
        elif 'dXNlcmlkIGVycm9yMQ==' in reason:
            print("网段选择失败")
        elif 'dr1003({"result":"1","msg"' in reason:
            print("恭喜成功登录")
            self.user_info["login_success"] = 1
            print("正在将数据存入json中")
            self.DumpJson()
            print("存入成功")


    def DumpJson(self):
        with open(self.filename,"w") as f:
            f.write(dumps(self.user_info))


    def go(self):
        self.FileCheck()

        
if __name__ == "__main__":
    table = Table()
    table.go()