import os
import random
lb=[]
if os.path.exists("money.txt"):
    with open("money.txt","r")as f:
        for i in f:
            i=i.strip()
            lb.append(i)
while True:
    print("=====单词本======")
    print("1.添加单词")
    print("2.背单词")
    print("3.查看所有单词")
    print("4.退出")
    xuanze = input("请选择:")
    if xuanze == "1":
        dc = input("请输入单词:")
        ys = input("请输入翻译:")
        lb.append(dc+","+ys)
        print("添加成功")
        with open("money.txt","a")as f:
            f.write(dc+","+ys+"\n")
    if xuanze == "2":
        if len(lb)==0:
            print("没有单词")
        else:
            while True:
                lb=random.choice(list())
