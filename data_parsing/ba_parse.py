import sys

with open(sys.argv[1], 'r') as f:
	list = []
	for l in f:
		if len(l) > 583 and l[582:584] == "AD":
		# if len(l) > 313:
			list.append(l[582:584])
	print filter(None, list)
	print len(list)
