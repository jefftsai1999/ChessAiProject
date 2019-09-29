from chessPlayer_helper import *

def chessPlayer(t,player):
    candid=[]
    if (player==10):
        whiteplayerpos=[]
        d=getPlayerposition(t,10)
        minValue = 9000
        minMove = None
        for i in d:
            z=GetPieceLegalMoves(t,i)
            for j in z:
                whiteplayerpos=whiteplayerpos + [[i,j,t[i]]]

            temp=whiteplayerpos
            for k in temp:
                temp2=list(t)
                temp2[k[1]] = k[2]
                temp2[k[0]]=0
                (value,x) =  minimax(temp2, 2, False)
                c=[x.levelorder()]
                if value < minValue:
                    prevalue=minValue
                    minValue = value
                    minMove = k[1]
                    piece=k[2]
                    initial=k[0]
                    candid=candid +[[initial,minMove],float((minValue-100)/-1000)]
                if (value < prevalue) and (value>minValue):
                    preval=value
                    value1=value
                    move1=k[1]
                    initial1=k[0]
                    candid=candid +[[initial1,move1],float((value1-100)/-1000)]
                
                if (value < prevalue) and (value>minValue):
                    prevalue=value
                    value2=value
                    move2=k[1]
                    initial2=k[0]
                    candid=candid +[[initial2,move2],float((value2-100)/-1000)]
                
                if (value < prevalue) and (value>minValue):
                    prevalue=value
                    value3=value
                    move3=k[1]
                    initial3=k[0]
                    candid=candid +[[initial2,move2],float((value2-100)/-1000)]

        return [True,[initial,minMove],candid,c]
    
    else:
        if (player==20):
            blackplayerpos=[]
            d=getPlayerposition(t,20)
            maxValue = -9000
            maxMove = None
            for i in d:
                z=GetPieceLegalMoves(t,i)
                for j in z:
                    blackplayerpos=blackplayerpos + [[i,j,t[i]]]

                temp=blackplayerpos
                for k in temp:
                    temp2=list(t)
                    temp2[k[1]] = k[2]
                    temp2[k[0]]=0
                    (value,x) =  minimax(temp2, 2, True)
                    c=[x.levelorder()]
                    if value > maxValue:
                        prevalue=maxValue
                        maxValue = value
                        maxMove = k[1]
                        piece=k[2]
                        initial=k[0]
                        candid=candid +[[initial,maxMove],float((maxValue+100)/1000)]
                    if (value > prevalue) and (value<maxValue):
                        preval=value
                        value1=value
                        move1=k[1]
                        initial1=k[0]
                        candid=candid + [[initial1,move1],float(value1+100)/1000]

                    if (value > prevalue) and (value<maxValue):
                        prevalue=value
                        value2=value
                        move2=k[1]
                        initial2=k[0]
                        candid=candid + [[initial2,move2],float(value2+100)/1000]
                    if (value > prevalue) and (value<maxValue):
                        prevalue=value
                        value3=value
                        move3=k[1]
                        initial3=k[0]
                        candid=candid + [[initial2,move3],float(value2+100)/1000]

            return [True,[initial,maxMove],candid,c]

        



def minimax(t, depth, maximizingplayer):
    #maximizingplayeris black
    if (depth == 0):
        a=len(getPlayerposition(t,20))-len(getPlayerposition(t,10))
        x=tree(a)
        return [a,x]
    
    maxplayerpos=[]
    whiteplayerpos=[]
    
    c=getPlayerposition(t,20)
    for i in c:
        a=GetPieceLegalMoves(t,i)
        for j in range(0,len(a)):
            maxplayerpos=maxplayerpos + [[i,a[j],t[i]]]
    
    d=getPlayerposition(t,10)
    for i in d:
        a=GetPieceLegalMoves(t,i)
        for j in range(0,len(a)):
            whiteplayerpos=whiteplayerpos + [[i,a[j],t[i]]]
            
    if (maximizingplayer==True):
        bestval = -9000
        x=tree(bestval)
        temp=list(maxplayerpos)
        for i in temp:
            temp2=list(t)
            temp2[i[1]] = i[2]
            temp2[i[0]]=0
            (val,p) = minimax(temp2, depth-1,False)
            x.addsuccessor(p)
            if val > bestval: # white maximizes her score
                bestval = val
        
        x.store[0]=bestval
        
        return (bestval,x)
    
    else:
        bestval = 9000
        x=tree(bestval)
        temp= list(whiteplayerpos)
        for i in temp:
            temp2=list(t)
            temp2[i[1]] = i[2]
            temp2[i[0]]=0
            (val,p) = minimax(temp2, depth - 1,True)
            x.addsuccessor(p)
            if val < bestval: # white maximizes her score
                bestval = val
        
        x.store[0]=bestval
        
        return (bestval,x)
