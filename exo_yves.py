from random import *

def game_config():
    min_number = int(input(f"Quel est le nombre minimum ?:"))
    max_number = int(input(f"Quel est le nombre maximum ?:"))
    max_round = int(input(f"Quel est le nombre de tour maximum autorisé ?:"))
    start_guess_game(min_number, max_number, max_round)


def end_guess_game():
    user_choice = input("Voulez-vous rejouer ? Tapez Y/y pour oui N/n pour non").lower()
    if user_choice == 'y':
        return game_config()
    else:
        print("Merci d'avoir joué ! À bientôt.")


def start_guess_game(min_number, max_number, max_round):
    number = randint(min_number, max_number)
    round = 1

    while True:
        guess = input(f"Choisissez un nombre entre {min_number} et {max_number}:")
        guess = int(guess)

        if guess == number:
            print(f"Bravo ! {guess} était la bonne réponse.")
            return end_guess_game()

        if round >= max_round:
            print(f"Perdu !")
            return end_guess_game()

        if guess > number:
            print(f"Perdu ! {guess} est trop grand. Il vous reste {max_round - round} tours.")
        else:
            print(f"Perdu ! {guess} est trop petit. Il vous reste {max_round - round} tours.")

        round+=1

game_config()