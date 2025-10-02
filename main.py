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
    print(f"{nombre1} - {nombre2} = {somme}")

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




def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "22":
        exercice22()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()