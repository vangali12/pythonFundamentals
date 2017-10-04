name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def makingDictionary(arr1, arr2):
	new_dictionary = {}
	for i in range (0, len(arr1)):
		new_dictionary[arr1[i]] = arr2[i]
	print(new_dictionary)

makingDictionary(name, favorite_animal)