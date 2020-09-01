from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

mp = Tk()
mp.geometry("720x720")
mp.title('Love Confirming Program')
mp.configure(background='pink')

img = ImageTk.PhotoImage(Image.open(r'C:\Users\กาย เอสซีไอ\Desktop\main\heart.jpg'))
panel = Label(mp, image = img)
panel.pack()


lb = Label(mp,text = 'โปรแกรมนี้จะทำให้คุณรู้จักหัวใจตัวเองมากขึ้น.',fg = 'black',bg = 'yellow')
lb.pack()
lb1 = Label(mp,text = 'โปรดเลือกข้อดังต่อไปนี้หากเป็นจริง.',fg = 'black',bg = 'yellow')
lb1.pack()


v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
v6 = IntVar()
v7 = IntVar()
v8 = IntVar()
v9 = IntVar()
v10 = IntVar()
v11 = IntVar()
v12 = IntVar()

cb1 = Checkbutton(mp,text = 'ทั้งๆ ที่คุณอยากโกรธเค้าใจจะขาด แต่คุณก็ทนโกรธ หรืองอนให้เค้าง้อได้อย่างเก่งก็ไม่เกิน 2 นาที เดี๋ยวคุณก็หายโกรธเค้าแล้ว',variable = v1 ,onvalue = 1 ,offvalue = 0)
cb1.var = v1
cb1.pack()

cb2 = Checkbutton(mp,text = 'คุณจะอ่านข้อความที่เค้าส่งมา โดยไม่รู้จักเบื่อทั้งๆ ที่มันเก่าเป็นชาติแล้วก็ตามทีเหอะ',variable = v2 ,onvalue = 1 ,offvalue = 0)
cb2.var = v2
cb2.pack()

cb3 = Checkbutton(mp,text = 'ถึงแม้ว่าคุณจะรีบขนาดไหน แต่เมื่ออยู่กับเค้าคนนั้น คุณจะเดินช้าลง ลองนับจังหวะการเดินของคุณดูสิคะ ว่าคุณน่ะเดินช้าลงจริงๆ',variable = v3 ,onvalue = 1 ,offvalue = 0)
cb3.var = v3
cb3.pack()

cb4 = Checkbutton(mp,text = 'คุณจะเขินอายทุกครั้งที่อยู่ใกล้เค้าคนนั้น',variable = v4 ,onvalue = 1 ,offvalue = 0)
cb4.var = v4
cb4.pack()

cb5 = Checkbutton(mp,text = 'หัวใจคุณจะเต้นแรงขึ้น …แรงขึ้น และแรงขึ้น  เมื่อคุณคิดถึงเค้า',variable = v5 ,onvalue = 1 ,offvalue = 0)
cb5.var = v5
cb5.pack()

cb6 = Checkbutton(mp,text = 'แค่ได้ยินเสียงเค้า…คุณก็ยิ้มได้โดยไม่มีเหตุผล (ถามจริง …บ้ารึป่าวคะ?)',variable = v6 ,onvalue = 1 ,offvalue = 0)
cb6.var = v6
cb6.pack()

cb7 = Checkbutton(mp,text = 'เมื่อคุณมองเค้า ภาพที่เห็นก็จะมีเพียงเค้าคนเดียว ถึงแม้ว่า สิ่งที่เกิดขึ้นข้างหลังของเค้าจะมีอุบัติเหตุหรือไฟไหม้ หรือคนอื่นๆที่หน้าตาดีกว่าก็ตาม !!',variable = v7 ,onvalue = 1 ,offvalue = 0)
cb7.var = v7
cb7.pack()

cb8 = Checkbutton(mp,text = 'แม้ว่าคุณเป็นสาวกตัวจริงของ Eminem แต่คุณจะเริ่มฟังเพลงช้าก็คราวนี้แหละ',variable = v8 ,onvalue = 1 ,offvalue = 0)
cb8.var = v8
cb8.pack()

cb9 = Checkbutton(mp,text = ' ทุกครั้งทึ่คุณคิดถึงใครสักคน คนเดียวที่คุณคิดถึงคือ เค้า …',variable = v9 ,onvalue = 1 ,offvalue = 0)
cb9.var = v9
cb9.pack()

cb10 = Checkbutton(mp,text = ' คุณจะเพ้อ ฝันหวานทุกครั้งเพียงแค่ได้กลิ่นน้ำหอมของเค้า',variable = v10 ,onvalue = 1 ,offvalue = 0)
cb10.var = v10
cb10.pack()

cb11 = Checkbutton(mp,text = 'คุณจะยิ้มทุกครั้งเวลาที่คุณคิดถึงเค้า',variable = v11 ,onvalue = 1 ,offvalue = 0)
cb11.var = v11
cb11.pack()

cb12 = Checkbutton(mp,text = 'อะไรๆ ก็เป็นเรื่องง่ายๆ ที่คุณสามารถทำได้ทั้งนั้น เพื่อเค้า ทั้งๆ ที่ในชีวิตนี้ไม่เค๊ย..ไม่เคยทำมาก่อนเลย',variable = v12 ,onvalue = 1 ,offvalue = 0)
cb12.var = v12
cb12.pack()



def calc():
    love = 0

    if cb1.var.get() == 1:
        love = love + 1
    else:
        love = love + 0

    if cb2.var.get() == 1:
        love = love + 1
    else:
        love = love +0

    if cb3.var.get() == 1:
        love = love + 1
    else:
        love = love + 0

    if cb4.var.get() == 1:
        love = love + 1
    else:
        love = love + 0

    if cb5.var.get() == 1:
        love = love + 1
    else:
        love = love + 0

    if cb6.var.get() == 1:
        love = love + 1
    else:
        love = love + 0

    if cb7.var.get() == 1:
        love = love + 1
    else:
        love = love + 0

    if cb8.var.get() == 1:
        love = love + 1
    else:
        love = love + 0
    if cb9.var.get() == 1:
        love = love + 1
    else:
        love = love + 0

    if cb10.var.get() == 1:
        love = love + 1
    else:
        love = love + 0

    if cb11.var.get() == 1:
        love = love + 1
    else:
        love = love + 0

    if cb12.var.get() == 1:
        love = love + 1
    else:
        love = love + 0

    if love == 12:
        love_res = "แน่นอน คุณโคตรรักเขาเลย"
    if love < 12 and love >= 7:
        love_res = "คุณกำลังมีความรักนะ"
    if love <= 6 and love > 0:
        love_res = "คุณมีความรู้สึกกับใครอยู่สินะ"
    if love == 0:
        love_res = "ไม่ใช่หรอกความรักน่ะ "
    messagebox.showinfo('การยืนยัน','ผลลัพธ์คือ.. '+ str(love_res))

bt = Button(mp,text = 'ยืนยัน',bg = 'red',fg = 'white',command = calc)
bt.pack()

bla = Label(mp,fg = 'black',bg = 'pink',text = '')
bla.pack()
bla1 = Label(mp,fg = 'black',bg = 'pink',text = '')
bla1.pack()
z = Label(mp,fg = 'yellow',bg = 'green',text = 'This program made by mr.guy thongtrachoo')
z.pack()

mp.mainloop()

