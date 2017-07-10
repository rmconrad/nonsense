import sys

with open(sys.argv[1], 'r') as f:
	list = []
	for l in f:
		if len(l) > 530 and l[529:531] == "CP":
			list.append(l[529:531])
	print filter(None, list)
	print len(list)
