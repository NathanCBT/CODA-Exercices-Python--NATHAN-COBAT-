def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2():
    print("Exercice 2 : Afficher son prenom")
    prenom = input("Entrer votre prenom")
    print(f"Bonjour {prenom}!")




def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "2":
        exercice2()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()