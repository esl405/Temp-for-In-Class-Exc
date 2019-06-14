import tkinter

from tkinter import *
from tkinter import Label

import random
user_choice=0
#options=["Rock", "Paper", "Scissor"]
#Comp_Choice=random.choice(options)
def new_window():
    top=Toplevel()
    top.title("Results:")
    top.geometry("300x200")
    line1=Label(top, Text="User Choice: ") #confirm
    top.mainloop()




def click_button(user_choice):
    options=["Rock", "Paper", "Scissor"]
    Comp_Choice=random.choice(options)
    #window2=Tk.Toplevel()
    #Label(text="Results: ").pack(side=TOP) 
    #window2=Label(root, text="You Chose: " + user_choice).pack(side=RIGHT)
    #window2=Label(root, text="Comp Chose: " + Comp_Choice).pack(side=BOTTOM)
    #window2.pack()
    #print("You Chose: " + user_choice)
    #print("Comp Chose: " + Comp_Choice)
    if user_choice == Comp_Choice:
        print ("Tie")
        new_window
    elif user_choice == "Rock" and Comp_Choice == "Paper":
        print ('You Win')
    elif user_choice == "Rock" and Comp_Choice == "Scissor":
        print ("You Loose")
    elif user_choice == "Paper" and Comp_Choice== "Rock":
        print ("You Win")
    elif user_choice == "Paper" and Comp_Choice == "Scissor":
        print ("You Loose")
    elif user_choice == "Scissor" and Comp_Choice== "Paper":
        print ("You Win")
    elif user_choice == "Scissor" and Comp_Choice == "Rock":
        print ("You Loose")

root=Tk()
root.title("Choose One:")
root.geometry("500x500")
Rock=Button(root, text='Rock',command=lambda:[click_button("Rock"), new_window()]).pack(side=LEFT)
Button(root, text='Paper',command=lambda:[click_button("Paper"), new_window()]).pack(side=LEFT)
Button(root, text='Scissor',command=lambda:[click_button("Scissor"), new_window()]).pack(side=LEFT)
Button(root, text='Quit',command=root.quit, fg='red').pack(side=LEFT)
root.mainloop()



