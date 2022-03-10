SIZE = 26
 
def longCommomAnagramSubseq(str1, str2,n1, n2):
 
   
    freq1 = [0] * SIZE
    freq2 = [0] * SIZE
     
    l = 0
     
    
    for i in range(n1):
        freq1[ord(str1[i]) - ord('a')] += 1
     
    for i in range(n2) :
        freq2[ord(str2[i]) - ord('a')] += 1
     
    res=""
    for i in range(SIZE):
        k = min(freq1[i], freq2[i])
        l+=k
        res += chr(i+97)*k

    return [res,l]                            
 

if __name__ == "__main__":
     
    str1 = "abdacp"
    str2 = "ckamb"
    n1 = len(str1)
    n2 = len(str2)
    print("Length = ",longCommomAnagramSubseq(str1, str2,n1, n2))
 
