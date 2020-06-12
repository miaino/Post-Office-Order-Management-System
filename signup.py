from tkinter import *
from tkinter.messagebox import *
from MainPage import *
from Page import *
import MySQLdb
from tkinter import messagebox
import pymysql
from Page1 import *

db = pymysql.connect("localhost","root","1234","testdb" )
cursor = db.cursor()
tag = 0
# 连接数据库
class MysqlSearch(object):
    def __init__(self):
        self.get_conn()

    # 获取连接
    def get_conn(self):
        try:
            self.conn = MySQLdb.connect(
                host='127.0.0.1',
                user='root',
                passwd='1234',
                db='testdb',
                charset='utf8'
            )
        except MySQLdb.Error as e:
            print('Error: %s' % e)

    # 关闭连接
    def close_conn(self):
        try:
            if self.conn:
                self.conn.close()
        except MySQLdb.Error as e:
            print('Error: %s' % e)

    # 注册
    def insert_userinfo(self, a, b,c,d,e,f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        sql = 'SELECT * FROM user'
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        result = [dict(zip([k[0] for k in cursor.description], row)) for row in result]
        ulist = []
        for item in result:
            ulist.append(item['id'])
        if int(self.a) in ulist:
            messagebox.showerror('警告', message='用户名已存在')
        else:
            #for item in result:
                #ulist.append(item['id'])
            try:
                # sql = 'INSERT INTO 登陆账户(用户名,密码) VALUES(%s,%s)'
                cursor = self.conn.cursor()
                cursor.execute('INSERT INTO user(id,pwd,name,tel,address,zip) VALUES(%s,%s,%s,%s,%s,%s)', (self.a, self.b,self.c,self.d,self.e,self.f))
                # 提交事务
                self.conn.commit()
                messagebox.showinfo(title='恭喜', message='注册成功')
                cursor.close()
                self.close_conn()
                tag = 1
                return tag
            except:
            #messagebox.showerror('警告', message='用户名已存在')
            # 限制提交
                self.conn.rollback()


class SignupPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (300, 340))  # 设置窗口大小
        self.username = StringVar()
        self.password = StringVar()
        self.name = StringVar()
        self.tel = StringVar()
        self.address = StringVar()
        self.zip = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='账户: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text='密码: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Label(self.page, text='姓名: ').grid(row=3, stick=W, pady=10)
        Entry(self.page, textvariable=self.name).grid(row=3, column=1, stick=E)
        Label(self.page, text='电话: ').grid(row=4, stick=W, pady=10)
        Entry(self.page, textvariable=self.tel).grid(row=4, column=1, stick=E)
        Label(self.page, text='地址: ').grid(row=5, stick=W, pady=10)
        Entry(self.page, textvariable=self.address).grid(row=5, column=1, stick=E)
        Label(self.page, text='邮编: ').grid(row=6, stick=W, pady=10)
        Entry(self.page, textvariable=self.zip).grid(row=6, column=1, stick=E)
        Button(self.page, text='注册', command=self.signupCheck).grid(row=7, stick=W, pady=10)
        Button(self.page, text='退出', command=self.page.quit).grid(row=7, column=1, stick=E)


    def signupCheck(self):
        username = self.username.get()
        pwd = self.password.get()
        name =self.name.get()
        tel = self.tel.get()
        address = self.address.get()
        zip =self.zip.get()
        obj_r = MysqlSearch()
        tag = obj_r.insert_userinfo(username, pwd,name,tel,address,zip)
        if(tag == 1):
            self.page.destroy()
            Page1(self.root)


