#!/usr/local/bin/python3

import pickle
import csv

if __name__ == "__main__":
    dict1 = []
    with open("HSK-1.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            chara = row['word'].strip(" ") 
            if chara not in dict1:
                dict1.append(chara)
            
    print(dict1)
    data1 = open("HSK-1",'wb')
    pickle.dump(dict1,data1)
    data1.close()
    
    dict2 = []
    with open("HSK-2.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            chara = row['word'].strip(" ")
            if chara not in dict1 and chara not in dict2:
                dict2.append(chara)

    print(dict2)
    data2 = open("HSK-2",'wb')
    pickle.dump(dict2,data2)
    data2.close()
    HSK_3 = open("HSK-3",'rb')
    dict3 = pickle.load(HSK_3)
    dict4 = []
    with open("HSK-4.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            chara = row['word'].strip(" ")
            if chara not in dict1 and chara not in dict2 and chara not in dict3 and chara not in dict4:
                dict4.append(chara)

    print(dict4)
    data4 = open("HSK-4",'wb')
    pickle.dump(dict4,data4)
    data4.close()

    dict5 = []
    with open("HSK-5.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            chara = row['word'].strip(" ")
            if chara not in dict1 and chara not in dict2 and chara not in dict3 and chara not in dict4 and chara not in dict5:
                dict5.append(chara)

    print(dict5)
    data5 = open("HSK-5",'wb')
    pickle.dump(dict5,data5)
    data5.close()
