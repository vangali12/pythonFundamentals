def draw_stars(nums):
	for i in nums:
		print("*" * i)

# draw_stars([4, 7, 2, 8, 4])

def draw_stars_first(num):
	for i in num:
		if (type(i) is int):
			print("*" * i)
		else:
			print((i[0]).lower() * len(i))

draw_stars_first([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])