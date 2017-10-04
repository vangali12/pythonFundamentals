import random



def coinToss(end):
	headCount = 0
	tailCount = 0
	for i in range(1, end):
		num = round(random.random())

		if (num ==0):
			headCount += 1
			print("Attempt #" + str(i) + " Throwing a coin... It's a head!... Got " + str(headCount) + " head(s) so far and " + str(tailCount) + " so far")
		else:
			tailCount += 1
			print("Attempt #" + str(i) + " Throwing a coin... It's a tail!... Got " + str(headCount) + " head(s) so far and " + str(tailCount) + " so far")

coinToss(12)


