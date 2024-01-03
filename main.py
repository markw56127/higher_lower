import random
from art import logo, vs
from game_data import data

print(logo)

def higher_lower():
  score = 0
  game_cont = True
  
  num1 = random.choice(data)
  num2 = random.choice(data)
  while num1 == num2:
    num2 = random.choice(data)
  
  while game_cont == True:
    while num1 == num2:
      num2 = random.choice(data)
    print(f"Compare A: {num1['name']}, a {num1['description']}, from {num1['country']}.")
    print(vs)
    print(f"Against B: {num2['name']}, a {num2['description']}, from {num2['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if choice == 'A':
      if num1["follower_count"] > num2["follower_count"]:
        score += 1
        print(f"You're right! Current score: {score}.")
        num1 = num2
        num2 = random.choice(data)
      else:
        print("You lose.")
        print(f"Your final score was {score}.")
        game_cont = False
    elif choice == 'B':
      if num1["follower_count"] > num2["follower_count"]:
        print("You lose.")
        print(f"Your final score was {score}.")
        game_cont = False
      else:
        score += 1
        print(f"You're right! Current score: {score}.")
        num1 = num2
        num2 = random.choice(data)

  cont = input("Would you like to play again? Type 'yes' or 'no': ")
  if cont == 'yes':
    higher_lower()

higher_lower()
