import os		#operating system

#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f:		#encoding = 'utf-8' 就是讓它讀取時不出現亂碼。
		for line in f:										#建立一個for loop 迴圈。
			if '商品,價格' in line:							#如果'商品,價格'這個字串有在 line 裡面的話。
				continue									#continue 的意思是指跳到下一迴的意思。
			name, price = line.strip().split(',')			#用.strip() 來除掉換行符號(\n), 用split(',')來用逗點做分割。當split 完成後，它就會變成清單，然而存進name, price 裡。
			products.append([name,price])					#將讀取出來的name, price 存入products的清單中。
	return products 										#把清單（products） 結果回傳。

#讓使用者輸入
def user_input(products):					#這兒的products是因應第31行所需，因為第31行它不知道哪裡有products，如果沒訂議products,第31行它會到外面拿（因此不好）。
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
	return products 						#把清單（products） 結果回傳。

#印出所有購買紀錄
def print_products(products):				#這兒的products是因應第37行所需，因為第37行它不知道哪裡有products，如果沒訂議products,第31行它會到外面拿（因此不好）。
	for product in products:									
		print(product[0], '的價格是', product[1])

#寫入檔案
def write_file(filename, products):			#這兒的filename是因應第42行所需，而products 是因應44行所需，因為他們不知道哪裡有filename 和 products，如果沒訂議filename和products,它會到外面拿（因此不好）。
	with open(filename, 'w', encoding = 'utf-8') as f:				#建立一個product.csv 的檔案，w 是指write（寫入的意思），as f 就是把這個檔案命名為f, 好讓它方便呼叫。 encoding = 'utf-8' 就是讓它寫入時不出現亂碼。
		f.write('商品,價格\n')
		for product in products:						#建立一個for loop 迴圈。
			f.write(product[0] + ',' + str(product[1]) + '\n')	#就是把product的第0格＋ "，" 就是分格 ＋ 第1格＋＼N 就是換行， 然而 f.write 就是寫入products.txt中。
																#在第21行中的str(product[1])就是把數值變字串，因為字串只能和字串相加



def main():									#把執行檔也訂議為一個fuction,並命名為main
	filename ='products.csv'
	if os.path.isfile(filename):			#檢查檔案在不在
		print('找到檔案了！')
		products = read_file(filename)	#有return（在17行）, function的執行結果就可以存下來開。而這個read_file(products.csv)意思就是把products.csv 投進第4行上的filename，而第6行就變成了讀取products.csv,第8行就打開product.csv。
	else:
		print('沒找到檔案')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()										#呼叫執行程式。		
