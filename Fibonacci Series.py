def fibonacci(n):
    if n<=1:
        print("Invalid Number of terms")
        return
    prev1= 1
    prev2 = 0
    print(prev2,end=" ")
    if n==1:
        return
    print(prev1,end= " ")

    for i in range (3,n+1):
        curr = prev1+prev2
        prev2 = prev1
        prev1 = curr
        print(curr,end=" ")

print(fibonacci(int(input())))
