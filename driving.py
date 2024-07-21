drive = input('你有沒有開過車?')
if drive != '有' and drive != '沒有':
	print('請輸入"有"或"沒有"!')
	raise SystemExit

age = input('你今年幾歲?')
age = int(age)
if drive == '有':
	if age >= 18:
		print('你是個遵守規矩的駕駛！')
	else:
		print('你是未成年開車喔！')
elif drive == '沒有':
	if age >= 18:
		print('你怎麼還沒去考駕照?')
	else:
		print('沒關係，再過幾年就可以考了!')


