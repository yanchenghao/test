a=[1,2,3,4]
def func1():
 for i in range(len(a)):
    return a[i]
def func2():
     for i in range(len(a)):
         print("sdsds")
         yield func1()
         # yield a[i]
         print("ssfsdfsdfsdf")
# a1=func1()
# print(a1)
b1=func2()
for i in b1:
    print(i)
print(b1)
