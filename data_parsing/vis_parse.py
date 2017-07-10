import sys

with open(sys.argv[1], 'r') as f:
	list = []
	for l in f:
		if len(l) > 364 and l[363:365] == "VV":
			list.append(l[363:365])
	print filter(None, list)
	print len(list)
