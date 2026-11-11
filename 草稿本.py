students = [
    {"name": "小明", "score": 85},
    {"name": "小红", "score": 92},
    {"name": "小刚", "score": 78},
]
for stu in students:
    print(stu["name"]),stu["score"]
total = 0
for stu in students:
    total += stu["score"]      # 只累加成绩
print("平均分:", total / len(students))
max_score = 0
max_name = ""
for stu in students:
    if stu["score"] > max_score:
        max_score = stu["score"]
        max_name = stu["name"]
print("最高分:", max_name, max_score)