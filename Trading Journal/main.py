from tkinter import *

fontsize=15

window=Tk()
window.geometry("1500x920")

#_________________________________________________________________________________________
# ------------------------------------Functions-------------------------------------------
#_________________________________________________________________________________________
def submit():
    print("You entered "+Risk_percent_entry.get())


#_________________________________________________________________________________________
# ------------------------------------Menubar-------------------------------------------
#_________________________________________________________________________________________
menubar=Menu(window)            #adding menubar to window
window.config(menu=menubar)     #configuring our menu as menubar
FileMenu=Menu(menubar,tearoff=0)          #assigning our menu to filemenu
menubar.add_cascade(label="File",menu=FileMenu)
FileMenu.add_command(label="Open")
FileMenu.add_command(label="Save")
FileMenu.add_command(label="Close")

#_________________________________________________________________________________________
# -----------------------Risk percent & Capital-------------------------------------------
#_________________________________________________________________________________________

Risk_percent=Label(text="Risk percent (%)",
                   font=("Times new Roman",fontsize)).grid(row=0,column=0)

Capital=Label(text="What is your capital",
              font=("Times new Roman",fontsize),
              padx=40).grid(row=1,column=0)

Risk_percent_entry=Entry(window).grid(row=0,column=1)
Capital_entry=Entry(window).grid(row=1,column=1)

Risk_percent_submit=Button(window,text="Submit", command=submit).grid(row=0,column=2)
Capital_submit=Button(window,text="Submit").grid(row=1,column=2)



space=Label(window,text=" ").grid(row=2,column=2)
space=Label(window,text=" ").grid(row=3,column=2)

Day=Label(window,text="Day",font=("Times new Roman",fontsize),relief=RAISED,padx=40).grid(row=4,column=0)
entry=Entry().grid(row=5,column=0)

Risk_amount=Label(window,text="Risk Amount",font=("Times new Roman",fontsize),relief=RAISED)
Risk_amount.grid(row=4,column=1)
entry=Entry(width=20).grid(row=5,column=1)



Indice=Label(window,text="Indice\Forex",font=("Times new Roman",fontsize),relief=RAISED)
Indice.grid(row=4,column=2)
entry=Entry().grid(row=5,column=2)

Opening_Balance=Label(window,text="Opening Balance",font=("Times new Roman",fontsize),relief=RAISED)
Opening_Balance.grid(row=4,column=3)
entry=Entry(width=20).grid(row=5,column=3)

Profit=Label(window,text="Profit",font=("Times new Roman",fontsize),relief=RAISED,bg="Green",padx=30)
Profit.grid(row=4,column=4)
entry=Entry().grid(row=5,column=4)

Loss=Label(window,text="Loss",font=("Times new Roman",fontsize),relief=RAISED,bg="Red",padx=40)
Loss.grid(row=4,column=5)
entry=Entry().grid(row=5,column=5)

Closing_Balance=Label(window,text="Closing Balance",font=("Times new Roman",fontsize),relief=RAISED)
Closing_Balance.grid(row=4,column=6)
entry=Entry(width=30).grid(row=5,column=6)

Percent_Change=Label(window,text="Percent Change",font=("Times new Roman",fontsize),relief=RAISED)
Percent_Change.grid(row=4,column=7)
entry=Entry().grid(row=5,column=7)

window.mainloop()

