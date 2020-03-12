from vector import Vector

class Matrix :
	"""A class for Matrix"""

	def __init__(self, data=[[]], shape=()) :
		self.data = []
		if isinstance(data, tuple) :
			for i in range(0, data[0], 1) :
				self.data.append([])
				for j in range(0, data[1]) :
					self.data[i].append(0.0)
			self.shape = data
		else :
			self.data = []
			for i in data :
				self.data.append(i)
			if shape :
				if shape[0] == len(self.data) and shape[1] == len(self.data[0]) :
					self.shape = shape
				else :
					print("ERROR Matrix data and shape does not correspond")
					exit()
			else :
				self.shape = (len(self.data), len(self.data[0]))

	def __str__(self) :
		text = "Matrix : {} of shape {}".format(self.data, self.shape)
		return(text)

	def __repr__(self) :
		text = "Matrix({})".format(self.data)
		return(text)

	def __add__(self) :
		pass

	def __radd__(self) :
		pass

	def __sub__(self) :
		pass

	def __rsub__(self) :
		pass

	def __truediv__(self, other) :
		if isinstance(other, int) :
			temp = Matrix((self.shape[0], self.shape[1]))
			for i in range(0, self.shape[0], 1) :
				for j in range(0, self.shape[1]) :
					temp.data[i][j] = self.data[i][j] / other
			return(temp)
		else :
			print("ERROR can only divide by scalars")

	def __rtruediv__ (self) :
		pass

	def __mul__(self, other) :
		if isinstance(other, Vector) :
			if other.size == self.shape[1] :
				temp = Matrix((self.shape[0], 1))
				for i in range(0, self.shape[0], 1) :
					for j in range(0, self.shape[1], 1) :
						temp.data[i][0] += self.data[i][j] * other.values[j]
			else :
				print("ERROR Matrix and Vector are not the same n size M:{}/V:[]".format(self.shape[1], other.size))
		elif isinstance(other, Matrix) :
			if self.shape[1] == other.shape[0] :
				temp = Matrix((self.shape[0], other.shape[1]))
				for i in range(0, temp.shape[0], 1) :
					for j in range(0, temp.shape[1], 1) :
						for k in range(0, self.shape[1]) :
							temp.data[i][j] += self.data[i][k] * other.data[k][j]
			else :
				print("ERROR Matrix are not the same n size M1:{}/M2:{}".format(self.shape[1], other.shape[0]))
				exit()
		else :
			temp = Matrix((self.shape[0], self.shape[1]))
			for i in range (0, self.shape[0], 1) :
				temp.data[i][0] += self.data[i][0] * other
		return (temp)

	def __rmul__(self) :
		pass
