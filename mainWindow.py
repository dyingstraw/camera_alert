import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from main_ui import Ui_MainWindow
#-*- coding:utf-8 -*-
from PyQt5.QtCore import QThread, pyqtSignal
 
import socket 
import threading

    

class MyDesiger(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyDesiger, self).__init__(parent)
        self.setupUi(self)



def doOpenServer(port):
    print("doOpenServer")
    t=serverThread("1222","0.0.0.0",port)
    # t.setDaemon(True)
    
    t.start()
    t.exec()
    
class serverThread (QThread):
    def __init__(self, threadID, addr, port):
        print("tetet")
        super(serverThread,self).__init__()
        self.threadID = threadID
        self.addr = addr
        self.port = port
    def run(self):
        print("runrun")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.addr, self.port))
        s.listen(3)
        while True:
            conn, addr = s.accept()
            t=ListenThread("123",conn,addr)
            # t.setDaemon(True)
            t.singnal.connect(ui.logText.setText)
            t.start()

class ListenThread (QThread):   #继承父类threading.Thread

    singnal=pyqtSignal(str)
    def __init__(self, threadID, conn, addr):
        super(ListenThread,self).__init__()
        self.threadID = threadID
        self.addr = addr
        self.conn = conn
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        # 每次新开一个线程，处理客户端的请求
        print("ListenThread",self.conn)
        self.link(self.conn,self.addr)
    # 处理函数
    def link(self,conn, addr):
        while True:
            data = conn.recv(1).decode('utf-8')
            print(data)
            if data=='1':
                ui.light01.setText("hello")
            elif data=='2':
                ui.light01.setText("word")
            else:
                ui.light01.setText("-")
            self.singnal.emit(data)
            conn.sendall(data.encode('utf-8'))
app = QApplication(sys.argv)     
ui = MyDesiger()
if __name__ == "__main__":
    
    ui.openServer.clicked.connect(lambda txt: doOpenServer(80))
    ui.show()
    sys.exit(app.exec_())