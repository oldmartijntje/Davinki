import tkinter as tk
def aanUit():
    global lichtAanOfUit
    if lichtAanOfUit == True:
        lichtAanOfUit = False
        print("light is off")
        button["text"] = "Switch Light On"
        window["bg"] = "black"
    elif lichtAanOfUit == False:
        lichtAanOfUit = True
        print("light is on")
        button["text"] = "Switch Light Off"
        window["bg"] = "yellow"
    
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