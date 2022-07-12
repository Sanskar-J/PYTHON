def cSort(arrA):
    maxV= max(arrA)
    print(maxV)
    arrB=[]
    for i in range(0,maxV+1):
        arrB.append(0)
    for i in range(0,len(arrA)):
        arrB[arrA[i]] += 1
    arrC=[]
    for i in range(0,maxV+1):
        while arrB[i] != 0:
            arrC.append(i)
            arrB[i] -= 1
    return arrC

arr=[1,0,0,6,2,1,3,6,5]
print(arr)
print(cSort(arr))
