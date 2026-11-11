sales = {
    "张三": [1200, 800, 1500],
    "李四": [900, 1100, 1000],
    "王五": [2000, 1800, 2200]
}

totals = []                        # ① 空列表放外层
for name, amounts in sales.items():
    total = sum(amounts)           # ② 求这个人总和
    totals.append(total)           # ③ 加到列表里
print(totals)           # [3500, 3000, 6000]