def genboard():
    T=  [13,11,12,14,15,12,11,13,
        10,10,10,10,10,10,10,10,     
         0, 0, 0, 0, 0, 0, 0, 0,  
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0,
        20,20,20,20,20,20,20,20,
        23,21,22,24,25,22,21,23,]
    return T
def printboard(T):
    G=T[:]
    for i in range(0,63):
        if (G[i]<10):
            G[i]= str(G[i]) + " "
    print G[63],"",G[62],"", G[61],"", G[60],"",G[59],"",G[58],"",G[57],"",G[56],""
    print G[55],"",G[54],"", G[53],"", G[52],"",G[51],"",G[50],"",G[49],"",G[48],""
    print G[47],"",G[46],"", G[45],"", G[44],"",G[43],"",G[42],"",G[41],"",G[40],""
    print G[39],"",G[38],"", G[37],"", G[36],"",G[35],"",G[34],"",G[33],"",G[32],""
    print G[31],"",G[30],"", G[29],"", G[28],"",G[27],"",G[26],"",G[25],"",G[24],""
    print G[23],"",G[22],"", G[21],"", G[20],"",G[19],"",G[18],"",G[17],"",G[16],""
    print G[15],"",G[14],"", G[13],"", G[12],"",G[11],"",G[10],"",G[9],"",G[8],""
    print  G[7],"", G[6],"",  G[5],"",  G[4],"", G[3],"", G[2],"", G[1],"", G[0],""
    
def getPlayerposition(T,number):
    black=[]
    white=[]
    for i in range(0,64):
        if (T[i]<26) and (T[i]>19):
            black = black + [i]
        if (T[i]<16) and (T[i]>9):
            white = white + [i]
    if (number==10):
        return white
    if (number==20):
        return black

def getPiece(name):
    if name=="pawn":
        return 0
    elif name=="knight":
        return 1
    elif name=="bishop":
        return 2
    elif name=="rook":
        return 3
    elif name=="queen":
        return 4
    elif name=="king":
        return 5
    else:
        return -1

def IsOnboard(pos):
    if (pos >= 0) and (pos <= 63):
        return True
    else:
        return False
    
        

def GetPawnMoves(T,pos):
    if (IsOnboard(pos)==False):
        return []
    if (T[pos]<>20) and (T[pos]<>10):
        return []
    accum = []
    if (T[pos]==20):
        if (pos==0) or (pos==8) or (pos==16) or (pos==24) or (pos==32) or (pos==40) or (pos==48) or (pos==56):
            col='black'
            return pawnend(T,pos,col)
        if (pos==7) or (pos==15) or (pos==23) or (pos==31) or (pos==39) or (pos==47) or (pos==55) or (pos==63):
            col = 'black'
            return pawnend(T,pos,col)
        if (IsOnboard(pos-7)==True) and (((T[pos-7]<16) and (T[pos-7]>9))):
            accum = accum + [pos-7]
        if (IsOnboard(pos-8)==True) and (T[pos-8]==0):
            accum = accum + [pos-8]
        if (IsOnboard(pos-9)==True) and (((T[pos-9]<16) and (T[pos-9]>9))):
            accum = accum + [pos-9]
    if (T[pos]==10):
        if (pos==0) or (pos==8) or (pos==16) or (pos==24) or (pos==32) or (pos==40) or (pos==48) or (pos==56):
            col='white'
            return pawnend(T,pos,col)
        if (pos==7) or (pos==15) or (pos==23) or (pos==31) or (pos==39) or (pos==47) or (pos==55) or (pos==63):
            col='white'
            return pawnend(T,pos,col)
        if (IsOnboard(pos+7)==True) and(((T[pos+7]<26) and (T[pos+7]>19))):
            accum = accum + [pos+7]
        if (IsOnboard(pos+8)==True) and (T[pos+8]==0):
            accum = accum + [pos+8]
        if (IsOnboard(pos+9)==True) and (((T[pos+9]<26) and (T[pos+9]>19))):
            accum = accum + [pos+9]
    return accum

def pawnend(T,pos,col):
    accum=[]
    if (pos==0) or (pos==8) or (pos==16) or (pos==24) or (pos==32) or (pos==40) or (pos==48) or (pos==56):
        if (col=='black'):
            if (IsOnboard(pos-7)==True) and (((T[pos-7]<16) and (T[pos-7]>9))):
                accum = accum + [pos-7]
            if (IsOnboard(pos-8)==True) and (T[pos-8]==0):
                accum = accum + [pos-8]
        if (col=='white'):
            if (IsOnboard(pos+8)==True) and (T[pos+8]==0):
                accum = accum + [pos+8]
            if (IsOnboard(pos+9)==True) and (((T[pos+9]<26) and (T[pos+9]>19))):
                accum = accum + [pos+9]
    if (pos==7) or (pos==15) or (pos==23) or (pos==31) or (pos==39) or (pos==47) or (pos==55) or (pos==63):
        if (col=='black'):
            if (IsOnboard(pos-9)==True) and (((T[pos-9]<16) and (T[pos-9]>9))):
                accum = accum + [pos-9]
            if (IsOnboard(pos-8)==True) and (T[pos-8]==0):
                accum = accum + [pos-8]
        if (col=='white'):
            if (IsOnboard(pos+8)==True) and (T[pos+8]==0):
                accum = accum + [pos+8]
            if (IsOnboard(pos+7)==True) and (((T[pos+7]<26) and (T[pos+7]>19))):
                accum = accum + [pos+7]

    return accum
            

def knightend(T,pos,col):
    accum=[]
    if (pos==0) or (pos==8) or (pos==16) or (pos==24) or (pos==32) or (pos==40) or (pos==48) or (pos==56):
        if (col=='black'):
            if (IsOnboard(pos+17)==True) and ((T[pos+17]==0) or ((T[pos+17]<16) and (T[pos+17]>9))):
                accum = accum + [pos+17]
            if (IsOnboard(pos+10)==True) and ((T[pos+10]==0) or ((T[pos+10]<16) and (T[pos+10]>9))):
                accum = accum + [pos+10]
            if (IsOnboard(pos-6)==True) and ((T[pos-6]==0) or ((T[pos-6]<16) and (T[pos-6]>9))):
                accum = accum + [pos-6]
            if (IsOnboard(pos-15)==True) and ((T[pos-15]==0) or ((T[pos-15]<16) and (T[pos-15]>9))):
                accum = accum + [pos-15]
            
        if (col=='white'):
            if (IsOnboard(pos+17)==True) and ((T[pos+17]==0) or ((T[pos+17]<26) and (T[pos+17]>19))):
                accum = accum + [pos+17]
            if (IsOnboard(pos+10)==True) and ((T[pos+10]==0) or ((T[pos+10]<26) and (T[pos+10]>19))):
                accum = accum + [pos+10]
            if (IsOnboard(pos-6)==True) and ((T[pos-6]==0) or ((T[pos-6]<26) and (T[pos-6]>19))):
                accum = accum + [pos-6]
            if (IsOnboard(pos-15)==True) and ((T[pos-15]==0) or ((T[pos-15]<26) and (T[pos-15]>19))):
                accum = accum + [pos-15]
    if (pos==0+1) or (pos==8+1) or (pos==16+1) or (pos==24+1) or (pos==32+1) or (pos==40+1) or (pos==48+1) \
            or (pos==56+1):
            if (col=='black'): 
                if (IsOnboard(pos+17)==True) and ((T[pos+17]==0) or ((T[pos+17]<16) and (T[pos+17]>9))):
                    accum = accum + [pos+17]
                if (IsOnboard(pos+10)==True) and ((T[pos+10]==0) or ((T[pos+10]<16) and (T[pos+10]>9))):
                    accum = accum + [pos+10]
                if (IsOnboard(pos-6)==True) and ((T[pos-6]==0) or ((T[pos-6]<16) and (T[pos-6]>9))):
                    accum = accum + [pos-6]
                if (IsOnboard(pos-15)==True) and ((T[pos-15]==0) or ((T[pos-15]<16) and (T[pos-15]>9))):
                    accum = accum + [pos-15]
                if (IsOnboard(pos+15)==True) and ((T[pos+15]==0) or ((T[pos+15]<16) and (T[pos+15]>9))):
                    accum = accum + [pos+15]
                if (IsOnboard(pos-17)==True) and ((T[pos-17]==0) or ((T[pos-17]<16) and (T[pos-17]>9))):
                    accum = accum + [pos-17]
                
            if (col=='white'):
                if (IsOnboard(pos+17)==True) and ((T[pos+17]==0) or ((T[pos+17]<26) and (T[pos+17]>19))):
                    accum = accum + [pos+17]
                if (IsOnboard(pos+10)==True) and ((T[pos+10]==0) or ((T[pos+10]<26) and (T[pos+10]>19))):
                    accum = accum + [pos+10]
                if (IsOnboard(pos-6)==True) and ((T[pos-6]==0) or ((T[pos-6]<26) and (T[pos-6]>19))):
                    accum = accum + [pos-6]
                if (IsOnboard(pos-15)==True) and ((T[pos-15]==0) or ((T[pos-15]<26) and (T[pos-15]>19))):
                    accum = accum + [pos-15]
                if (IsOnboard(pos+15)==True) and ((T[pos+15]==0) or ((T[pos+15]<26) and (T[pos+15]>19))):
                    accum = accum + [pos+15]
                if (IsOnboard(pos-17)==True) and ((T[pos-17]==0) or ((T[pos-17]<26) and (T[pos-17]>19))):
                    accum = accum + [pos-17]
                
           
    if (pos==7) or (pos==15) or (pos==23) or (pos==31) or (pos==39) or (pos==47) or (pos==55) or (pos==63):
        if (col=='black'):
            if (IsOnboard(pos+15)==True) and ((T[pos+15]==0) or ((T[pos+15]<16) and (T[pos+15]>9))):
                accum = accum + [pos+15]
            if (IsOnboard(pos+6)==True) and ((T[pos+6]==0) or ((T[pos+6]<16) and (T[pos+6]>9))):
                accum = accum + [pos+6]
            if (IsOnboard(pos-10)==True) and ((T[pos-10]==0) or ((T[pos-10]<16) and (T[pos-10]>9))):
                accum = accum + [pos-10]
            if (IsOnboard(pos-17)==True) and ((T[pos-17]==0) or ((T[pos-17]<16) and (T[pos-17]>9))):
                accum = accum + [pos-17]
        if (col=='white'):
            if (IsOnboard(pos+15)==True) and ((T[pos+15]==0) or ((T[pos+15]<26) and (T[pos+15]>19))):
                accum = accum + [pos+15]
            if (IsOnboard(pos+6)==True) and ((T[pos+6]==0) or ((T[pos+6]<26) and (T[pos+6]>19))):
                accum = accum + [pos+6]
            if (IsOnboard(pos-10)==True) and ((T[pos-10]==0) or ((T[pos-10]<26) and (T[pos-10]>19))):
                accum = accum + [pos-10]
            if (IsOnboard(pos-17)==True) and ((T[pos-17]==0) or ((T[pos-17]<26) and (T[pos-17]>19))):
                accum = accum + [pos-17]
    if (pos==7-1) or (pos==15-1) or (pos==23-1) or (pos==31-1) or (pos==39-1) or (pos==47-1) or (pos==55-1) \
            or (pos==63-1):
            if (col=='black'): 
                if (IsOnboard(pos+15)==True) and ((T[pos+15]==0) or ((T[pos+15]<16) and (T[pos+15]>9))):
                    accum = accum + [pos+15]
                if (IsOnboard(pos+6)==True) and ((T[pos+6]==0) or ((T[pos+6]<16) and (T[pos+6]>9))):
                    accum = accum + [pos+6]
                if (IsOnboard(pos-10)==True) and ((T[pos-10]==0) or ((T[pos-10]<16) and (T[pos-10]>9))):
                    accum = accum + [pos-10]
                if (IsOnboard(pos-17)==True) and ((T[pos-17]==0) or ((T[pos-17]<16) and (T[pos-17]>9))):
                    accum = accum + [pos-17]
                if (IsOnboard(pos+17)==True) and ((T[pos+17]==0) or ((T[pos+17]<16) and (T[pos+17]>9))):
                    accum = accum + [pos+17]
                if (IsOnboard(pos-15)==True) and ((T[pos-15]==0) or ((T[pos-15]<16) and (T[pos-15]>9))):
                    accum = accum + [pos-15]
                
            if (col=='white'):
                if (IsOnboard(pos+15)==True) and ((T[pos+15]==0) or ((T[pos+15]<26) and (T[pos+15]>19))):
                    accum = accum + [pos+15]
                if (IsOnboard(pos+6)==True) and ((T[pos+6]==0) or ((T[pos+6]<26) and (T[pos+6]>19))):
                    accum = accum + [pos+6]
                if (IsOnboard(pos-10)==True) and ((T[pos-10]==0) or ((T[pos-10]<26) and (T[pos-10]>19))):
                    accum = accum + [pos-10]
                if (IsOnboard(pos-17)==True) and ((T[pos-17]==0) or ((T[pos-17]<26) and (T[pos-17]>19))):
                    accum = accum + [pos-17]
                if (IsOnboard(pos+17)==True) and ((T[pos+17]==0) or ((T[pos+17]<26) and (T[pos+17]>19))):
                    accum = accum + [pos+17]
                if (IsOnboard(pos-15)==True) and ((T[pos-15]==0) or ((T[pos-15]<26) and (T[pos-15]>19))):
                    accum = accum + [pos-15]
            
    return accum    

def GetKnightMoves(T,pos):
    if (IsOnboard(pos)==False):
        return []
    if (T[pos]<>21) and (T[pos]<>11):
        return []
    accum = []
    if (T[pos]==21):
        if (pos==0) or (pos==8) or (pos==16) or (pos==24) or (pos==32) or (pos==40) or (pos==48) or (pos==56):
            col='black'
            return knightend(T,pos,col)
        if (pos==0+1) or (pos==8+1) or (pos==16+1) or (pos==24+1) or (pos==32+1) or (pos==40+1) or (pos==48+1) \
            or (pos==56+1):
            col='black'
            return knightend(T,pos,col)
        if (pos==7) or (pos==15) or (pos==23) or (pos==31) or (pos==39) or (pos==47) or (pos==55) or (pos==63):
            col = 'black'
            return knightend(T,pos,col)
        if (pos==7-1) or (pos==15-1) or (pos==23-1) or (pos==31-1) or (pos==39-1) or (pos==47-1) or (pos==55-1) \
            or (pos==63-1):
            col = 'black'
            return knightend(T,pos,col)
        if (IsOnboard(pos+6)==True) and ((T[pos+6]==0) or ((T[pos+6]<16) and (T[pos+6]>9))):
            accum = accum + [pos+6]
        if (IsOnboard(pos-10)==True) and ((T[pos-10]==0) or ((T[pos-10]<16) and (T[pos-10]>9))):
            accum = accum + [pos-10]
        if (IsOnboard(pos+17)==True) and ((T[pos+17]==0) or ((T[pos+17]<16) and (T[pos+17]>9))):
            accum = accum + [pos+17]
        if (IsOnboard(pos+15)==True) and ((T[pos+15]==0) or ((T[pos+15]<16) and (T[pos+15]>9))):
            accum = accum + [pos+15]
        if (IsOnboard(pos-15)==True) and ((T[pos-15]==0) or ((T[pos-15]<16) and (T[pos-15]>9))):
            accum = accum + [pos-15]
        if (IsOnboard(pos-17)==True) and ((T[pos-17]==0) or ((T[pos-17]<16) and (T[pos-17]>9))):
            accum = accum + [pos-17]
        if (IsOnboard(pos+10)==True) and ((T[pos+10]==0) or ((T[pos+10]<16) and (T[pos+10]>9))):
            accum = accum + [pos+10]
        if (IsOnboard(pos-6)==True) and ((T[pos-6]==0) or ((T[pos-6]<16) and (T[pos-6]>9))):
            accum = accum + [pos-6]
        
    if (T[pos]==11):
        if (pos==0) or (pos==8) or (pos==16) or (pos==24) or (pos==32) or (pos==40) or (pos==48) or (pos==56):
            col='white'
            return knightend(T,pos,col)
        if (pos==0+1) or (pos==8+1) or (pos==16+1) or (pos==24+1) or (pos==32+1) or (pos==40+1) or (pos==48+1) \
            or (pos==56+1):
            col='white'
            return knightend(T,pos,col)
        if (pos==7) or (pos==15) or (pos==23) or (pos==31) or (pos==39) or (pos==47) or (pos==55) or (pos==63):
            col='white'
            return knightend(T,pos,col)
        if (pos==7-1) or (pos==15-1) or (pos==23-1) or (pos==31-1) or (pos==39-1) or (pos==47-1) or (pos==55-1) \
            or (pos==63-1):
            col = 'white'
            return knightend(T,pos,col)
        if (IsOnboard(pos+6)==True) and ((T[pos+6]==0) or ((T[pos+6]<26) and (T[pos+6]>19))):
            accum = accum + [pos+6]
        if (IsOnboard(pos-10)==True) and ((T[pos-10]==0) or ((T[pos-10]<26) and (T[pos-10]>19))):
            accum = accum + [pos-10]
        if (IsOnboard(pos+17)==True) and ((T[pos+17]==0) or ((T[pos+17]<26) and (T[pos+17]>19))):
            accum = accum + [pos+17]
        if (IsOnboard(pos+15)==True) and ((T[pos+15]==0) or ((T[pos+15]<26) and (T[pos+15]>19))):
            accum = accum + [pos+15]
        if (IsOnboard(pos-15)==True) and ((T[pos-15]==0) or ((T[pos-15]<26) and (T[pos-15]>19))):
            accum = accum + [pos-15]
        if (IsOnboard(pos-17)==True) and ((T[pos-17]==0) or ((T[pos-17]<26) and (T[pos-17]>19))):
            accum = accum + [pos-17]
        if (IsOnboard(pos+10)==True) and ((T[pos+10]==0) or ((T[pos+10]<26) and (T[pos+10]>19))):
            accum = accum + [pos+10]
        if (IsOnboard(pos-6)==True) and ((T[pos-6]==0) or ((T[pos-6]<26) and (T[pos-6]>19))):
            accum = accum + [pos-6]
    return accum

def GetBishopMoves(T,pos):
    t1=1
    t2=1
    t3=1
    t4=1 
    nr = pos % 8
    nl = 7 - (pos % 8)
    accum=[]
    ul = pos
    ll = pos
    ur = pos
    lr = pos
    if (T[pos]==22) or (T[pos]==24):
        for i in range(0,nr,1):
            ur += 7
            lr -= 9
            if (IsOnboard(lr)==True) and (T[lr]==0):  
                if (t1==0):
                    accum=accum
                else: 
                    accum += [lr]
            if (IsOnboard(lr)==True) and ((T[lr]<16) and (T[lr]>9)):
                if (t1==0):
                    accum=accum
                else: 
                    accum += [lr]
                    t1=0
            if (IsOnboard(lr)==True) and (T[lr]<26) and (T[lr]>19):
                t1=0
            if (IsOnboard(ur)==True) and (T[ur]==0):
                if (t2==0):
                    accum=accum
                else: 
                    accum += [ur]
            if (IsOnboard(ur)==True) and ((T[ur]<16) and (T[ur]>9)):
                if (t2==0):
                    accum=accum
                else: 
                    accum += [ur]
                    t2=0
            if (IsOnboard(ur)==True) and ((T[ur]<26) and (T[ur]>19)):
                t2=0

        for i in range(0,nl,1):
            ul += 9
            ll -= 7
            if (IsOnboard(ul)==True) and (T[ul]==0):
                if (t3==0):
                    accum==accum
                else:
                    accum += [ul]
            if (IsOnboard(ul)==True) and ((T[ul]<16) and (T[ul]>9)):
                if (t3==0):
                    accum==accum
                else:
                    accum += [ul]
                    t3=0
            if (IsOnboard(ul)==True) and ((T[ul]<26) and (T[ul]>19)):
                t3=0
            if (IsOnboard(ll)==True) and (T[ll]==0):
                if (t4==0):
                    accum=accum
                else:
                    accum += [ll]
            if (IsOnboard(ll)==True) and ((T[ll]<16) and (T[ll]>9)):
                if (t4==0):
                    accum=accum
                else:
                    accum += [ll]
                    t4=0
            if (IsOnboard(ll)==True) and ((T[ll]<26) and (T[ll]>19)):
                t4=0
    if (T[pos]==12) or (T[pos]==14):
        for i in range(0,nr,1):
            ur += 7
            lr -= 9
            if (IsOnboard(lr)==True) and (T[lr]==0):
                if (t1==0):
                    accum=accum
                else: 
                    accum += [lr]
            if (IsOnboard(lr)==True) and ((T[lr]<26) and (T[lr]>19)):
                if (t1==0):
                    accum=accum
                else: 
                    accum += [lr]
                    t1=0
            if (IsOnboard(lr)==True) and ((T[lr]<16) and (T[lr]>9)):
                t1=0
            if (IsOnboard(ur)==True) and ((T[ur]==0)):
                if (t2==0):
                    accum=accum
                else: 
                    accum += [ur]
            if (IsOnboard(ur)==True) and ((T[ur]<26) and (T[ur]>19)):
                if (t2==0):
                    accum=accum
                else: 
                    accum += [ur]
                    t2=0
            if (IsOnboard(ur)==True) and ((T[ur]<16) and (T[ur]>9)):
                t2=0

        for i in range(0,nl,1):
            ul += 9
            ll -= 7
            if (IsOnboard(ul)==True) and ((T[ul]==0)):
                if (t3==0):
                    accum==accum
                else:
                    accum += [ul]
            if (IsOnboard(ul)==True) and (IsOnboard(ul)==True) and ((T[ul]<26) and (T[ul]>19)):
                if (t3==0):
                    accum==accum
                else:
                    accum += [ul]
                    t3=0
            if (IsOnboard(ul)==True) and ((T[ul]<16) and (T[ul]>9)):
                t3=0
            if (IsOnboard(ll)==True) and ((T[ll]==0)):
                if (t4==0):
                    accum=accum
                else:
                    accum += [ll]
            if (IsOnboard(ll)==True) and ((T[ll]<26) and (T[ll]>19)):
                if (t4==0):
                    accum=accum
                else:
                    accum += [ll]
                    t4=0
            if (IsOnboard(ll)==True) and ((T[ll]<16) and (T[ll]>9)):
                t4=0
    return accum

def GetRookMoves(T,pos):
    nl = pos % 8
    nr = 7 - (pos % 8)
    nd = pos / 8
    nu = 7 - (pos / 8)
    t1=1
    t2=1
    t3=1
    t4=1
    accum=[]
    l=r=u=d=pos
    if (T[pos]==23) or (T[pos]==24):
        for i in range(0,nl,1):
            l -= 1
            if (IsOnboard(l)==True) and (T[l]==0):
                if (t1==0):
                    accum = accum
                else:
                    accum += [l]
            if (IsOnboard(l)==True) and ((T[l]<16) and (T[l]>9)):
                if (t1==0):
                    accum = accum
                else:
                    t1=0                     
                    accum += [l]
            if (IsOnboard(l)==True) and ((T[l]<26) and (T[l]>19)):
                t1 = 0

        for i in range(0,nr,1):
            r += 1
            if (IsOnboard(r)==True) and (T[r]==0):
                if (t2==0):
                    accum = accum
                else:
                    accum += [r]
            if (IsOnboard(r)==True) and ((T[r]<16) and (T[r]>9)):
                if (t2==0):
                    accum = accum
                else:
                    t2=0                     
                    accum += [r]
            if (IsOnboard(r)==True) and ((T[r]<26) and (T[r]>19)):
                t2 = 0


        for i in range(0,nd,1):
            d -= 8
            if (IsOnboard(d)==True) and (T[d]==0):
                if (t3==0):
                    accum = accum
                else:
                    accum += [d]
            if (IsOnboard(d)==True) and ((T[d]<16) and (T[d]>9)):
                if (t3==0):
                    accum = accum
                else:
                    t3=0                     
                    accum += [d]
            if (IsOnboard(d)==True) and ((T[d]<26) and (T[d]>19)):
                t3 = 0


        for i in range(0,nu,1):
            u += 8
            if (IsOnboard(u)==True) and (T[u]==0):
                if (t4==0):
                    accum = accum
                else:
                    accum += [u]
            if (IsOnboard(u)==True) and ((T[u]<16) and (T[u]>9)):
                if (t4==0):
                    accum = accum
                else:
                    t4=0                     
                    accum += [u]
            if (IsOnboard(u)==True) and ((T[u]<26) and (T[u]>19)):
                t4 = 0
    
    
    if (T[pos]==13) or (T[pos]==14):
        for i in range(0,nl,1):
            l -= 1
            if (IsOnboard(l)==True) and (T[l]==0):
                if (t1==0):
                    accum = accum
                else:
                    accum += [l]
            if (IsOnboard(l)==True) and ((T[l]<26) and (T[l]>19)):
                if (t1==0):
                    accum = accum
                else:
                    t1=0                     
                    accum += [l]
            if (IsOnboard(l)==True) and ((T[l]<16) and (T[l]>9)):
                t1 = 0
 
        for i in range(0,nr,1):
            r += 1
            if (IsOnboard(r)==True) and (T[r]==0):
                if (t2==0):
                    accum = accum
                else:
                    accum += [r]
            if (IsOnboard(r)==True) and ((T[r]<26) and (T[r]>19)):
                if (t2==0):
                    accum = accum
                else:
                    t2=0                     
                    accum += [r]
            if (IsOnboard(r)==True) and ((T[r]<16) and (T[r]>9)):
                t2 = 0


        for i in range(0,nd,1):
            d -= 8
            if (IsOnboard(d)==True) and (T[d]==0):
                if (t3==0):
                    accum = accum
                else:
                    accum += [d]
            if (IsOnboard(d)==True) and ((T[d]<26) and (T[d]>19)):
                if (t3==0):
                    accum = accum
                else:
                    t3=0                     
                    accum += [d]
            if (IsOnboard(d)==True) and ((T[d]<16) and (T[d]>9)):
                t3 = 0


        for i in range(0,nu,1):
            u += 8
            if (IsOnboard(u)==True) and (T[u]==0):
                if (t4==0):
                    accum = accum
                else:
                    accum += [u]
            if (IsOnboard(u)==True) and ((T[u]<26) and (T[u]>19)):
                if (t4==0):
                    accum = accum
                else:
                    t4=0                     
                    accum += [u]
            if (IsOnboard(u)==True) and ((T[u]<16) and (T[u]>9)):
                t4 = 0

    return accum

def GetQueenMoves(T,pos):
    return GetRookMoves(T,pos) + GetBishopMoves(T,pos)

def GetKingMoves(T,pos):
    accum=[]
    if (T[pos]==25):
        if (pos==0) or (pos==8) or (pos==16) or (pos==24) or (pos==32) or (pos==40) or (pos==48) or (pos==56):
            col='black'
            return kingend(T,pos,col)
        if (pos==7) or (pos==15) or (pos==23) or (pos==31) or (pos==39) or (pos==47) or (pos==55) or (pos==63):
            col = 'black'
            return kingend(T,pos,col)
        if (IsOnboard(pos-1)==True) and ((T[pos-1]==0) or ((T[pos-1]<16) and (T[pos-1]>9))):
            accum = accum + [pos-1]
        if (IsOnboard(pos+1)==True) and ((T[pos+1]==0) or ((T[pos+1]<16) and (T[pos+1]>9))):
            accum = accum + [pos+1]
        if (IsOnboard(pos-7)==True) and ((T[pos-7]==0) or ((T[pos-7]<16) and (T[pos-7]>9))):
            accum = accum + [pos-7]
        if (IsOnboard(pos-8)==True) and ((T[pos-8]==0) or ((T[pos-8]<16) and (T[pos-8]>9))):
            accum = accum + [pos-8]
        if (IsOnboard(pos-9)==True) and ((T[pos-9]==0) or ((T[pos-9]<16) and (T[pos-9]>9))):
            accum = accum + [pos-9]
        if (IsOnboard(pos+7)==True) and ((T[pos+7]==0) or ((T[pos+7]<16) and (T[pos+7]>9))) :
            accum = accum + [pos+7]
        if (IsOnboard(pos+8)==True) and ((T[pos+8]==0) or ((T[pos+8]<16) and (T[pos+8]>9))):
            accum = accum + [pos+8]
        if (IsOnboard(pos+9)==True) and ((T[pos+9]==0) or ((T[pos+9]<16) and (T[pos+9]>9))):
            accum = accum + [pos+9]
    if (T[pos]==15):
        if (pos==0) or (pos==8) or (pos==16) or (pos==24) or (pos==32) or (pos==40) or (pos==48) or (pos==56):
            col='white'
            return kingend(T,pos,col)
        if (pos==7) or (pos==15) or (pos==23) or (pos==31) or (pos==39) or (pos==47) or (pos==55) or (pos==63):
            col='white'
            return kingend(T,pos,col)
        if (IsOnboard(pos-1)==True) and ((T[pos-1]==0) or ((T[pos-1]<26) and (T[pos-1]>19))):
            accum = accum + [pos-1]
        if (IsOnboard(pos+1)==True) and ((T[pos+1]==0) or ((T[pos+1]<26) and (T[pos+1]>19))):
            accum = accum + [pos+1]
        if (IsOnboard(pos-7)==True) and ((T[pos-7]==0) or ((T[pos-7]<26) and (T[pos-7]>19))):
            accum = accum + [pos-7]
        if (IsOnboard(pos-8)==True) and ((T[pos-8]==0) or ((T[pos-8]<26) and (T[pos-8]>19))):
            accum = accum + [pos-8]
        if (IsOnboard(pos-9)==True) and ((T[pos-9]==0) or ((T[pos-9]<26) and (T[pos-9]>19))):
            accum = accum + [pos-9]
        if (IsOnboard(pos+7)==True) and ((T[pos+7]==0) or ((T[pos+7]<26) and (T[pos+7]>19))):
            accum = accum + [pos+7]
        if (IsOnboard(pos+8)==True) and ((T[pos+8]==0) or ((T[pos+8]<26) and (T[pos+8]>19))):
            accum = accum + [pos+8]
        if (IsOnboard(pos+9)==True) and ((T[pos+9]==0) or ((T[pos+9]<26) and (T[pos+9]>19))):
            accum = accum + [pos+9]
    else:
        accum=accum + []
        
    return accum

def kingend(T,pos,col):
    accum=[]
    if (pos==0) or (pos==8) or (pos==16) or (pos==24) or (pos==32) or (pos==40) or (pos==48) or (pos==56):
        if (col=='black'):
            if (IsOnboard(pos+1)==True) and ((T[pos+1]==0) or ((T[pos+1]<16) and (T[pos+1]>9))):
                accum = accum + [pos+1]
            if (IsOnboard(pos-7)==True) and ((T[pos-7]==0) or ((T[pos-7]<16) and (T[pos-7]>9))):
                accum = accum + [pos-7]
            if (IsOnboard(pos-8)==True) and ((T[pos-8]==0) or ((T[pos-8]<16) and (T[pos-8]>9))):
                accum = accum + [pos-8]
            if (IsOnboard(pos+8)==True) and ((T[pos+8]==0) or ((T[pos+8]<16) and (T[pos+8]>9))):
                accum = accum + [pos+8]
            if (IsOnboard(pos+9)==True) and ((T[pos+9]==0) or ((T[pos+9]<16) and (T[pos+9]>9))):
                accum = accum + [pos+9]
        if (col=='white'):
            if (IsOnboard(pos+1)==True) and ((T[pos+1]==0) or ((T[pos+1]<26) and (T[pos+1]>19))):
                accum = accum + [pos+1]
            if (IsOnboard(pos-7)==True) and ((T[pos-7]==0) or ((T[pos-7]<26) and (T[pos-7]>19))):
                accum = accum + [pos-7]
            if (IsOnboard(pos-8)==True) and ((T[pos-8]==0) or ((T[pos-8]<26) and (T[pos-8]>19))):
                accum = accum + [pos-8]
            if (IsOnboard(pos+8)==True) and ((T[pos+8]==0) or ((T[pos+8]<26) and (T[pos+8]>19))):
                accum = accum + [pos+8]
            if (IsOnboard(pos+9)==True) and ((T[pos+9]==0) or ((T[pos+9]<26) and (T[pos+9]>19))):
                accum = accum + [pos+9]
    if (pos==7) or (pos==15) or (pos==23) or (pos==31) or (pos==39) or (pos==47) or (pos==55) or (pos==63):
        if (col=='black'):
            if (IsOnboard(pos-1)==True) and ((T[pos-1]==0) or ((T[pos-1]<16) and (T[pos-1]>9))):
                accum = accum + [pos-1]
            if (IsOnboard(pos-8)==True) and ((T[pos-8]==0) or ((T[pos-8]<16) and (T[pos-8]>9))):
                accum = accum + [pos-8]
            if (IsOnboard(pos-9)==True) and ((T[pos-9]==0) or ((T[pos-9]<16) and (T[pos-9]>9))):
                accum = accum + [pos-9]
            if (IsOnboard(pos+7)==True) and ((T[pos+7]==0) or ((T[pos+7]<16) and (T[pos+7]>9))):
                accum = accum + [pos+7]
            if (IsOnboard(pos+8)==True) and ((T[pos+8]==0) or ((T[pos+8]<16) and (T[pos+8]>9))):
                accum = accum + [pos+8]
        if (col=='white'):
            if (IsOnboard(pos-1)==True) and ((T[pos-1]==0) or ((T[pos-1]<26) and (T[pos-1]>19))):
                accum = accum + [pos-1]
            if (IsOnboard(pos-8)==True) and ((T[pos-8]==0) or ((T[pos-8]<26) and (T[pos-8]>19))):
                accum = accum + [pos-8]
            if (IsOnboard(pos-9)==True) and ((T[pos-9]==0) or ((T[pos-9]<26) and (T[pos-9]>19))):
                accum = accum + [pos-9]
            if (IsOnboard(pos+7)==True) and ((T[pos+7]==0) or ((T[pos+7]<26) and (T[pos+7]>19))):
                accum = accum + [pos+7]
            if (IsOnboard(pos+8)==True) and ((T[pos+8]==0) or ((T[pos+8]<26) and (T[pos+8]>19))):
                accum = accum + [pos+8]
    return accum

def GetPieceLegalMoves(T,pos):
    if (T[pos]==10) or (T[pos]==20):
        return GetPawnMoves(T,pos)
    if (T[pos]==11) or (T[pos]==21):
        return GetKnightMoves(T,pos)
    if (T[pos]==12) or (T[pos]==22):
        return GetBishopMoves(T,pos)
    if (T[pos]==13) or (T[pos]==23):
        return GetRookMoves(T,pos)
    if (T[pos]==14) or (T[pos]==24):
        return GetQueenMoves(T,pos)
    if (T[pos]==15) or (T[pos]==25):
        return GetKingMoves(T,pos)

def IsPositionUnderThreat(T,pos,player):
    if (player==10):
        for i in range(0,64):
            if IsOnboard(i) and (i<>pos) and ((T[i]<26) and (T[i]>19)):
                temp=GetPieceLegalMoves(T,i)
                for j in range(0,len(temp)):
                    if (temp[j]==pos):
                        return True
    
    if (player==20):
        for i in range(0,64):
            if IsOnboard(i) and (i<>pos) and ((T[i]<16) and (T[i]>9)):
                temp=GetPieceLegalMoves(T,i)
                for j in range(0,len(temp)):
                    if (temp[j]==pos):
                        return True
    
    
    return False
               
class tree:
    def __init__(self,x):
        self.store = [x,[]]

    def addsuccessor(self,x):
        self.store[1] = self.store[1] + [x]
        return True

    def levelorder(self):
        R = [self.store[0]]
        A = self.store[1]
        #print(A)
        while A != []:
            B = list(A)
            A = []
            for i in range(0, len(B)):
                R = R + [B[i].store[0]]
                A = A + B[i].store[1]
        return R
    
    def depth(self):
        space = '   '
        space_count = 1
        A = []
        print(self.store[0])
        s = self.store[1] + [space_count]
        A = A + [s]
        l = 0
        while A != []:
            y = A[len(A)-1][0]
            space_count = A[len(A)-1][len(A[len(A)-1])-1]
            A[len(A)-1] = A[len(A)-1][1:(len(A[len(A)-1]))]
            if (len(A[len(A)-1]) == 1):
                A = A[0:(len(A)-1)]
            while(y.store[1] != []):
                print(space*space_count + str(y.store[0]))
                space_count = space_count + 1
                if type(y.store[1][len(y.store[1])-1]) == int:
                    y.store[1][len(y.store[1])-1] = space_count
                else:
                    n = y.store[1] + [space_count]
                A = A + [n[1:len(n)]]
                y = y.store[1][0]
                if (len(A[len(A)-1]) == 1):
                    A = A[0:(len(A)-1)]
            #print(A)
            l = l+1
            if (y.store[1] == []):
                print(space*space_count + str(y.store[0])) 
