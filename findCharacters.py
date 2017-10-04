word_list = ['hello', 'world', 'my', 'name', 'is', 'Anna']
char = "o"


def findCharacter(words, char):
	new_list = []
	for i in range (0, len(words)):
		if char in words[i]:
			new_list.append(words[i])
	print(new_list)

findCharacter(word_list, char)