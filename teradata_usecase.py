#!/usr/bin/env python3
import os
from os import path
import shutil
import fnmatch , sys
import string
from random import *
min_char = 10
max_char = 70
allchar = string.ascii_letters + string.digits

#create three directories i.e teradata_logs,new_log_dir1 and new_log_dir1
os.mkdir("teradata_logs")
os.mkdir("new_log_dir1")
os.mkdir("new_log_dir2")

# Setting the log directory below to create log file.
dr = "./teradata_logs"
name_initial = "teradata_logs_"
extension = ".log"
shebang = ""
existing = os.listdir(dr)
n = 1
while n <= 45:

#creates the file name with teradata_logs_###.log with the right zero-padding the number
	file = dr+"/"+name_initial+str(n).zfill(3)+extension
#Generates alpha numeric string ranges from 10 to 70.
    	with open(file, "wt") as out:
            out.write("".join(choice(allchar) for x in range(randint(min_char, max_char))))
            n +=1
src = "./teradata_logs"
dst = "./new_log_dir1"
dst1 = "./new_log_dir2"

# Copies all file except last 3 in new_log_dir2
def copy_last3(src,dst):
    listOfFiles = os.listdir(src)
    for f in listOfFiles[-3:]:
        shutil.copy(path.join(src, f), dst1)
copy_last3(src,dst1)

# Copies all file except last 3 in new_log_dir1
def copy_all(src,dst):
    listOfFiles = os.listdir(src)
    for f in listOfFiles[:-3]:
        shutil.copy(path.join(src, f), dst)
copy_all(src,dst)

# replaces all occurance of "a,b and c" with word teradata.
def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)
    
    return  mainString
def main ():
    replacement = "teradata"
    for dname, dirs, files in os.walk("./new_log_dir1/"):
        for fname in files:
            #print(fname)
            fpath = os.path.join(dname, fname)
            fpathnew = os.path.join(dname,"temp")
            with open(fpath) as f:
                s = f.read()
                s = replaceMultiple(s,['a', 'b', 'c'], replacement)
            f.close()
            with open(fpathnew, "w") as f1:
                f1.write(s)
            f1.close()
            os.remove(fpath)
            os.rename(fpathnew,fpath)
if __name__ == '__main__':
    main()
dr = './new_log_dir1'
for fname in os.listdir(dr):
	filepath = os.path.join(dr, fname)
count=0
with open(filepath, 'r') as fp:
        for line in fp:
        #String to search for:
            count += line.count('teradata')
        if count <= 0:
            print >> sys.stderr , "No occurance of the word teradata in new_log_dir1"
        else:
            print count