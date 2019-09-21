# -*- coding: UTF-8 -*-

# 定义初始高度，默认单位 (m)
H0 = 100

# 定义弹跳次数
times = 10

# 第二次高度与前一次之比
rate = 0.5

# ------------------------

# 定义行程初始累加器
SUM = H0

Hn = H0 * rate

for n in range(2, times +1):
    SUM += 2 * Hn
    print('No.%2d - Hn=%7.4f  SUM=%f' %(n, Hn, SUM))
    Hn *= rate

print(SUM)
