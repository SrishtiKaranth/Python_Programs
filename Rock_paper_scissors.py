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

opt1=input("Choose your option: 0-Rock , 1-Paper and 2-Scissors ")
if opt1=="0":
  print(rock)
elif opt1=="1":
  print(paper)
elif opt1=="2":
  print(scissors)
else:
  print("Invalid number, choose again")
print("Computer chose:")
opt2=str(random.randint(0,2))
if opt2=="0":
  print(rock)
elif opt2=="1":
  print(paper)
elif opt2=="2":
  print(scissors)
if opt1=="0" and opt2=="2":
  print("You win")
elif opt1=="0" and opt2=="1":
  print("You lose")
elif opt1=="0" and opt2=="0":
  print("Match drawn")
elif opt1=="1" and opt2=="2":
  print("You lose")
elif opt1=="1" and opt2=="0":
  print("You win")
elif opt1=="1" and opt2=="1":
  print("Match drawn")
elif opt1=="2" and opt2=="2":
  print("Match drawn")
elif opt1=="2" and opt2=="0":
  print("You lose")
elif opt1=="2" and opt2=="1":
  print("You win") 
