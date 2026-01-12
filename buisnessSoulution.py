from tkinter import *
#need to install on all machines
from tkmacosx import Button

def save():
	root.title(text1.get())
def auto_check():
	root.title(text2.get())
def clear():
	root.title(text1.get())

# Create the main window
root = Tk()
root.title("Enter Title Here")

#Set size of window
root.geometry("1200x600")

# Create buttons
button_save = Button(root, text="save", background='green',command=save)
button_check = Button(root, text="auto check", background='skyBlue')
button_clear = Button(root, text="clear", background='red')

#text box
text_box = Text(height=600, width=300)

text1 = Text(root, height=5, width=52)
text2 = Text(root, height=5, width=52)
text3 = Text(root, height=5, width=52)


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