from random import *

dummy_char1 = ["q","w","r","t","y","p","s","d","f","g","h","j","k","l","c","v","b","n"]
dummy_char2 = ["a","e","i","o","u"]
dummy_char3 = ["q","w","r","t","y","p","s","d","f","g","h","j","k","l","c","v","b","n"]
dummy_char4 = ["a","e","i","o","u"]
all_stud = []
students = []
z = 1
while z <= 1000:
    dummy_name = choice(dummy_char1)+choice(dummy_char2)+choice(dummy_char3)+choice(dummy_char4)
    all_stud.append(dummy_name)
    students.append(z)
    z = z + 1
zz = 0
for x in all_stud:
 print(zz,x)
 zz = zz + 1

i = 0


while i <= 1000:
 if all_stud[i] == "coke":

  print("index of coke : "+str(i))


# if all_stud[i] == "civi":
#  print("index of civi : "+str(i))


 i = i + 1



