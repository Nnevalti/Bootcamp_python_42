def generator(text, sep=" ", option=None) :
	list = text.split(sep)
	if option :
		if option == "shuffle" :
			print("En fait nique toi")
		elif option == "unique" :
			list2 = []
			for i in list :
				if i not in list2 :
					list2.append(i)
			list = list2
		elif option == "ordered" :
			list.sort()
	for i in list :
		yield i

for i in generator("test test jbjhb jhjsdf jhkvdjhbgs", option="unique") :
	print(i)
