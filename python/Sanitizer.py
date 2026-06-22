Banned_words = [';', ':', '&&', 'grep', '|', '/']
Usernames = ['admin', 'crashtheweb', 'holyslap']
x = input("Enter your username: ")

for unexeptable in Banned_words:
    if unexeptable in x:
        print("You cannot use these.")
        break

    elif x in Usernames:
        print("Welcome! You found the way in.")
        break

else:
        print("Sorry, please try again.")
