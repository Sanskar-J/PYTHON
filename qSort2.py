import random

def quickSort(arr,low,high,randPivot):
    if low<high:
        pIndex= partition(arr,low,high,randPivot)
        quickSort(arr,low,pIndex-1,randPivot)
        quickSort(arr,pIndex+1,high,randPivot)

def partition(arr,low,high,randPivot):
    pivot=arr[randPivot]
    i=low-1
    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

arr=[25,16,32,92,18,57]
print(arr)
randPivot=random.randint(0,5)
quickSort(arr,0,5,randPivot)
print(arr)
arrOld=arr;
arr.reverse();
print("Descending order is",arr);
#print(random.randint(1,6))
