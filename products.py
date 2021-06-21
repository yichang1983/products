products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	# p = []							#建立p 為大清單中裡的小清單
	# p.append(name)					#把商品名稱加上去p的清單裡
	# p.append(price)					#把商品價格加上去p的清單裡
	# p = [name, price]					#以上的7-9 行程式碼，相當於第十行的程式碼。
	products.append([name, price])		#把小清單裡的內容（商品名稱和商品價格）加上去大清單（product）裡.,  除了第十行的寫法外，更簡單的寫法，直接把小清單寫進大清單中。
print(products)