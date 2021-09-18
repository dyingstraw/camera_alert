
# coding=utf-8
import threading
import socketserver
from typing import NoReturn
client = None
class MyTCPHandler(socketserver.BaseRequestHandler):

    def setup(self):
        print("setup")
        client = self
    def send(self,data):
        self.request.send(data)
    def handle(self):
        print("handle")
        while True:
            try:
                self.data = self.request.recv(1)
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                # 下面3行代码防止服务器端随着客户端的断开而断开
                # 经过测试发现，在linux有效，Windows无效。
                if not self.data:
                    print(self.client_address, "断开了")
                    break
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print('出现错误',e)
                break


def run():
    HOST, PORT = "0.0.0.0", 80

    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
if __name__ == "__main__":

    


    t1 = threading.Thread(target=run)
    t1.start()
    print("2121")
    while True:
        # data = input()
        if client!=None:
            print("send")
            client.send("data")
    
    