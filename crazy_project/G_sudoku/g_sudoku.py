import random

def shape():  
    element = [1,2,3,4,5,6,7,8,9]
    element1 = [1,2,3,4,5,6,7,8,9]
    element2 = [1,2,3,4,5,6,7,8,9]
    

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

    z1 = random.choice(element1)
    element1.remove(z1)
    z2 = random.choice(element1)
    element1.remove(z2)
    z3 = random.choice(element1)
    element1.remove(z3)
    z4 = random.choice(element1)
    element1.remove(z4)
    z5 = random.choice(element1)
    element1.remove(z5)
    z6 = random.choice(element1)
    element1.remove(z6)
    z7 = random.choice(element1)
    element1.remove(z7)
    z8 = random.choice(element1)
    element1.remove(z8)
    z9 = random.choice(element1)
    element1.remove(z9)

    x1 = random.choice(element2)
    element2.remove(x1)
    x2 = random.choice(element2)
    element2.remove(x2)
    x3 = random.choice(element2)
    element2.remove(x3)
    x4 = random.choice(element2)
    element2.remove(x4)
    x5 = random.choice(element2)
    element2.remove(x5)
    x6 = random.choice(element2)
    element2.remove(x6)
    x7 = random.choice(element2)
    element2.remove(x7)
    x8 = random.choice(element2)
    element2.remove(x8)
    x9 = random.choice(element2)
    element2.remove(x9)
    

    line0 = " _______________________"+" _______________________"+" ________________________"
    line1 = "|       |       |       |"+"|       |       |       |"+"|       |       |       |"
    line2 = "|   "+str(g1)+"   |   "+str(g2)+"   |   "+str(g3)+"   |"+"|   "+str(z1)+"   |   "+str(z2)+"   |   "+str(z3)+"   |"+"|   "+str(x1)+"   |   "+str(x2)+"   |   "+str(x3)+"   |"
    line3 = "|_______|_______|_______|"+"|_______|_______|_______|"+"|_______|_______|_______|"
    line4 = "|       |       |       |"+"|       |       |       |"+"|       |       |       |"
    line5 = "|   "+str(g4)+"   |   "+str(g5)+"   |   "+str(g6)+"   |"+"|   "+str(z4)+"   |   "+str(z5)+"   |   "+str(z6)+"   |"+"|   "+str(x4)+"   |   "+str(x5)+"   |   "+str(x6)+"   |"
    line6 = "|_______|_______|_______|"+"|_______|_______|_______|"+"|_______|_______|_______|"
    line7 = "|       |       |       |"+"|       |       |       |"+"|       |       |       |"
    line8 = "|   "+str(g7)+"   |   "+str(g8)+"   |   "+str(g9)+"   |"+"|   "+str(z7)+"   |   "+str(z8)+"   |   "+str(z9)+"   |"+"|   "+str(x7)+"   |   "+str(x8)+"   |   "+str(x9)+"   |"
    line9 = "|_______|_______|_______|"+"|_______|_______|_______|"+"|_______|_______|_______|"

    all_line = [line0,line1,line2,line3,line4,line5,line6,line7,line8,line9]

    i = 0
    while i <= 9:
        print(all_line[i]) 
        i = i + 1

 


d = 0
while d <= 5:
    shape()
    d = d+1

