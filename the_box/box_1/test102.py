
dataset = []
i = 1
while i <= 100:
    dataset.append(i)
    i = i+1

c = 1
while c <= 70:
    dataset.remove(c)
    c = c+1


for x in dataset:
    print(x)