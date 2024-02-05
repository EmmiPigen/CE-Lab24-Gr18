import os
os.remove("TestFile.txt")

f = open("/home/ubuntu/Desktop/TestFile.txt", "x")
f.write("Text")
f.close()