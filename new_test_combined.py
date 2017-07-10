import sys


# # To be added:
# 1179//Employee Critical Illness Attained Age//"GE = EE paid attained age//EC = ER paid attained age"
# 1218	Dependent Critical Illness Attained Age	2	alpha	"GD = EE paid attained age
# DC = ER paid attained age"
# 1257	Employee Critical Illness Level Funded 	2	alpha	"DE = EE paid level funded
# HE = ER paid level funded"
# 1301	Dependent Critical Illness Level Funded	2	alpha	"DD = EE paid level funded
# HD = ER paid level funded"
# 1345	MetDefender	2	alpha	DF= Defender
# 1381	Employee Critical Illness Cancer	2	alpha	"RE = EE paid
# KE = ER paid"
# 1417	Dependent Critical Illness Cancer	2	alpha	"RD = EE paid
# KD = ER paid"


# initialize all empty lists
ba_list = ["Basic ADD"]
bl_list = ["Basic Life"]
den_list = ["Dental"]
ltd_list = ["LTD"]
std_list = ["STD"]
vis_list = ["Vision"]
vel_list = ["EE Vol Life"]
vea_list = ["EE Vol ADD"]
vsl_list = ["SP Vol Life"]
vsa_list = ["SP Vol ADD"]
vcl_list = ["CH Vol Life"]
vca_list = ["CH Vol ADD"]
pet_list = ["Pet"]
legal_list = ["Hyatt Legal"]
ee_accident = ["EE Accident"]
er_accident = ["ER Accident"]
ee_hospital = ["EE Hospital"]
er_hospital = ["ER Hospital"]


list_of_lists = [ba_list, bl_list, den_list, ltd_list, std_list, vis_list, vel_list, vea_list, vsl_list, vsa_list, vcl_list, vca_list, pet_list, legal_list, ee_accident, er_accident, ee_hospital, er_hospital]

# - MAKE THIS WORK AGAIN USING A CLASS?
# - Instead of using len(given_list) can i just increment values for each one?
#       ^ that might make it more difficult to name them as clearly as I have.  # Look at # counts.py for reference
# - Add starting pos and code as element in intitial list. use printer to feed  # in and then add/subtract on each iteration to find full number

file = with open(sys.argv[1], 'r')

def counter(file):
    for l in file:
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
        # pet
        if len(l) > 1032 and l[1031:1033] == "VP":
            pet_list.append(l[1031:1033])
        # hyatt legal
        if len(l) > 1068 and l[1067:1069] == "LE":
            legal_list.append(l[1067:1069])
        # ee paid accident
        if len(l) > 1104 and l[1103:1105] == "AH":
            ee_accident.append(l[1103:1105])
        # er paid accident
        if len(l) > 1104 and l[1103:1105] == "AI":
            er_accident.append(l[1103:1105])
        # ee paid hospital indemnity
        if len(l) > 1140 and l[1139:1141] == "HH":
            ee_hospital.append(l[1139:1141])
        # er paid hospital indemnity
        if len(l) > 1140 and l[1139:1141] == "HI":
            er_hospital.append(l[1139:1141])


def printer(list_of_lists):
    for l in list_of_lists:
        if len(l) > 1:
            print("%s Count:\t%s" % (l[0], len(l) - 1))

printer(list_of_lists)
