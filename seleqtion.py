arr=[64,32,10,53]
for i in range(len(arr)):
    poqr=i
    for j in range(i+1,len(arr)):
        if arr[poqr]>arr[j]:
            poqr=j
    arr[i],arr[poqr]=arr[poqr],arr[i]
for i in range(len(arr)):
    print(arr[i])

