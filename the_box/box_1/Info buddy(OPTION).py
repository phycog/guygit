from tkinter import *
from tkinter import messagebox
import sqlite3

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
        conn = sqlite3.connect('testDATAINFO.db')
        conn.execute('''CREATE TABLE DATAINFO(number text,name text,sex text,age real,salary real);''')
        conn.close()
        messagebox.showinfo('Done', 'the database has been created. ')

    bt1 = Button(mp2, text='CREATE DATABASE', fg='black', bg=w,command = create_table )
    bt1.place(x=300, y=300)
    bt1.pack()

    bla02 = Label(mp2, fg='black', bg=g, text='')
    bla02.pack()

    bt2 = Button(mp2, text='DELETE DATA', fg='black', bg=w, )
    bt2.place(x=300, y=300)
    bt2.pack()

    bla03 = Label(mp2, fg='black', bg=g, text='')
    bla03.pack()

    def color():
        global g
        g = 'light pink'
        messagebox.showinfo('Done', 'color is pink now. ')

    bt3 = Button(mp2, text='CHANGE COLOR', fg='black', bg=w,command = color )
    bt3.place(x=300, y=300)
    bt3.pack()

    bla04 = Label(mp2, fg='black', bg=g, text='')
    bla04.pack()

    def back():
        mp2.destroy()
        main_menu()

    bt4 = Button(mp2, text='back', fg='black', bg=w, )
    bt4.place(x=300, y=300)
    bt4.pack()

