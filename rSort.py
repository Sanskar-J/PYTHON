def rSort(arr):
    maxOfArray= max(arr)
    digits=noOfDigits(maxOfArray)
    for i in range(0,digits):
        cSort(arr,i)

def noOfDigits(n):
    c=0
    while n != 0:
        n=int(n/10)
        c +=1
    return c

def cSort(arrA,c):
    arrTemp=[]
    temp=0
    for i in range(0,len(arrA)):
        for j in range(0,c):
            temp=arrA[i]%10
            arrA[i]=int(arrA[i]/10)
        arrTemp.append(temp)
    maxV= max(arrTemp)
    print(arrTemp)
    print(maxV)
    arrB=[]
    for i in range(0,maxV+1):
        arrB.append(0)
    for i in range(0,len(arrTemp)):
        arrB[arrTemp[i]] += 1
    arrC=[]
    for i in range(0,maxV+1):
        while arrB[i] != 0:
            arrC.append(i)
            arrB[i] -= 1
    return arrC

a=[456,912,321,227,553,251,687]
rSort(a)
