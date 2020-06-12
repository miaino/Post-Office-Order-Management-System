import threading
from tkinter import *
import pymysql
import time
from tkinter.messagebox import *


db = pymysql.connect("localhost","root","1234","testdb" )
cursor = db.cursor()


class choose_window(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (400, 200))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Button(self.page, text='所有报纸', command=self.all).grid(row=9, column=1,stick=E)
        Button(self.page, text='已订报纸', command=self.booked).grid(row=9, column=2, stick=E)
        Button(self.page, text='订阅报纸', command=self.insert).grid(row=9, column=3, stick=E)
        Button(self.page, text='退订报纸', command=self.delete).grid(row=9, column=4, stick=E)

    def all(self):
        self.page.destroy()
        all_newspaper(self.root)

    def booked(self):
        self.page.destroy()
        booked_newspaper(self.root)
    
    def insert(self):
        self.page.destroy()
        insert(self.root)

    def delete(self):
        self.page.destroy()
        delete(self.root)





class all_newspaper(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (500, 600))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        self.list=Listbox(self.root)
        self.list.pack(fill=BOTH, expand=1, padx=10, pady=10)
        self.button=Button(self.root,text="后退",command=self.goback)
        self.button.pack(side=RIGHT, padx=(0, 20), pady=(0, 20))
        cursor.execute("select * from newspaper")
        data = cursor.fetchone()
        
        while data != None:
            string = ""
            for i in data:
                string = string +" "+str(i)
            self.list.insert("end",string)
            data = cursor.fetchone()


    def goback(self):
        self.list.destroy()
        self.button.destroy()
        choose_window(self.root)



class booked_newspaper(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (600, 400))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        self.list=Listbox(self.root)
        self.list.pack(fill=BOTH, expand=1, padx=10, pady=10)
        self.button=Button(self.root,text="后退",command=self.goback)
        self.button.pack(side=RIGHT, padx=(0, 20), pady=(0, 20))
        query ="select newspaper.newspaper_id,newspaper.newspaper_name,newspaper.publisher,newspaper.newspaper_price from newspaper,book_state where  book_state.user_id = "+str(self.root.user_id) + " and book_state.newspaper_id = newspaper.newspaper_id"
  
        cursor.execute(query)
        data = cursor.fetchone()
        
        while data != None:
            string = ""
            for i in data:
                string = string +" "+str(i)
            self.list.insert("end",string)
            data = cursor.fetchone()

    def goback(self):
        self.list.destroy()
        self.button.destroy()
        choose_window(self.root)    


class insert(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (300, 200))  # 设置窗口大小
        self.paper_id = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='要预定的报纸id:').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.paper_id).grid(row=1, column=1, stick=E)
        Button(self.page,text="确定",command=self.insert).grid(row=3, stick=W)
        Button(self.page,text="后退",command=self.goback).grid(row=3, stick=E)
    
    def insert(self):
        temp_paper_id = self.paper_id.get()
        print (self.paper_id.get())
        print ("test")
        print (temp_paper_id)


        
        
        
        deter = True




        if temp_paper_id != "":


            query = "select * from book_state where  newspaper_id = "+str(temp_paper_id)+" and  user_id = "+str(self.root.user_id)
            cursor.execute(query)
            print (query)
            data = cursor.fetchone()
            print (data)
            if data != None:
                messagebox.showinfo(title='提示', message='订阅失败') 
                self.goback()

            else:
                query = "insert into book_state value ("+str(temp_paper_id)+","+str(self.root.user_id)+")"
                try:    
                    cursor.execute(query)
                    messagebox.showinfo(title='提示', message='订阅成功') 
                    db.commit()
                    self.goback()
                except Exception:
                    messagebox.showinfo(title='提示', message='订阅失败') 
                    self.goback()

        else:
            messagebox.showinfo(title='提示', message='订阅失败') 
            self.goback()


            
        

        self.paper_id =StringVar()

    def goback(self):
        self.page.destroy()
        choose_window(self.root) 



class delete(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (300, 200))  # 设置窗口大小
        self.paper_id = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='要退订的报纸id:').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.paper_id).grid(row=1, column=1, stick=E)
        Button(self.page,text="确定",command=self.delete).grid(row=3, stick=W)
        Button(self.page,text="后退",command=self.goback).grid(row=3, stick=E)
        
        
    
    def delete(self):
        temp_paper_id = self.paper_id.get()
        if temp_paper_id != "":
            query = "select * from book_state where  newspaper_id = "+str(temp_paper_id)+" and  user_id = "+str(self.root.user_id)
            cursor.execute(query)
            print (query)
            data = cursor.fetchone()
            print (data)
            if data == None:
                messagebox.showinfo(title='提示', message='退订失败') 
                self.goback()
            else:
                query = "delete from book_state where newspaper_id = "+str(temp_paper_id)+" and user_id = "+str(self.root.user_id)
                print (query)
                cursor.execute(query)
                messagebox.showinfo(title='提示', message='退订成功') 
                db.commit()
                self.goback()
        else:
            messagebox.showinfo(title='提示', message='退订失败') 
            self.goback()
        
    def goback(self):
        self.page.destroy()
        choose_window(self.root) 