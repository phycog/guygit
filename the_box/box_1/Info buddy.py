from tkinter import *
from tkinter import messagebox
import sqlite3

mp = Tk()
mp.geometry("360x400")
mp.title('INFO BUDDY')
mp.configure(background='grey')
w = 'white'
g = 'grey'

lb = Label(mp,text = "ADD INFO" ,fg = 'black',bg = g)
lb.config(font =("Courier", 15))
lb.pack()

lb1 = Label(mp,text = "number",fg = 'black',bg = g)
lb1.pack()
lb.pack()

en_number = Entry(mp, bd = 2,bg = w)
en_number.pack()

lb2 = Label(mp,text = 'name',fg = 'black',bg = g)
lb2.pack()

en_name = Entry(mp, bd = 2,bg = w)
en_name.pack()

lb3 = Label(mp,text = 'sex ',fg = 'black',bg = g)
lb3.pack()

en_sex = Entry(mp, bd = 2,bg = w)
en_sex.pack()

lb4 = Label(mp,text = 'age',fg = 'black',bg = g)
lb4.pack()

en_age = Entry(mp, bd = 2,bg = w)
en_age.pack()

lb5 = Label(mp,text = 'salary',fg = 'black',bg = g)
lb5.pack()

en_salary = Entry(mp, bd = 2,bg = w)
en_salary.pack()

def create_table():
    conn = sqlite3.connect('testDATAINFO.db')
    conn.execute('''CREATE TABLE DATAINFO(number text,name text,sex text,age real,salary real);''')
    conn.close()
    messagebox.showinfo('Done', 'the database has been created. ')

def confirm():
    info1 = en_number.get()
    info2 = en_name.get()
    info3 = en_sex.get()
    info4 = en_age.get()
    info5 = en_salary.get()

    conn = sqlite3.connect('testDATAINFO.db')


    conn.execute("INSERT INTO DATAINFO (number,name,sex,age,salary) VALUES(?,?,?,?,?)",
                 (info1,info2,info3,info4,info5))
    conn.commit()
    conn.close()


    messagebox.showinfo('Done','all data has been sent to database. ')

bla0 = Label(mp,fg = 'black',bg = g,text = '')
bla0.pack()

bt = Button(mp,text= 'OK',fg='black' ,bg = w,command = confirm)
bt.place(x = 300,y = 300)
bt.pack()

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



