from random import *


class BI:
  
  # Attributes

  warehouse = list()
  #Method

  def __init__(self, product):
    self.product = product
    self.warehouse.append(self.product)

  def insert(self,product):
      self.product = product
      self.warehouse.append(self.product)

  def insert_random(self,t):

      self.t = t
      i = 0
      while i <= self.t:
        tree1.insert(randrange(1,999))
        i = i + 1

  def make_sorting(self):
      sorting = self.warehouse


      r = 0
      i = 0
      while r < len(sorting)-1 :
       if sorting[i] > sorting[i+1]:
          backup = sorting[i]
          backup2 = sorting[i+1]
          sorting[i] = backup2
          sorting[i+1] = backup
    
       else:
          i = i + 1

       if i == len(sorting)-1:
          i = 0
          backup = None
          backup2 = None

          r = r + 1

      



 
  def printData(self):
    print(self.warehouse)
  
    
 # Create Object

tree1 = BI(20)
tree1.insert(32)
tree1.printData()

print()

tree1.insert_random(10)
tree1.printData()

print()

tree1.make_sorting()
tree1.printData()





