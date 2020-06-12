from tkinter import *
from LoginPage import *
from Page import *
import pymysql


class myTk(Tk):
    def __init__(self):
        super().__init__()
        self.user_id=None


root = myTk()
root.title('邮局订报管理系统')

Page(root)
root.mainloop()
