# Why does a MAC address exist and how is it used in data transfer?

- MAC (Media Access Control) address is actually our systems hardware code which is given to our system when it is manufactured.
- It is a 12 digit code with pair of 2 in each section with 6 in total -> A0:B2:C6:R3:M1:E6
- Here the first 3 represent the manufature like intel or AMD and the last 3 are just random digits.

- Now, MAC address is actually used as a postal address in digital world. When you send a file it gets attached to your data(which is in frames or packets) and same goes to the recievers MAC. It also gets tagged on it.
- When the recievers system gets this data it checks if it has its own MAC address on it or not otherwise it rejects the data sent.
- Also the MAC address which the reciever sents does not travel through internet it uses a local automated discovery protocol.
- Also your MAC is only shared if the device is in your LAN outside that others dont recive your MAC address they just send it using your IP.
