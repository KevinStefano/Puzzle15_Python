#Name   : Kevin Austin Stefano
#NIM    : 13518104



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
                    if (matriks[m][n]<matriks[k][l] and matriks[m][n]!=0 and matriks[k][l]!=0):
                        kurang=kurang+1
                    n=n+1
                n=0
                m=m+1
    #hitung total
    kurang = kurang+x
    #check apakah genap atau bukan
    if kurang%2==0:
        return 1; #bisa
    else:
        return 0 #tidakbisa
            
            

#MAIN           
#Masukan file eksternal
with open('datainput.txt', 'r') as f:
    matriks = [[int(idx) for idx in line.split(' ')] for line in f]
    if len(matriks)!= 4 or len(matriks[0])  != 4:
        print("Masukan file matriks harus berukuran 4x4");
    else:
        #matrixA = Matrix()
        #matrixA[0][1] = 5
        printMatriks(matriks)

        if (checkReachableGoal(matriks)==0):
            print("Matriks tidak bisa di proses")
     
            
    


