# listbox = A listing of selectable text items within it's own container



#**************************************************
#FUNCTIONS FOR THE COMMNANDS OF THE BUTTONS
##**************************************************

def submit():

    food = []                                   #This is the list for the food

    for index in listbox.curselection():        #listbox.curselection() is for current selection in listbox
        food.insert(index,listbox.get(index))   #This will add the selection to the list, "FOOD", gets the
                                                #index number as well as the item at that index number

    print("You have ordered: ")
    for index in food:                        #This will print the items stored in the list
        print(index)

def add():                                          #This is a function to add to the list box
    listbox.insert(listbox.size(),entryBox.get())   #listbox.size() retrieves number of items in listbox
                                                    #entryBox.get() retrieves text from entryBox

    listbox.config(height=listbox.size())           #This is to update the size of the listbox for every entry

def delete():
    for index in reversed(listbox.curselection()): #we reverse the current selection as the indexes are
                                                   #changing with every item deleted
        listbox.delete(index)

    listbox.config(height=listbox.size())

from tkinter import *

window = Tk()

#********************************************
#This is to add a listbox, below:
#********************************************
listbox = Listbox(window,
                  bg="#f7ffde",             #background of the list box
                  font=("Constantia",35),   #font of the list box
                  width=12,                 #width of the list box
                  selectmode=MULTIPLE)      #To be able to select more than one
listbox.pack()
#*****************************************************************
#This is to add/append to the list box a listbox and index, below:
#*****************************************************************
listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height=listbox.size())   #This is to change the current
                                        # size of our list box, to adjust to the items in the list box


#********************************************************
#WE CREATE AN ENTRY BOX BEFORE THE SUBMIT BUTTON
#********************************************************
entryBox = Entry(window)
entryBox.pack()

frame = Frame(window)   #important for the process of grouping and organizing other widgets
frame.pack()

#**********************************************
#This is to add buttons to the list box :
#**********************************************

submitButton = Button(frame,text="submit",command=submit)
submitButton.pack(side=LEFT)

addButton = Button(frame,text="add",command=add)
addButton.pack(side=LEFT)

deleteButton = Button(frame,text="delete",command=delete)
deleteButton.pack(side=LEFT)

window.mainloop()