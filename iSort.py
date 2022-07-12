def iSort(arr):
    for i in range(1,len(arr)):
        key=arr[i];
        j=i-1;
        while arr[j]>key and j>=0:
            arr[j+1]=arr[j];
            j=j-1;
        arr[j+1]=key;

def inputArray(arr):
    for i in range(0,1000):
        arr.append(int(input("Enter Telephone no.")));
    return arr;
#
#x=int(input("Enter x: "))
#y=int(input("Enter y: "))
#
#arr=[5,3,1,4,2]
arr=[];
inputArray(arr);
print("Array is",arr);
iSort(arr);
print("Ascending order is",arr);
arrOld=arr;
arr.reverse();
print("Descending order is",arr);
