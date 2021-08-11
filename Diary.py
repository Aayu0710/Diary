from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
Password = "Aayu"
root = Tk()
root.geometry("566x366")
root.title("MY DIARY")
img = PhotoImage(file="C:\\Users\\HP\\Downloads\\Diary.png")
root.iconphoto(False, img)

#sval = StringVar()
#sval.set("")
canvas = Canvas(root)
canvas.pack()

bg_image = PhotoImage(file="C:\\Users\\HP\\Downloads\\Nature.png")
bg_l = Label(root, image=bg_image)
bg_l.place(relwidth=1, relheight=1)


# This frame is for writing date
f1 = Frame(root, bd=5, bg="brown")
f1.place(relx=0.5, relwidth=0.2, relheight=0.1, anchor="n")
entry = Entry(f1)
entry.place(relwidth=0.7, relheight=1)

# I will create a button
b1 = Button(f1, text="Open diary", font="italic 9", fg="brown", command=lambda:Pass(entry.get()))
b1.place(relx=0.75, relheight=1)

def Pass(entry):
    if entry == Password:
        tmsg.showinfo("Welcome!", " Hope you will recall all yor memories")
        text = Text(f2, font="italic")
        text.pack(expand=True, fill=BOTH)
        yourMenu = Menu(f2)
        m1 = Menu(yourMenu, tearoff=0)
        m1.add_command(label="save", command=myfunc)
        yourMenu.add_cascade(label="File", menu=m1)
        root.config(menu=yourMenu)



    else:
        label["text"] = "You are not Aayushi"
        tmsg.showwarning("Unauthorised", "It seems you are not the one")
        root.destroy()





# Now i will create thw lower frame
f2 = Frame(root,bg="brown",bd=5)
f2.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.6, anchor="n")
label = Label(f2)
label.place(relwidth=1,relheight=1)

root.mainloop()