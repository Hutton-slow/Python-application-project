import datetime
currentTime = datetime.datetime.now()
currentTime.hour
index_numberDb=[["0321080001","0321080002","0321080003"]]
print("\t\tWelcome to the AXCLR8 CLUB.\n")
index_number=input("Please enter your index number:\n")
x=1

while currentTime.hour < 16:
    for a in range(len(index_numberDb)):
      for b in range(len(index_numberDb[a])):
        if index_numberDb[a][b]==index_number:
            print("\nCongratulation!", end = '')
            print("\nYou're invited to join today's meeting.", end = '')
            print("\nThank you!", end = '')
            x=x+1
            break
        
    
        else:
                print("\nSorry!\nYou're not invited", end = '')
                print("\n", end = '')
    
print("\nSorry!\nYou're late\n See you another time", end = '')

    
