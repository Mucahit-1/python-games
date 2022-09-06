from art import vs
from game_data import data
import random


def format_data(account):
 account_name = account["name"]  
 account_desc = account["description"]  
 account_country = account["country"]  
 return f'{account_name}, a {account_desc} , from {account_country}'

def check_answer(guess , a_followers , b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
    

score = 0
game_should_continue = True
account_b = random.choice(data)


while game_should_continue:

 account_a = account_b
 account_b = random.choice(data)
 while account_a == account_b:
   account_b = random.choice(data)

 print(f"compare A: {format_data(account_a)}.")
 print(vs)
 print(f"compare B: {format_data(account_b)}.")

 guess = input("who has more followers ? type 'A' or 'B' :").lower()

 a_followers_count = account_a["follower_count"]
 b_followers_count = account_b["follower_count"]


 is_correct = check_answer(guess , a_followers_count , b_followers_count)
 if is_correct:
  score += 1
  print(f'you are right current score {score}')
  if score == 3:
   game_should_continue = False
 else:
  game_should_continue = False
  print(f'sorry it is wrong final score is {score}')