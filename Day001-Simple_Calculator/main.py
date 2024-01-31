"""
Main file for the simple calculator
"""

import Calculator_Function as cf

ongoing = True


def menu():
    print("🤗🤗 Salut, Apparemment tu veux m'utiliser. Alors allons-y :\n")
    print("Alors, vous pouvez utiliser 6 opérations :\n")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Division Entière")
    print("6. Puissance")
    print("7. Quitter\n")
    print("NB: Choisissez un des chiffres pour indiquer pour effectuer une opération\n")


# Display menu
menu()
menu_choice = int(input("Entrer votre choix : \n"))

if menu_choice == 7:
    ongoing = False


while ongoing:

    # Variables set
    first_number = int(input("Entrer le premier nombre entier : "))
    second_number = int(input("Entrer le second nombre entier : "))

    # Fonctionnalités
    if menu_choice == 1:
        addition = cf.addition(first_number, second_number)
        print(f"L'addition de {first_number} par {second_number} est : {addition}")
    elif menu_choice == 2:
        substract = cf.substraction(first_number, second_number)
        print(f"La soustraction de {first_number} par {second_number} est : {substract}")
    elif menu_choice == 3:
        divide = cf.divide(first_number, second_number)
        print(f"La division de {first_number} par {second_number} est : {divide}")
    elif menu_choice == 4:
        multiply = cf.multiply(first_number, second_number)
        print(f"La multiplication de {first_number} par {second_number} est : {multiply}")
    elif menu_choice == 5:
        integer_divide = cf.integer_divide(first_number, second_number)
        print(f"La division entière de {first_number} par {second_number} est : {integer_divide}")
    elif menu_choice == 6:
        power = cf.power(first_number, second_number)
        print(f"La puissance de {first_number} par {second_number} est : {power}")
    else:
        menu()
        menu_choice = int(input("Votre choix est invalide, Veuillez entrer un autre choix : "))

    # Continuité du programme
    print("\n🥳🥳 Bravo, veux-tu continuer ? Oui / Non ")
    decision = input().lower()

    while decision != "oui" and decision != "o" and decision != "non" and decision != "n":
        print("\n🤔🤔 Tu n'a pas répondu à ma question. Est-ce que tu veux continuer ? Oui / Non ")
        decision = input().lower()

    if decision == "oui" or decision == "o":
        menu()
        menu_choice = int(input("Entrer votre choix : "))
    elif decision == "non" or decision == "n":
        ongoing = False
