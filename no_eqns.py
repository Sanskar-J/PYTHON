def no_of_eqns(n):
    sum=[0,1]
    temp=0
    for i in range(2,n+1):
        for j in range(1,i+1):
            temp += sum[j]*sum[i-j]

            sum.append(temp)
    print(temp)



no_of_eqns(3)
