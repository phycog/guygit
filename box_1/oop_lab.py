from random import *


'''
class player:
    # Attr
    eye = "blue"
    age = 22
    hair = "long"

    # Method
    def say_hi(self):
        print("Aloha !! ")

# test
obj = player()

print(obj.eye,obj.age,obj.hair)
print()
obj.say_hi()
'''


class student:
    def name(self,name):
        self.name = name
    def iq(self,iq):
        self.iq = iq
    def show_info(self):
        print(self.name)
        print(self.iq)


dummy_char1 = ["q","w","r","t","y","p","s","d","f","g","h","j","k","l","c","v","b","n"]
dummy_char2 = ["a","e","i","o","u"]
dummy_char3 = ["q","w","r","t","y","p","s","d","f","g","h","j","k","l","c","v","b","n"]
dummy_char4 = ["a","e","i","o","u"]
all_stud = []
students = []
z = 1
while z <= 10000:
    dummy_name = choice(dummy_char1)+choice(dummy_char2)+choice(dummy_char3)+choice(dummy_char4)
    all_stud.append(dummy_name)
    students.append(z)
    z = z + 1

print(len(students))


i = 0

while i <= 9999:
    students[i] = student()
    students[i].name(choice(all_stud))
    students[i].iq(randrange(110,160))

    i = i+1
j = 0

while j <= 9999:
    print(j ," : ",students[j].name,"  ",students[j].iq)
    j = j + 1


