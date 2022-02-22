def boxid(r,c): 
    return r//3*3+c//3 
    
def isvalid(box,row,col,num): 
    if num in box or num in row or num in col: 
        return False 
    return True 
    
     
def bt(m,box,row,col,r,c): 
    if r==9 or c==9: 
        return True  
        
    elif m[r][c]=="0":   
        for i in range(1,10): 
            val=str(i)   
            m[r][c]=val
            id=boxid(r,c) 
            sbox=box[id] 
            srow=row[r] 
            scol=col[c] 
            
            if isvalid(sbox,srow,scol,val):   
                
                id=boxid(r,c) 
                box[id][val]=True 
                row[r][val]=True 
                col[c][val]=True 
                
                if c==8: 
                    if bt(m,box,row,col,r+1,0): 
                        return True 
                else: 
                    if bt(m,box,row,col,r,c+1): 
                        return True
                
                del box[id][val] 
                del row[r][val] 
                del col[c][val] 
                
            m[r][c]="0"
    else:   
        if c==8: 
            if bt(m,box,row,col,r+1,0): 
                return True 
        else: 
            if bt(m,box,row,col,r,c+1): 
                return True
    return False
   
       
m=[input().split() for i in range(9)]   

box=[{} for i in range(9)] 
row=[{} for i in range(9)] 
col=[{} for i in range(9)]  

for i in range(9): 
    for j in range(9): 
        if m[i][j]!="0":   
            val=m[i][j]
            box[boxid(i,j)][val],row[i][val],col[j][val]=True,True,True
   

if bt(m,box,row,col,0,0):
    [print(*i) for i in m]
else:
    print("Not Solved")
