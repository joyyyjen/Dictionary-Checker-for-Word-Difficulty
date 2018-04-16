#!/usr/local/bin/python3

import pickle
import csv
from sys import stdin

#---LOARDING DICTIONARIES---#

level1 = open("level1",'rb')
default_dict = pickle.load(level1)
level2 = open("level2",'rb')
default_dict2 = pickle.load(level2)
level3 = open("level3",'rb')
default_dict3 = pickle.load(level3)
level4 = open("level4",'rb')
default_dict4 = pickle.load(level4)
level5 = open("level5",'rb')
default_dict5 = pickle.load(level5)

HSK_1 = open("HSK-1",'rb')
HSK_dict1 = pickle.load(HSK_1)
HSK_2 = open("HSK-2",'rb')
HSK_dict2 = pickle.load(HSK_2)
HSK_3 = open("HSK-3",'rb')
HSK_dict3 = pickle.load(HSK_3)
HSK_4 = open("HSK-4",'rb')
HSK_dict4 = pickle.load(HSK_4)
HSK_5 = open("HSK-5",'rb')
HSK_dict5 = pickle.load(HSK_5)

#---CHECK FUNCTION FOR HSK Dictionary---#
def check(word):
    if word in HSK_dict1: print("HSK_level 1")
    elif word in HSK_dict2: print("HSK_level 2")
    elif word in HSK_dict3: print("HSK_level 3")
    elif word in HSK_dict4: print("HSK_level 4")
    elif word in HSK_dict5: print("HSK_level 5")
    else: print()

if __name__ == "__main__":
    used = []
#---Get Data---MANUAL RENAME--#
    with open("TVJT stimuli.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader: 
        # VERB is the colunmn in CSV file which name "verb" #
            if row['verb'] not in used:
                used.append(row['verb'])
            string1 = row['Num_CL']
        # REMOVE ASPECT MARKER #
            if len(string1) >= 2:
                if string1[1:] not in used:
                    used.append(string1[1:])
       # object is the column in the CSV file which name 'object' 
            if row['object'] not in used:
                used.append(row['object'])

#===Check Level===#
    for i in used:
        if i in default_dict: print(i,":level 1",end=" "); check(i) 
        elif i in default_dict2: print(i,":level 2",end = " "); check(i)
        elif i in default_dict3: print(i,":level 3",end = " "); check(i)
        elif i in default_dict4: print(i,":level 4",end = " "); check(i)
        elif i in default_dict5: print(i,":level 5",end =" "); check(i)
        else: print(i,":none")
