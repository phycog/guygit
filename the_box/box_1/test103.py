dummy_day = []
dummy_case = []

total = []
lev = 0
i = 0

while i <= 100:
    dummy_case.append(i+lev)
    dummy_day.append(i)
    lev = lev+(dummy_case[i]/100*13)
    i = i + 1

    total.append(sum(dummy_case))

print("day","   ","case","   ","total")
ii = 1

while ii <= len(dummy_day):
    print(dummy_day[ii],"     ",int(dummy_case[ii]),"      ",int(total[ii]) )

    ii = ii +1




