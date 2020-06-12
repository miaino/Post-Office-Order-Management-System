from tkinter import *
from tkinter.messagebox import *
from MainPage import *
from LoginPage import *
from signup import *



class Page1(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (300, 180))  # 设置窗口大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Button(self.page, text='登陆', command=self.login).grid(row=9, stick=W, pady=10)
        Button(self.page, text='注册', command=self.signup).grid(row=9, column=1, stick=E)
        Button(self.page, text='退出', command=self.page.quit).grid(row=9, column=2, stick=E)

    def login(self):
        self.page.destroy()
        LoginPage(self.root)

    def signup(self):
        self.page.destroy()
        SignupPage(self.root)