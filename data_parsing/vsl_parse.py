import sys

with open(sys.argv[1], 'r') as f:
	list = []
	for l in f:
		if len(l) > 794 and l[793:795] == "LZ":
		# if len(l) > 794:
			list.append(l[793:795])
	print filter(None, list)
	print len(list)
