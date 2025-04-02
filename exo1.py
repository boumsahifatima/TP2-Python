def surface(a,b,h):
    return (a+b)*h/2
a=float(input("enter la base sup"))
b=float(input("enter la base inf"))
h=float(input("enter la hauteur"))
s=surface(a,b,h)
print("la surface de trapeze est :",s)
