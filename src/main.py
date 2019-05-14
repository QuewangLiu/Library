import time

from PyQt5.QtCore import QDate, QTime
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QListWidgetItem
from UI.main import Ui_Library
from UI.add import Ui_addReadingRoom
from PyQt5 import QtWidgets,QtGui,QtCore
from UI.vip import Ui_vip
import sys
import os

import pickle
with open('..\major_dict.pkl', 'rb') as f:model = pickle.load(f)

class mainWindow(QtWidgets.QMainWindow, Ui_Library):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.addRead)
        self.listWidget.itemClicked.connect(self.showRoom)
        self.pushButton.clicked.connect(self.find)
        self.pushButton_3.clicked.connect(self.remove)

    def remove(self):
        reply = QMessageBox.question(self, "Tips", "确认删除阅览室？")
        if reply == QMessageBox.Yes:
            self.tableWidget.clear()
            row = self.listWidget.currentRow()
            fname = '..\ReadingRoom/' + self.listWidget.item(row).text().strip('\n') + '.txt'
            if os.path.exists(fname):
                os.remove(fname)
            with open("..\ReadingRoom.txt", "r") as f:
                lines = f.readlines()
                # print(lines)
            with open("..\ReadingRoom.txt", "w") as f_w:
                for line in lines:
                    if self.listWidget.item(row).text() in line:
                        continue
                    f_w.write(line)
            window.listWidget.clear()
            f = open('..\ReadingRoom.txt', 'r')
            name = f.readline()
            while name != "":
                Item = QListWidgetItem(name)
                window.listWidget.addItem(Item)
                name = f.readline()
            f.close()


    def find(self):
        data=self.dateTimeEdit.date()
        d = QDate(2019, 3, 4)
        day=d.daysTo(data)
        time=self.dateTimeEdit.time()
        hour=time.hour()
        minute=time.minute()
        row = self.listWidget.currentRow()
        fname = '..\ReadingRoom/' + self.listWidget.item(row).text().strip('\n') + '.txt'
        fobj = open(fname, 'r')
        name = fobj.readline()
        while name != "":
            line = name.strip('\n')
            line = line.split(" ")
            num = 0
            for i in line[0]:
                num=num*10+int(i)
            zhuanye=line[2]
            if zhuanye!="空":
                scope=model[zhuanye]
                if day/7>=18:
                    newItem = QTableWidgetItem("放假")
                    newItem.setBackground(QtCore.Qt.gray)  # 空闲灰色
                    self.tableWidget.setItem(num / 10, num % 10, newItem)
                else:
                    if day%7>4:             #周六日
                        newItem = QTableWidgetItem("占用")  # 查询的时间
                        newItem.setBackground(QtCore.Qt.red)  # 非空闲显示红色
                        self.tableWidget.setItem(num / 10, num % 10, newItem)
                    else:
                        if time<t1:
                            newItem = QTableWidgetItem("占用")  # 查询的时间
                            newItem.setBackground(QtCore.Qt.red)  # 非空闲显示红色
                            self.tableWidget.setItem(num / 10, num % 10, newItem)
                        elif time>t1 and time<t2:
                            col = day % 7 * 5 + 0
                            if scope[int(day/7)][col]==1:
                                t=100-(hour-8)*60-minute
                                newItem = QTableWidgetItem('空闲'+str(t)+'分钟') # 查询的时间
                                newItem.setBackground(QtCore.Qt.gray)  # 空闲灰色
                                self.tableWidget.setItem(num / 10, num % 10, newItem)
                            else:
                                newItem = QTableWidgetItem("占用")  # 查询的时间
                                newItem.setBackground(QtCore.Qt.red)  # 非空闲显示红色
                                self.tableWidget.setItem(num / 10, num % 10, newItem)
                        elif time>t3 and time<t4:
                            col = day % 7 * 5 + 1
                            if scope[int(day/7)][col]==1:
                                t=100-(hour-10)*60-minute
                                newItem = QTableWidgetItem('空闲' + str(t) + '分钟')  # 查询的时间
                                newItem.setBackground(QtCore.Qt.gray)  # 空闲灰色
                                self.tableWidget.setItem(num / 10, num % 10, newItem)
                            else:
                                newItem = QTableWidgetItem("占用")  # 查询的时间
                                newItem.setBackground(QtCore.Qt.red)  # 非空闲显示红色
                                self.tableWidget.setItem(num / 10, num % 10, newItem)
                        elif time>t5 and time<t6:
                            col = day % 7 * 5 + 2
                            if scope[int(day/7)][col]==1:
                                t=130-(hour-13)*60-minute
                                newItem = QTableWidgetItem('空闲' + str(t) + '分钟')  # 查询的时间
                                newItem.setBackground(QtCore.Qt.gray)  # 空闲灰色
                                self.tableWidget.setItem(num / 10, num % 10, newItem)
                            else:
                                newItem = QTableWidgetItem("占用")  # 查询的时间
                                newItem.setBackground(QtCore.Qt.red)  # 非空闲显示红色
                                self.tableWidget.setItem(num / 10, num % 10, newItem)
                        elif time>t7 and time<t8:
                            col = day % 7 * 5 + 3
                            if scope[int(day/7)][col]==1:
                                t = 130 - (hour - 15) * 60 - minute
                                newItem = QTableWidgetItem('空闲' + str(t) + '分钟')  # 查询的时间
                                newItem.setBackground(QtCore.Qt.gray)  # 空闲灰色
                                self.tableWidget.setItem(num / 10, num % 10, newItem)
                            else:
                                newItem = QTableWidgetItem("占用")  # 查询的时间
                                newItem.setBackground(QtCore.Qt.red)  # 非空闲显示红色
                                self.tableWidget.setItem(num / 10, num % 10, newItem)
                        elif time>t9 and time<t10:
                            col = day % 7 * 5 + 4
                            if scope[int(day/7)][col]==1:
                                t = 180 - (hour - 18) * 60 - minute
                                newItem = QTableWidgetItem('空闲' + str(t) + '分钟')  # 查询的时间
                                newItem.setBackground(QtCore.Qt.gray)  # 空闲灰色
                                self.tableWidget.setItem(num / 10, num % 10, newItem)
                            else:
                                newItem = QTableWidgetItem("占用")  # 查询的时间
                                newItem.setBackground(QtCore.Qt.red)  # 非空闲显示红色
                                self.tableWidget.setItem(num / 10, num % 10, newItem)
                        else:
                            newItem = QTableWidgetItem("占用")  # 查询的时间
                            # newItem.setBackground(QtCore.Qt.gray)  # 空闲灰色
                            newItem.setBackground(QtCore.Qt.red)  # 非空闲显示红色
                            self.tableWidget.setItem(num / 10, num % 10, newItem)
            else:
                newItem = QTableWidgetItem("未分配")
                newItem.setBackground(QtCore.Qt.gray)  # 空闲灰色
                self.tableWidget.setItem(num / 10, num % 10, newItem)
            name = fobj.readline()

    def load_data(self, sp):
        for i in range(1, 100):  # 模拟主程序加载过程
            # time.sleep(0.04)  # 加载数据
            sp.showMessage("加载... {0}%".format(i), QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.white)
            QtWidgets.qApp.processEvents()  # 允许主进程处理事件

    def addRead(self):
        add.show()

    def showEvent(self, *args, **kwargs):
        self.listWidget.clear()
        f = open('..\ReadingRoom.txt', 'r')
        name = f.readline()
        while name != "":
            newItem = QListWidgetItem(name)
            self.listWidget.addItem(newItem)
            name = f.readline()
        f.close()

    def showRoom(self):
        self.tableWidget.clear()
        row=self.listWidget.currentRow()
        fname='..\ReadingRoom/'+self.listWidget.item(row).text().strip('\n')+'.txt'
        fobj=open(fname,'r')
        name = fobj.readline()
        while name != "":
            line=name.strip('\n')
            line=line.split(" ")
            num=0
            for i in line[0]:
                num=num*10+int(i)
            newItem=QTableWidgetItem()
            newItem.setBackground(QtCore.Qt.gray)
            self.tableWidget.setItem(num/10,num%10,newItem)
            name=fobj.readline()



class addWimdow(QtWidgets.QMainWindow,Ui_addReadingRoom):
    def __init__(self):
        super(addWimdow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add)
        self.tableWidget.cellClicked.connect(self.block)

        # self.tableWidget.doubleClicked.connect(self.clear)

    def block(self):
        row=self.tableWidget.currentRow()
        cou=self.tableWidget.currentColumn()
        if row*10+cou in x:
            x.remove(row*10+cou)
            newItem = QTableWidgetItem("")
            self.tableWidget.setItem(row, cou, newItem)
        else:
            addVip.show()


    def add(self):
        if self.lineEdit.text()=="":
            self.label_2.setText("名称不能为空")
        elif len(x)==0:
            self.label_2.setText( "座位不能为空")
        else:
            f=open('..\ReadingRoom.txt','r+')
            name=f.readline()
            bool=True
            while name!='':
                if name==(self.lineEdit.text()+"\n"):
                    self.label_2.setText("名称重复")
                    bool=False
                name=f.readline()
            if bool:
                fname='..\ReadingRoom/'+self.lineEdit.text()+'.txt'
                # if os.path.exists(fname):
                #     self.label_2.setText("阅览室已存在")
                # else:
                f.write(self.lineEdit.text() + "\n")
                fobj=open(fname,'w')
                for num in x:
                    fobj.write(str(num)+" "+self.tableWidget.item(num/10,num%10).text()+"\n")
                fobj.close()
                reply=QMessageBox.information(self,"Tips","添加成功")
                if reply==QMessageBox.Ok:
                    window.listWidget.clear()
                    f = open('..\ReadingRoom.txt', 'r')
                    name = f.readline()
                    while name != "":
                        Item = QListWidgetItem(name)
                        window.listWidget.addItem(Item)
                        name = f.readline()
                    f.close()
                    self.close()
                f.close()

    def closeEvent(self, *args, **kwargs):
        x.clear()
        self.tableWidget.clear()
        self.lineEdit.clear()


class addVip(QtWidgets.QMainWindow,Ui_vip):
    def __init__(self):
        super(addVip, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click)
        self.comboBox.setCurrentText("空")
        self.comboBox.addItem("空")
        for cla in model:
            self.comboBox.addItem(cla)

    def showEvent(self, *args, **kwargs):
        self.lineEdit.setText("未设置")
        self.comboBox.setCurrentText("空")

    def click(self):
        row=add.tableWidget.currentRow()
        cou=add.tableWidget.currentColumn()
        x.add(row * 10 + cou)
        newItem = QTableWidgetItem(self.lineEdit.text() + " " + self.comboBox.currentText())
        newItem.setBackground(QtCore.Qt.gray)
        add.tableWidget.setItem(row, cou, newItem)
        self.close()

if __name__=="__main__":
    t1 = QTime(8, 0)
    t2 = QTime(9, 40)
    t3 = QTime(10, 0)
    t4 = QTime(11, 40)
    t5 = QTime(13, 30)
    t6 = QTime(15, 10)
    t7 = QTime(15, 30)
    t8 = QTime(17, 10)
    t9 = QTime(18, 30)
    t10 = QTime(21, 00)
    app = QtWidgets.QApplication(sys.argv)
    add=addWimdow()
    addVip=addVip()
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap('..\img.png'))
    splash.showMessage("加载... 0%", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.white)
    splash.show()  # 显示启动界面
    QtWidgets.qApp.processEvents()  # 处理主进程事/件
    app.processEvents()
    window = mainWindow()
    window.load_data(splash)  # 加载数据
    window.show()
    splash.finish(window)
    x = set()
    sys.exit(app.exec_())