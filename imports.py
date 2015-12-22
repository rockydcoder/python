dict = {}
f = open('imports.txt', 'r')
for line in f:
	array = line.split(" ")
	if array[2].strip() != "TEXAS":
		continue
	elif dict.has_key(array[0]):
		dict[array[0]] += float(array[1])
	else:
		dict[array[0]] = float(array[1])

for item in dict:
	print (item, dict[item])

