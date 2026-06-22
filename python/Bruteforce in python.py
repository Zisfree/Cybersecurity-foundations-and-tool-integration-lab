code = 'aa7dbc'
attempts = 3

while attempts > 0:                                     # While loop tells python to keep running the command. The attempts > 0 tell it to do it till the attempts left are 0.
    guess = input("Password of 5 digits:")

    if guess == code:                                   # Here the if command analizes that the code matched with our guess or not.
       print("Correct!")
       break

    else:      
       attempts = attempts - 1
       print("Wrong")

