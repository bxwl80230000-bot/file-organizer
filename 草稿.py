zidain={}
with open("test.tst", "w") as f:  # 先用 "w" 清空
    pass
with open("test.tst","a")as f:
    f.write("张三,138\n")
    f.write("李四,139\n")
with open("test.tst","a")as f:
    f.write("王五,137\n")
with open("test.tst","r")as f:
    for i in f:
        i=i.strip()
        print(i)

