def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2():
    print("Exercice 2 : Afficher son prenom")
    prenom = input("Entrer votre prenom")
    print(f"Bonjour {prenom}!")

def exercice3():
    print("Exercice 3 : Afficher 3 lignes")
    print(" ligne1\n ligne2\n ligne3\n")

def exercice4():
    print("Exercice 4 : Calculer l'âge")
    annee_de_naissance = int(input("votre année de naissance"))
    annee_actuelle = 2025
    age = annee_actuelle - annee_de_naissance
    print(f"Vous avez environ {age} ans")

def exercice5():
    print("Exercice 5 : Addition simple")
    nombre1 = int(input("Choisir un premier nombre"))
    nombre2 = int(input("Choisir un second nombre"))
    somme = nombre1 + nombre2
    print(f"{nombre1} + {nombre2} = {somme}")

def exercice6():
    print("Exercice 6 : Soustraction simple")
    nombre1 = int(input("Choisir un premier nombre"))
    nombre2 = int(input("Choisir un second nombre"))
    soustraction = nombre1 - nombre2
    print(f"{nombre1} - {nombre2} = {soustraction}")

def exercice7():
    print("Exercice 7 : Multiplication simple")
    nombre1 = int(input("Choisir un premier nombre"))
    nombre2 = int(input("Choisir un second nombre"))
    addition = nombre1 * nombre2
    print(f"{nombre1} x {nombre2} = {somme}")

def exercice8():
    print("Exercice 8 : Division simple")
    nombre1 = int(input("Choisir un premier nombre"))
    nombre2 = int(input("Choisir un second nombre"))
    if nombre2 <= 0:
        print("Erreur : le dénominateur (nombre2) ne peut pas être 0")
        return 
    division = nombre1 / nombre2
    print(f"{nombre1} / {nombre2} = {division}")

def exercice9():
    print("Exercice 9 : Le carré d'un nombre")
    nombre = int(input("Choisir un nombre"))
    carre = nombre **2
    print(f"{nombre}² = {carre}")

def exercice10():
    print("Exercice 10 : Le double d'un nombre")
    nombre = int(input("Choisir un nombre"))
    double = nombre * 2 
    print(f"Le double de {nombre} = {double}")

def exercice11():
    print("Exercice 11 : Moitié d'un nombre ")
    nombre = int(input("Choisir un nombre"))
    moitie = nombre / 2 
    print(f"La moitié de {nombre} = {moitie}")

def exercice12():
    print("Exercice 12 : Afficher 5 fois ")
    message = (input("Quel message voulez-vous dire ?"))
    for i in range(5):
        print(f"{message}")

def exercice13():
    print("Exercice 13 : Afficher les nombres de 1 à 5")
    i = 1 
    for i in range(5):
        print(f"{i}")

def exercice14():
    print("Exercice 14 : Table de 2")
    table = int(input("Quelle table voulez-vous mutiplier"))
    for i in range(1, 11):
        print(f"{table} x {i} = {table * i}")

def exercice15():
    print("Exercice 15 : Aire du carré")
    carre = int(input("De quelle longueure est le côté du carré en cm"))
    aire = carre * carre 
    print(f"L'aire = {aire} cm")

def exercice16():
    print("Exercice 15 : Périmètre du carré")
    carre = int(input("De quelle longueure est le côté du carré en cm"))
    perimetre = carre * 4 
    print(f"L'aire = {perimetre} cm")

def exercice17():
    print("Exercice 17 : Conversion euros → dollars")
    euro = int(input("Combien d'Euros voulez-vous convertir ?"))
    dollars = euro * 1.17 
    print(f"{euro} = {dollars}$")

def exercice18():
    print("Exercice 18 : Conversion minutes → secondes ")
    minute = int(input("Combien de minutes voulez-vous convertir en secondes ?"))
    seconde = minute * 60 
    print(f"{minute} minutes = {seconde} secondes")

def exercice19():
    print("Exercice 19 : Prix TTC")
    HTC = int(input("Combien d'Euros HTC voulez-vous conventir en TTC"))
    TTC = HTC / 100 * 20 + HTC
    print(f"Prix TTC = {TTC}")

def exercice20():
    print("Exercice 20 : Message personnalisé ")
    nom =input("Comment vous-appelez vous ?")
    age = int(input("Quel âge avez-vous ?"))
    print(f"{nom} a {age} ans")

def exercice21():
    print("Exercice 21 : Test positif/négatif")
    nombre = int(input("Quel nombre voulez vous choisir ?"))
    if nombre > 0 : 
        print(f" {nombre} est positif")
    elif nombre < 0 : 
        print(f" {nombre} est négatif")
    else :
        print(f"{nombre} est nul")

def exercice22():
    print("Exercice 22 : Majeur ou mineur")
    age = int(input("Quel âge avez-vous ?"))
    if age < 18 : 
        print("Tu es mineur")
    else : 
        print("Tu es Majeur")

def exercice23():
    print("Exercice 23 : Note validée ")
    note = int(input("Quelle est ta note ?"))
    if note >= 10 : 
        print(f"{note} est validé")
    else :
        print(f"{note} n'est pas validé")   

def exercice24():
    print("Exercice 24 : Le plus grand de deux")
    nombre1 = int(input("Choisir un premier nombre"))
    nombre2 = int(input("Choisir un second nombre"))
    if nombre1 > nombre2 :
        print(f"{nombre1} est plus grand que {nombre2}")
    else :
        print(f"{nombre2} est plus grand que {nombre1}")

def exercice25():
    print("Exercice 25 : Ordre croissant")
    nombre1 = int(input("Choisir un premier nombre"))
    nombre2 = int(input("Choisir un second nombre"))
    if nombre1 < nombre2 :
        print(f"{nombre1} et {nombre2} sont dans l'ordre croissant")
    else :
        print(f"{nombre1} et {nombre2} ne sont pas dans l'ordre croissant")    

def exercice26():
    print("Exercice 26 : Divisible par 5")
    nombre = int(input("Choisir un nombre"))
    if nombre % 5 == 0 :
        print(f"{nombre} est divisible par 5")
    else :
        print(f"{nombre} n'est pas divisible par 5")

def exercice27():
    print("Exercice 27 : Catégorie d'âge")
    age = int(input("Quel âge avez-vous"))
    if age < 12 :
        print("Vous êtes dans la catégorie enfant")
    elif age < 18 :
        print("Vous êtes dans la catégorie ado")
    else :
        print("Vous êtes dans la catégorie adulte")

def exercice28():
    print("Exercice 28 : Température de l'eau")
    temp = int(input("A quelle température est l'eau ?"))
    if temp <0 :
        print(f"{temp}° donc l'eau est glacée")
    elif temp <= 100 : 
        print(f"{temp}° donc l'eau est liquide")
    else : 
        print(f"{temp}° donc l'eau est en ébulition")

def exercice29():
    print("Exercice 29 : Mention au bac ")
    note = float(input("Quelle note avez-vous obtenue au Bac ? "))
    if 8 <=  note < 10 :
        print(f"Votre note est de {note} vous êtes donc recalé")
    elif 10  <=  note  < 14 : 
        print(f"Votre note est de {note} c'est passable")
    elif 14 <= note < 16 : 
        print(f"Votre note est de {note} vous avez donc la mention Bien")
    else :  
        print(f"Votre note est de {note} vous avez donc la mention Très bien")

def exercice30():
    print("Exercice 30 : Compter de 1 à n")
    N = int(input("Jusqu'où vous voulez compter ? "))
    for i in range(1, N + 1):
        print(f"{i}")

def exercice31():
    print("Exercice : Compter à rebours")
    N = int(input("Depuis quel nombre voulez-vous faire un décompte ? "))
    for i in range(N, -1, -1):
        print(f"{i}")

def exercice32():
    print("Exercice 32 : Somme jusqu'à N")
    N = int(input("Choisir un nombre entier"))
    somme = 0 
    for i in range(1, N + 1):
        somme += i 
        print(f"{somme}")

def exercice33():
    print("Exercice 33 : Table de multiplication")
    table = int(input("Quelle table voulez-vous mutiplier"))
    for i in range(1, 11):
        print(f"{table} x {i} = {table * i}")    
    
def exercice34():
    print("Exercice 34 : Nombres pairs jusqu'à N") 
    n = int(input("Jusqu'à quel nombre vous voulez afficher les nombres pairs"))
    for i in range(0, n+1, 2):
        print(f"{i}")   

def exercice35():
    print("Exercice 35 : Carrés parfaits")
    n = int(input("Jusqu'à quel nombre vous voulez afficher les carrés parfait "))
    for i in range( 1,n+1):
            carre = i**2
            if carre <= n :
                print(f"{carre}")

def exercice36():
    print("Exercice 36 : Répéter un mot ")
    n = int(input("Combien de fois vous voulez répéter salut! ? "))
    for i in range(n):
        print("Salut!") 

def exercice37():
    print("Exercice 37 : Pyramide d'étoiles")
    l = int(input("Choisir la largeur de la base "))
    for i in range(l,0,-1):
        print(" " * (l-i) + "*" * (2*i-1))

def exercice38():
    print("Exercice 38 : Calculatrice simple")
    operation = input("Quelle opération souhaitez-vous faire ? ")
    n1 = int(input("Choisir un premier nombre. "))
    n2 = int(input("Choisir un second nombre. "))
    if operation == "+" :
        print(f"{n1} + {n2} = {n1+n2} ")
    elif operation == "-" : 
        print(f"{n1} - {n2} = {n1-n2}")
    elif operation == "*" :
        print(f"{n1} x {n2} = {n1*n2}")
    elif operation == "/" :
        print(f"{n1} / {n2} = {n1/n2}")
    else : 
        print("Choisir une opération parmis celle-si : +, -, x, /")

def exercice39():
    print("Exercice 39 :  Deviner pair/impair")
    import random 
    def n():
        return random.randint(0, 100)
    nombre = n()
    ru = input("pair ou impair ? ")
    if nombre % 2 == 0 :
        print(f"Le nombre est {nombre}")
        if ru == "pair":
            print("le nombre est pair vous avez gagné !")
        else : 
            print(" le nombre est impair vous avez perdu !")
    else :
        print(f"Le nombre est {nombre}") 
        if ru == "impair":
            print("le nombre est impair vous avez gagné !")
        else : 
            print(" le nombre est pair vous avez perdu !")

def exercice40(): 
    print("Exercice 40 : Validation de mot de passe")
    mp = input("Entrer un mot de passe contenant au minimum 6 caractères : ")
    nb_caracteres = len(mp)
    if nb_caracteres < 6 :
        print("Votre mot de passe est trop court")
    elif not any(c.isdigit()for c in mp) : 
            print("Votre mot dois contenir un chiffre")
    else : 
        print("Valide")
    
    

def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "40":
        exercice40()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()