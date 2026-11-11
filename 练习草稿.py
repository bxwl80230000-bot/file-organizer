import os
import  random
danci={}
if os.path.exists("money.txt"):
    with open("money.txt","r")as f:
        for i in f:
            i=i.strip()
            dc,ys=i.split(",")
            danci[dc]=ys
while True:
    print("=====单词本======")
    print("1.添加单词")
    print("2.背单词")
    print("3.查看所有单词")
    print("4.退出")
    xuanze=input("请选择:")
    if xuanze=="1":
        dc = input("请输入单词:")
        ys = input("请输入翻译:")
        danci[dc]=ys
        print("添加成功")
        with open("money.txt","a")as f:
            f.write(dc+","+ys+"\n")
    elif xuanze=="2":

        if len(danci)==0:
            print("目前还没有单词")
        else:
            while True:
                dc=random.choice(list(danci.keys()))
                print("单词",dc)
                ys=input("请输入中文（输入q退出）：")
                if ys=="q":
                    break
                if ys==danci[dc]:
                    print("对了")
                else:
                    print("错了，正确答案是：",danci[dc])
    elif xuanze=="3":
        print("待完成")
    elif xuanze=="4":
        print("再见")
        break
    else:
        print("没有这个选项")

