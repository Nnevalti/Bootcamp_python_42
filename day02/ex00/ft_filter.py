def ft_filter(function_to_apply, list_of_inputs) :
	result = []
	for i in list_of_inputs :
		if function_to_apply(i) == True :
			result.append(i)
	return(result)


alphabets = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

def filterVowels(alphabet):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if(alphabet in vowels):
        return True
    else:
        return False

filteredVowels = filter(filterVowels, alphabets)
for vowel in filteredVowels:
    print(vowel)

print ("ft_filter")
filteredVowels = ft_filter(filterVowels, alphabets)
for vowel in filteredVowels:
    print(vowel)
