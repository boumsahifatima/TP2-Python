def absl(x):
    if x<0:
        return x=(-1)*x
    else :
        return x
n=int(input("entrer un nombre :"))
print("la valeur absoulue de ",n,"est : ", absl(n))
