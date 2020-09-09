

###################
#the problem is input is str i have to make it int (solve)
######################




from tkinter import *
from tkinter import messagebox

#defind window of program
mp = Tk() #name of window
mp.geometry("480x500") #size of window
mp.title('the math') #title name of window
mp.configure(background='grey') # blackgorund color


lb = Label(mp,text = 'make your graph with the math ',fg = 'black',bg = 'grey')
lb.config(font =("Courier", 15))
lb.pack()

x_line = []
y_line = []

lb_slot = Label(mp,text = 'insert X line',fg = 'black',bg = 'yellow')
lb_slot.pack()

en_slot_x1 = Entry(mp, bd = 2,bg = "light pink")
en_slot_x1.pack()
en_slot_x2 = Entry(mp, bd = 2,bg = "light pink")
en_slot_x2.pack()
en_slot_x3 = Entry(mp, bd = 2,bg = "light pink")
en_slot_x3.pack()
en_slot_x4 = Entry(mp, bd = 2,bg = "light pink")
en_slot_x4.pack()
en_slot_x5 = Entry(mp, bd = 2,bg = "light pink")
en_slot_x5.pack()
en_slot_x6 = Entry(mp, bd = 2,bg = "light pink")
en_slot_x6.pack()

lb_slot1 = Label(mp,text = 'insert Y line',fg = 'black',bg = 'yellow')
lb_slot1.pack()

en_slot_y1 = Entry(mp, bd = 2,bg = "light pink")
en_slot_y1.pack()
en_slot_y2 = Entry(mp, bd = 2,bg = "light pink")
en_slot_y2.pack()
en_slot_y3 = Entry(mp, bd = 2,bg = "light pink")
en_slot_y3.pack()
en_slot_y4 = Entry(mp, bd = 2,bg = "light pink")
en_slot_y4.pack()
en_slot_y5 = Entry(mp, bd = 2,bg = "light pink")
en_slot_y5.pack()
en_slot_y6 = Entry(mp, bd = 2,bg = "light pink")
en_slot_y6.pack()

def admit():
    data_x1 = en_slot_x1.get()
    data_x2 = en_slot_x2.get()
    data_x3 = en_slot_x3.get()
    data_x4 = en_slot_x4.get()
    data_x5 = en_slot_x5.get()
    data_x6 = en_slot_x6.get()



    data_y1 = en_slot_y1.get()
    data_y2 = en_slot_y2.get()
    data_y3 = en_slot_y3.get()
    data_y4 = en_slot_y4.get()
    data_y5 = en_slot_y5.get()
    data_y6 = en_slot_y6.get()

    x_line.append(data_x1)
    x_line.append(data_x2)
    x_line.append(data_x3)
    x_line.append(data_x4)
    x_line.append(data_x5)
    x_line.append(data_x6)

    y_line.append(data_y1)
    y_line.append(data_y2)
    y_line.append(data_y3)
    y_line.append(data_y4)
    y_line.append(data_y5)
    y_line.append(data_y6)

    i = 0

    while i <= 5:
        x_line[i] = int(x_line[i])
        y_line[i] = int(y_line[i])

        i = i+1

    messagebox.showinfo("done.","your data was admitted.")

def make_graph():
    import tkinter

    from matplotlib.backends.backend_tkagg import (
        FigureCanvasTkAgg, NavigationToolbar2Tk)
    # Implement the default Matplotlib key bindings.
    from matplotlib.backend_bases import key_press_handler
    from matplotlib.figure import Figure

    root = tkinter.Tk()
    root.wm_title("the math (graph)")

    fig = Figure(figsize=(5, 4), dpi=100)
    fig.add_subplot().plot(x_line, y_line)

    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)

    canvas.mpl_connect("key_press_event", on_key_press)

    def _quit():
        root.quit()  # stops mainloop
        root.destroy()  # this is necessary on Windows to prevent
        # Fatal Python Error: PyEval_RestoreThread: NULL tstate

    button = tkinter.Button(master=root, text="Quit", command=_quit)
    button.pack(side=tkinter.BOTTOM)

    tkinter.mainloop()
    # If you put root.destroy() here, it will cause an error if the window is
    # closed with the window manager.

bt1 = Button(mp,text= 'admit',fg='black' ,bg = 'red',command = admit)
bt1.place(x = 300,y = 300)
bt1.pack()

bt2 = Button(mp,text= 'make graph',fg='black' ,bg = 'red',command = make_graph)
bt2.place(x = 300,y = 300)
bt2.pack()

def refresh():
    x_line.clear()
    y_line.clear()

bt3 = Button(mp,text= 'clear',fg='black' ,bg = 'red',command = refresh)
bt3.place(x = 300,y = 300)
bt3.pack()

mp.mainloop()