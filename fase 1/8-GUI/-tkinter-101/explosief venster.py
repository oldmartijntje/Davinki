import tkinter

window = tkinter.Tk()

print('6')

colors = ['black','purple','red','orange','yellow']
times = 6
size = 50
def grow():
    global size
    global times
    global colors
    size += 50
    times -= 1
    window.configure(bg=colors[times-1])
    window.geometry(f'{size}x{size}')
    if times != 0:print(times)
    else: 
        print('BOOM!')
        window.destroy()


window.title('“My First Window”')
window.geometry(f'{size}x{size}')
for x in range(6):
    window.after(1000 * (x+1), grow)
window.mainloop()