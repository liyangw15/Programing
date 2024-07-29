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
print(products[0][1]) #大清單裡面的位置 -> 小清單裡面的位置

for p in products:
	print(p[0])