
list=[1,1,2,3,4,5,6]
sd=10
for i in range(len(list)-2):
    num=list[i]
    j=i+1
    while(num<sd):
        num=num+list[j]
        j=j+1
    if num==sd:
        print(i)
        print(j)
        break
    if num>sd:
        continue