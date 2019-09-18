#start of the program
#take input string
s=raw_input("enter binary bit data that has to be transmitted: ")
#sting conversion
s=str(s)
count_one=s.count("1")
if(count_one%2==0):
	p="1"
else:
	p="0"
print("Parity bit data: {s}".format(s=s+p))
s=s.replace("010","0100")
s=s+p+"0101"
print('Transmitting data: {p}'.format(p=s))
