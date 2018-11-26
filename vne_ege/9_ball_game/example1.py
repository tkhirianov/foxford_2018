import tkinter


def hello():
    print("Left click somewhere")
    

def bye(event):
    print("Good by!")


root = tkinter.Tk()
button1 = tkinter.Button(master=root, text="Нажми меня!")
button1.pack()
button1["command"] = hello

root.bind("<Key>", bye)

root.mainloop()
