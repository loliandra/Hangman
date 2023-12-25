import random
from hangman_art import logo, stages
from hangman_words import word_list
from replit import clear

chosen_word = random.choice(word_list)
end_of_game = False
lives = 6

print(logo)

#Create blanks
display = []
for letter in chosen_word:
    display.append("_")  #  display += "_"

while end_of_game == False:
    guess = (input("Write your letter: ")).lower()

    clear()
  
    if guess in display: 
      print(f"You've already guessed {guess}")
  
    #Check guessed letter
    for i in range(len(chosen_word)):
        if (chosen_word[i] == guess) and guess not in display[i]:
            display[i] = guess
  
    if guess not in chosen_word:
      print(f"There isnt letter {guess} in this word")
      lives -= 1
      if lives == 0:
        print("You lose.")
        end_of_game = True
        
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You are win")

    print(stages[lives])
    