def activitySelect(start,end,n):
    i=0
    c=1
    print(start[i])
    for j in range(0,n):
        if start[j]>=end[i]:

            i = j
            c += 1
            print(start[i])
    print("Max no. of activities",c);

start=[0,1,3,5,8,5]
end=[6,2,4,7,9,9]
activitySelect(start,end,6)
