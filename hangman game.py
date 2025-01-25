import random

def choose_word():
    words = ["python", "java", "hangman", "programming", "debugging"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 10

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! {display_word(word, guessed_letters)}")
        else:
            guessed_letters.add(guess)
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left. {display_word(word, guessed_letters)}")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word!")
            break
    else:
        print(f"Sorry, you ran out of attempts. The word was '{word}'.")

if __name__ == "__main__":
    hangman()
