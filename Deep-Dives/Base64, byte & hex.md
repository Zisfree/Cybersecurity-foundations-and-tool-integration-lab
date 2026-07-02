## How does Base64 work?
- Base64 is a cipehr with == or = at its end.
- It reads an 8 bit standard bit or any bit's every 6 bits.
- This causes it to miss the remaining 2 bits in a 8 bit. So it uses the lowest common multiple of both.
- If the bit does not have any Lowest common multiple with 6 then it misses some of the words and to compensate that it adds = or == for mising 1 or 2 words.

## Byte
- Byte is actually the binary code of 0's and 1's.
- The system can convert these 0's and 1's to text and can read.
- So they might be some binary asometimes or a text the other times.

## Hex-byte
- These are 2 different things.
- Hex byte is the actual computer readable data. It is a 8-bit binary data inside the system.
- We call 100010 a binary while something represented by 2 charecters in crypto is called hex-byte.

## Hex
- Hex is the actuall 2 digit base16 data we see. It is base16 cause it uses charecters from 0-9 and A-F
- A single hex charecter represents only 4 bits(like in 4A 4 only represents the 4 bits. The other 4 are done by A).
- To identify the hex system usualy starts it with *0x* charecters.
