
class queue:
    
    
    def __init__(self):
        self.DB = list()
        self.val = None

    def addQ(self,E):

        self.val = E
        self.DB.append(self.val)
        

    def showDB(self):
        print(self.DB)
    



queue.addQ(50,50)

#queue.showDB()
'''


QDB = []

def addQ(data):
    QDB.append(data)

def showQ():
    print(QDB[0])
    QDB.pop(0)
    if len(QDB) == 0:
        print("EMPTY")



addQ(20)
addQ(15)
addQ(61)
addQ(14)
addQ(42)
showQ()
showQ()
addQ(45)
addQ(11)
showQ()
showQ()
showQ()
showQ()
showQ()
'''