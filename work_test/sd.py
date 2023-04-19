#每行加一个逗号
# def sd():
#   line3=""
#   with open("/Users/yanchenghao/Desktop/log.txt", "r", encoding="utf-8") as f1, open("/Users/yanchenghao/Desktop/log2.txt", "w", encoding="utf-8") as f2:
#
#     for line in f1.readlines():
#         print(line)
#         line1='"'+line.strip()+'"'+'\r\n'
#         line3=line3+line1
#         f2.write(line1)
# sd()
#生成数字并且写入文件
def sd():
  a=80004000
  with open("/Users/yanchenghao/Desktop/log22.txt", "w", encoding="utf-8") as f1:

    for i in range(500):
        a=a+1
        f1.write(a.__str__()+",")
sd()
# def sd():
#   line3=""
#   with open("/Users/yanchenghao/Desktop/log2.txt", "r", encoding="utf-8") as f1, open("/Users/yanchenghao/Desktop/log3.txt", "w", encoding="utf-8") as f2:
#
#     for line in f1.readlines():
#         print(line)
#         line1=line.strip()+","'\r\n'
#         line3=line3+line1
#         f2.write(line1)
# sd()
