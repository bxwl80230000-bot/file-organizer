def analyze(scores):
    zonshu=0
    renshu=0
    for i in scores:
        if i>=60:
            zonshu+=i
            renshu+=1
    if renshu == 0:
        return {"总分": 0, "人数": 0, "平均分": 0}
    return {"总数是":zonshu,"人数":renshu,"平均分":zonshu/renshu}
print(analyze([85, 58, 92, 45, 76]))
# 应该输出 {'人数': 3, '总分': 253, '平均分': 84.33333333333333}