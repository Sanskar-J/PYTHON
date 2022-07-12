def mSort(arr,l,r):
    if l>=r:
        return;
    m=int(l+(r-l)/2);
    mSort(arr,l,m);
    mSort(arr,m+1,r);
    merge(arr,l,m,r);
    print(m);
#

def merge(arr,l,m,r):
    arrNew=[];i=0;j=m+1;
    while i<m and j<r:
        if arr[i]<arr[j]:
            arrNew.append(arr[i]);
            i=i+1;
        else:
            arrNew.append(arr[j]);
            j=j+1;

    while i<m:
        arrNew.append(arr[i]);
        i=i+1;

    while j<r:
        arrNew.append(arr[j]);
        j=j+1;
    print(arrNew);
#

def inputArray(arr):
    for i in range(0,4):
        arr.append(int(input("Enter Telephone no.")));
    return arr;

#

arr=[];
arrNew=[];
inputArray(arr);
print("Array is",arr);
mSort(arr,0,4);
print("sadas",arr);
print("dasq",arrNew);
