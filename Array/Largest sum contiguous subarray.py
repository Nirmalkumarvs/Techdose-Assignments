arr=[-2, -3, 4, -1, -2, 1, 5, -3]
max_so_far=arr[0]
curr_sum=0
start=0
end=0
s=0
for i in range(len(arr)):
    curr_sum+=arr[i]
    if curr_sum>max_so_far:
        max_so_far=curr_sum
        start=s
        end=i
    if curr_sum<0:
        curr_sum=0
        s=i+1
print(arr[start:end+1])
