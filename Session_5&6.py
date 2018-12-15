#Sessions 5&6
# The player is trapped in the “magic maze”.
# If still in the “magical maze”, ask the player which way to go. Announce it like:
# “You are in the magic maze. Which way to go? (N,S,E,W)”
# Accepted directions are N[orth], S[outh], E[ast] and W[est].
# The secret escape combination is: SSNWES
# Keep track of the number of “moves”
# If the escape sequence is correct, announce that the player has won:
# “You have escaped the maze in X moves”
# If the escape chain is broken, start from the beginning. Suppose the player has the sequence SSN and then tries E. This breaks the chain an we must start again from the first valid move: S. After 10 moves the player loses one life
# The player starts with 3 lives and “dies” when the life counter reaches 0
# Inform the player when he loses one life and how many he has left




moves = 0
lives = 3
combination = "SSNWES"
decision = ""

boolean = True

while True:
   if lives == 0:
       print("You ran out of lives. You dead.")
       break

   else:

       m1 = input("Choose first move""\n")
       moves = moves+1
       m1 = m1.lower()
       if m1 == "s":
           decision = decision + m1
       else:
           print("Wrong move. You lose a life")
           lives = lives-1
           print("Remaining lives: ")
           print(lives)
           continue


       m2 = input("Choose second move""\n")
       m2 = m2.lower()
       if m2 == "s":
           decision = decision + m2
       else:
           print("Wrong move. You lose a life")
           lives = lives-1
           print("Remaining lives: ")
           print(lives)
           continue


       m3 = input("Choose third move""\n")
       m3 = m3.lower()
       if m3 == "n":
           decision = decision + m3
       else:
           print("Wrong move. You lose a life")
           lives = lives-1
           print("Remaining lives: ")
           print(lives)
           continue

       m4 = input("Choose fourth move""\n")
       m4 = m4.lower()
       if m4 == "w":
           decision = decision + m4
       else:
           print("Wrong move. You lose a life")
           lives = lives-1
           print("Remaining lives: ")
           print(lives)
           continue

       m5 = input("Choose fifth move""\n")
       m5 = m5.lower()
       if m5 == "e":
           decision = decision + m5
       else:
           print("Wrong move. You lose a life")
           lives = lives-1
           print("Remaining lives: ")
           print(lives)
           continue


       m6 = input("Choose final move""\n")
       m6 = m6.lower()
       if m6 == "s":
           decision = decision + m6

       else:
           print("Wrong move. You lose a life")
           lives = lives-1
           print("Remaining lives: ")
           print(lives)
           continue

       decision = decision.upper()

   if decision == combination:
           print("Congratulations. You are out of the maze")