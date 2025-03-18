n = int(input())

arr= []

for i in range(0,n):
    arr.append(int(input()))
    
arr2 =[]
for i in arr:
    power = 2**i
    s= 0
    while (power != 0):
        l = power%10
        s += l
        power //= 10
    arr2.append(s)
    
for i in arr2:
    print(i)
