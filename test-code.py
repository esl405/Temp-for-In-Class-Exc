#print ("hello world")

#Define F to Celsius Fxn

#c = 1
#def temp_f(f):
#    return (f-32) * 5/9
#c = temp_f (1)    
#print(c)
##def convert_temperature(f):
##    # (32°F − 32) × 5/9 = 0°C
##    return (f - 32) * 5/9
##
##c = convert_temperature(32)
##print(c) #> 0
#
#type("hello")
import tkinter


from tkinter import *
#top = tkinter.Tk()
root = Tk()
Widget=Label(None, text="Choose One")
Widget.pack()
Button (root, text='Rock', command=root.quit).pack(side=LEFT)
Button (root, text='Paper', command=root.quit).pack(side=LEFT)
Button (root, text='Scissor', command=root.quit).pack(side=LEFT)
root.mainloop()
#from tkinter import *
#widget=Label(None,text='testing')
#widget.pack()
#widget.mainloop()

