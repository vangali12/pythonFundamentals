
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def makingTuples(dictionary):
	arr = []
	tup = ()
	for key in dictionary:
		tup = (key, dictionary[key])
		arr.append(tup)
	print(arr)

makingTuples(my_dict)