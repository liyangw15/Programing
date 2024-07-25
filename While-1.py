while True:
	mode = input('請輸入遊戲模式: ')
	if mode == 'q':
		break
	elif mode == '1':
		print('已啟動模式一')
	elif mode == '2':
		print('已啟動模式二')
	else:
		print('只能夠輸入1/2/q')

