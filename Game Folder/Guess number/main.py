from random import randint
from art import logo, won_logo, lost_logo

EASY_LEVEL = 15
NORMAL_LEVEL = 10
HARD_LEVEL = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):

  if guess > answer:
    print("The Guess is Too high.\n")
    return turns - 1
  elif guess < answer:
    print("The Guess is Too low.\n")
    return turns - 1
  else:
    print(f"\nYou got it! The answer was {answer}.")
    print(won_logo)
    play_again()

#Make function to set difficulty.
def game_difficulty():
  level = input("Choose a difficulty. Type 'easy', 'normal' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL
  elif level == "normal":
    return NORMAL_LEVEL
  else:
    return HARD_LEVEL

def play_again():
  again = input("\nDo you still want to play again? Y/N: ").upper()
  if again == 'N':
      exit()
  else:
      game()

def game():
  print(logo)
  print("Enjoy the Number Guessing Game!\n")
  print("I bear-buddy will randomly generate a number, you must gess it before your life runs out!\n")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)

  turns = game_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"\nYou only have {turns} chances to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose. You will be crucified")
      print(lost_logo)
      play_again()
      
    elif guess != answer:
      print("Guess again.")


game()
