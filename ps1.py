#start of the program
#take input string
s=raw_input("enter binary bit data that has to be transmitted: ")
#sting conversion
s=str(s)
#count 1 in string
count_one=s.count("1")
#if count is even append 1
if(count_one%2==0):
	p="1"
else:
	p="0"  
# append parity
print("Parity bit data: {s}".format(s=s+p))
#insert 0 after 010
s=s.replace("010","0100")
#append parity  and flag
s=s+p+"0101"
#print it
print('Transmitting data: {p}'.format(p=s))
