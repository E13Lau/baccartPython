# -*- coding: utf-8 -*-

#判断A,J,Q,K方法
def selection(CardNumber):
	if CardNumber >=10:
		CardNumber = 0
		return CardNumber
	else:
		return CardNumber

#计算当前个位点数的方法
def getCardPoint(CardOne,CardTwo,CardThree = 0):
	# 只取个位数，取除10的余数
	point = (CardOne + CardTwo + CardThree)%10
	return point

#判断胜负方法
def whoWinAndWhat(playerPoint,bankerPoint):
	if playerPoint > bankerPoint:
		return ('庄家%d点,闲家%d点,闲赢'%(bankerPoint,playerPoint))
	elif playerPoint == bankerPoint:
		return ('庄家%d点,闲家%d点,和局'%(bankerPoint,playerPoint))
	elif playerPoint < bankerPoint:
		return ('庄家%d点,闲家%d点,庄赢'%(bankerPoint,playerPoint))

#判断胜负方法只输出胜负
def whoWin(playerPoint,bankerPoint):
	if playerPoint > bankerPoint:
		return ('闲赢')
	elif playerPoint == bankerPoint:
		return ('和局')
	elif playerPoint < bankerPoint:
		return ('庄赢')

#是否补牌方法


#庄家补牌方法
def bankerGetCard(One,Two,Three):
	Three = selection(Three)
	bankerPoint = getCardPoint(One,Two,Three)
	return bankerPoint
	pass

def mainfunction():
	# raw_input 得到的是 string 
	cards = raw_input('请输入牌组(以.号隔开):')
	# 分隔开 http://wangwei007.blog.51cto.com/68019/903426
	cards = cards.split('.')
	# cards 的 int 数组
	cardsArray = []
	# 循环把 string 转换成 int
	for x in cards:
		cardsArray.append(int(x))
		pass

	#下标 i
	i = 0 
	while i < len(cardsArray):
		if len(cardsArray) - i < 4:
			# print 语句输出格式 http://www.pythonclub.org/python-basic/print
			# 数组截取中间段 http://blog.itpub.net/22664653/viewspace-702940/
			print('余下%s'%(cardsArray[-4:len(cardsArray)]))
			break
			pass
		playerCardOne = cardsArray[i]
		i += 1
		bankerCardOne = cardsArray[i]
		i += 1
		bankerCardThree = 0
		playerCardTwo = cardsArray[i]
		i += 1
		bankerCardTwo = cardsArray[i]
		i += 1
		playerCardThree = 0

		bankerCardOne = selection(bankerCardOne)
		bankerCardTwo = selection(bankerCardTwo)
		playerCardOne = selection(playerCardOne)
		playerCardTwo = selection(playerCardTwo)

		bankerPoint = getCardPoint(bankerCardOne,bankerCardTwo)
		playerPoint = getCardPoint(playerCardOne,playerCardTwo)

		# http://www.bowenwang.com.cn/how-to-play-baccarat1.htm
		if playerPoint > 7 or bankerPoint > 7:
			pass
		elif bankerPoint < 6 or playerPoint < 6:
			if playerPoint < 6:
				playerCardThree = cardsArray[i]
				i += 1
				playerCardThree = selection(playerCardThree)
				playerPoint = getCardPoint(playerCardOne,playerCardTwo,playerCardThree)
				pass
			if bankerPoint == 3:
				if playerCardThree != 8:
					print(playerPoint)
					bankerCardThree = cardsArray[i]
					i += 1
					bankerPoint = bankerGetCard(bankerCardOne,bankerCardTwo,bankerCardThree)
					pass
				pass
			if bankerPoint == 4:
				if playerCardThree < 8 and playerCardThree > 1:
					bankerCardThree = cardsArray[i]
					i += 1
					bankerPoint = bankerGetCard(bankerCardOne,bankerCardTwo,bankerCardThree)
					pass
				pass
			if bankerPoint == 5:
				if playerCardThree < 8 and playerCardThree > 3:
					bankerCardThree = cardsArray[i]
					i += 1
					bankerPoint = bankerGetCard(bankerCardOne,bankerCardTwo,bankerCardThree)
					pass
				pass
			if bankerPoint == 6:
				if playerCardThree == 6 or playerCardThree == 7:
					bankerCardThree = cardsArray[i]
					i += 1
					bankerPoint = bankerGetCard(bankerCardOne,bankerCardTwo,bankerCardThree)
					pass
				pass
			if bankerPoint < 3:
				bankerCardThree = cardsArray[i]
				i += 1
				bankerPoint = bankerGetCard(bankerCardOne,bankerCardTwo,bankerCardThree)
				pass
			pass
		print(whoWinAndWhat(playerPoint,bankerPoint))
		pass
	# 循环运行
	mainfunction()
	pass

mainfunction()
