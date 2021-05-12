# find the n-th fib number

def fib(n):
    if (n <=2):
        return 1
    return fib(n-1) + fib(n-2)

print(fib(10))


# print the first n fib numbers
def first_fib_nums(n):
    j = 1
    k = 1
    fibarr = []
    for i in range(0,n):
        if i < 2:
            fibarr.append(j)
        else:
           fibarr.append(j+k)
           l = j
           j = k
           k=k+l
    return fibarr 
print(first_fib_nums(10))
