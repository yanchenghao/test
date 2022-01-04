import copy
a=[0,1,[2,3]]
c=a
d=copy.copy(a)
e=copy.deepcopy(a)
print(id(a))
print(id(c))
print(id(d))
print(id(e),end="")
print("-----------")
if a==e:
    print ("1")
else:
    print("-1")
a[0]=10
if a==e:
    print ("1")
else:
    print("-1")
# a[0]=10
# d[2][0]=0
# print(a)
# print(d)
# print(e)
# a[0][1]=10
# print(a)
# print(d)
# print(e)
# a[0]=4
# print(a)
# print(d)
# print(e)