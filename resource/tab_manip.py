import sys

inFile = open(sys.argv[1],'r')

if len(sys.argv) == 2:
	cols = inFile.next().strip().split('\t')[1:]
	i = 1
	print
	for col in cols:
		print str(i) + ": " + col
		i += 1
	print
	sys.exit()


inFile.next()

colNames = [x.split(':')[0] for x in sys.argv[2:]]
print 'id\t' + '\t'.join(colNames)
for line in inFile:
	data = line.strip().split()
	vals = data[1:]
	out = []
	out.append(data[0])
	for colData in sys.argv[2:]:
		colData = colData.split(':')
		cols = [int(x) for x in colData[1].split(',')]

		total = 0
		for col in cols:
			total += float(vals[col - 1])

		avg = total / len(cols)

		out.append(str(avg))

	print '\t'.join(out)
