mix = ['magical unicorns', 19, 'hello', 98.98, 'world']
integers = [2, 3, 1, 7, 4, 12]
words = ['magical', 'unicorns']

def typeList(arr):
	string = ""
	sum = 0
	stringCount = 0
	numCount = 0
	for i in range(0, len(arr)):
		if type(arr[i]) is str:
			string += arr[i]
			stringCount += 1
		if type(arr[i]) is int:
			sum += arr[i]
			numCount += 1
		if type(arr[i]) is float:
			sum += arr[i]
			numCount += 1
	if stringCount == len(arr):
		print("The list you entered is of string type")
		print("Strings:", string)
	elif numCount == len(arr):
		print("The list you entered is of integer type")
		print("Sum:", sum)
	else:
		print("The list you entered is of mixed type")
		print("Strings:", string)
		print("Sum:", sum)

typeList(mix)
typeList(integers)
typeList(words)

