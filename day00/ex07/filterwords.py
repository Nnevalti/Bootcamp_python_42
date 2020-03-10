import sys

argv = sys.argv

if len(argv) != 3 :
	print("ERROR")
elif argv[1].isdigit() or not argv[2].isdigit():
	print("ERROR")
else :
	n = int(argv[2])
	str = argv[1].split()
	result = []
	for i in str :
		if (len(i) > n) :
			result.append(i)
	print (result)
