import os
os.remove("TestFile.txt")

f = open("/home/TestFile.txt", "x")
f.write("Text")