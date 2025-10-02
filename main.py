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


def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "4":
        exercice4()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()