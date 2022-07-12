def multiplication(num):
    if num<=1:
        return 1
    rult=0
    for k in range(num):
        rult += multiplication(k) * multiplication(num-k-1)
    return rult

num=int(input("enter the number "))
for i in range(num):
    ans= multiplication(i)
print(ans)
