from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

mp_intro = Tk()
mp_intro.geometry("360x400")
mp_intro.title('Love Confirming Program')
mp_intro.configure(background='grey')

img = ImageTk.PhotoImage(Image.open(r'MRGUY.jpg'))
panel = Label(mp_intro, image = img)
panel.pack()

def intro_to_menu():
    main_menu()
    mp_intro.destroy()

bt_intro = Button(mp_intro, text='CLICK TO CONTINUE', fg='black', bg='white', command=intro_to_menu())
bt_intro.place(x=300, y=300)
bt_intro.pack()

mp_intro.mainloop()