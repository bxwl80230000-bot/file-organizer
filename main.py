import random
jishu=0

name = input("输入你的名字")
a = random.randint(1, 100)
while True:
    cai=int(input("猜1~100的数字："))
    if cai==a :
        jishu+= 1
        print("猜对了你用了",jishu,"次")
        with open("record.txt", "a") as f:
            f.write(name + "," + str(jishu) + "\n")
        break
    elif cai<a:
        jishu+=1
        print("小了")
    elif cai>a:
        jishu+=1
        print("大了")
records = []
with open("record.txt", "r") as f:
    for line in f:
        line = line.strip()
        name, count = line.split(",")
        records.append((int(count), name))
records.sort()                        # 按次数从小到大排

print("===== 排行榜 =====")
for count, name in records:
    print(name, "用了", count, "次")