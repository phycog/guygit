# i am going to make a sorting algor by myself lets see what it si going to be.

from random import *


junk = []
q = 0
while q < 1000:
  junk.append(randrange(1,999))
  q = q + 1

print()
print(junk)
print()


sorting = junk


r = 0
i = 0
while r < len(sorting)-1 :
  if sorting[i] > sorting[i+1]:
    backup = sorting[i]
    backup2 = sorting[i+1]
    sorting[i] = backup2
    sorting[i+1] = backup
    #print(sorting)
  else:
        i = i + 1

  if i == len(sorting)-1:
      i = 0
      backup = None
      backup2 = None

      r = r + 1

print()
print(sorting)
print()





'''
these below code work ^^

sorting = [19,12,2,55,78,98,43,21,33,65,1,34,55,22,45,17]


r = 0

i = 0
while r < len(sorting)-1 :
  if sorting[i] > sorting[i+1]:
    backup = sorting[i]
    backup2 = sorting[i+1]
    sorting[i] = backup2
    sorting[i+1] = backup
    print(sorting)
  else:
        i = i + 1

  if i == len(sorting)-1:
      i = 0
      backup = None
      backup2 = None

      r = r + 1
      
'''
