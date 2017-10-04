from random import randint


def scoresGrades(end):
	for i in range (0, end):
		num = randint(60, 100)
		if (num < 70):
			print("Score: " + str(num) + "; Your grade is D")
		elif (num < 80 and num >= 70):
			print("Score: " + str(num) + "; Your grade is C")
		elif (num < 90 and num >= 80):
			print("Score: " + str(num) + "; Your grade is B")
		else:
			print("Score: " + str(num) + "; Your grade is A")
	print("End of the program. Bye!")

scoresGrades(10)