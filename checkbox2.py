from tkinter import *
root=Tk()
root.geometry("500x500")
lbltitle=Label(root,text="checkbox Button")
lbltitle.grid(row=0, column=0, columnspan=2)


check1=IntVar()
check2=IntVar()

def fun1():
    if check1.get()==1 and check2.get()==1:
        lbl.configure(text="you select : java and python")
    elif check1.get()==1:
        lbl.configure(text="you select : java")
    elif check2.get()==1:
        lbl.configure(text="you select: python")
    else:
        lbl.configure(text="yoy select none ")


chkbtn1=Checkbutton(root, text="java", onvalue=1, offvalue=0, command=fun1, variable=check1)
chkbtn2=Checkbutton(root, text="python", onvalue=1, offvalue=0, command=fun1, variable=check2)
chkbtn1.grid(row=1, column=1)
chkbtn2.grid(row=2, column=1)
lbl=Label(root, text="")
lbl.grid(row=3,column=1)
root.mainloop()