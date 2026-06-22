import os

def Seemless(dir):
    x = os.listdir(dir)
    total_files = 0

    for y in x:
        print(y)
        total_files = total_files +1                   # Everytime the loop starts again it will +1

        print("The total no. of files are:", total_files)  # This must run after loop ends otherwise it shows everytime it counts a file.
        

Seemless("/")
