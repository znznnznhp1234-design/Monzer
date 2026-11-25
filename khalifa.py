


import random

print ("Welcome to the Rock, Paper, scissors game : ")

rules = input ("Press Enter to continue or type (Help) for the rules help : ").lower()

if rules == "help" :
    print ("********Rules********")
    print ("1️⃣  You choose and the computer chooses\n" \
           "2️⃣  Rock smashes scissors ---> Rock Wins\n" \
           "3️⃣  Scissors cut paper ---> scissors Win\n" \
           "4️⃣  Paper covers rock ---> paper Wins")
    
Y =     ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

""")

U =      ("""
     _______
---'    ____)____
           ______)
          _______)  
         _______)
---.__________)
""")

I =     ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""") 

choose = input ("\n\nEnter your choice (rock, paper, scissors) : ").lower()
A = ("rock", "paper", "scissors")
if choose not in A :
        print ("Invalid choice. Please run the program again and choose rock, paper, or scissors")
else:
     computer =random.choice(A)
     if choose == "rock" :
       print (f"You choose  {Y}")
     elif choose == "paper" :
       print (f"You choose  {U}")
     elif choose == "scissors" :
       print (f"You choose  {I}")
     if computer == "rock" :
       print (f"computer choose  {Y}")
     elif computer == "paper" :
       print (f"computer choose  {U}")
     elif computer == "scissors" :
       print (f"computer choose  {I}")
     if choose == "rock" and computer == "rock" :
      print ("Resemble❗❗❗ Please try again\n")
     elif choose == "rock" and computer == "paper" :
      print ("You Lose😥😥😥\n")
     elif choose == "rock" and computer == "scissors" :
      print ("You win🔥🔥🔥\n")
     elif choose == "paper" and computer == "rock" :
      print ("You win🔥🔥🔥\n")
     elif choose == "paper" and computer == "paper" :
      print ("Resemble❗❗❗ Please try again\n")
     elif choose == "paper" and computer == "scissors" :   
      print ("You lose😥😥😥\n")
     if choose == "scissors" and computer == "rock" :
      print ("You lose😥😥😥")
     elif choose == "scissors" and computer == "paper" :
      print ("You win🔥🔥🔥")
     elif choose == "scissors" and computer == "scissors" :   
      print ("Resemble❗❗❗ Please try again") 



