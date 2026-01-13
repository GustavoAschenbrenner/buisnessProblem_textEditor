from tkinter import *
#need to install on all machines
from tkmacosx import Button

def save():
	root.title(text1.get(text="saved"))
def auto_check():
	root.title(text2.get(text="checked"))
def clear():
	root.title(text3.get(text="cleared"))

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





# Place widgets in window (with pack function!)
button_save.pack()
button_check.pack()
button_clear.pack()
text1.pack()
text2.pack()
text3.pack()
text_box.pack()

#button code


# Start the GUI event loop
root.mainloop()