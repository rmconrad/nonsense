import sys

# initialize all empty lists
ba_list = []
bl_list = []
den_list = []
ltd_list = []
std_list = []
vis_list = []
vel_list = []
vea_list = []
vsl_list = []
vsa_list = []
vcl_list = []
vca_list = []

list_of_lists = [ba_list, bl_list, den_list, ltd_list, std_list, vis_list, vel_list, vea_list, vsl_list, vsa_list, vcl_list, vca_list]

# MAKE THIS WORK AGAIN USING A CLASS?

with open(sys.argv[1], 'r') as f:
    for l in f:
        # basic ADD
        if len(l) > 583 and l[582:584] == "AD":
            ba_list.append(l[582:584])
        # basic life
        if len(l) > 530 and l[529:531] == "CP":
            bl_list.append(l[529:531])
        # dental
        if len(l) > 313 and l[312:313] == "D":
            den_list.append(l[312:313])
        # long term disability
        if len(l) > 466 and l[465:467] == "LT":
            ltd_list.append(l[465:467])
        # short term disability
        if len(l) > 402 and l[401:403] == "AS":
            std_list.append(l[401:403])
        # vision
        if len(l) > 364 and l[363:365] == "VV":
            vis_list.append(l[363:365])
        # ee voluntary life
        if len(l) > 680 and l[679:681] == "OP":
            vel_list.append(l[679:681])
        # ee vol add
        if len(l) > 737 and l[736:738] == "OD":
            vea_list.append(l[736:738])
        #sp voluntary life
        if len(l) > 794 and l[793:795] == "LZ":
            vsl_list.append(l[793:795])
        #sp voluntary add
        if len(l) > 843 and l[842:844] == "AE":
            vsa_list.append(l[842:844])
        # ch voluntary life
        if len(l) > 892 and l[891:893] == "LF":
            vcl_list.append(l[891:893])
        # ch voluntary add
        if len(l) > 940 and l[939:941] == "AT":
            vca_list.append(l[939:941])


def printer(list_of_lists):
    for l in list_of_lists:
        if len(l) > 0:
            print("%s Count:\t%s" % (l[0], len(l)))

printer(list_of_lists)
