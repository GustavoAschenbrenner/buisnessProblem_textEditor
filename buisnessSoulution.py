from tkinter import *
#need to install on all machines
from tkmacosx import Button

def save():
	text1.config(text="saved")
def auto_check():
	text2.config(text="checked")
def clear():
	text3.config(text="cleared")

# Create the main window
root = Tk()
root.title("Enter Title Here")

#Set size of window
root.geometry("1200x600")

# Create buttons
button_save = Button(root, text="save", background='green',command=save)
text1 = Label(root,text="unsaved",height=5,width=52)
button_check = Button(root, text="auto check",background='skyBlue', command=auto_check)
text2 = Label(root,text="unchecked",height=5,width=52)
button_clear = Button(root, text="clear",background='red',command=clear)
text3 = Label(root,text="uncleared",height=5,width=52)

#text box
text_box = Text(height=600, width=300)





# Place widgets in window (with grid function!)
button_save.grid(row=0,column=0)
button_check.grid(row=0,column=0)
button_clear.grid(row=0,column=0)
text1.grid(row=0,column=0)
text2.grid(row=0,column=0)
text3.grid(row=0,column=0)
text_box.grid(row=0,column=0)

#button code


# Start the GUI event loop
root.mainloop()