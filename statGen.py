#import
import operator
from pprint import pprint
import time

print("Starting metric")

#create names
dic = {'name': 0}
f = open('birdfood.txt','r')
#parse loop
while 1:
    line = f.read()
    if len(line) > 0:
        #split, count, add to dict
        tok = line.strip().split(' ')
        for num in tok:
            if num is not "":
                try:
                    dic[num] = dic[num] +1
                except:
                    dic[num] = 1
    #break at end
    if line == "":
        break
#sort by decending appearances
sortedDic = sorted(dic.items(),key=operator.itemgetter(1))
sortedDic.reverse()
f.close()

#write data to file
fileName = time.strftime("%d-%m-%Y")
fileName = fileName + " stats.txt"
f = open(fileName,'w')
for item in sortedDic:
    f.write(str(item)+"\n")
f.close()
print("Metric complete")
