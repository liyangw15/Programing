import random
r = random.randint(1, 100)
n = 0

while True:
	num = input('請輸入數字: ')
	num = int(num)
	n = n + 1
	if num == r:
		print('這是你猜的第', n  ,'次，你答對了！')
		break
	elif num > r:
		print('這是你猜的第', n ,'次，比答案大!')
	elif num < r:
		print('這是你猜的第', n ,'次，比答案小!')



