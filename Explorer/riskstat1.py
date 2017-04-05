import math

def calculate(PAR,e,force):
    LOL = PAR/(1+13.277*(math.pow(PAR,0.44))*(math.pow(e,(0.750-3.790*force+2.223*force))))
    print ("Par = ",PAR)
    print ("Force = ",force)
    print ("LOL = ",LOL)
    print ("")

e = 2.71828

PAR = 100000
force = 0
calculate(PAR,e,force)

PAR = 10000
force = 0
calculate(PAR,e,force)

PAR = 100000
force = 1
calculate(PAR,e,force)

PAR = 10000
force = 1
calculate(PAR,e,force)