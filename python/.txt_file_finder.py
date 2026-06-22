import os

def smell(etc):                                                             # This etc might seem to have no use but it acts as a dynamic folder. Without it we cannot run search with ("/").
    
    x = os.listdir(etc)
    text_files = 0

    for file in x:
        if file.endswith(".txt"):                                            # .endswith() as its name suggests is a tool to find what u tell it to which the file ends with.
            print(file)
            text_files = text_files + 1
            break
    
    print("No. of txt files in etc directory are:", text_files)

smell("/")
# Peace
