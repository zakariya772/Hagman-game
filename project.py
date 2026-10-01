import random
words = ["javascript","html","css","python"]
def hagman_game():
    guess_word = random.choice(words)
    print(guess_word)
    attempt = len(guess_word)
    guess_bar = ["_"]*attempt
    seen = []
    while attempt > 0:
        found = False
        choice = input("guess a letter ?")
        if len(choice) != 1 or not choice.isalpha():
            print("enter only one alphabet letter")
            continue 
        if choice in seen:
                print("repeating guessed letter not allow.")
                continue
        seen.append(choice)
        for index,letter in enumerate(guess_word):
            if choice == letter:
                found = True  
                guess_bar[index] = choice 
        if not found:
            attempt-=1
            print(attempt)
            if attempt == 0:
                print("you loose ❌")
        else:
            answer = "".join(guess_bar)
            print(answer)
            if answer == guess_word:
                print("you win the game 🎉")
                break

def restart_game():
    while True:
        hagman_game()
        while True:
            question = input("will you like to play again ? yes/no.").lower().strip()
            if question == "yes":
                break
            elif question == "no":
                print("program end.")
                return
            else:
                print("Please input yes or no.")
restart_game()