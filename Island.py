print('''
 mm.           dM8
 YMMMb.       dMM8
  YMMMMb     dMMM'
   `YMMMb   dMMMP
     `YMMM  MMM'
        "MbdMP
    .dMMMMMM.P
   dMM  MMMMMM
   8MMMMMMMMMMI
    YMMMMMMMMM
      "MMMMMMP
     MxM .mmm
     W"W """
''')
print("Welcome to PlayBoy Island.")
print("Your mission is to find the propper room with the girl.") 

# Room 1
print("You are in corridor.")
print("There are three doors: white, yellow and red")
print("Which whan will you open?")
door=input("Choose the door: white, yellow or red \n").lower()
if door=="white":
  print("You are in room 2")
  print("The room is empty.")
  print("Game Over")
if door=="red":
    print("You are in room 3")
    print("The room is empty.")
    print("Game Over") 
if door == "yellow":
  print("You have opened yellow door.")
  print("There are three beds: small, medium and big")
  print("Which whan will you choose?")
  bed=input("Choose the bed: small, medium or big \n").lower()
  if bed == "small":
    print("The bad is empty. Game Over")
  elif bed == "medium":
    print("The bad is empty. Game Over")
  else:
    print("Theare is your love. You win this game")
else:
  print("Game Over")

//the end
