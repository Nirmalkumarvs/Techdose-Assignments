def wilcard(pat,text):
    c = len(pat)
    r = len(text)
    m=[[0]*(c+1) for i in range(r+1)]
    m[0][0]=True
    for i in range(1,c+1):
        if pat[i-1]=='*':
            m[0][i]=m[0][i-1]
    for i in range(1,r):
        m[i][0]=False
        
    for i in range(1,r+1):
        for j in range(1,c+1):
            if pat[j-1]==text[i-1] or pat[i-1]=='?':
                m[i][j]=m[i-1][j-1]
            elif pat[i-1]=="*":
                m[i][j]=m[i][j-1] or m[i-1][j]
            else:
                m[i][j]=False
    return m[-1][-1]
        

pat = "*****ba*****ab"
text = "baaabab"

print(wilcard(pat,text))
