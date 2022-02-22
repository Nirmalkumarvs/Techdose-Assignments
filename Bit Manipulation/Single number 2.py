nums=[1,1,1,2,2,2,4]
no=0
for i in range(32):
    for j in range(len(nums)):
        num=abs(nums[j])
        count=0
        if num&(1<<i)==1<<i:
            count+=1
          
          
    if(count%3!=0):
        no+=(1<<i)
            


for i in nums:
    if i==no:
        print(no)
        exit()

print(-no)
