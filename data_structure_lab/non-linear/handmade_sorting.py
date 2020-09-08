# i am going to make a binary tree by myself lets see what it si going to be.
# most of developer would use class statment but i am not going to use it at first
import random


junk = []
q = 0
while 1 < 1000:
    


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
      
      
