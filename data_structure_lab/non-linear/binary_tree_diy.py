# i am going to make a binary tree by myself lets see what it si going to be.
# most of developer would use class statment but i am not going to use it at first


sorting = [19,12,33,65,1,34,22,45,17]
i = 0
while i < len(sorting):
  if sorting[i] > sorting[i+1]:
    backup = sorting[i]
    backup2 = sorting[i+1]
    sorting[i] = backup2
    sorting[i+1] = backup
    print(sorting)
    else:
        i = i + 1
  

 
print(sorting)










'''
ROOT = None
BRANCH_LEFT = []
BRANCH_RIGHT = []

def binarytree( root ):
    
    global ROOT 
    ROOT = root
    
    global BRANCH_LEFT 
    BRANCH_LEFT = left
    
    global BRANCH_RIGHT 
    BRANCH_RIGHT = right
    
def insert_node(val):
    if val < ROOT:
        global BRANCH_LEFT 
        if BRANCH_LEFT == None:
            BRANCH_LEFT.append(val)
        if BRANCH_LEFT != None:
            BRANCH_LEFT.append(val)
 #       if BRANCH_LEFT[0] > BRANCH_LEFT[1]:
  #          BRANCH_LEFT[0] = BRANCH_LEFT[1]
   #         BRANCH_LEFT[1] = BRANCH_LEFT[0]
    if val > ROOT:
        global BRANCH_RIGHT
        if BRANCH_RIGHT == None:
            BRANCH_RIGHT.append(val)
        if BRANCH_RIGHT != None:
            BRANCH_RIGHT.append(val)
  #      if BRANCH_RIGHT[0] > BRANCH_RIGHT[1]:
   #         BRANCH_RIGHT[0] = BRANCH_RIGHT[1]
    #        BRANCH_RIGHT[1] = BRANCH_RIGHT[0]
               

def sort_tree():
    pass

def show_tree():
    print("Root Node : ",ROOT)
    print("left_side_branch : ",BRANCH_LEFT)
    print("right_side_branch : ",BRANCH_RIGHT)
    print(BRANCH_LEFT,ROOT,BRANCH_RIGHT)





binarytree(12)
insert_node(76)
insert_node(9)
insert_node(35)
insert_node(55)
insert_node(11)

'''