time = 3
time = int(time)
while time >= 1:
	time = time - 1
	password = input('請輸入密碼: ')
	if password == 'a123456':
		print('登入成功')
		break
	elif time >= 1:
		print('密碼錯誤，你還有',time,'次機會')
	else:
		print('你的機會用完了!')







