from tkinter import *
from tkinter import messagebox

mp = Tk()
mp.geometry("360x400")
mp.title('INFO BUDDY')
mp.configure(background='grey')
w = 'white'
g = 'grey'

lb = Label(mp,text = "MAIN MENU" ,fg = 'black',bg = g)
lb.config(font =("Courier", 15))
lb.pack()

bla01 = Label(mp,fg = 'black',bg = g,text = '')
bla01.pack()

bt1 = Button(mp,text= 'ADD INFO',fg='black' ,bg = w,)
bt1.place(x = 300,y = 300)
bt1.pack()

bla02 = Label(mp,fg = 'black',bg = g,text = '')
bla02.pack()

bt2 = Button(mp,text= 'SHOW INFO',fg='black' ,bg = w,)
bt2.place(x = 300,y = 300)
bt2.pack()

bla03 = Label(mp,fg = 'black',bg = g,text = '')
bla03.pack()

bt3 = Button(mp,text= 'FIX INFO',fg='black' ,bg = w,)
bt3.place(x = 300,y = 300)
bt3.pack()

bla04 = Label(mp,fg = 'black',bg = g,text = '')
bla04.pack()

bt4 = Button(mp,text= 'OPTION',fg='black' ,bg = w,)
bt4.place(x = 300,y = 300)
bt4.pack()

bla05 = Label(mp,fg = 'black',bg = g,text = '')
bla05.pack()

bt5 = Button(mp,text= 'EXIT',fg='black' ,bg = w, )
bt5.place(x = 300,y = 300)
bt5.pack()



bla0 = Label(mp,fg = 'black',bg = g,text = '')
bla0.pack()



bla = Label(mp,fg = 'black',bg = g,text = '')
bla.pack()
bla1 = Label(mp,fg = 'black',bg = g,text = '')
bla1.pack()

bla3 = Label(mp,fg = 'black',bg = g,text = '')
bla3.pack()
bla4 = Label(mp,fg = 'black',bg = g,text = '')
bla4.pack()

z = Label(mp,fg = 'black',bg = g ,text = 'This program made by mr.guy thongtrachoo')
z.pack()

mp.mainloop()



