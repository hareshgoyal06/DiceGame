import random 
print("      DICE GAME \n")

#intialize variables; start game with 500 pts
total_points = 500
user_total = 0
cpu_total = 0 
restart = True  
tiebreaker = True

while restart == True: 
  print("You have " + str(total_points) + " points.")
  int(total_points)
  wagered_points = int(input("Enter points to wager (-1 to QUIT):      "))
#possibilites dependant on points wagered 
  if wagered_points == -1:
    print("\nThanks for playing! Goodbye!")
    break
  elif wagered_points > total_points: 
    print("\nPlease enter a wager equal to or less than " + str(total_points) + " points.\n")
    int(total_points)
  elif wagered_points <= 0: 
    print("\nYou must at least wager one (1) point.\n")
  else: 
#generating random numbers and outputting
    while tiebreaker == True:
      user_number1 = random.randrange(1, 7)
      user_number2 = random.randrange(1, 7)
      cpu_number1 = random.randrange(1, 7)
      cpu_number2 = random.randrange(1, 7)
      user_total = user_number1 + user_number2
      cpu_total = cpu_number1 + cpu_number2
      print("\nYou rolled a [", end="")
      print(user_number1, end="")
      print("][", end="")
      print(user_number2, end="")
      print("]")
      print("Computer rolled a [", end="")
      print(cpu_number1, end="")
      print("][", end="")
      print(cpu_number2, end="")
      print("] ")
#possibilites depending on the sum of dice rolled
      if user_total > cpu_total: 
        user_total = 0
        cpu_total = 0 
        print("\nYou win " + str(wagered_points) + " points! \n" )
        int(wagered_points)
        total_points += wagered_points
        wagered_points == 0 
        break
      elif user_total < cpu_total: 
        user_total = 0
        cpu_total = 0 
        print("\nYou lose " + str(wagered_points) + " points! \n" )
        int(wagered_points)
        total_points -= wagered_points
        wagered_points == 0  
        break
      elif user_total == cpu_total: 
        print("\nIt's a tie!")
        user_total = 0
        cpu_total = 0 
        tie = input("Enter 'R' to roll again:   ")
        if tie.lower() == "r":
          tie_breaker = True  
        else:
          print("\n")
          break
#if all points are lost     
    if total_points <= 0: 
      print("GAME OVER! You have 0 points left! \n")
      replay = input("Would you like to play again (Y or N)? ")
      if replay.lower() == "y": 
        restart == True
        total_points += 500
        print("\nWelcome back! \n")
        continue
      elif replay.lower() == "n":
        print("Thanks for playing! Goodbye!")
        break
      else: 
        print("Please enter a valid answer!\n")
        replay = input("Would you like to play again (Y or N)? ")
        if replay.lower() == "y": 
          restart == True
          total_points += 500
          print("\nWelcome back! \n")
          continue
        elif replay.lower() == "n":
          print("Thanks for playing! Goodbye!")
          break
        else:
          print("Goodbye!")
        

      
    
  
    
    
    
    
    
      
    
