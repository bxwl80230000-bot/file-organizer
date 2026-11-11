import os

lianxiren={}
if os.path.exists("test.tst"):
    with open("test.tst","r")as f:
        for i in f:
            i=i.strip()
            mz,hm=i.split(",")
            lianxiren[mz]=hm
def save():
    with open("test.tst", "w") as f:
        for k, v in lianxiren.items():
            f.write(k + "," + v + "\n")
while True:
    print("----通讯录----")
    print("1.添加联系人")
    print("2.查看全部联系人")
    print("3.查找联系人")
    print("4.删除联系人")
    print("5.退出通讯录")
    xuanze=input("请选择：")
    if xuanze=="1":
        mz=input("请填写联系人名字:")
        hm=input("请填写号码:")
        lianxiren[mz]=hm
        print("添加成功")
        save()
    elif xuanze=="2":
        if len(lianxiren)==0:
            print("没有联系人")
        else:
            for i,io in lianxiren.items():
                print(i,"的电话号码是:",io)
    elif xuanze=="3":
        mz=input("请输入查找姓名:")
        if mz in lianxiren:
            print(lianxiren[mz])
        else:
            print("查无此人")
    elif xuanze=="4":
        mz=input("请填写删除的姓名:")
        if mz in lianxiren:
            del lianxiren[mz]
            print("删除成功")
            save()
        else:
            print("尚未有此联系人")
    elif xuanze=="5":
        print("再见")
        break
    else:
        print("没有这个选项")