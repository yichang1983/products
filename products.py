products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	p = input('請輸入商品價格：')
	price = int(p)
	# p = []							#建立p 為大清單中裡的小清單
	# p.append(name)					#把商品名稱加上去p的清單裡
	# p.append(price)					#把商品價格加上去p的清單裡
	# p = [name, price]					#以上的7-9 行程式碼，相當於第十行的程式碼。
	products.append([name, price])		#把小清單裡的內容（商品名稱和商品價格）加上去大清單（product）裡.,  除了第十行的寫法外，更簡單的寫法，直接把小清單寫進大清單中。
print(products)

for product in products:
	print(product[0], '的價格是', product[1])


with open('products.csv', 'w', encoding = 'utf-8') as f:				#建立一個product.csv 的檔案，w 是指write（寫入的意思），as f 就是把這個檔案命名為f, 好讓它方便呼叫。 encoding = 'utf-8' 就是讓它寫入時不出現亂碼。
	f.write('商品,價格\n')
	for product in products:						#建立一個for loop 迴圈。
		f.write(product[0] + ',' + str(product[1]) + '\n')	#就是把product的第0格＋ "，" 就是分格 ＋ 第1格＋＼N 就是換行， 然而 f.write 就是寫入products.txt中。
															#在第21行中的str(product[1])就是把數值變字串，因為字串只能和字串相加。