# Range 範圍
# Python內建功能: 清單產生器

#range(5) --> [0, 1, 2, 3, 4]

#range(2,5) --> [2, 3, 4]

#range(2, 10, 3) --> [2, 5, 8]
#range(10, 3, -2) --> [10, 8, 6, 4]


#for i in range(5):
#	print(i)

import random

for i in range(100):
	r = random.randint(1, 1000)
	print('這是第', i + 1, '次產生隨機變數: ', r)
