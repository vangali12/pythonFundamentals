students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


def partOne(names):
	for i in names:
		name = ""
		for key in i:
			name += i[key] + " "
		print(name)

partOne(students)

def partTwo(users):
	for title in users:
		print(title)
		shelf = list(enumerate(users[title]))
		for k in range (0, len(shelf)):
			obj = (shelf[k][1])
			name = ""
			for key in obj:
				name += (obj[key] + " ").upper()


			print(str(shelf[k][0]+1) + " - " + name + " - " + str(len(name)-2)) 
			# name = ""
			# for key in j:
				# name += (j[key] + " ").upper()
			# print(str(shelf[j]) + " - " + name + " - " + str(len(name)-2))

users = {
'Students': [{'first_name':  'Michael', 'last_name' : 'Jordan'}, {'first_name' : 'John', 'last_name' : 'Rosales'}, {'first_name' : 'Mark', 'last_name' : 'Guillen'}, {'first_name' : 'KB', 'last_name' : 'Tonel'}],
'Instructors': [{'first_name' : 'Michael', 'last_name' : 'Choi'}, {'first_name' : 'Martin', 'last_name' : 'Puryear'}]
}

partTwo(users)