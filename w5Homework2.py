print "Rock Scissors Paper Games!"
print "Input r, s, p only!"
def win():
    print "win"
def draw():
    print "draw"
def lose():
    print "lose"
def changeToNum(player):
	if player=="r":
		return 0
	elif player=="s":
		return 1
	elif player=="p":
		return 2
	else:
		print "Wrong Input!"
		raw_input()
		exit()

#main함수안에 replay함수가 필요함으로 에러를 방지하기 위해 미리 정의 합니다.

def replay():
	print "hello"
def main():
	player1=raw_input("player1 input:")
	changeToNum(player1)
	player2=raw_input("player2 input:")
	changeToNum(player2)
	res=changeToNum(player1)-changeToNum(player2)
	if res==0:
		draw()
	elif res==-2:
		lose()
	elif res==-1:
		win()
	elif res==1:
		lose()
	elif res==2:
		win()
	else:
		print "error!"
	print "Do you want to play again?"
	replay()

#이제 다시 replay를 정의합니다.

def replay():
	rep=raw_input("y/n: ")
	if rep=="y":
		main()
	elif rep=="n":
		exit()
	else:
		print "Wrong Input!"
		raw_input()
		exit()

main()

raw_input()