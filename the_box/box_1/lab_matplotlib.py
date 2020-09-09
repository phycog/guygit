import matplotlib.pyplot as plt
import random

day = []
newcase = []
z = 1

total =[]
while z <= 500 :
    day.append(z)
    if z <= 10 :
     newcase.append(random.randrange(1*z,80*z))
    if z >= 11 and z <= 30 :
        newcase.append(random.randrange(81*z,200*z))
    if z > 30 :
        newcase.append((random.randrange(201*z,500*z)))

    total.append(sum(newcase))
    z = z + 1

plt.plot(day, newcase)
plt.title("COVIT-19 total case : " + str(sum(total)))
# plt.plot(day,total)
plt.xlabel("Day")
plt.ylabel("Case")

plt.show()












