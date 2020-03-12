from functools import reduce

def ft_reduce(function_to_apply, list_of_inputs) :
	result = list_of_inputs[0]
	i = 1;
	while i < len(list_of_inputs) :
		result = function_to_apply(result, list_of_inputs[i])
		i += 1
	return(result)

def afficher(a, b):
    return a * b

res = reduce(afficher, range(1,10))
print("Résultat final", res)

res = ft_reduce(afficher, range(1,10))
print("Résultat final", res)
