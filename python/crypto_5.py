from pwn import xor

x = b"slash"         
# b converts it into bytes. Though not adding it will not change anything. The system will convert it itself.
key = 15
xored = xor(x, key)
# xor() is the function used here,

print(xored)
