# def check_validity():

# def enter():
print("Welcome to the Game!")
def game():
	print("Player 1's chance")
	check=1
	while check==1   : #ask user want to continue
		p=raw_input("Enter the position and number to be entered: ")
		print(p)
		check=0



arr=[[0 for i in range(3)] for j in range(3)]
print(game)
flag="1"
while flag=="1":
	game()
	flag=str(raw_input("enter 1 for continue enter 0 other key for exit "))
