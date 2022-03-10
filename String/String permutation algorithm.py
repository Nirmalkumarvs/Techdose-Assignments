def permutation(s):
    n=len(s)
    return permutations(0,s,n)

def permutations(ind,s,n):
    if ind==n:
        return [''.join(s)]
    res=[]
    for i in range(ind,n):
        s[ind],s[i]=s[i],s[ind]
        res+=permutations(ind+1,s,n)
        s[ind],s[i]=s[i],s[ind]
    return res


s="1234"
print(*permutation(list(s)))
