from random import *



class human:
    def ability(self,name,power,speed,age,intel):
        self.name = name
        self.power = power
        self.speed = speed
        self.age = age
        self.intel = intel

class human2:
    def ability(self,name,power,speed,age,intel):
        self.name = name
        self.power = power
        self.speed = speed
        self.age = age
        self.intel = intel

def rand_name():
    dummy_char1 = ["q", "w", "r", "t", "y", "p", "s", "d", "f", "g", "h", "j", "k", "l", "c", "v", "b", "n"]
    dummy_char2 = ["a", "e", "i", "o", "u"]
    dummy_char3 = ["q", "w", "r", "t", "y", "p", "s", "d", "f", "g", "h", "j", "k", "l", "c", "v", "b", "n"]
    dummy_char4 = ["a", "e", "i", "o", "u"]


    dummy_name = choice(dummy_char1) + choice(dummy_char2) + choice(dummy_char3) + choice(dummy_char4)
    return dummy_name

def rand_pow():
    return randrange(60,180)
def rand_spd():
    return randrange(10,44)
def rand_age():
    return randrange(18,100)
def rand_int():
    return randrange(80,160)

all = []

obj_human1 = human()
obj_human2 = human()

obj_human1.ability(rand_name(), rand_pow(), rand_spd(), rand_age(), rand_int())
obj_human2.ability("paul",300,500,150,123)




def show():

    print("name : ",obj_human2.name)
    print("power : ",obj_human2.power)
    print("speed : ",obj_human2.speed)
    print("age : ",obj_human2.age)
    print("intel : ",obj_human2.intel)

show()


