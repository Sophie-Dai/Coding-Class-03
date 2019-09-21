# -*- coding: UTF-8 -*-

import fractions

num_start = 1
num_end = 5

sum = 0

for num in range(num_start, num_end + 1):
    # fc = 1 / num
    fc = fractions.Fraction(1, num)
    sum += fc
    print('Add %s to summary, then sum=%s' % (fc, sum))

print(sum)
