'''

MISSION COMPLETE!!!!!

I HAVE ALREADY MADE SUDOKU PROGRAMS THAT IT WORK ON RULE AND LOGIC!!!..(even it is not finished 100% but i understand the algorithym.)

12/09/2020

MR.GUY THONGTRACHOO



'''
from random import *
import random

element = [1,2,3,4,5,6,7,8,9]
element0 = [1,2,3,4,5,6,7,8,9]
element1 = [1,2,3,4,5,6,7,8,9]


g1 = random.choice(element)
element.remove(g1)
g2 = random.choice(element)
element.remove(g2)
g3 = random.choice(element)
element.remove(g3)
g4 = random.choice(element)
element.remove(g4)
g5 = random.choice(element)
element.remove(g5)
g6 = random.choice(element)
element.remove(g6)
g7 = random.choice(element)
element.remove(g7)
g8 = random.choice(element)
element.remove(g8)
g9 = random.choice(element)
element.remove(g9)
#---------------------------------------------------
element0.remove(g1)
element0.remove(g2)
element0.remove(g3)

element1.remove(g4)
element1.remove(g5)
element1.remove(g6)


g10 = random.choice(element0)

if g10 == g1:
    while g10 == g1 :
          g10 = random.choice(element0)
element0.remove(g10)
          
g11 = random.choice(element0)

if g11 == g2:
    while g11 == g2 :
          g11 = random.choice(element0)
element0.remove(g11)

g12 = random.choice(element0)

if g12 == g3:
    while g12 == g3 :
          g12 = random.choice(element0)
element0.remove(g12)
#---------------------------------------
g13 = random.choice(element1)

if g13 == g4 or g13 == g10 or g13 == g11 or g13 == g12:
    while g13 == g4 or g13 == g10 or g13 == g11 or g13 == g12:
          g13 = random.choice(element1)
element1.remove(g13)

g14 = random.choice(element1)

if g14 == g5 or g14 == g10 or g14 == g11 or g14 == g12 or g14 == g13:
    while g14 == g5 or g14 == g10 or g14 == g11 or g14 == g12 or g14 == g13:
          g14 = random.choice(element1)
element1.remove(g14)

g15 = random.choice(element1)

if g15 == g6 or g15 == g10 or g15 == g11 or g15 == g12 or g15 == g13 or g15 == g14:
    while g15 == g6 or g15 == g10 or g15 == g11 or g15 == g12 or g15 == g13 or g15 == g14:
          g15 = random.choice(element1)
element1.remove(g15)

#-------------------------------------

g16 = randrange(1,9)

if g16 == g7:
    while g16 == g7 :
          g16 = randrange(1,9)

g17 = randrange(1,9)

if g17 == g8:
    while g17 == g8 :
          g17 = randrange(1,9)

g18 = randrange(1,9)

if g18 == g9:
    while g18 == g9 :
          g18 = randrange(1,9)

g19 = random.choice(element0)

if g19 == g1 or g19 == g10:
    while g19 == g1 or g19 == g10 :
          g19 = random.choice(element0)
element0.remove(g19)

g20 = random.choice(element0)

if g20 == g2 or g20 == g11:
    while g20 == g2 or g20 == g11 :
          g20 = random.choice(element0)
element0.remove(g20)

g21 = random.choice(element0)

if g21 == g3 or g21 == g12:
    while g21 == g3 or g21 == g12 :
          g21 = random.choice(element0)
element0.remove(g21)

#---------------------------------------

g22 = random.choice(element1)

if g22 == g4 or g22 == g13:
    while g22 == g4 or g22 == g13 :
          g22 = random.choice(element1)
element1.remove(g22)

g23 = random.choice(element1)

if g23 == g5 or g23 == g14:
    while g23 == g5 or g23 == g14 :
          g23 = random.choice(element1)
element1.remove(g23)


g24 = random.choice(element1)

if g24 == g6 or g24 == g15:
    while g24 == g6 or g24 == g15 :
          g24 = random.choice(element1)
element1.remove(g24)

#---------------------------------------

g25 = randrange(1,9)
g26 = randrange(1,9)
g27 = randrange(1,9)
g28 = randrange(1,9)
g29 = randrange(1,9)
g30 = randrange(1,9)
g31 = randrange(1,9)
g32 = randrange(1,9)
g33 = randrange(1,9)
g34 = randrange(1,9)
g35 = randrange(1,9)
g36 = randrange(1,9)
g37 = randrange(1,9)
g38 = randrange(1,9)
g39 = randrange(1,9)
g40 = randrange(1,9)
g41 = randrange(1,9)
g42 = randrange(1,9)
g43 = randrange(1,9)
g44 = randrange(1,9)
g45 = randrange(1,9)
g46 = randrange(1,9)
g47 = randrange(1,9)
g48 = randrange(1,9)
g49 = randrange(1,9)
g50 = randrange(1,9)
g51 = randrange(1,9)
g52 = randrange(1,9)
g53 = randrange(1,9)
g54 = randrange(1,9)
g55 = randrange(1,9)
g56 = randrange(1,9)
g57 = randrange(1,9)
g58 = randrange(1,9)
g59 = randrange(1,9)
g60 = randrange(1,9)
g61 = randrange(1,9)
g62 = randrange(1,9)
g63 = randrange(1,9)
g64 = randrange(1,9)
g65 = randrange(1,9)
g66 = randrange(1,9)
g67 = randrange(1,9)
g68 = randrange(1,9)
g69 = randrange(1,9)
g70 = randrange(1,9)
g71 = randrange(1,9)
g72 = randrange(1,9)
g73 = randrange(1,9)
g74 = randrange(1,9)
g75 = randrange(1,9)
g76 = randrange(1,9)
g77 = randrange(1,9)
g78 = randrange(1,9)
g79 = randrange(1,9)
g80 = randrange(1,9)
g81 = randrange(1,9)






'''
g1 = randrange(1,4)
print(r)

if g == g or g == g :
    while g == g or g == g :
          g = randrange(1,9)
print("---")
print(r)
'''


line0 = " _______________________"+" _______________________"+" ________________________"
line1 = "|       |       |       |"+"|       |       |       |"+"|       |       |       |"
line2 = "|   "+str(g1)+"   |   "+str(g2)+"   |   "+str(g3)+"   |"+"|   "+str(g4)+"   |   "+str(g5)+"   |   "+str(g6)+"   |"+"|   "+str(g7)+"   |   "+str(g8)+"   |   "+str(g9)+"   |"
line3 = "|_______|_______|_______|"+"|_______|_______|_______|"+"|_______|_______|_______|"
line4 = "|       |       |       |"+"|       |       |       |"+"|       |       |       |"
line5 = "|   "+str(g10)+"   |   "+str(g11)+"   |   "+str(g12)+"   |"+"|   "+str(g13)+"   |   "+str(g14)+"   |   "+str(g15)+"   |"+"|   "+str(g16)+"   |   "+str(g17)+"   |   "+str(g18)+"   |"
line6 = "|_______|_______|_______|"+"|_______|_______|_______|"+"|_______|_______|_______|"
line7 = "|       |       |       |"+"|       |       |       |"+"|       |       |       |"
line8 = "|   "+str(g19)+"   |   "+str(g20)+"   |   "+str(g21)+"   |"+"|   "+str(g22)+"   |   "+str(g23)+"   |   "+str(g24)+"   |"+"|   "+str(g25)+"   |   "+str(g26)+"   |   "+str(g27)+"   |"
line9 = "|_______|_______|_______|"+"|_______|_______|_______|"+"|_______|_______|_______|"
line10 = " _______________________"+" _______________________"+" ________________________"
line11 = "|       |       |       |"+"|       |       |       |"+"|       |       |       |"
line12 = "|   "+str(g28)+"   |   "+str(g29)+"   |   "+str(g30)+"   |"+"|   "+str(g31)+"   |   "+str(g32)+"   |   "+str(g33)+"   |"+"|   "+str(g34)+"   |   "+str(g35)+"   |   "+str(g36)+"   |"
line13 = "|_______|_______|_______|"+"|_______|_______|_______|"+"|_______|_______|_______|"
line14 = "|       |       |       |"+"|       |       |       |"+"|       |       |       |"
line15 = "|   "+str(g37)+"   |   "+str(g38)+"   |   "+str(g39)+"   |"+"|   "+str(g40)+"   |   "+str(g41)+"   |   "+str(g42)+"   |"+"|   "+str(g43)+"   |   "+str(g44)+"   |   "+str(g45)+"   |"
line16 = "|_______|_______|_______|"+"|_______|_______|_______|"+"|_______|_______|_______|"
line17 = "|       |       |       |"+"|       |       |       |"+"|       |       |       |"
line18 = "|   "+str(g46)+"   |   "+str(g47)+"   |   "+str(g48)+"   |"+"|   "+str(g49)+"   |   "+str(g50)+"   |   "+str(g51)+"   |"+"|   "+str(g52)+"   |   "+str(g53)+"   |   "+str(g54)+"   |"
line19 = "|_______|_______|_______|"+"|_______|_______|_______|"+"|_______|_______|_______|"
line20 = " _______________________"+" _______________________"+" ________________________"
line21 = "|       |       |       |"+"|       |       |       |"+"|       |       |       |"
line22 = "|   "+str(g55)+"   |   "+str(g56)+"   |   "+str(g57)+"   |"+"|   "+str(g58)+"   |   "+str(g59)+"   |   "+str(g60)+"   |"+"|   "+str(g61)+"   |   "+str(g62)+"   |   "+str(g63)+"   |"
line23 = "|_______|_______|_______|"+"|_______|_______|_______|"+"|_______|_______|_______|"
line24 = "|       |       |       |"+"|       |       |       |"+"|       |       |       |"
line25 = "|   "+str(g64)+"   |   "+str(g65)+"   |   "+str(g66)+"   |"+"|   "+str(g67)+"   |   "+str(g68)+"   |   "+str(g69)+"   |"+"|   "+str(g70)+"   |   "+str(g71)+"   |   "+str(g72)+"   |"
line26 = "|_______|_______|_______|"+"|_______|_______|_______|"+"|_______|_______|_______|"
line27 = "|       |       |       |"+"|       |       |       |"+"|       |       |       |"
line28 = "|   "+str(g73)+"   |   "+str(g74)+"   |   "+str(g75)+"   |"+"|   "+str(g76)+"   |   "+str(g77)+"   |   "+str(g78)+"   |"+"|   "+str(g79)+"   |   "+str(g80)+"   |   "+str(g81)+"   |"
line29 = "|_______|_______|_______|"+"|_______|_______|_______|"+"|_______|_______|_______|"


all_line = [line0,line1,line2,line3,line4,line5,line6,line7,line8,line9,
line10,line11,line12,line13,line14,line15,line16,line17,line18,line19,
line20,line21,line22,line23,line24,line25,line26,line27,line28,line29]

for x in all_line:
    print(x)