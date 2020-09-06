from datetime import datetime

# current date and time
now = datetime.now()
timestamp = datetime.timestamp(now)


class memo:
    def info(self,name,pay,date):
        self.name = name
        self.pay = pay
        self.date = date

    
momo = memo()

def show():
    print("customer name : ",momo.name)
    print("paid : ",momo.pay)
    print("date : ",momo.date)

momo.info("jaew",40000,now)

show()




