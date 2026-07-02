import base64
x = "B2 29 5E 9D C7 A2 B2 D8 5E B1 E7 28 9D D6 DE B2"
# The hex code
y = bytes.fromhex(x)
# converting the hex to byte
z = base64.b64encode(y)
# The base64 converter
print(z)
