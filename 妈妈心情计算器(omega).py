# 采集妈妈心情指数
mom_xinqing = int(input("请输入妈妈今日心情指数（0~100）："))
if 30 >= mom_xinqing >= 1:
    print("今日妈妈心情极为不好,不要招惹！千万不要！")
# 再次嵌套elif函数

elif 51 < mom_xinqing >= 60:
    print("今天妈妈心情还好,可以试试提小要求.")
elif 61 < mom_xinqing >= 85:
    print("今天妈妈心情好,适合坦白从宽.")
elif 86 < mom_xinqing >= 100:
    print("今天妈妈心情棒极了！")
else:
    print("今天心情还好.")
# 设置一个菜单
user_pingjia = float(input("您对我们的产品满意吗请打分(满分：100)："))
if user_pingjia >= 100:
    print("感谢！")
elif 1 <= user_pingjia >= 99:
    print("谢谢！")
elif 9.99>=user_pingjia<=9.991:
    print("盲生你发现了华点")
else :
    print("最大100！")
