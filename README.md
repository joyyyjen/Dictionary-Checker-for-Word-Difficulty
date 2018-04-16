# dictionary_check

This program read a set of dictionariesin the same directory and outputs level of given words. It's a python program. (Idealy python3)

using library sys, codece, collection, pickle, and re

The dictionary is formatted into python dict, given csv file. There are two sets of dictionaries, one is from 師大8000, and another one is from HSK.


###1. How to run?
If you are using Mac, open Terminal. Run ./checker.py

### 2. Double check the python path in your environment
mine is in /usr/local/bin/python3
After executed, if you received this error: "No such file or directory"
try changing the first line #!/usr/local/bin/python3 to #!/usr/bin/python3

### 3. How to change the input file?
- If you want to test the level on different file (the defalut file is TVJT stimuli), 
find #---Get Data---MANUAL RENAME--# paragraph, change the file name in "with open"to your desired one.
- If you want to change the column, chaneg xxx from row['xxx'] to your desired one. 
