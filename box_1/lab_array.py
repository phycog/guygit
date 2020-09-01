

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

car = [car1,car2,car3]

car.insert(1,"Benz")
number = [1,2,3,4]

engine = ["190 hp","320 hp" ,"400 hp","200 hp"]
seat = [4,2,4,6]
xx = 0
print("no.","brand","  HP","seat")
for x in number:
    print(x,'  ',car[xx],'  ',"  ",engine[xx],"   ",seat[xx])
    xx = xx+1