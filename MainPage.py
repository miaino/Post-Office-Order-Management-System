from tkinter import *
from view import *  # 菜单栏对应的各个子页面
import pymysql
import os

user_id =sys.argv[-1]
print (user_id)

db = pymysql.connect("localhost","root","1234","testdb" )
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()



class MainPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (600, 400))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        self.inputPage = InputFrame(self.root)  # 创建不同Frame
        self.queryPage = QueryFrame(self.root)
        self.inputPage.pack()  # 默认显示数据录入界面
        menubar = Menu(self.root)
        menubar.add_command(label='所有报刊', command=self.inputData)
        menubar.add_command(label='订阅报刊', command=self.queryData)
        menubar.add_command(label='已订报刊', command=self.inputData)
        menubar.add_command(label='退订报刊', command=self.queryData)
        self.root['menu'] = menubar  # 设置菜单栏



