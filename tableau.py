n=int(input("entrer le nombre des eleve :"))
tableau = []
#remplir un tableaux
for i in range(n):
    entier = int(input(f"Entrez la note de l'eleve {i + 1}: ")) 
    tableau.append(entier)
for i in range(n):
    print(f'la note de l eleve {i+1} est : {tableau[i]}')
#cherchons le max et le min 
max=tableau[0]
min=tableau[0]
for i in range(n):
    if max<tableau[i] :
        max=tableau[i]
    if min>tableau[i] :
        min=tableau[i]
print(f"le max est : {max}, le min est : {min}")
#calculons le moyenne
s=0
for i in range(n):
   s+=tableau[i]
m=s/n
print(f"la moyenne est : {m}")
#le nombre des eleves qui valide (note>moyenne)
k=0
for i in range(n):
    if tableau[i]>m :
        k++
print(f"le nombre des eleve qui passe est : {k}")
