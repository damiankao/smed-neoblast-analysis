import sys

inFile = open(sys.argv[1],'r')
print inFile.next().strip()

for line in inFile:
	data = line.strip().split()
	vals = [float(x) for x in data[1:]]

	check = False
	for val in vals:
		if val > 10:
			check = True

	if check:
		print line.strip()
