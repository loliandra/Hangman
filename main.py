import random
#Step 3

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for letter in chosen_word:
    display.append("_")
print(display)


#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game = False

while end_of_game == False:
  guess = (input("Write your letter: ")).lower()
  #Check guessed letter
  for i in range(len(chosen_word)):
   if chosen_word[i] == guess:
     display[i] = guess
  print(display)

  if "_" not in display:
      end_of_game = True
      print("You are win")

