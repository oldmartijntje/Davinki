import tkinter

window = tkinter.Tk()

box1 = tkinter.Label(
    window,
    text="Hello\ntkinter!",
    bg="#FF7000",
    fg="#007FFF"
)
box1.pack(
    ipadx=10,
    ipady=10,
    expand=True
)
window.configure(bg='#FF00BF')
window.title('Hello')
window.geometry('100x100')
window.mainloop()