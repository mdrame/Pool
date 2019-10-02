import random

#Global Varibales 
congrats_sentence = ["Nice, You is smart", "Lol that's it. Good job", "Wow. Check you out", "AYYYY you smart ash"]

def starter():
    # game welcome statement
    print( " \nHey welcome to chilling my name is Bot: -> 🤖")
    print("_____________________________________\n")
    print("Today you gone be playing a guessing game built my me")
    print("Let Go !! \n")


def game_Engine():
    
    #count determine the stage of game.
    gameCount = 0

    # user enter b/w 0 to .. and, programe randomely pick a number.
    num_Range_user_would_like = int(input("\nStarting from 0, enter the number you would like your guess to be between $: "))
    randomNumber = random.randint(0, num_Range_user_would_like)
    print(f"\nCool so now your guess number is between 0 - {num_Range_user_would_like}\n")
    #amount of time user would like the game to run.
    guessAmount = int(input("Lol how many times would you like to guess? $: "))
    # if the game stage is lesser than the amount of time the user wants to play, keep playing.
    while gameCount < guessAmount:
        user_Guess_Number = int(input("\nGuess The Secret Number $: "))
        gameCount += 1 #increment game stage for ever time user guess.
        # if next evaluate to True
        if user_Guess_Number == randomNumber:
            print(random.choice(congrats_sentence)) #congrats user by seleting an index form the congrats list (global variable)
            print("🤖")
            #ask user if they wanna play agian, if yes run game_Engine() function agian from the top
            try_Again = input('\nEnter "P" to play agin & "Q" to quite $: \n')
            try_Again.lower()
            if try_Again == "p":
                game_Engine()
            #quite game if user enter q
            elif try_Again == "q":
                return False
            else:
                #let user know they not slick and quit
                print("Wrong Input ")
                return False
        elif user_Guess_Number != randomNumber:
            print(f"Sorry {user_Guess_Number} is wrong")

    #this else clause runs if the game count is equal or grater to the amount of time user wanted to play.     
    else:
        print("\n* * * * * * * * * * * * * * ")
        print("You ran out of guess $: \n")
        try_Again = input('Enter "P" to play agin & "Q" to quite $: ')
        try_Again.lower()
        if try_Again == "p":
            game_Engine()
        elif try_Again == "q":
            return False
        else:
            print("Sorry you've enter a wrong key. GAME OVER !!!")

print("Thnaks for taking your precious time to check this cool game out")

# calling both function here 
starter()
game_Engine()










