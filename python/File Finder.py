import os                            # to import imp toolkits inside os

def smashpc(etc):                    # smashpc is the pc's name we r searching on(tho its my pc its going to search)
    file_scanner = os.listdir(etc)   # a tool to find directories. Here it will search the folder etc.
    
    for y in file_scanner:           # This loop will visit each file in etc folder 1 by 1.
        print(y)

smashpc("/")                         # This makes it scan the entire directory.
