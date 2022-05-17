from tkinter import *

root = Tk()
root.title("Posting App")
root.geometry('400x300')
root['bg'] = 'blue'

frame1 = Frame(root, width=200, height=300, bg="red")
frame1.pack(side="right")

def printValue():
    post = Post.get()
    Label(frame1, text=f'{post}', bg='red').pack()

Post = Entry(root)
Post.pack(pady=30)

Button(root, text="Submit Post", padx=10, pady=5, command=printValue).pack()

root.mainloop()
