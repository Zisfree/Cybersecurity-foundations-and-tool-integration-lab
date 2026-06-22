Banned_words = [';', ':', '&&', 'grep', '|', '/']
Usernames = ['admin', 'crashtheweb', 'holyslap']    # I know this is a flaw to leave such things open in cyebr but I just made it there for fun as an additional feature.
x = input("Enter your username: ")

for unexeptable in Banned_words:                    # The for loop here does not repeat like 'for in range(5)', no. Here it is to keep checking the Banned_words 
                                                    # one after another and for us it is different but the system thinks its repeating same thing since for it they are just strings in a list.
    if unexeptable in x:
        print("You cannot use these.")
        break

    elif x in Usernames: 
        print("Welcome! You found the way in.")
        break

else:
        print("Sorry, please try again.")
