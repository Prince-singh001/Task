import random

def guess_number():
    
    number_guess = random.randint(1, 100)

  
    max_attempts = 8
    attempts = 0

    print(" Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess the number.\n")


    while attempts < max_attempts:

        try:

            user_guess = int(input("Enter your guess: "))
            attempts += 1

        
            if user_guess < number_guess:
                print(" Too low! Try again.")
            elif user_guess > number_guess:
                print(" Too high! Try again.")

            else:
                print(f"\n Congratulations! You guessed the number {number_guess} correctly.")
                print(f"You guessed it in {attempts} attempts.")
                return

            
            print(f"Attempts left: {max_attempts - attempts}\n")

        except ValueError:
            print("Invalid input! Please enter a valid integer.\n")


    print("\nGame Over!")
    print(f"The correct number was: {number_guess}")

if __name__ == "__main__":
    while True:
        guess_number()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\n Thanks for playing!")
            break

guess_number()
