import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0
    guessed_number = 0
    
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while guessed_number != secret_number:
        try:
            guessed_number = int(input("Take a guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        
        attempts += 1
        
        if guessed_number < secret_number:
            print("Too low! Try again.")
        elif guessed_number > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
        if attempts == 5:
         print("You run out of attempts", )
         break

guess_number()
