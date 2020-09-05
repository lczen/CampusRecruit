n = int(input())

ROW = n
COL = n

def isvalid(row,col,prevRow,prevCol):
    return (row>=0) and (row<ROW) and (col>=0) and (col<COL) and not (row==prevRow and col==prevCol)

rowNum = [0,0,-1,1]
colNum = [1,-1,0,0]
def DFS(mat,row,col,prevRow,prevCol,word,path,index,n):
    if (index>n or mat[row][col]!=word[index]):
        return
    path += word[index]+"("+str(row)+","+str(col)+")"
    if index == n:
        ans.append(path)
        return
    for k in range(4):
        if (isvalid(row+rowNum[k],col+colNum[k],prevRow,prevCol)):
            DFS(mat,row+rowNum[k],col+colNum[k],row,col,word,path,index+1,n)
def findWords(mat,word,n):
    for i in range(ROW):
        for j in range(COL):
            if mat[i][j] == word[0]:
                DFS(mat,i,j,-1,-1,word,"",0,n)
mat=[['C','H','I','A'],['C','A','N','T'],['G','R','A','C'],['B','B','D','E']]

word=list("CHINA")

ans = []
findWords(mat,word,len(word)-1)
print(len(ans))
# CANT
# GRAC
# BBDE