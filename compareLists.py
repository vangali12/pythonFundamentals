a = [1, 2, 5, 6, 2]
b = [1, 2, 5, 6, 5, 3]
c = [1, 2, 5, 6, 5, 16]
d = ['celery', 'carrots', 'bread', 'milk']
e = ['celery', 'carrots', 'bread', 'cream']




def compareLists(one, two):
	if len(one) != len(two):
		print("The lists are not the same")
		return
	for i in range (0, len(one)):
		if one[i] != two[i]:
			print("The lists are not the same")
			return
	print("The lists are the same")

compareLists(a, a)
compareLists(a, b)
compareLists(c, a)
compareLists(d, e)

