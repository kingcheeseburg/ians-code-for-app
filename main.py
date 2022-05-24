from tkinter import *

root = Tk()
root.title("Posting App")
root.geometry('400x300')
root['bg'] = 'blue'

frame1 = Frame(root, width=200, height=300, bg="red")
frame1.config(width=200, height=150)
frame1.pack(side=RIGHT, fill='both', expand=True)

frame2 = Frame(root, bg="orange")
frame2.config(width=200, height=150)
frame2.pack(side=LEFT, fill='both', expand=True)

def printValue():
    post = Post.get()
    Label(frame1, text=f'{post}', bg='red').pack(side=TOP)

Post = Entry(frame2)
Post.pack(side=TOP)

Button1 = Button(frame2, text="Submit Post", command=printValue)
Button1.pack(side=LEFT)

root.mainloop()
