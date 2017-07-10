import sys

with open(sys.argv[1], 'r') as f:
	list = []
	for l in f:
		if len(l) > 680 and l[679:681] == "OP":
		# if len(l) > 313:
			list.append(l[679:681])
	print filter(None, list)
	print len(list)
