from tkinter import *
from tkinter import messagebox

mp = Tk()
mp.geometry("720x720")
mp.title('Note Creator')
mp.configure(background='pink')


lb = Label(mp,text = 'save your story or making contents with "Note Creator" ',fg = 'blue',bg = 'yellow')
lb.config(font =("Courier", 15))
lb.pack()

lb1 = Label(mp,text = "Let's make some note ",fg = 'black',bg = 'pink')
lb1.pack()
lb.pack()

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

txt = open("for note(test).txt","w+")

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

T = Text(mp, height = 5, width = 52,bg = "light pink")
T.pack()

bt2 = Button(mp,text= 'SHOW',fg='black' ,bg = 'red',command = inserttobox)
bt2.place(x = 300,y = 300)
bt2.pack()




'''
## ไม่ส่งข้อมูลไปที่ Messagebox

def another():
    mp1 = Tk()
    mp1.geometry("200x170")
    mp1.title('Food Program')

    lb7 = Label(mp1, text='Please select food item.')
    lb7.pack()
    v1 = IntVar()
    v2 = IntVar()
    v3 = IntVar()
    v4 = IntVar()

    cb1 = Checkbutton(mp1, text='Noodle : 45 ฿', variable=v1, onvalue=1, offvalue=0)
    cb1.var = v1
    cb1.pack()

    cb2 = Checkbutton(mp1, text='fried rice : 50 ฿', variable=v2, onvalue=1, offvalue=0)
    cb2.var = v2
    cb2.pack()

    cb3 = Checkbutton(mp1, text='bottle of water : 10 ฿', variable=v3, onvalue=1, offvalue=0)
    cb3.var = v3
    cb3.pack()

    cb4 = Checkbutton(mp1, text='orange juice : 20 ฿', variable=v4, onvalue=1, offvalue=0)
    cb4.var = v4
    cb4.pack()



    def calc():
        if cb1.var.get() == 1:
            summy.append(int(45))
        else:
            summy.append(int(0))

        if cb2.var.get() == 1:
            summy.append(int(50))
        else:
            summy.append(int(0))

        if cb3.var.get() == 1:
            summy.append(int(10))
        else:
            summy.append(int(0))

        if cb4.var.get() == 1:
            summy.append(int(20))
        else:
            summy.append(int(0))

        messagebox.showinfo('Food prices', 'Total : ' + str(summy))



    bt7 = Button(mp1, text='Order', bg='blue', fg='white', command=calc)
    bt7.pack()

    mp1.mainloop()

bt8 = Button(mp, text='another program', bg='blue', fg='white', command=another)
bt8.pack()
'''

bla3 = Label(mp,fg = 'black',bg = 'pink',text = '')
bla3.pack()
bla4 = Label(mp,fg = 'black',bg = 'pink',text = '')
bla4.pack()

z = Label(mp,fg = 'black',bg = 'pink',text = 'This program made by mr.guy thongtrachoo')
z.pack()

mp.mainloop()



