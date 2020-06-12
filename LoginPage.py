from tkinter import *
from tkinter.messagebox import *
from MainPage import *
import MySQLdb
import pymysql
import choose

db = pymysql.connect("localhost","root","1234","testdb" )
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()



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

    # 获取用户信息（登录用）
    def get_userinfo(self):
        sql = 'SELECT * FROM user'

        # 使用cursor()方法获取操作游标
        cursor = self.conn.cursor()

        # 使用execute()方法执行SQL语句
        cursor.execute(sql)

        # 使用fetchall()方法获取全部数据
        result = cursor.fetchall()

        # 将数据用字典形式存储于result
        result = [dict(zip([k[0] for k in cursor.description], row)) for row in result]
        #print(result)
        # 关闭连接
        cursor.close()
        self.close_conn()
        return result


class LoginPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (300, 180))  # 设置窗口大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='账户: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text='密码: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='登陆', command=self.login).grid(row=3, stick=W, pady=10)
        Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1, stick=E)

    def cancel(self):
        # 清空用户输入的用户名和密码
        user.set('')
        passwd.set('')

    def login(self):
        # 获取用户名和密码
        obj = MysqlSearch()
        result = obj.get_userinfo()
        username = self.username.get()
        pwd = self.password.get()
        ulist = []
        plist = []
        print (pwd)
        for item in result:
            ulist.append(item['id'])
            plist.append(item['pwd'])
        deter = True
        tag = 1
        for i in range(len(ulist)):
            if username == str(ulist[i]) and pwd == plist[i]:
                    #messagebox.showinfo(title='恭喜', message='登陆成功')  # 登陆成功则执行begin函数
                deter = False
                    #self.page.destroy()
                    #MainPage(self.root)
                tag = 2
                break
            else:
                tag = 1
                #break
                    #messagebox.showerror('警告', message='用户名或密码错误')
                    #showinfo(title='错误', message='账号或密码错误！')
                    #self.page.destroy()
                    #MainPage(self.root)

        if tag== 1:
            showinfo(title='错误', message='账号或密码错误！')
        else:
            messagebox.showinfo(title='恭喜', message='登陆成功')  # 登陆成功则执行begin函数
            deter = False
            self.page.destroy()
            self.root.user_id = username
            choose.choose_window(self.root)

