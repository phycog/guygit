'''

print("lets make some note")
topic = str(input("topic name "))
date = str(input("insert date"))
content = str(input("write the context"))
set1 = [topic,date,content]

for x in set1:
    print(x)
    print()
'''

bigdatagame = []

def showdetail(i,o,p):
    datagame = []
    datagame.append(i)
    datagame.append(o)
    datagame.append(p)


    bigdatagame.append(datagame)




    print("game title = ",i)
    print()
    print("year release = " , o)
    print()
    print("rating = ", p)
    print()


showdetail("crysis",2008,9.9)
showdetail("mario",1980,7.5)

for x in bigdatagame:
    print(x)



