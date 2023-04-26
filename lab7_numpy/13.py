import linecache
import random

fp = open('test.txt', 'r')
length = len(fp.readlines())
temp = random.randint(0, length - 1)
line = linecache.getline('test.txt', temp)
print(line)
