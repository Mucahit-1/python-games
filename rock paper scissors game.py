import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

play = True
while play:
  x = input("\nwhat do you choose? 0 for rock , 1 for paper , 2 for scissors\nor exit to stop playing")
  computer = random.randint(0 , 2)

  if x == "0":
    print(rock)
    if computer == 0:
      print("computer choise\n" + rock + "\nplay again")
    elif computer == 1:
      print("computer choise\n" + paper + "\nyou lose")
    else:
      print("computer choise\n" + scissors + "\nyou win")

  if x == "1":
    print(paper)
    if computer == 0:
      print("computer choise\n" + rock + "\nyou win")
    elif computer == 1:
      print("computer choise\n" + paper + "\nplay again")
    else:
      print("computer choise\n" + scissors + "\nyou lose")

  if x == "2":
    print(scissors)
    if computer == 0:
      print("computer choise\n" + rock + "\nyou lose")
    elif computer == 1:
      print("computer choise\n" + paper + "\nyou win")
    else:
      print("computer choise\n" + scissors + "\nplay again")

  if x =="exit":
    play = False

