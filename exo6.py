ef somme(x):
    s=0
    for i in range (2,x+1):
        if i%2==0 and i%3!=0:
            s+=i
    return s
x=int(input("entrer un nombre positif : "))
print(f'la somme est : {somme(x)}')