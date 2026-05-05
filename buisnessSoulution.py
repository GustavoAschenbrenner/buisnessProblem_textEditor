from tkinter import *
#need to install on all machines
from tkmacosx import Button



def save():
	text1.config(text="saved")
	with open("demofile.txt","w") as f:
		f.write("this is what will be inside of that file")
		draft = textbox.get("1.0",END)
		print("you entered:")
		print(draft)


def auto_check():
	text2.config(text="checked")
def clear():
	text3.config(text="cleared")
def openfile():
	text4.config(text="opened")


# Create the main window
root = Tk()
root.title("Enter Title Here")

#Set size of window
root.geometry("1600x800")

# Create buttons
button_save = Button(root, text="save", background='green',command=save)
text1 = Label(root,text="unsaved",height=5,width=52)
button_check = Button(root, text="auto check",background='skyBlue', command=auto_check)
text2 = Label(root,text="unchecked",height=5,width=52)
button_clear = Button(root, text="clear",background='red',command=clear)
text3 = Label(root,text="uncleared",height=5,width=52)
button_open = Button(root, text="open", background='yellow',command=openfile)
text4 = Label(root,text="unopened",height=5,width=52)
#text box

textbox = Text(height=300, width=150)




# Place widgets in window (with grid function!)
button_save.grid(row=0, column=0)
button_check.grid(row=0, column=1)
button_clear.grid(row=0, column=2)
button_open.grid(row=0, column=3)
text1.grid(row=1, column=0)
text2.grid(row=1, column=1)
text3.grid(row=1, column=2)
text4.grid(row=1, column=3)
textbox.grid(row=2,column=0,columnspan=3)

#button code


# Start the GUI event loop
root.mainloop()