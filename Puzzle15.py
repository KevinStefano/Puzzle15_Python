#Name   : Kevin Austin Stefano
#NIM    : 13518104

import collections
import time

def printMatriks (matriks):
    print("Bentuk Puzzlenya adalah : ")
    print("+----+----+----+----+")
    for i in range(4):
        print("", end='| ')
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

def swipeAndCheck(matriks, queue, kosongI, kosongJ, swipeI, swipeJ,langkah, cost0, queuePath):
    costNow = 0
    langkah = langkah +1
    if len(queuePath)!=0:
        mat= queuePath[0]
    else:
        mat=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    
    if (swipeI==kosongI-1 and swipeJ==kosongJ) or (swipeI==kosongI+1 and swipeJ==kosongJ) or (swipeJ==kosongJ+1 and swipeI==kosongI) or (swipeJ==kosongJ-1 and swipeI==kosongI):
        matriks[kosongI][kosongJ] =matriks[swipeI][swipeJ]
        matriks[swipeI][swipeJ]=0
        costNow = checkDenganSusunanAkhir(matriks)+langkah
        isTrue = 0
        for i in range(4):
            for j in range(4):
                if mat[i][j] != matriks[i][j]:
                    isTrue = 1
                    break
            if mat[i][j] != matriks[i][j]:
                isTrue = 1
                break

        if isTrue ==1:    
            matriksacuan = []
            for k in range(4):
                new=[]
                for l in range(4):
                    new.append(matriks[k][l])
                matriksacuan.append(new)              
            if (len(queue)!=0):
                if cost0>=costNow:
                    queue.appendleft((matriksacuan,costNow,langkah))
                else:
                    queue.append((matriksacuan,costNow,langkah))    
            else:
                queue.append((matriksacuan,costNow,langkah))
        matriks[swipeI][swipeJ]=matriks[kosongI][kosongJ]
        matriks[kosongI][kosongJ] = 0
        return isTrue
def MinQueue(queue):
    min = 0
    for i in range(len(queue)):
        mat,c,l = queue[i]
        mat2, c2, l2 = queue[min]
        if c < c2: 
            min = i
    return min

def checkUDLRandAddQueue(queue,queuePath,sumsimpul,queueBefore):
    min = MinQueue(queue)
    matriks,c,langkah = queue[min]
    kosongI,kosongJ = whereKotakKosong(matriks)
    count =checkDenganSusunanAkhir(matriks)
    if count==0:
        return 1
    else:
        matriksPath= []
        for k in range(4):
            new=[]
            for l in range(4):
                new.append(matriks[k][l])
            matriksPath.append(new)
        queuePath.appendleft((matriksPath,c,langkah))
        del queue[min]
        
        #checkjika UP    
        if (kosongI-1>=0):
            isU = swipeAndCheck(matriks,queue,kosongI,kosongJ,kosongI-1,kosongJ,langkah,c,queueBefore)
            if isU==1:
                sumsimpul.append(1)
            
        #checkjika DOWN
        if (kosongI+1<=3):
            isD = swipeAndCheck(matriks,queue,kosongI,kosongJ,kosongI+1,kosongJ,langkah,c,queueBefore)            
            if isD==1:
                sumsimpul.append(1)
            
        #checkjika LEFT
        if (kosongJ-1>=0):
            isL = swipeAndCheck(matriks,queue,kosongI,kosongJ,kosongI,kosongJ-1,langkah,c,queueBefore)
            if isL==1:
                sumsimpul.append(1)
            
        #checkjika RIGHT
        if (kosongJ+1<=3):
            isR = swipeAndCheck(matriks,queue,kosongI,kosongJ,kosongI,kosongJ+1,langkah,c,queueBefore)
            if isR==1:
                sumsimpul.append(1)

        min = MinQueue(queue)
        mat,cos,walk = queue[min]
        matB, cosB, walkB = queuePath[0]

        if len(queueBefore)!=0:
            del queueBefore[0]
        matriksBefore = []
        for o in range(4):
            matrik=[]
            for p in range(4):
                matrik.append(matB[o][p])
            matriksBefore.append(matrik)
        queueBefore.appendleft(matriksBefore)
        
        if(walk==walkB):
            del queuePath[0]
        elif(walkB>walk):
            while(walk>walkB):
                del queuePath[0]
                matB, cosB, walkB = queuePath[0]
        return 0
    
#MAIN
#Masukan file eksternal
print("Masukkan nama file")
print("- Jika file test dan source code dalam 1 folder langsung ketik datainput.txt")
print("- Jika file test dan source code tidak dalam 1 folder, ketikkan juga lokasinya cth: D:/Tucil3StrAlgo-13518104/test/datainput.txt")
filemasuk = input("Nama file: ")
with open(filemasuk, 'r') as f:
    matriks = [[int(idx) for idx in line.split(' ')] for line in f]
    if len(matriks)!= 4 or len(matriks[0])  != 4:
        print("Masukan file matriks harus berukuran 4x4");
    else:
        if (checkReachableGoal(matriks)==0):
            print("Matriks tidak bisa di proses")
        else:
            
            i=0
            sumsimpul = collections.deque()
            queue = collections.deque([(matriks,999,i)])
            queuePath = collections.deque()
            queueBefore = collections.deque() 
            starttime = time.time()
            while(queue):
                checker =  checkUDLRandAddQueue(queue,queuePath,sumsimpul,queueBefore)
                if checker==1:
                    break
            
            finaltime = time.time()
            p=0
            i= len(queuePath)
            while (i!=0):
                print("----Langkah ke-",p,"----")
                ma, c, l = queuePath[i-1]
                printMatriks(ma)
                i=i-1
                p=p+1
                
            print("====Langkah ke-",p,"====")
            ma, c, l = queue[0]
            printMatriks(ma)
            print("Time execution algorithm :", finaltime-starttime)
            print("Jumlah simpul yang dibangkitkan :",len(sumsimpul))

         

            
            
     
            
    


