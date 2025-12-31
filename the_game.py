import random

def start_game():
    print("--- Welcome to the Smart Number Guessing Game ---")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            user_input = input(f"Attempt {attempts + 1}/{max_attempts}. Enter your guess: ")
            guess = int(user_input)
            
            # Check for range
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100!")
                continue

            attempts += 1
            
            # Logic to check the guess
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
                
        except ValueError:
            print("Invalid input! Please enter a numeric integer.")
    
    if attempts == max_attempts and guess != secret_number:
        print(f"\n❌ Game Over! The secret number was {secret_number}.")

if __name__ == "__main__":
    start_game()
