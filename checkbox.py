from tkinter import *
root=Tk()
lbltitle=Label(root,text="checkbox Button")
lbltitle.grid(row=0, column=0, columnspan=2)
check1=IntVar()
check2=IntVar()

def fun1():
    if check1.get()==1:
        print("you select : java")

def fun2():
    if check2.get()==0:
        print("you select : pyhton")


chkbtn1=Checkbutton(root, text="java", onvalue=1, offvalue=0, command=fun1, variable=check1)
chkbtn2=Checkbutton(root, text="python", onvalue=1, offvalue=0, command=fun2, variable=check2)
chkbtn1.grid(row=1, column=1)
chkbtn2.grid(row=2, column=1)

root.mainloop()