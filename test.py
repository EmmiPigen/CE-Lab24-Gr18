import datetime
from os.path import expanduser

f = open(expanduser("~") + '/Desktop/TestFile.txt', 'w')
f.write("Text\n" + str(datetime.datetime.now()))
f.close()