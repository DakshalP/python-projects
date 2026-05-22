#meant to be played on a computer
#make your console wider/taller if it's displaying weird

dayGoal = 10;
levelGoal = 10;

breakLineLength = 61

bank = 1000
#don't use this var in calculations, instead use getDaily() to calculate it
daily = 0 
day = 0

#this was for rooms, a functionality removed
#perRoomDaily = 50
addOnToDaily = -50 #start off w/ 50 less to pay staff


name = "Null"

#In the following arrays, at index 0 is an array with the daily-value-add, price,  and description. The rest of the array is the ascii art
roof = [[200,"(You can't buy a roof)"], ". . o o  ","       o","_______][__","[] [] [] []","[_________]"]

level = [[200, 1000, "You bought a normal level with four rooms."], "[] [] [] []","[_________]"]
restaurant = [[1400, 3000, "You bought a restaurant! Your patrons are starting to give you better reviews on Belp. "], "(___) (___)_","[_________]/"]
suite = [[300, 1000, "You bought a one room suite! The view from the balcony is great."], "(_________)_","[_________]/"]
bowling_alley = [[600, 1550, "You bought a bowling alley! Just hope the sound doesn't keep some guests from sleeping"], "() (___) ()","[_________]-🎳"]

taxi_cabs_at_base = [[500, 1800,"You hired a taxi cab company to proivde some transportation for your patrons. You get a percentage of the profit!"], "[] [] [] []     /〜\     /〜\\","[___|=|___]     o--o     o--o"]
pool_at_base = [[440, 1250,"You hired a taxi cab company to proivde some transportation for your patrons. You get a percentage of the profit!"], "[] [] [] []      _|〜〜〜〜〜〜〜|","[___|=|___]     / |              |"]
base = [[0,"(You can't buy a base)"], "[] [] [] []     @@@@     @@@@","[___|=|___]      ||       ||"]

#hotel array of ascii art
#if you want to see how some art looks, add it to this array
hotel = [roof, suite, bowling_alley, base]

#other non-building ascii
title = [" __      ______  __   ________  __           __  __  ______  ", "/\ \    /\  ___\/\ \ / /\  ___\/\ \         /\ \/\ \/\  == \ ", "\ \ \___\ \  __\\ \ \ '/\ \  __\\  \ \____    \ \ \_\ \ \  _-/", " \ \_____\ \_____\ \__| \ \_____\ \_____\    \ \_____\ \_\   ", "  \/_____/\/_____/\/_/   \/_____/\/_____/     \/_____/\/_/   " ]

soldSign = [" __  _  _    __  ", "/ _|/ \| |  |  \ ", "\_ ( o ) |_ | o )", "|__/\_/|___||__/ "]

def printAscii(arr):
  for string in arr:
    print(string)

def getLevels():
  return str(len(hotel))

def getDaily():
  daily = 0
  for levelArr in hotel:
    #each daily value is stored in the first index of the first index of the ascii art array, varies for each level art
    daily += levelArr[0][0]
  return str(daily)

def printStats():
  stats = "\nDay " + str(day) + ":  $" + str(bank) + "   " + getLevels() + " Levels" + "   " + "$" +  getDaily() + "/Day"
  for i in stats:
    print("-", end="")
  print(stats)

def printBuilding(arr_sqrd):
  print("\n\n")
  for arr in arr_sqrd:
    for i in range(len(arr)):
      if(i != 0):
        print(arr[i])
  printStats()

def dayPasses():
  global day, bank, daily
  day += 1
  bank += int(getDaily())

  print("\n\n")
  for i in range(breakLineLength):
    print("-", end = "")
  print("\nA DAY HAS PASSED. IT'S NOW DAY " + str(day) + ".")
  playTurn()

def playTurn():
  printBuilding(hotel)
  
  print("\nHere's what you can do: \n  - Go to the shop to buy more levels. \n  - Sleep to move on to the next day and collect your daily profit.")

  action = "null"
  while(action != "shop" and action != "sleep"):
    action = input("\n  Type 'shop' or 'sleep': ").lower()

  if(action == "shop"):
    print("Access shop (WIP)")
  elif(action == "sleep"):
    dayPasses()

def beginGame():
  global name
  global hotel

  print("\n\n")
  printAscii(title)
  print("\nA console-based game meant to be played on a monitor.")

  # while name == "Null":
  #   name = input("\n\nHi! What's your name? \nTell me: ").title()

  printBuilding(hotel)
  print("\nWelcome to your hotel, " + name + "!" + "\nThis screen also shows how much money you have and how much you make each day. More levels = more money each day. ")
  
  enter = "null"
  while(enter == "null"):
   enter = input("\n  Press enter to continue")

  print("\n\nThere's a large convention coming to town in " + str(dayGoal) + " days, and you want to capture all the business you can.\nYou've been told, though, that your hotel is too small.\nYou have " + str(dayGoal) + " days to get " + str(levelGoal) + " levels.\nAre you up for the challenge?")
  
  enter = "null"
  while(enter == "null"):
    enter = input("\n  Press enter to continue")


beginGame()

day += 1
playTurn()