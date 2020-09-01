import random

# 1 = head
# 2 = tail

head = []
tail = []

chance = ["head","tail"]

i = 1

while i <= 1000000:
    res = random.randint(1,2)
    if res == 1:
        head.append("head")
    if res == 2:
        tail.append("tail")

    
    

    i = i + 1

print("head : ",len(head))
print("tail : ",len(tail))
