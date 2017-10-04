


def multiplication(top):
	topLine = "x "
	for i in range (1, top+1):
		topLine += " " + str(i)
	print topLine
	for j in range (1, top+1):
		multLine = str(j) + " "
		for k in range (1, top+1):
			multLine += " " + str(k * j)
		print(multLine)

multiplication(12)