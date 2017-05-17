import os
import glob


#fromdir = "~/"
todir="/home/haei/Music"
#os.chdir(fromdir)
files = glob.glob("*")
os.chdir(todir)
for f in files:
  if f =="output.wav":
   print "!!!"
  print "file name ["+f+"]"
