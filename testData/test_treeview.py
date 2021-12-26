import tkinter as tk
from tkinter import ttk
from typing_extensions import IntVar
root = tk.Tk()
root.geometry('320x240')
tk.Label(root,text='成绩表').pack()
area=('#','数学','语文','英语')
ac=('all','m','c','e')
R1 = tk.IntVar()
R1.set(0)
data=[('张三','90','88','95'),
      ('李四',R1.get(),'92', '90'),
      ('王二','88','90', '91')
      ]
tv=ttk.Treeview(root,columns=ac,show='headings',
                height=5)
for i in range(4):
    tv.column(ac[i],width=70,anchor='e')
    tv.heading(ac[i],text=area[i])
tv.pack()
for i in range(3):
    tv.insert('','end',values=data[i])

def run_RSA():
    R1.set(1000)
    tv.item('I002',values=('李峰',R1.get(),'88','66'))

ttk.Button(root, text="RSA", command=run_RSA).pack()
root.mainloop()