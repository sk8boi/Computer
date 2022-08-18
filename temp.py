# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 17:29:25 2022

@author: LYQ
"""

from tkinter import *
import hashlib
import time
import tkinter.messagebox as mess



class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #设置窗口
    def set_init_window(self):
        
        self.init_window_name.title("简单的公式计算软件v1.0")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('760x300+10+10')
        self.init_window_name.resizable(False, False)

        
        #标签row0-5 colimn0
        self.L00 = Label(self.init_window_name,text='数值0',bd =10,width=16,font=('Helvetica', '13')) #原始数据录入框
        self.L00.grid(row=0, column=0)
        
        self.L10 = Label(self.init_window_name,text='数值1',bd =10,width=16,font=('Helvetica', '13')) #原始数据录入框
        self.L10.grid(row=1, column=0)
        
        self.L20 = Label(self.init_window_name,text='数值2',bd =10,width=16,font=('Helvetica', '13')) #原始数据录入框
        self.L20.grid(row=2, column=0)
        
        self.L30 = Label(self.init_window_name,text='数值3',bd =10,width=16,font=('Helvetica', '13')) #原始数据录入框
        self.L30.grid(row=3, column=0)
        
        self.L40= Label(self.init_window_name,text='数值4',bd =10,width=16,font=('Helvetica', '13')) #原始数据录入框
        self.L40.grid(row=4, column=0)
        
        self.L50= Label(self.init_window_name,text='数值5',bd =10,width=16,font=('Helvetica', '13')) #原始数据录入框
        self.L50.grid(row=5, column=0)
        
        
        #输入框row0-5 colimn1
        #E01
        self.E01 = Entry(self.init_window_name,bg='lightyellow',bd =10,width=15,relief=SUNKEN) #原始数据录入框
        self.E01.grid(row=0, column=1)
        #E11
        self.E11 = Entry(self.init_window_name,bg='lightyellow',bd =10,width=15,relief=SUNKEN) #原始数据录入框
        self.E11.grid(row=1, column=1)
        #E21
        self.E21 = Entry(self.init_window_name,bg='lightyellow',bd =10,width=15,relief=SUNKEN) #原始数据录入框
        self.E21.grid(row=2, column=1)
        #E31
        self.E31 = Entry(self.init_window_name,bg='lightyellow',bd =10,width=15,relief=SUNKEN) #原始数据录入框
        self.E31.grid(row=3, column=1)
        #E41
        self.E41 = Entry(self.init_window_name,bg='lightyellow',bd =10,width=15,relief=SUNKEN) #原始数据录入框
        self.E41.grid(row=4, column=1)
        #E51
        self.E51= Entry(self.init_window_name,bg='lightyellow',bd =10,width=15,relief=SUNKEN) #原始数据录入框
        self.E51.grid(row=5, column=1)
        
        
        #帮助关于

        self.B02 = Button(self.init_window_name, text="帮助",bg="lightgray",bd =6, width=8,command =lambda:self.about(0))  # 调用内部方法  加()为直接调用
        self.B02.grid(row=0, column=2)

        self.B12 = Button(self.init_window_name, text="帮助", bg="lightgray",bd =6, width=8,command =lambda:self.about(1))  # 调用内部方法  加()为直接调用
        self.B12.grid(row=1, column=2)

        self.B22 = Button(self.init_window_name, text="帮助", bg="lightgray",bd =6, width=8,command =lambda:self.about(2))  # 调用内部方法  加()为直接调用
        self.B22.grid(row=2, column=2)

        self.B32 = Button(self.init_window_name, text="帮助", bg="lightgray",bd =6, width=8,command =lambda:self.about(3))  # 调用内部方法  加()为直接调用
        self.B32.grid(row=3, column=2)

        self.B42 = Button(self.init_window_name, text="帮助", bg="lightgray",bd =6, width=8,command =lambda:self.about(4))  # 调用内部方法  加()为直接调用
        self.B42.grid(row=4, column=2)
        
        
        #计算结果显示
        self.L13 = Label(self.init_window_name,text='结果1',font=('Helvetica', '13'),bd =10,width=26) #原始数据录入框
        self.L13.grid(row=1, column=3)
        
        self.L23 = Label(self.init_window_name,text='结果2',font=('Helvetica', '13'),bd =10,width=26) #原始数据录入框
        self.L23.grid(row=2, column=3)
        
        self.L33 = Label(self.init_window_name,text='结果3',font=('Helvetica', '13'),bd =10,width=26) #原始数据录入框
        self.L33.grid(row=3, column=3)
        
        self.L43 = Label(self.init_window_name,text='结果4',font=('Helvetica', '13'),bd =10,width=26) #原始数据录入框
        self.L43.grid(row=4, column=3)
        
        #计算结果显示

        self.E14 = Entry(self.init_window_name,bg="lightgreen",bd =10,width=15,relief=SUNKEN) #原始数据录入框
        self.E14.grid(row=1, column=4)

        self.E24 = Entry(self.init_window_name,bg="lightgreen",bd =10,width=15,relief=SUNKEN) #原始数据录入框
        self.E24.grid(row=2, column=4)

        self.E34 = Entry(self.init_window_name,bg="lightgreen",bd =10,width=15,relief=SUNKEN) #原始数据录入框
        self.E34.grid(row=3, column=4)
        
        self.E44 = Entry(self.init_window_name,bg="lightgreen",bd =10,width=15,relief=SUNKEN) #原始数据录入框
        self.E44.grid(row=4, column=4)
        


        self.B61 = Button(self.init_window_name, text="计算", bg="lightgray",bd =10, width=15,command =self.computer)  # 调用内部方法  加()为直接调用
        self.B61.grid(row=6, column=1)


        self.B63 = Button(self.init_window_name, text="清除", bg="lightgray",bd =10, width=15,command =self.clear)  # 调用内部方法  加()为直接调用
        self.B63.grid(row=6, column=3)

    #操作计算函数
    def computer(self):
        
        try:
  
            self.E14.delete(0,'end')
            E01 = float(self.E01.get())
            E11 = float(self.E11.get())

            E14=E01+E01*E11
            self.E14.insert('insert', '%.2f'%E14)
        

            self.E24.delete(0,'end')
            E21 = float(self.E21.get())
            #E24=(E14/273.15)*(273.15+E31)
            E24=(E14/273.15)*(273.15+E21)
            self.E24.insert('insert', '%.2f'%E24)
            

            self.E34.delete(0,'end')
            E31 = float(self.E31.get())
            E24 = float(self.E24.get())
            E41 = float(self.E41.get())
            #E24=(E14/273.15)*(273.15+E31)
            E34=((E21-40)/((E31-40))*E24+E24)*E41
            self.E34.insert('insert', '%.2f'%E34)
            
 
            self.E44.delete(0,'end')
            E51 = float(self.E51.get())
    
            #E44=E34*(E51/100)+E34
            E44=E34*(E51/100)+E34
            self.E44.insert('insert', '%.2f'%E44)
        except ValueError:
            mess.showinfo(title='错误',message='数据未输入或输入错误')
            
            
    def clear(self):
        self.E14.delete(0,'end')
        self.E24.delete(0,'end')
        self.E34.delete(0,'end')
        self.E44.delete(0,'end')

    def about(self,row):
        help_list=['说明0','说明1',
                   '说明2','说明3',
                   '说明4']
        return mess.showinfo(title='帮助',message=help_list[row])


def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()
