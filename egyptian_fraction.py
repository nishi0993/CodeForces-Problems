import math
def egpytian_fraction(n, d):
    if n>0:
        c = math.ceil(d/n)
        print("1/"+str(c))
        n = (n*c) - d
        d = d *c
        egpytian_fraction(n,d)

egpytian_fraction(6, 14)
        