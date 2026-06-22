import os

def hacked(root):
    x = os.listdir(root)
    
    for file in x:
        if "password" in file or "passwords" in file or "username" in file or "flag" in file:
            print("This files has the name u need", file)

hacked("/")
