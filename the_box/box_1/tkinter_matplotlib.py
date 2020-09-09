import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import random

day = []
newcase = []
z = 1

total =[]
while z <= 40 :
    day.append(z)
    if z <= 10 :
     newcase.append(random.randrange(1*z,80*z))
    if z >= 11 and z <= 30 :
        newcase.append(random.randrange(81*z,200*z))
    if z > 30 :
        newcase.append((random.randrange(201*z,500*z)))

    total.append(sum(newcase))
    z = z + 1


root = tkinter.Tk()
root.wm_title("COVIT-19 total case : " + str(sum(total)))

fig = Figure(figsize=(5, 4), dpi=100)
fig.add_subplot().plot(day, newcase)



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
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.