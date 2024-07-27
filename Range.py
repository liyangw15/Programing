# Range 範圍
# Python內建功能: 清單產生器

#range(5)

#for i in range(5):
#	print(i)

import random

for i in range(100):
	r = random.randint(1, 1000)
	print('這是第', i + 1, '次產生隨機變數: ', r)
