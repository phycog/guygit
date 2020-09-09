'''
mass = int(input("mass (kg.) : "))
acc0 = int(input("speed (km/h) : "))
convertor = (acc0*1000)/3600
#acc1 = int(input("speed (m/s) : "))
#force0 = mass*acc
force1 = mass*convertor
print("force : ",force1, "N")
'''

def forceKMpH(mass,acc):
    mass = mass
    acc = acc
    convertor = (acc * 1000) / 3600
    force = mass * convertor

    return force

def forceMpS(mass,acc):
    mass = mass
    acc = acc
    force = mass*acc

    return force



