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
    


def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "8":
        exercice8()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()