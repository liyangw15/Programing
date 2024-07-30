products = []

while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	#p = []
	#p.append(name)
	#p.append(price)
	#p = [name, price]
	products.append([name, price])

print(products)

#for p in products:
#    print(products[0][1]) #大清單裡面的位置 -> 小清單裡面的位置

for p in products:
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')