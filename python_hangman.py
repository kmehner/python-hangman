
# Derrick 

# TODO: Input

# Ask the user for letters they think are in the word 
# guessed_word 
# fail_count 

# Take the letter they gave us and check if it is part of the word 
# if the letter is in the word, it fills out the "guessed word"
# if the letter is not in the word, hangman gets closer to death (6)

# loop until fail_count > 6 

# print - console.log()
# len(word) - word.length 
# if letter in word:  - if (word.includes(letter)) 

word = "Derrick"
guessed_letters = []
word_length = len(word)
fail_count = 0 

# Game starts 
while fail_count < 6: 
  # Show the word progress 
  # The underscore or the letter to show the progress of how many has been guessed 

  # User makes their guess
  guess = input("Guess a letter: ")

  # BONUS: validate the letter (is through a-z, !)

  # Add it to our guessed letters 
  if guess in guessed_letters:
    print(f"You already guessed this letter: {guess}")
  else:
    guessed_letters.append(guess)

  # Check if the letter is in the word 
  if guess in word.lower():
    print("Good guess! Your letter is in the word")
  else:
    print("Sorry, that letter is not in your word")
    fail_count += 1


  # CHECK IF IT IS A WIN 

  # break 