#最小值
nums = [3, 7, 2, 9, 5]

min_val = nums[0]
for x in nums[1:]:
    if x < min_val:      # 只有 "<" 变了
        min_val = x

print(min_val)           # 2
#基础版
nums = [3, 7, 2, 9, 5]

# ① 初始化:第一个元素当擂主
max_val = nums[0]

# ② 从第二个开始逐个挑战
for x in nums[1:]:
    if x > max_val:      # 挑战成功
        max_val = x      # 换擂主

print(max_val)           # 9
#进阶:同时找 最大 和 最小(一趟扫描)
nums = [3, 7, 2, 9, 5]
max_val = min_val = nums[0]
for x in nums[1:]:
    if x > max_val:
        max_val = x
    if x < min_val:
        min_val = x

print(f"最大 {max_val},最小 {min_val}")   # 最大 9,最小 2
#d.get(k, default)	安全取值	d.get("赵六", 0) → 0
#d.keys()	所有键	dict_keys(['张三',...])
#d.values()	所有值	dict_values([3500,...])
#d.items()	所有键值对	dict_items([('张三',3500),...])
#d.setdefault(k, default)	有则返回,无则先设再返回	见下方
#d.update(d2)	合并另一个字典	d.update({"赵六": 5000})
#d.pop(k, default)	删并返回	d.pop("张三") → 3500
#d.popitem()	删最后一个键值对	Python 3.7+ 按插入顺序
#d.clear()	清空
#d.copy()	浅拷贝
## ① 每人总数(你写过的)
totals = {k: sum(v) for k, v in sales.items()}
# {'张三': 3500, '李四': 3000, '王五': 6000}

# ② 带条件过滤:只要总数 ≥ 4000 的
big = {k: v for k, v in totals.items() if v >= 4000}
# {'王五': 6000}

# ③ 值全部翻倍
doubled = {k: v * 2 for k, v in totals.items()}

# ④ 键值互换(注意值必须唯一)
reversed_d = {v: k for k, v in totals.items()}
# {3500: '张三', 3000: '李四', 6000: '王五'}
totals = {"张三": 3500, "李四": 3000, "王五": 6000}

# ① 按值从大到小 → 返回列表
sorted(totals.items(), key=lambda x: x[1], reverse=True)
# [('王五', 6000), ('张三', 3500), ('李四', 3000)]

# ② 按值排序 → 返回新字典(Python 3.7+)
dict(sorted(totals.items(), key=lambda x: x[1], reverse=True))
# {'王五': 6000, '张三': 3500, '李四': 3000}

# ③ 按键排序
sorted(totals.items())           # 按名字默认字符顺序

# ④ 值相同再按键排(稳定排序)
sorted(totals.items(), key=lambda x: (-x[1], x[0]))