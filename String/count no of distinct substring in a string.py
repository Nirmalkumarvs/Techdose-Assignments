def distinctSubstring(str):
    
    result = set()
 
    
    for i in range(len(str)+1):
        for j in range( i + 1, len(str)+1):
 
            result.add(str[i:j]);
    return len(result);
 

str = "aaaa"
print(distinctSubstring(str));
