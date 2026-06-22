import os

def smell(etc):
    x = os.listdir(etc)
    text_files = 0

    for file in x:
        if file.endswith(".txt"):
            print(file)
            text_files = text_files + 1
            break
    
    print("No. of txt files in etc directory are:", text_files)

smell("/")
# Peace!
