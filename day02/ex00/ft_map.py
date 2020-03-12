def ft_map(function_to_apply, list_of_inputs) :
	result = []
	for i in list_of_inputs :
		result.append(function_to_apply(i))
	return(result)

def square(n) :
	return n*n

numbers = (1, 2, 3, 4, 5)
print(ft_map(square, numbers))
print(list(map(square, numbers)))
print("With lambda :")
print(ft_map(lambda x : x*x, numbers))
print(list(map(lambda x: x*x, numbers)))
