import tkinter as tk
import os

if os.path.exists('actions.log'):
    logFile = open('actions.log', 'a')
else:
    logFile = open('actions.log', 'w')


def aanUit():
    global lichtAanOfUit
    if lichtAanOfUit == True:
        lichtAanOfUit = False
        print("light is off")
        button["text"] = "Switch Light On"
        window["bg"] = "black"
        logFile.write("light is off\n")
    elif lichtAanOfUit == False:
        lichtAanOfUit = True
        print("light is on")
        button["text"] = "Switch Light Off"
        window["bg"] = "yellow"
        logFile.write("light is on\n")
    
window = tk.Tk()
window.geometry('300x200')
window.configure(bg='yellow')
button = tk.Button(text='Switch Light Off', bg="white", fg="black", command=aanUit)
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code
window.title("what if i don't want the title to be TK?")
lichtAanOfUit = True
# schijf hier tussen je code

window.mainloop()
logFile.close()