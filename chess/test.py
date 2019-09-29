from chessPlayer import *
from chessPlayer_helper import *

def printb():
    T=(range(64))
    for i in range(0,63):
            if (T[i]<10):
                T[i]= str(T[i]) + " "
    print T[63],"",T[62],"", T[61],"", T[60],"",T[59],"",T[58],"",T[57],"",T[56],""
    print T[55],"",T[54],"", T[53],"", T[52],"",T[51],"",T[50],"",T[49],"",T[48],""
    print T[47],"",T[46],"", T[45],"", T[44],"",T[43],"",T[42],"",T[41],"",T[40],""
    print T[39],"",T[38],"", T[37],"", T[36],"",T[35],"",T[34],"",T[33],"",T[32],""
    print T[31],"",T[30],"", T[29],"", T[28],"",T[27],"",T[26],"",T[25],"",T[24],""
    print T[23],"",T[22],"", T[21],"", T[20],"",T[19],"",T[18],"",T[17],"",T[16],""
    print T[15],"",T[14],"", T[13],"", T[12],"",T[11],"",T[10],"",T[9],"",T[8],""
    print T[7],"", T[6],"",  T[5],"",  T[4],"", T[3],"", T[2],"", T[1],"", T[0],""

    return 0

t=genboard()
count=10
while True:
        print""
        printboard(t)
        print ''
        printb()
        print ''
        u=getPlayerposition(t,20)
        print u
        userspot = int(raw_input("Enter a desired spot: "))
        a=GetPieceLegalMoves(t,userspot)
        print a
        userMove = int(raw_input("Enter the move you want to make: "))
        t[userMove]=t[userspot]
        t[userspot]=0
        print''
        printboard(t)
        print ''
        printboard(t)
        a=chessPlayer(t,10)
        t[a[1][1]] = t[a[1][0]]
        t[a[1][0]]=0
        count=count-1
        
