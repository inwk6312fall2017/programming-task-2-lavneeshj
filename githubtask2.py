a=open('crime.csv')

for i in a:
	r=i.strip()
	f=r.count('ASSAULT')


print(f)
