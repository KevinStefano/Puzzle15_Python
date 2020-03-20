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
            
def checkAwalMatriks (matriks):
    #cari index yang kosong
    for i in range(4):
        for j in range(4):
            if matriks[i][j]==0:
                break
        if matriks[i][j]==0:
                break
#Masukan file eksternal
with open('datainput.txt', 'r') as f:
    matriks = [[int(idx) for idx in line.split(' ')] for line in f]
    print(matriks)
    if len(matriks)!= 4 or len(matriks[0])  != 4:
        print("Masukan file matriks haris berukuran 4x4");
        quit()


#matrixA = Matrix()
#matrixA[0][1] = 5
print(matriks[0][1])
printMatriks(matriks)
