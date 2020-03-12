class Evaluator :

	def zip_evaluate(words, coefs) :
		if len(words) == len(coefs) :
			result = 0
			list = zip(words, coefs)
			for i in list :
				result += len(i[0]) * i[1]
			print(result)
		else :
			return(-1)

	def enumerate_evaluate(words, coefs) :
		result = 0
		for i in enumerate(words) :
			result += len(i[1]) * coefs[i[0]]
		print (result)


words= ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs= [1.0, 2.0, 1.0, 4.0, 0.5]
Evaluator.zip_evaluate(words, coefs)
Evaluator.enumerate_evaluate(words, coefs)
