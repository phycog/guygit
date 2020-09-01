from tkinter import *
from tkinter import messagebox

MainWindow = Tk()
MainWindow.title('Say Hi Program')
MainWindow.geometry('250x250')
MainWindow.configure(background='red')

z = Label(MainWindow,fg = 'black',bg = 'yellow',text = 'This programs made by mr.guy thongtrachoo')
z.pack()
pp = Label(MainWindow,fg = 'black',bg = 'yellow',text = 'What is your A.K.A.')
pp.pack()

entry = Entry(MainWindow,bd = 2)
entry.pack()




#messagebox.showinfo('Hi! Mr.Guy ' ,'This is your fucking badass programs')
#messagebox.askquestion('Hi! Mr.Guy ' ,'Are you badass?')
def badass_or_not():
    yy = entry.get()
    messagebox.showinfo('you are bad ass','That is right! '+ yy)

bt = Button(MainWindow,text = 'Who are you?',bg = 'green',fg = 'white',command = badass_or_not)
bt.pack()
#xx = messagebox.showinfo('i know that you are bad ass','and you know it')


MainWindow.mainloop()

