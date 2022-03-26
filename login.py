from  requests import get
from socket import socket,AF_INET,SOCK_DGRAM
from json import  loads
from sys import exit
class Login:
    """
     登录的核心操作
    """
    def __init__(self):
        self.url = "http://192.168.200.2"
        self.url = "http://192.168.200.2:801/eportal/"
        self.nat_company = {
            "1": "telecom",
            "2": "cmcc",
            "3": "xyw",
            "4": "xyw"  # 校园网
        }
        self.ip=self.GetIp()


    def send(self,info):
        nat = info['user_nat']
        real_nat = self.nat_company[nat]
        user_code = info['user_code']
        self.param={
            "c":"Portal",
            "a":"login",
            "callback":"dr1003",
            "login_method":"1",
            "user_account":f",0,{user_code}@{real_nat}",
            "user_password":f"{info['user_passwd']}",
            "wlan_user_ip":f"{self.ip}",
            "wlan_user_ipv6":"",
            "wlan_user_mac":"000000000000",
            "wlan_ac_ip":"",
            "wlan_ac_name":"",
            #"jsVersio":"3.3.3",
            #"v":"2589",
        }
        reason = get(self.url, params=self.param)
        return reason.text


    def GetIp(self):
        s = socket(AF_INET, SOCK_DGRAM)  # 创建一个套接字，前一个常量表示ipv4，后一个表示udp
        s.connect(('114.114.114.114', 80))  # 这个地址是任意的，主要目的是用来获取上网的地址
        ip = s.getsockname()[0]  # 返回是个元组，一个ip一个端口
        s.close()
        return ip


if __name__ =="__main__":
    filename= "information.json"
    login=Login()
    try :
        with open(filename,"r") as f:
            user_info = loads(f.read())
            if user_info['login_success'] == 1:
                login.send(user_info)
    except FileNotFoundError:exit()

