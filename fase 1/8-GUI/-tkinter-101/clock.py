import tkinter
import time
window = tkinter.Tk()
string = tkinter.StringVar(value=time.strftime('%H:%M:%S'))
label = tkinter.Label(window)
label.configure(textvariable=string)
label.pack()

def tick():
    global string
    string.set(time.strftime('%H:%M:%S'))
    window.after(1000, tick)
tick()
window.mainloop()
