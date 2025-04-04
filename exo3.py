def le_max(a,b,c):
    m=a
    if b>m :
        m=b
    if c>m :
        m=c
    return m 
a=int(input("entrar a :"))
b=int(input("entrer b :"))
c=int(input("entrer c :"))
print(f'le max est {le_max(a,b,c)}')