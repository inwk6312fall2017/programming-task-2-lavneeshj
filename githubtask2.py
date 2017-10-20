import csv
fails = 0
with open("crime.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        for item in row:
            if item == "ASSAULT":
                fails += 1
print(fails)

