# n的阶乘
n=int(input('请输入一个正整数：'))
print(n)
sum=1
for n in range(1,n+1):
    sum*=n
    n+=n
print(sum)

# 折纸上月球
n=1
while n <100:
    if 0.088*2**n>=3.633*10**11:
        break
    n+=1
print(n)