import sys

with open(sys.argv[1], 'r') as f:
	list = []
	for l in f:
		if len(l) > 892 and l[891:893] == "LF":
		# if len(l) > 794:
			list.append(l[891:893])
	print filter(None, list)
	print len(list)
