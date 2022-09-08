import tkinter
import random
from tkinter.messagebox import showerror, showwarning, showinfo

#imported this name list from my uno bot names
grabbelton = ['thomas', 'thom', 'muik', 'coen', 'staninna', 'stijn', 'florida man', 'mandrex', 'bob', 'grian', 'mumbo jumbo', 'scar', '[CLASSEFIED]', 'george',
'lianne', 'tommy', 'tiffany', 'katie', 'jase', 'lennert', 'mellodie', 'mark rutte', 'Master of scares', 'Null', 'Herobrine', 'None', 'Undefined', 'liam', 'anne', 'colorblind guy', 
'Ms.Kittens', 'attack helicopter', 'mr Blue Sky','joe','Vogeljongen', 'kaas', 'peter quill','Nat','Loki','Nick Furry','Vision', 'Eather', 'Mind Stone', 'Power Stone','Tesseract','Wanda', 'Soul Stone', 'Time Stone',
'Dr Strange','Coulson', 'Banner','Peter Parker','Tony Stark', 'Scott Lang','pjotter', 'Thanos', 'Thor', 'GLaDOS', 'chell', 'Phileine', 'emiel', 'twan', 'david', 'joelia', 'sneal', 'pieter', 'merijn', 'marjin',
'oldmartijntje', 'martijn', 'mercury', 'lara', 'steve jobs', 'mark zuckerburg', 'elon musk', 'sinterklaas', 'bart', 'ewood', 'mathijs', 'joris', 'zwarte piet','Gamora','Why Is Gamora?','I Am Groot','Rocket Raccoon','KORG',
'izuku','bakugo','uraraka','iida','mineta','todoroki','Eris','Sylphiette','Rudeus','Roxy','Tomori','Ruijerd','neko',
'Nebula' ,'Drax','Hugo de Jonge','thierry baudet','Jesse Klaver','Djoopie','MisterPringleMan','Agent Carter','Misterio','Captain Marvel','Odin','Stan Lee','Fitz', 'Hawk Eye','Skye','Black Panther','Jemma Simmons', '', 'Quick silver','Wolverine', 'Deadpool','Flash','SuperMan','Batman','Mantis']

def grabbel():
    global grabbelton
    chosen = random.randint(0,len(grabbelton)-1)
    showinfo('grabbellen', f'Gefeliciteerd, je hebt een {grabbelton[chosen]} gegrabbeld!')
    grabbelton.pop(chosen)
    amount.set(len(grabbelton))

window = tkinter.Tk()
amount = tkinter.StringVar(value=len(grabbelton))
label = tkinter.Label(window)
label.configure(textvariable=amount)
label.pack(ipadx=10, ipady=10, fill='y')
button = tkinter.Button(text='Grabbel', bg="white", fg="black", command=grabbel)
button.pack(pady = 20, padx = 20)
window.mainloop()