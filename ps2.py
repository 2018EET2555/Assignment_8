# def check_validity():

# def enter():
print("Welcome to the Game!")
def enter(p,v):
	i=(v-1)/3
	j=(v-1)%3
	arr[i][j]=v

def isvalid(p,val,player):
	if p>9 || p<1 || (player==1 && v%2==0) || (player=2 && v%2==1) || v>9 ||v<1 || (v in numbers):
		return 0
	return 1 

def game():
	print("Player 1's chance")
	check=1     #->>>>>>>>>>>>>>>>>>>>>>>>>>> modifgfy check
	player=1
	while check==1   : #ask user want to continue
		p,v=raw_input("Enter the position and number to be entered: ").split()
		p=int(p)
		v=int(v)
		if isvalid(p,v,player):
			enter(p,v)

			numbers=[]
			print(p,v,type(p))
			check=0
		else:
			print("value not valid enter again")



# print(game)
flag="1"
while flag=="1":
	numbers=[]
	arr=[[0 for i in range(3)] for j in range(3)]
	game()
	flag=str(raw_input("enter 1 for continue enter 0 other key for exit "))
