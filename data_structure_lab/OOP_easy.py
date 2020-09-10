class Car:
  
  # Attributes
  color = "No color"
  brand = "No brand"
  numOfwheels = 4 # จำนวนล้อ
  numOfseats = 4  # จำนวนเบาะนั่ง
  maxSpeed = 0
  numberOfcar = 0
  stock = list()
  
  def __init__(self, color, brand, maxSpeed):
    self.color = color
    self.brand = brand
    self.maxSpeed    = maxSpeed
    self.stock.append(self.color)
  
  # Methods
  def setColor(self,c):
    self.color = c
 
  def setBrand(self,b):
    self.brand = b
  
  def setMaxSpeed(self,s):
    self.maxSpeed = s
  
  def printData(self):
    print("The color of car is : ",self.color)
    print("The car was built by :",self.brand)
    print("The Maximun speed is :",self.maxSpeed," km/hr.")
    
 # Create Object
car1 = Car("blue","Honda",250)
car1.printData()
car1.setColor("Goldrose")
print("After set color :",car1.color)
print(car1.stock)