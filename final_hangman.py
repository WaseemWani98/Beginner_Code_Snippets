import random

langs = ['python', 'java', 'kotlin', 'javascript']
no_of_chances = 8

print("H A N G M A N")
session_inputs = ["play", "exit"]
while True:
    session = input('Type "play" to play the game, "exit" to quit:')
    if session == "play":
        select = random.choice(langs)
        hyphens = "-" * len(select)
        already_guessed = []
        while no_of_chances != 0:
            if hyphens.count('-') != 0:
                print()
                print(hyphens)
                choice = input("Input a letter:")
                if len(choice) != 1:
                    print("You should input a single letter")
                else:
                    if choice.islower() == False:
                        print("Please enter a lowercase English letter")
                    elif choice in already_guessed:
                        print("You've already guessed this letter")  
                    elif choice in select and choice not in already_guessed:
                        already_guessed.append(choice)
                        count = select.count(choice)
                        ind = select.index(choice)
                        while count >= 1:
                            if select[ind] == choice:
                                hyphens = hyphens[:ind] + choice + hyphens[ind+1:]
                                count -= 1
                                ind += 1
                            else:
                                ind += 1
                    elif choice not in select and choice not in already_guessed:
                        no_of_chances -= 1
                        print("That letter doesn't appear in the word")
                        already_guessed.append(choice)
            else:
                print()
                print(select)
                print("You guessed the word!\nYou survived!")
                print()
                break
        if no_of_chances == 0:
            print("You lost!")
            print()
    elif session == "exit":
        break
