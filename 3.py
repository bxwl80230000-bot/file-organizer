import os
import shutil
xiazai=input(r"请输入您需要整理的文件")
if not os.path.exists(xiazai):
    print("文件不存在")
else:
    print("开始整理")
    for wenjianming in os.listdir(xiazai):
        if not os.path.isfile(os.path.join(xiazai,wenjianming)):
            continue
        kuozhanming=wenjianming.split(".")[-1]
        mubiao=os.path.join(xiazai,kuozhanming)
        os.makedirs(mubiao,exist_ok=True)
        yuanlujing=os.path.join(xiazai,wenjianming)
        shutil.move(yuanlujing,mubiao)
        print("移动成功：", wenjianming, "->", kuozhanming)

print("🎉 整理完成！")