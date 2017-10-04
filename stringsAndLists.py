words = "It's thanksgiving day. It's my birthday, too!"

print(words.find("day"))
print(words.replace("day", "month"))


x = [2, 54, -2, 7, 12, 98]

def maxMin(arr):
	max = arr[0]
	min = arr[0]
	for i in range (0, len(arr)):
		if arr[i] > max:
			max = arr[i]
		if arr[i] < min:
			min = arr[i]
	print("Max: " + str(max))
	print("Min: " + str(min))

maxMin(x)

y = ["hello", 2, 54, -2, 7, 12, 98, "world"]

def firstLast(arr):
	first = arr[0]
	last = arr[len(arr)-1]
	print([first, last])

firstLast(y)

z = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]

def newList(arr):
	arr.sort()
	short = []
	for i in range (0, (len(arr)-1)/2):
		short.append(arr[i])
	newList = [short]
	for j in range ((len(arr)-1)/2, len(arr)-1):
		newList.append(arr[j])
	print(newList)

newList(z)