int = [61,36,63,38,62,36,37,33,33,63,39,62,32,32,64,65,37,62,63,30,32,35,33,32,36,36,61,33,38,36,37,64,66,35,35,61,63,64,65,38,36,33,35,65,31,39,63,37,33,33,31,33]

ascii = ""

for ascii_charecter in int:
  ascii += chr(ascii_charecter)

print(ascii)
# chr() is used to convert the integers above to ASCII charecters
# ord() function does opposite of chr()
