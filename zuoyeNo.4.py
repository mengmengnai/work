# 篮球高度
h = int(input("请输入篮球初始高度（米）："))
m = h
sum = h
for i in range(0,10):
    if i == 0:
        sum = m
    else:
        m = m / 2
        sum = sum + 2 * m
print("到球第10次落地一共经过 %.9f 米"% sum)
print("第10次弹跳高度是%.9f米"% m)


# 1到5的阶乘之和
s = 1
sum = 0
for i in range(1,6):
    s *= i
    sum += s
print("1!+2!+3!+4!+5!的和是：%d"% sum)