age = input('你今年幾歲? ')
age = int(age)
if age < 13:
	print('國小生')
elif age >= 13 and age < 16:
	print('國中生')
elif age >= 16 and age < 19:
	print('高中生')
elif age >= 19 and age < 23:
	print('大學生')
else: 
	print('社會人士')
