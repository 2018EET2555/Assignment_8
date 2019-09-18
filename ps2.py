# def check_validity():

# def enter():
print("Welcome to the Game!")
def enter(p,v,player):
	flag=4
	i=(v-1)/3
	j=(v-1)%3
	arr[i][j]=v
	# sum_r[i][player]+=
	sum_r[i][0]+=v
	sum_r[i][1]+=1
	if sum_r[i][0]==15 && sum_r[i][1]==3:
		return player
	sum_c[j][0]+=v
	sum_c[j][1]+=1
	if sum_c[j][0]==15 && sum_c[j][1]==3:
		return player
	if(i==j):
			sum_d[0][0]+=v
			sum_d[0][1]+=1
	if i+j==2:
			sum_d[1][0]+=v
			sum_d[1][1]+=1
    if (sum_d[0][0]==15 && sum_d[0][1]==3) || (sum_d[1][0]==15 && sum_d[1][1]==3) :
		return player
   
	for k in range(3):
		if sum_r[k][0]<15 || sum_c[k][0]<15:
			flag=0
			return flag
	for k in range(2):
		if(sum_d[i][0]<15):
			flag=0
			return flag
	return flag
def isvalid(p,v,player):
	if p>9 || p<1 || (player==1 && v%2==0) || (player=2 && v%2==1) || v>9 ||v<1 || (v in num) || (p in pos):
		return 0
	return 1 

def game():
	print("Player 1's chance")
	     #->>>>>>>>>>>>>>>>>>>>>>>>>>> modifgfy check
	player=1
	while(1)   : #ask user want to continue
		print("player {play}'s chance".format(play=player))
		p,v=raw_input("Enter the position and number to be entered: ").split()
		p=int(p)
		v=int(v)
		if isvalid(p,v,player):
			dic=enter(p,v,player)
			num.append(v)
			pos.append(p)
			if(dic==4):
				print("Game Draw")
				break
		    if(dic==player):
		    	print("player {play} wins".format(play))
		    	break
			if player==1:
				player=2
			else:
				player=1
		else:
			print("pos or value not valid enter again")



# print(game)
flag="1"
while flag=="1":
	sum_r=[[0,0] for i in range(3)]
	sum_c=[[0,0] for i in range(3)] 
    sum_d=[[0,0] for i in range(2)]
	num=[]
	pos=[]
	arr=[[0 for i in range(3)] for j in range(3)]
	game()
	flag=str(raw_input("enter 1 for continue enter 0 other key for exit "))
