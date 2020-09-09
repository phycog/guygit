from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("720x720")
window.title('gpu choosing program')
window.configure(background='grey')

choosed_gpu = []

def click1():
    choosed_gpu.append(16000)

def click2():
    choosed_gpu.append(8500)

def click3():
    choosed_gpu.append(6000)

def click4():
    choosed_gpu.append(11600)

def click5():
    choosed_gpu.append(10000)

def click6():
    choosed_gpu.append(1600)

def total():
    messagebox.showinfo('Total : ', 'Total : ' + str(sum(choosed_gpu)))


lb1 = Label(window,text = 'MENU List',fg = 'black',bg = 'grey')
lb1.config(font =("Courier", 15))
lb1.pack()



lb2 = Label(window,text = 'GTX 2080 TI : 16,000 ฿ ',fg = 'black',bg = 'yellow')
lb2.pack()

bt1 = Button(window,text = 'Choose',bg = 'red',fg = 'white',command = click1 )
bt1.pack()

#-----------------------------------------------------------------------------------
lb3 = Label(window,text = 'GTX 1660 TI : 8,500 ฿ ',fg = 'black',bg = 'yellow')
lb3.pack()

bt2 = Button(window,text = 'Choose',bg = 'red',fg = 'white',command = click2 )
bt2.pack()

#-----------------------------------------------------------------------------------
lb4 = Label(window,text = 'GTX 2080 TI : 6,000 ฿ ',fg = 'black',bg = 'yellow')
lb4.pack()

bt3 = Button(window,text = 'Choose',bg = 'red',fg = 'white',command = click3 )
bt3.pack()

#-----------------------------------------------------------------------------------
lb5 = Label(window,text = 'GTX 2080 TI : 11,600 ฿ ',fg = 'black',bg = 'yellow')
lb5.pack()

bt4 = Button(window,text = 'Choose',bg = 'red',fg = 'white',command = click4 )
bt4.pack()

#-----------------------------------------------------------------------------------
lb6 = Label(window,text = 'GTX 2080 TI : 10,000 ฿ ',fg = 'black',bg = 'yellow')
lb6.pack()

bt5 = Button(window,text = 'Choose',bg = 'red',fg = 'white',command = click5 )
bt5.pack()

#-----------------------------------------------------------------------------------
lb7 = Label(window,text = 'GTX 2080 TI : 1,600 ฿ ',fg = 'black',bg = 'yellow')
lb7.pack()

bt6 = Button(window,text = 'Choose',bg = 'red',fg = 'white',command = click6 )
bt6.pack()

#-----------------------------------------------------------------------------------

bla = Label(window,fg = 'black',bg = 'grey',text = '')
bla.pack()
bla1 = Label(window,fg = 'black',bg = 'grey',text = '')
bla1.pack()


bt8 = Button(window,text = 'Total',bg = 'blue',fg = 'white',command = total)
bt8.pack()





window.mainloop()