import sys

inFile = open(sys.argv[1],'r')

libs = inFile.next().strip().split()[1:]
tids = []

vectors = {}
for lib in libs:
	vectors[lib] = []

for line in inFile:
	data = line.strip().split()
	vals = data[1:]
	tids.append(data[0])

	for i in range(len(libs)):
		vectors[libs[i]].append((data[0], float(vals[i])))

ranks = {}
for lib in libs:
	ranks[lib] = {}

for i in range(len(libs)):
	rank = vectors[libs[i]]
	rank.sort(key = lambda x : x[1])
	a = 1
	for b in range(len(rank)):
		if b > 0:
			if rank[b] == rank[b-1]:
				a -= 1
		ranks[libs[i]][rank[b][0]] = a
		a += 1

print 'id\t' + "\t".join(libs)
for tid in tids:
	out = [tid]
	for lib in libs:
		out.append(str(ranks[lib][tid]))

	print '\t'.join(out)