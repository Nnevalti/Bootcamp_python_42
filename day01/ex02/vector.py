class Vector :
	"""A class for vector"""

	size = 0
	def __init__(self, values=[]) :
		if isinstance(values, int) :
			self.values = []
			for i in range (0, values, 1) :
				self.values.append(float(i))
			self.size = len(self.values)
		elif isinstance(values, tuple) :
			self.values = []
			for i in range (values[0], values[1], 1) :
				self.values.append(float(i))
			self.size = len(self.values)
		else :
			self.values = values
			self.size = len(self.values)

	def __str__(self) :
		"""Return Vector infos"""
		text = "(Vector {} of size {})".format(self.values, self.size)
		return(text)

	def __repr__(self) :
		"""Convert to formal string for repr()"""
		text = "Vector({})".format(self.values)
		return(text)

	def __add__(self, other) :
		if isinstance(other, int) :
			return(self.__radd__(other))
		else :
			if self.size == other.size :
				temp = Vector()
				for i in range (0, self.size, 1) :
					temp.values.append(self.values[i] + other.values[i])
				return(temp)

	def __radd__(self, other) :
		temp = Vector(0)
		for i in range (0, self.size, 1) :
			temp.values.append(self.values[i] + other)
		return(temp)


	def __sub__(self, other) :
		if isinstance(other, int) :
			return(self.__rsub__(other))
		else :
			if self.size == other.size :
				temp = Vector(0)
				for i in range (0, self.size, 1) :
					temp.values.append(self.values[i] - other.values[i])
				return(temp)

	def __rsub__(self, other) :
		temp = Vector(0)
		for i in range (0, self.size, 1) :
			temp.values.append(self.values[i] - other)
		return(temp)


	def __truediv__(self, other) :
		temp = Vector(0)
		if isinstance(other, int) :
			for i in range (0, self.size, 1) :
				if other == 0 :
					temp.values.append(self.values[i])
				else :
					temp.values.append(self.values[i] / other)
			return(temp)
		else :
			for i in range (0, self.size, 1) :
				if other.values[i] == 0 :
					temp.values.append(self.values[i])
				else :
					temp.values.append(self.values[i] / other.values[i])
			return(temp)

	def __rtruediv__(self, other) :
		temp = Vector(0)
		for i in range (0, self.size, 1) :
			if self.values[i] == 0 :
				temp.values.append(self.values[i])
			else :
				temp.values.append(other / self.values[i])
		return(temp)


	def __mul__(self, other) :
		if isinstance(other, int) :
			return(self.__rmul__(other))
		else :
			if self.size == other.size :
				temp = Vector(0)
				for i in range (0, self.size, 1) :
					temp.values.append(self.values[i] * other.values[i])
				return(temp)
			else :
				print("Vectors are not the same length")

	def __rmul__(self, other) :
		temp = Vector(0)
		for i in range (0, self.size, 1) :
			temp.values.append(self.values[i] * other)
		return(temp)
