from tkinter import*
def add():
 a=int(n1.get())
 b=int(n2.get())
 c=a+b
 res.config(text=str(c))
def sub():
 a=int(n1.get())
 b=int(n2.get())
 c=a-b
 res.config(text=str(c))
def multi():
 a=int(n1.get())
 b=int(n2.get())
 c=a*b
 res.config(text=str(c))
def div():
 a=int(n1.get())
 b=int(n2.get())
 c=a/b
 res.config(text=str(c))
root=Tk()
root.title("simple calculator")
root.geometry("500x400+500+200")
root.resizable(False,False)
root.config(bg="lightgrey")
lbl=Label(root,text="simple calculator",fg="black",font=("Arial 20 bold"))
lbl.place(x=120,y=20)
lbl1=Label(root,text="Enter first no: ",fg="black",font=("Arial 15"))
lbl1.place(x=20,y=90)
lbl2=Label(root,text="Enter second no: ",fg="black",font=("Arial 15"))
lbl2.place(x=20,y=150)
n1=Entry(root,font=("Arial 15"))
n1.place(x=200,y=90)
n2=Entry(root,font=("Arial 15"))
n2.place(x=200,y=150)
res=Label(root,text="Result",fg="black",font=("Arial 15 bold"))
res.place(x=200,y=200)
btnadd=Button(root,text="ADD",font=("Arial 15"),fg="black",command=add)
btnadd.place(x=50,y=280)
btnsub=Button(root,text="SUB",font=("Arial 15"),fg="black",command=sub)
btnsub.place(x=150,y=280)
btnmulti=Button(root,text="MULTI",font=("Arial 15"),fg="black",command=multi)
btnmulti.place(x=250,y=280)
btndiv=Button(root,text="DIV",font=("Arial 15"),fg="black",command=div)
btndiv.place(x=370,y=280)
root.mainloop()





