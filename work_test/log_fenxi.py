
path = "d:\\maidian.txt"
with open(path,"r") as f:
    line=f.readline()
line.strip()
b=line.split("Report")
b0=b[0]
b1=b[1]
d1=b1.strip("{").strip(",").strip().strip("}")
report_before=b0.split("|")
report_after=d1.split(",")
print(report_before)
print(report_after)
e={}
e1={}
print
for i in report_before:
    d=i.split(":")
    # print(d)
    # print(d[0])
    e[d[0]]=d[1]
for k,v in e.items():
    if "null" in v:
        print(k)
    if v=="''":
        print(k)
print("___________________")
print("___________________")
for i in report_after:
    f=i.split("=")
    e1[f[0]]=f[1]
for k,v in e1.items():
    if "null" in v:
        a=k.strip()
        print(a)
        print(len(k))
        print(len(a))
    if v=="''":
        print(k)
        print(len(k))
