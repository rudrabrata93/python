def display_board(board):
    for k in range(0,1):
        print("\n ******* \n")
    for i in range(3,10,3):
        print("|\t \t|\t \t|\t \t|")
        print(f"|\t{board[-i]}\t|\t{board[-i+1]}\t|\t{board[-i+2]}\t|")
        print("--------------------------------------------------")
def check(a):
    if(a[0]==a[8]==a[4]!="") or (a[2]==a[6]==a[4]!=""):
        return False
    else:
        for i in range(0,3):
            if (a[i]==a[i+3]==a[i+6]!=''):
                return False
            elif (a[3*i]==a[3*i+1]==a[3*i+2]!=''):
                return False
    return True
display=["","","","","","","","",""]
pos=0
p=[""]
winner=True
p[0]=input("PLayer 1 select X or O: ")
if (p[0]=='x'):
    p.append("o")
else:
    p.append("x")
for i in range(1,11):
    if winner and i<10:
        if i%2==0:
            pos=int(input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n Player 2 enter your location:\t"))
            display[pos-1]=p[1]
        else:
            pos=int(input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n Player 1 enter your location:\t"))
            display[pos-1]=p[0]
        display_board(display)
        winner=check(display)
    elif i<10:
        if i%2==0:
            print("\n\n\n\n\n\n\n\n\n\n\n Player 1 is Winner!\n")
            break
        else:
            print("\n\n\n\n\n\n\n\n\n\n\n Player 2 is Winner!\n")
            break
if winner:
    print ("Match Tied!!")