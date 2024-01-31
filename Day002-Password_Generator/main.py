"""
Title : Password Generator

Objectifs : Create a console application for generation of password
Output: We will have a programme which ask to the user the size of the password
        and generate secure password
"""
from string import ascii_letters
import random

ongoing = True


def display_menu():
    print("😊😊 I know why you are there, so start :")
    print("how much characters may your password have ?\n")


while ongoing:

    dictionnary = list(ascii_letters + r"&(-_à)=~#{[|`\@]}" + "1234567890" + ",;:!ù*^$<>?.§%µ¨£")
    new_dictionnary = "".join(random.sample(dictionnary, len(dictionnary)))

    display_menu()
    user_choice = int(input("Enter the password size (an integer) :"))

    start_indice = random.randrange(len(new_dictionnary) - user_choice + 1)
    password = new_dictionnary[start_indice: start_indice + user_choice]

    print(f"Your secure password is : {password}")
