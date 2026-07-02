from Crypto.Util.number import *

x = 1937076257

decodeds = long_to_bytes(x)
# To convert it back to base10 *bytes_to_long()*
# To veiw in ASCII use -> *variable.decode('ascii')*
print(decodeds)
