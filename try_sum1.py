# -*- coding: UTF-8 -*-

'''
for num in range(5):
for num in range(1,5):
for num in range(1,5,2):
'''

num_start = 1
num_end = 1000000000

num_input = input('Type a end number:')
num_end = int(num_input)

sum = 0

for num in range(num_start, num_end + 1):
    sum += num_end

print(sum)
