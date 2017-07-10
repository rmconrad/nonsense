import sys

with open(sys.argv[1], 'r') as f:
	list = []
	for l in f:
		if len(l) > 313 and l[312:313] == "D":
			list.append(l[312:313])
	print filter(None, list)
	print len(list)
