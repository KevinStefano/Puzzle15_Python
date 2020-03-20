#Name   : Kevin Austin Stefano
#NIM    : 13518104

import collections 

class Matrix(object) :
    def __init__ (self):
        self = [[0 for x in range(4)] for y in range(4)]

    def __getitem__(self,indeksi, indeksj):
        return self[indeksi][indeksj]

    def __setitem__(self,indeksi, indeksj, data):
        self[indeksi][indeksj] = data


def printMatriks (matriks):
    print("Bentuk Puzzlenya adalah : ")
    print("+----+----+----+----+")
    for i in range(4):
        print("",end='| ')
        for j in range(4):
            if matriks[i][j]<10 and matriks[i][j]>0:
                print(matriks[i][j],end='  | ')
            elif matriks[i][j]==0:
                print(" ",end='  | ')
            else:
                 print(matriks[i][j],end=' | ')
        
        print()
        print("+----+----+----+----+")
            
def checkReachableGoal (matriks):
    #cari index yang kosong
    for i in range(4):
        for j in range(4):
            if matriks[i][j]==0:
                break
        if matriks[i][j]==0:
                break

    #Cari nilai X
    if ((i==0 or i==2) and (j==1 or j==3)) or ((i==1 or i==3) and (j==0 or j==2)):
        x = 1
    else:
        x = 0

    
    #cari nilai fungsi KURANG(i)
    kurang = 0
    #itterasi tiap element matriks
    for k in range(4):
        for l in range(4):
            #check tiap element matriks
            if l==3 and k<3:
                m= k+1  #baris
                n= 0    #kolom
                stop=0
            elif l==3 and k==3:
                stop =1
            else:
                m = k
                n = l+1
                stop=0
            while (m<4 and stop==0):
                while (n<4):
                    if (matriks[m][n]<matriks[k][l] and matriks[m][n]!=0) or matriks[k][l]==0:
                        kurang=kurang+1
                    n=n+1
                n=0
                m=m+1
    #hitung total
    kurang = kurang+x
    #check apakah genap atau bukan
    if kurang%2==0:
        return 1 #bisa
    else:
        return 0 #tidakbisa
            
            
def checkDenganSusunanAkhir(matriks):
    count = 0
    check = 1
    for i in range(4):
        for j in range(4):
            if matriks[i][j]!=0 and matriks[i][j] != check:
                count=count+1
            check = (check+1)%16
    return count
    

def whereKotakKosong(matriks):
    for i in range(4):
        for j in range(4):
            if matriks[i][j]==0:
                break;
        if matriks[i][j]==0:
            break;
    return i,j

def AddQueue(queue, idxi, idxj, cost):
    if queue:
        i,j,c = queue[0]
        if c>=cost:
            queue.appendleft((idxi,idxj,cost))
        else:
            queue.append((idxi,idxj,cost))
    else:
        queue.append((idxi,idxj,cost))

def swipeAndCheck(matriks, queue, kosongI, kosongJ, swipeI, swipeJ,langkah,savedArray):
    cost = 0
    
    if (swipeI==kosongI-1 and swipeJ==kosongJ) or (swipeI==kosongI+1 and swipeJ==kosongJ) or (swipeJ==kosongJ+1 and swipeI==kosongI) or (swipeJ==kosongJ-1 and swipeI==kosongI):
        matriks[kosongI][kosongJ] =matriks[swipeI][swipeJ]
        matriks[swipeI][swipeJ]=0
        cost = checkDenganSusunanAkhir(matriks)+langkah
        AddQueue(queue,swipeI,swipeJ,cost)
        savedArray.append(matriks)
        matriks[swipeI][swipeJ]=matriks[kosongI][kosongJ]
        matriks[kosongI][kosongJ] = 0
    
def checkUDLRandAddQueue(matriks, queue, langkah, savedArray):
    i,j=whereKotakKosong(matriks)
    kosongI,kosongJ,cost= queue[0]
    temp =matriks[kosongI][kosongJ]
    matriks[kosongI][kosongJ]=0
    matriks[i][j] = temp
    #printMatriks(matriks)
    
    #print(queue)
    if 1+1==2:
    #matriks in savedArray:
     #   queue.popleft()
     #   return 0
    #else:
        count =checkDenganSusunanAkhir(matriks)
        if count==0:
            return 1
        else:
            #print(queue)
            queue.popleft()

            #checkjika UP
            if (kosongI-1>=0):
                swipeAndCheck(matriks,queue,kosongI,kosongJ,kosongI-1,kosongJ,langkah,savedArray)
            
            #checkjika DOWN
            if (kosongI+1<=3):
                swipeAndCheck(matriks,queue,kosongI,kosongJ,kosongI+1,kosongJ,langkah,savedArray)
                
            #checkjika LEFT
            if (kosongJ-1>=0):
                swipeAndCheck(matriks,queue,kosongI,kosongJ,kosongI,kosongJ-1,langkah,savedArray)
           
            
            #checkjika RIGHT
            if (kosongJ+1<=3):
                swipeAndCheck(matriks,queue,kosongI,kosongJ,kosongI,kosongJ+1,langkah,savedArray)
            return 0   
    
#MAIN
#Masukan file eksternal
with open('datainput.txt', 'r') as f:
    matriks = [[int(idx) for idx in line.split(' ')] for line in f]
    if len(matriks)!= 4 or len(matriks[0])  != 4:
        print("Masukan file matriks harus berukuran 4x4");
    else:

        if (checkReachableGoal(matriks)==0):
            print("Matriks tidak bisa di proses")
        else:
            
            i=1
            baris,kolom = whereKotakKosong(matriks)
            queue = collections.deque([(baris,kolom,0)])
            
            savedArray = matriks
            while(queue):
                if (checkUDLRandAddQueue(matriks,queue,i,savedArray)==1):
                    break
                i=i+1

         

            
            
     
            
    


