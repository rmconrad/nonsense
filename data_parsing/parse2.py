import sys
 
with open(sys.argv[1], 'r') as f:
    list_of_lts = []
    pos = 0
    list_pos = []
    for l in f:
    	#print l.replace("\n\t\r ","").replace(" ","").strip()
    	pos = l.find("TXDJ0273")
    	if pos > -1:
    		list_pos.append(pos)
        if len(l) > 800:
            list_of_lts.append(l[800:929])
    print list_pos
    print list_of_lts.count("TXDJ0273")
    print list_of_lts.count("TXDJ0156")
    print list_of_lts.count("TXDJ0275")