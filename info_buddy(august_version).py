from tkinter import *
from tkinter import messagebox
import sqlite3
from datetime import datetime

def show_link():
    messagebox.showinfo('data info','go to (https://inloop.github.io/sqlite-viewer/) and drop .db file to execute.')

def not_available():
    messagebox.showinfo('Done', 'this feature is not available ')

def option():
    global mp2
    mp2 = Tk()
    mp2.geometry("360x400")
    mp2.title('INFO BUDDY')
    mp2.configure(background='grey')
    w = 'white'
    g = 'grey'

    lb = Label(mp2, text="OPTION", fg='black', bg=g)
    lb.config(font=("Courier", 15))
    lb.pack()

    bla01 = Label(mp2, fg='black', bg=g, text='')
    bla01.pack()

    def create_table():
        conn = sqlite3.connect('storeDATAINFO.db')
        conn.execute('''CREATE TABLE DATAINFO(name text,pay real,date text);''')
        conn.close()
        messagebox.showinfo('Done', 'the database has been created. ')

    bt1 = Button(mp2, text='CREATE DATABASE', fg='black', bg=w, command=create_table)
    bt1.place(x=300, y=300)
    bt1.pack()

    bla02 = Label(mp2, fg='black', bg=g, text='')
    bla02.pack()

    bt2 = Button(mp2, text='DELETE DATA', fg='black', bg=w,command=not_available )
    bt2.place(x=300, y=300)
    bt2.pack()

    bla03 = Label(mp2, fg='black', bg=g, text='')
    bla03.pack()


    bt3 = Button(mp2, text='CHANGE COLOR', fg='black', bg=w, command=not_available)
    bt3.place(x=300, y=300)
    bt3.pack()

    bla04 = Label(mp2, fg='black', bg=g, text='')
    bla04.pack()

    def back():
        mp2.destroy()
        main_menu()

    bt4 = Button(mp2, text='back', fg='black', bg=w,command = back )
    bt4.place(x=300, y=300)
    bt4.pack()

    bla3 = Label(mp2, fg='black', bg=g, text='')
    bla3.pack()
    bla4 = Label(mp2, fg='black', bg=g, text='')
    bla4.pack()

    z = Label(mp2, fg='black', bg=g, text='This program made by mr.guy thongtrachoo')
    z.pack()

    mp.destroy()

    mp2.mainloop()

def main_menu():
    global mp
    mp = Tk()
    mp.geometry("360x400")
    mp.title('INFO BUDDY')
    mp.configure(background='grey')
    w = 'white'
    g = 'grey'

    lb = Label(mp, text="MAIN MENU", fg='black', bg=g)
    lb.config(font=("Courier", 15))
    lb.pack()

    bla01 = Label(mp, fg='black', bg=g, text='')
    bla01.pack()

    bt1 = Button(mp, text='ADD INFO', fg='black', bg=w, command=add_info)
    bt1.place(x=300, y=300)
    bt1.pack()

    bla02 = Label(mp, fg='black', bg=g, text='')
    bla02.pack()

    bt2 = Button(mp, text='SHOW INFO', fg='black', bg=w,command=show_link )
    bt2.place(x=300, y=300)
    bt2.pack()

    bla03 = Label(mp, fg='black', bg=g, text='')
    bla03.pack()

    bt3 = Button(mp, text='FIX INFO', fg='black', bg=w,command=not_available )
    bt3.place(x=300, y=300)
    bt3.pack()

    bla04 = Label(mp, fg='black', bg=g, text='')
    bla04.pack()

    bt4 = Button(mp, text='OPTION', fg='black', bg=w,command = option )
    bt4.place(x=300, y=300)
    bt4.pack()

    bla05 = Label(mp, fg='black', bg=g, text='')
    bla05.pack()

    def exit():
        mp.destroy()

    bt5 = Button(mp, text='EXIT', fg='black', bg=w, command=exit)
    bt5.place(x=300, y=300)
    bt5.pack()

    bla0 = Label(mp, fg='black', bg=g, text='')
    bla0.pack()

    bla = Label(mp, fg='black', bg=g, text='')
    bla.pack()
    bla1 = Label(mp, fg='black', bg=g, text='')
    bla1.pack()

    bla3 = Label(mp, fg='black', bg=g, text='')
    bla3.pack()
    bla4 = Label(mp, fg='black', bg=g, text='')
    bla4.pack()

    z = Label(mp, fg='black', bg=g, text='This program made by mr.guy thongtrachoo')
    z.pack()

    mp.mainloop()

def add_info():

    mp1 = Tk()
    mp1.geometry("360x400")
    mp1.title('INFO BUDDY')
    mp1.configure(background='grey')
    w = 'white'
    g = 'grey'

    lb = Label(mp1, text="ADD INFO", fg='black', bg=g)
    lb.config(font=("Courier", 15))
    lb.pack()



 
    lb2 = Label(mp1, text='name', fg='black', bg=g)
    lb2.pack()

    en_name = Entry(mp1, bd=2, bg=w)
    en_name.pack()







    lb5 = Label(mp1, text='pay', fg='black', bg=g)
    lb5.pack()

    en_pay = Entry(mp1, bd=2, bg=w)
    en_pay.pack()

    def confirm():
     
        info1 = en_name.get()
      
      
        info2 = en_pay.get()
        info3 = datetime.now()

        conn = sqlite3.connect('storeDATAINFO.db')

        conn.execute("INSERT INTO DATAINFO (name,pay,date) VALUES(?,?,?)",
                     (info1, info2, info3))
        conn.commit()
        conn.close()

        messagebox.showinfo('Done', 'all data has been sent to database. ')

    bla0 = Label(mp1, fg='black', bg=g, text='')
    bla0.pack()

    bt = Button(mp1, text='OK', fg='black', bg=w, command=confirm)
    bt.place(x=300, y=300)
    bt.pack()

    bla = Label(mp1, fg='black', bg=g, text='')
    bla.pack()
    bla1 = Label(mp1, fg='black', bg=g, text='')
    bla1.pack()

    bla3 = Label(mp1, fg='black', bg=g, text='')
    bla3.pack()

    def back():
        mp1.destroy()
        main_menu()


    bt1 = Button(mp1, text='back', fg='black', bg=w, command=back)
    bt1.place(x=300, y=300)
    bt1.pack()

    z = Label(mp1, fg='black', bg=g, text='This program made by mr.guy thongtrachoo')
    z.pack()

    mp.destroy()

    mp1.mainloop()


main_menu()