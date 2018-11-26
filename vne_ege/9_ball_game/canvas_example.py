import tkinter


def create_ball():
    canvas.create_oval(10, 10, 20, 20)


root = tkinter.Tk("Главное окно")
root.geometry("640x480")

canvas = tkinter.Canvas(root)
canvas.pack()

button_start = tkinter.Button(root, text="Start", command=create_ball)
button_start.pack()

root.mainloop()
