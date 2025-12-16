from tkinter import *
#need to install on all machines
from tkmacosx import Button


# Create the main window
root = Tk()
root.title("Enter Title Here")

#Set size of window
root.geometry("1200x600")

# Create buttons
button_save = Button(root, text="save", background='green')
button_check = Button(root, text="auto check", background='skyBlue')
button_clear = Button(root, text="clear", background='red')

#text box
text_box = Text(height=600, width=300)

# Place widgets in window (with pack function!)
button_save.pack()
button_check.pack()
button_clear.pack()
text_box.pack()

#button code


# Start the GUI event loop
root.mainloop()