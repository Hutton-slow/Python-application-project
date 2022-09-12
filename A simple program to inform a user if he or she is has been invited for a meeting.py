#A simple program to inform a user if he/she is has been invited for a meeting.

#To check weather u are late or not,u need to import time.
import datetime
currentTime = datetime.datetime.now()
currentTime.hour

#index_numberDb is my database
index_numberDb=("0321080001","0321080002","0321080003")
print("\t\tWelcome to the AXCLR8 CLUB.\n")
index_number=input("Please enter your index number:\n")
a=len(index_numberDb)


#Using if condition to check the time
if currentTime.hour < 16:

    #using for loop
    #a is representing the elements in the index_numberDb
    for a in range(len(index_numberDb)):
        
        if index_numberDb[a]==index_number:
                print("\nCongratulation!", end = '')
                print("\nYou're invited to join today's meeting.", end = '')
                print("\nThank you!", end = '')
                x=1
                break
               
        else:
            print("\nSorry!\nYou're not invited", end = '')
            print("\n", end = '')
            break
        
        
else:   
    print("\nSorry!\nYou're late\n See you another time", end = '')

    
