# i am going to make a binary tree by myself lets see what it si going to be.
# most of developer would use class statment but i am not going to use it at first

ROOT = None
BRANCH_LEFT = []
BRANCH_RIGHT = []

def binarytree( root ):
    
    global ROOT 
    ROOT = root
    
 #   global BRANCH_LEFT 
 #   BRANCH_LEFT = left
    
 #   global BRANCH_RIGHT 
 #   BRANCH_RIGHT = right
    
def insert_node(val):
    if val < ROOT:
        global BRANCH_LEFT 
        if BRANCH_LEFT == None:
            BRANCH_LEFT.append(val)
        if BRANCH_LEFT != None:
            BRANCH_LEFT.append(val)


    if val > ROOT:
        global BRANCH_RIGHT
        if BRANCH_RIGHT == None:
            BRANCH_RIGHT.append(val)
        if BRANCH_RIGHT != None:
            BRANCH_RIGHT.append(val)

               
               
def sort_tree(branch):

 sorting = branch

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
   if r == len(sorting)-1:
     branch = sorting


def show_tree():
    print()
    print("Root Node : ",ROOT)
    print("left_side_branch : ",BRANCH_LEFT)
    print("right_side_branch : ",BRANCH_RIGHT)
    print()
    print(BRANCH_LEFT,ROOT,BRANCH_RIGHT)





binarytree(12)
insert_node(76)
insert_node(9)
insert_node(35)
insert_node(55)
insert_node(11)

from random import * 
c = 0
while c < 20:
     insert_node(randrange(1,100))
     c = c + 1


sort_tree(BRANCH_LEFT)
sort_tree(BRANCH_RIGHT)

show_tree()