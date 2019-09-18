#print welcome message
print("Welcome to the Game!")
#this function enters the value at position and return 4 ig game is draw returnn 1 if player 1 wins or 2 if player 2 wins and 0 for continue game
def enter(p,v,player):
	flag=4 #inintiallize a flag to check the draw
	i=(p-1)/3 #array indicis using position
	j=(p-1)%3 #array indicis using position
	arr[i][j]=v #assign value
	# sum_r[i][player]+=
	sum_r[i][0]+=v #add value to row
	sum_r[i][1]+=1 #increase count of row
	if (sum_r[i][0]==15 and sum_r[i][1]==3): #if sum of row is 15 return ooutcome
		return player
	sum_c[j][0]+=v   #add value to col
	sum_c[j][1]+=1  #increase count of col
	if sum_c[j][0]==15 and sum_c[j][1]==3:  #if sum of row is 15 return ooutcome
		return player
	if(i==j): 
			sum_d[0][0]+=v #add value to diagional
			sum_d[0][1]+=1 #increase count of diagional
	if i+j==2:
			sum_d[1][0]+=v #add value to diagional
			sum_d[1][1]+=1 #increase count of diagional
	if (sum_d[0][0]==15 and sum_d[0][1]==3) or (sum_d[1][0]==15 and sum_d[1][1]==3) : #check diagonal for 15 sum and eturn outcome 
		return player
	var=0
	for i in range(3): #checks if all cells filled than draw 
		var+=sum_r[i][1]  
	if(var==9):  #draw the match
		return flag
	for k in range(3): #this loop check if possibility of any body win
		if sum_r[k][0]<15 or sum_c[k][0]<15:
			flag=0
			return flag
	for k in range(2): #this loop check if possibility of any body win
		if(sum_d[i][0]<15):
			flag=0
			return flag
	return flag #return draw
def isvalid(p,v,player): #check validity of user entered input
	if p>9 or p<1 or (player==1 and v%2==0) or (player==2 and v%2==1) or v>9 or v<1 or (v in num) or (p in pos):
		return 0
	return 1 
#handles the input and game flow
def game():
	print("Player 1's chance") 
	player=1
	while(1)   : #ask user want to continue
		print("player {play}'s chance".format(play=player)) #print which players chance
		p,v=raw_input("Enter the position and number to be entered: ").split() #take input
		if(not(p.isdigit() and v.isdigit())): #check if entered digit else give error
			print("pos or value not valid enter again")
			continue
		p=int(p)
		v=int(v) 
		if isvalid(p,v,player): #check validity
			dic=enter(p,v,player) #enter value in array cell
			for i in arr:  #prints the array
				for j in i:
					print("{v} |".format(v=j)),
				print("\n")
			num.append(v) #track numbered enterd
			pos.append(p) #track position
			if(dic==4): #print draw
				print("Game Draw")
				break
			if(dic==player): #print if player wins
				print("player {play} wins".format(play=player))
				break
			if player==1: #chnage the player in every loop
				player=2
			else:
				player=1
		else:
			print("pos or value not valid enter again") #if not valid [positoin enter again]

#-----------------------------------------------------
flag="1" #to check whether user wants to continue
while flag=="1": #loop till flag 1
	sum_r=[[0,0] for i in range(3)] #stores rows sum and elememnt count 
	sum_c=[[0,0] for i in range(3)] #stores column sum and elememnt count 
	sum_d=[[0,0] for i in range(2)]#stores diagonal sum and elememnt count 
	num=[] #contains number enytered
	pos=[] #contains posiotion entered
	arr=[[0 for i in range(3)] for j in range(3)] #game array
	game() #call game
	flag=str(raw_input("enter 1 for continue enter 0 other key for exit ")) #ask if user wants to continue
