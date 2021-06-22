#讀取檔案
products = []

with open('products.csv', 'r', encoding = 'utf-8') as f:			#encoding = 'utf-8' 就是讓它讀取時不出現亂碼。
	for line in f:													#建立一個for loop 迴圈。
		if '商品,價格' in line:										#如果'商品,價格'這個字串有在 line 裡面的話。
			continue												#continue 的意思是指跳到下一迴的意思。
		name, price = line.strip().split(',')						#用.strip() 來除掉換行符號(\n), 用split(',')來用逗點做分割。當split 完成後，它就會變成清單，然而存進name, price 裡。
		products.append([name,price])								#將讀取出來的name, price 存入products的清單中。
print(products)

#讓使用者輸入
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

#印出所有購買紀錄
for product in products:
	print(product[0], '的價格是', product[1])

#寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:				#建立一個product.csv 的檔案，w 是指write（寫入的意思），as f 就是把這個檔案命名為f, 好讓它方便呼叫。 encoding = 'utf-8' 就是讓它寫入時不出現亂碼。
	f.write('商品,價格\n')
	for product in products:						#建立一個for loop 迴圈。
		f.write(product[0] + ',' + str(product[1]) + '\n')	#就是把product的第0格＋ "，" 就是分格 ＋ 第1格＋＼N 就是換行， 然而 f.write 就是寫入products.txt中。
															#在第21行中的str(product[1])就是把數值變字串，因為字串只能和字串相加。