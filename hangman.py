import random

# List of words
words = ["python", "computer", "programming", "developer", "coding"]

# Select a random word
word = random.choice(words)

print("🎮 Welcome to Hangman!")
print("The word has", len(word), "letters.")

# Hide the word
hidden_word = ["_"] * len(word)

# Number of lives
lives = 6

# Store already guessed letters
guessed_letters = []

# Start the game
while lives > 0:

    print("\nWord:", " ".join(hidden_word))
    print("❤️ Lives remaining:", lives)
    print("🔤 Guessed letters:", " ".join(guessed_letters))

    # Get user's guess
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter only one letter!")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!")
        continue

    # Store the new guess
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print("✅ Correct guess!")

        # Reveal the correct letter
        for index, letter in enumerate(word):
            if letter == guess:
                hidden_word[index] = guess

    else:
        print("❌ Wrong guess!")
        lives = lives - 1

    # Check whether the player has won
    if "_" not in hidden_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

# Check whether the player has lost
if "_" in hidden_word:
    print("\n❌ Game Over!")
    print("The word was:", word)

