import sys

with open(sys.argv[1], 'r') as f:
	list_of_lts = []
	for l in f:
		if len(l) > 920 and l[919:921] == '01':
			list_of_lts.append(l[919:921])
	print filter(None, list_of_lts)
	print len(list_of_lts)