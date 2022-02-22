def merge(ar1, ar2, m, n):
 
    for i in range(n-1, -1, -1):
     
        last = ar1[m-1]
        j=m-2
        while(j >= 0 and ar1[j] > ar2[i]):
            ar1[j+1] = ar1[j]
            j-=1
  
        if (j != m-2 or last > ar2[i]):
         
            ar1[j+1] = ar2[i]
            ar2[i] = last
        
  
 
ar1 = [1, 5, 9, 10,12,15,20,23,35,67]
ar2 = [2, 3, 8, 13]
m = len(ar1)
n = len(ar2)
 
merge(ar1, ar2, m, n)
  
print("After Merging \nFirst Array:", end="")
for i in range(m):
    print(ar1[i] , " ", end="")
 
print("\nSecond Array: ", end="")
for i in range(n):
    print(ar2[i] , " ", end="")
 
    #basically what this code does is , it traverse the arr 2
    #from the last,it check whether there is a greater
    #number than this number is
    #present in arr 1 or not and also the apt position in arr 1 i.e j+1

    #there are three conditions
'''
      1)arr2[i] is largest
          leave as it is
      2)arr2[i] pos lies in 0 to m-2
          place it is crt position , make arr2[j]=last
      3)arr2[i] > all elements from 0 t0 m-2 but < arr1[last]
          place it in last,make arr[j]=last
'''
