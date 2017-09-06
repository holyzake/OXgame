import pickle

def Menu():
    x=1
    while x==1:
        print("      O/X  Game")
        print("        Start")
        print("        Score")
        print("        Exit")
        done=False
        while done==False:
            command=(raw_input("Select one of these:"))
            if command == 'start':
                start()
                done=True
            elif command == 'score':
                CheckScore()
                done=True
            elif command == 'exit':
                x=2
                done=True
            else:
                print "The command is unknown"

def start():
    global position,x,NumberList,m,n,ChosenNum
    NumberList=[[1,2,3],[4,5,6],[7,8,9]]
    n=m=int(1)
    ChosenNum=[]
    ShowCurrentTable()
    while (m<10):
        CheckOX()
        Input()         #And Check if Num
        CheckInputNum()
        ShowCurrentTable()
        CheckWin()
        m=m+1

    if m==10:
        print("Draw")
    else:
        AddScore()
        print(letter+" Win")

def CheckOX():
    global letter,n
    if n%2==1:
        n=n-1
        letter="X"
    else:
        n=n+1
        letter="O"

def ShowCurrentTable():
    global NumberList
    print NumberList[0][0] ,"|", NumberList[0][1] ,"|", NumberList[0][2]
    print("---------")
    print NumberList[1][0],"|",NumberList[1][1],"|",NumberList[1][2]
    print("---------")
    print NumberList[2][0],"|",NumberList[2][1],"|",NumberList[2][2]
    return

def CheckInputNum():
    global position,NumberList,ChosenNum
    if position not in ChosenNum:
        ChosenNum.insert(0,position)
        if 1<=position<=9:
            PostingOX()
        else:
            InvalidPosition()
    else:
        InvalidPosition()

def PostingOX():
    global position, letter, NumberList
    for x in range (0,3):
        for y in range (0,3):
            if NumberList[x][y]==position:
                NumberList[x][y]=letter
                break

def Input():
    global position
    while True:
        try:
            position = int(raw_input("You are "+letter+" select your position from 1-9: "))
            break
        except ValueError:
            print ("Please Enter a number")

def InvalidPosition():
    global m,n
    m=m-1
    print("your position is invalid")
    if n%2==1:
        n=n+1
    else:
        n=n-1

def CheckWin():
    global NumberList,m,letter
    if NumberList[0][0]==NumberList[0][1]==NumberList[0][2]==letter:
        m=10
    elif NumberList[1][0]==NumberList[1][1]==NumberList[1][2]==letter:
        m=10
    elif NumberList[2][0]==NumberList[2][1]==NumberList[2][2]==letter:
        m=10
    elif NumberList[0][0]==NumberList[1][0]==NumberList[2][0]==letter:
        m=10
    elif NumberList[0][1]==NumberList[1][1]==NumberList[2][1]==letter:
        m=10
    elif NumberList[0][2]==NumberList[1][2]==NumberList[2][2]==letter:
        m=10
    elif NumberList[0][0]==NumberList[1][1]==NumberList[2][2]==letter:
        m=10
    elif NumberList[2][0]==NumberList[1][1]==NumberList[0][2]==letter:
        m=10

def CheckScore():

    score=0
    try:
        with open('scoreO.txt','rb') as file:
            score = pickle.load(file)
    except:
        score = 0
    print  "    O score is",+score
    try:
        with open('scoreX.txt','rb') as file:
            score = pickle.load(file)
    except:
        score = 0
    print  "    X score is",+score
def AddScore():

    if n%2==1:
        with open('scoreO.txt','rb') as file:
            score = pickle.load(file)+1
        with open('scoreO.txt','wb') as file:
            pickle.dump(score,file)
        #letter="O"
    else:
        with open('scoreX.txt','rb') as file:
            score = pickle.load(file)+1
        with open('scoreX.txt','wb') as file:
            pickle.dump(score,file)
        #letter="X"

Menu()
