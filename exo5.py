# calcule la somme 
def somme(x):
    s=0
    for i in range (1,x+1):
        s+=i
    return s
x=int(input("entrer un nombre : "))
print(f'La somme est : {somme(x)}')
