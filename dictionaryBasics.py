
me = {"name": "Alisa", "age": "23", "country of birth": "Japan", "favorite language": "Python"}

def printDictionary(dictionary):
	for key in dictionary:
		print("My " + key + " is " + dictionary[key])

printDictionary(me)