data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		count += 1
		data.append(line)
		if count % 2000 == 0:
			print(len(data))

print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('平均長度是', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[500])

good = [d for d in data if 'good' in d]
print('一共有', len(good), '筆留言裡面提到good')

bad = ['bad' in d for d in data]
print(bad)

#gd = []
#for d in data:
#	if 'good' in d:
#		gd.append(d)
#print('一共有', len(gd), '筆留言裡面提到good')