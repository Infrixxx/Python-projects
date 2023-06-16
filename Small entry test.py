from tkinter import*



def Submit():
    
    Tab2=Tk()
        
    k="Boitumelo"
    Hello="Hey "+k
    Name=Label(Tab2,text=Hello,font=("Times new roman",50),fg="white",bg="Coral",relief=SUNKEN).grid(row=0,column=0)
    How=PhotoImage(file="How_are_you.png")
    Tab2.geometry("900x1000")
    Tab2.config(background="Coral")
    ImageL=Label(Tab2,image=How,bg="coral").grid(row=0,column=1)
    Q=Label(text="How are you doing today? ",font=("Times new roman",50),relief=RAISED,bg="coral",fg="white").grid(row=1,column=0)
    A=Entry(Tab2,font=("Times new Roman",50)).grid(row=2,column=0)
    Send=Button(Tab2,text="Submit",command=send).grid(row=3,column=0)
    Tab2.mainloop()


Window=Tk()
Window.config(background="Turquoise")
Trading=PhotoImage(file="Ask.png")
Tradei=Label(Window,image=Trading,background="Turquoise").grid(row=1,column=0)
NameL=Label(text="What is your name??",font=("Times New Roman",50),relief=RAISED).grid(row=0,column=1)
name=Entry(Window,font=("Times new roman",50))
Nw=Button(text="Submit",command=Submit).grid(row=1,column=2)
name.grid(row=1,column=1)

Window.mainloop()
