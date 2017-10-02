a = open('Crime.csv')

def assault(f):
	for i in f:
		print(i.strip())
		crime_count = 0
		if i.strip() == "assault":
			crime_count+=1
		else:
			return crime_count

	print('crime count is',crime_count)

assault(a)
	
	





