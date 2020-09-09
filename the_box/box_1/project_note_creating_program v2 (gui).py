from tkinter import *
from tkinter import messagebox

#defind window of program
mp = Tk() #name of window
mp.geometry("720x720") #size of window
mp.title('Note Creator') #title name of window
mp.configure(background='pink') # blackgorund color

#defind label (output something)
lb = Label(mp,text = 'save your story or making contents with "Note Creator" ',fg = 'blue',bg = 'yellow')
lb.config(font =("Courier", 15)) #defind size of font
lb.pack() #make text center

lb_slot = Label(mp,text = 'choose slot ',fg = 'black',bg = 'pink')
lb_slot.pack()

#defind fuction of input
en_slot = Entry(mp, bd = 2,bg = "light pink")
en_slot.pack()



def choose_slot():
    global sloted
    sloted = en_slot.get()
    messagebox.showinfo('OK : ', 'You slot : '+str(sloted))

def confirm_slot():
    global txt
    txt = open("for note(test)"+str(sloted)+".txt","w+")
    messagebox.showinfo('OK : ', 'Your slot is confirmed : '+str(sloted))

#defind fuction of command by using with def(function)
bt_slot = Button(mp,text= 'OK',fg='black' ,bg = 'red',command = choose_slot)
bt_slot.place(x = 300,y = 300)
bt_slot.pack()

bt_slot_con = Button(mp,text= 'Confirm slot',fg='black' ,bg = 'red',command = confirm_slot)
bt_slot_con.place(x = 300,y = 300)
bt_slot_con.pack()


lb1 = Label(mp,text = "Let's make some note ",fg = 'black',bg = 'pink')
lb1.config(font =("Courier", 13))
lb1.pack()

lb2 = Label(mp,text = 'Topic name ',fg = 'black',bg = 'pink')
lb2.pack()

en_topic = Entry(mp, bd = 2,bg = "light pink")
en_topic.pack()

lb3 = Label(mp,text = 'Insert date ',fg = 'black',bg = 'pink')
lb3.pack()

en_date = Entry(mp, bd = 2,bg = "light pink")
en_date.pack()


lb4 = Label(mp,text = 'Create the context ',fg = 'black',bg = 'pink')
lb4.pack()

en_context = Text(mp, height = 10,width = 25,bg = "light pink")
en_context.pack()

#defind vairieble for receive input
dataforbox = []

def confirm():
    str1 = en_topic.get()
    str2 = en_date.get()
    str3 = en_context.get("1.0","end")
    all = [str1,str2,str3]
    dataforbox.append(all)

    txt.write(str(all))
    messagebox.showinfo('Result','All : '+str1+" "+str2+" "+str3)

def inserttobox():
    T.insert(END, dataforbox)
    messagebox.showinfo('All done : ','Here..')

bla0 = Label(mp,fg = 'black',bg = 'pink',text = '')
bla0.pack()

bt = Button(mp,text= 'OK',fg='black' ,bg = 'red',command = confirm)
bt.place(x = 300,y = 300)
bt.pack()

bla = Label(mp,fg = 'black',bg = 'pink',text = '')
bla.pack()
bla1 = Label(mp,fg = 'black',bg = 'pink',text = '')
bla1.pack()

#defind some output function
T = Text(mp, height = 5, width = 52,bg = "light pink")
T.pack()

bt2 = Button(mp,text= 'SHOW',fg='black' ,bg = 'red',command = inserttobox)
bt2.place(x = 300,y = 300)
bt2.pack()




def another():
    window = Tk()
    window.geometry("480x480")
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

    lb1 = Label(window, text='MENU List', fg='black', bg='grey')
    lb1.config(font=("Courier", 15))
    lb1.pack()

    lb2 = Label(window, text='GTX 2080 TI : 16,000 ฿ ', fg='black', bg='yellow')
    lb2.pack()

    bt1 = Button(window, text='Choose', bg='red', fg='white', command=click1)
    bt1.pack()

    # -----------------------------------------------------------------------------------
    lb3 = Label(window, text='GTX 1660 TI : 8,500 ฿ ', fg='black', bg='yellow')
    lb3.pack()

    bt2 = Button(window, text='Choose', bg='red', fg='white', command=click2)
    bt2.pack()

    # -----------------------------------------------------------------------------------
    lb4 = Label(window, text='GTX 2080 TI : 6,000 ฿ ', fg='black', bg='yellow')
    lb4.pack()

    bt3 = Button(window, text='Choose', bg='red', fg='white', command=click3)
    bt3.pack()

    # -----------------------------------------------------------------------------------
    lb5 = Label(window, text='GTX 2080 TI : 11,600 ฿ ', fg='black', bg='yellow')
    lb5.pack()

    bt4 = Button(window, text='Choose', bg='red', fg='white', command=click4)
    bt4.pack()

    # -----------------------------------------------------------------------------------
    lb6 = Label(window, text='GTX 2080 TI : 10,000 ฿ ', fg='black', bg='yellow')
    lb6.pack()

    bt5 = Button(window, text='Choose', bg='red', fg='white', command=click5)
    bt5.pack()

    # -----------------------------------------------------------------------------------
    lb7 = Label(window, text='GTX 2080 TI : 1,600 ฿ ', fg='black', bg='yellow')
    lb7.pack()

    bt6 = Button(window, text='Choose', bg='red', fg='white', command=click6)
    bt6.pack()

    # -----------------------------------------------------------------------------------

    bla = Label(window, fg='black', bg='grey', text='')
    bla.pack()
    bla1 = Label(window, fg='black', bg='grey', text='')
    bla1.pack()

    bt8 = Button(window, text='Total', bg='blue', fg='white', command=total)
    bt8.pack()

    window.mainloop()

bt8 = Button(mp, text='another program', bg='blue', fg='white', command=another)
bt8.pack()


bla3 = Label(mp,fg = 'black',bg = 'pink',text = '')
bla3.pack()
bla4 = Label(mp,fg = 'black',bg = 'pink',text = '')
bla4.pack()

z = Label(mp,fg = 'black',bg = 'pink',text = 'This program made by mr.guy thongtrachoo')
z.pack()

#range of window
mp.mainloop()



