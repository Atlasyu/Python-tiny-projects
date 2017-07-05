from tkinter import *

window = Tk()

def convert():
    grams = float(e1_value.get())*1000
    pounds = float(e1_value.get())*2.20462
    ounces = float(e1_value.get())*35.274

    t1.insert('1.0',grams)
    t2.insert(END,pounds)
    t3.insert(END,ounces)


b1 = Button(window,text='Convert',command=convert,height=1,width=15)
b1.grid(row=0,column=3,columnspan=3)


e1_value = StringVar()
e1=Entry(window,textvariable = e1_value,width=8)
e1.grid(row=0,column=0)
l0 = Label(window,height=1,width=5,text='kg')
l0.grid(row=0,column=1)

t1 = Text(window,height=1,width=8)
t1.grid(row=1,column=0)
l1 = Label(window,height=1,width=5,text='grams')
l1.grid(row=1,column=1)

t2 = Text(window,height=1,width=8)
t2.grid(row=1,column=2)
l2 = Label(window,height=1,width=5,text='pounds')
l2.grid(row=1,column=3)

t3 = Text(window,height=1,width=5)
t3.grid(row=1,column=4)
l2 = Label(window,height=1,width=5,text='ounces')
l2.grid(row=1,column=5)

window.mainloop()
