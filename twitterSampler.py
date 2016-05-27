#import
from __future__ import print_function
from TwitterAPI import TwitterAPI
import urllib
import time

#intro
print ("Hello World, loading twitter...")
print ("Start load")

#OAuth info
key = "kOSXIqNC8z1eq4qtWUD9IlgGD"
sec = "mY52CWu7kURl7tnhooWCa3Z0yd1njH97ryRWFJXArQsGQhm6d1"
tok = "1056983022-mQ1rXwO80m0t8NaioITuilZg6BFnWs4bdYazPtK"
toksec = "U8A0zKhWNzCWO75TDtPpcZdO2CzH8q8eJ8B5L5wpmqnMb"

#start API stream
api = TwitterAPI(key,sec,tok,toksec)
responce = api.request('statuses/sample')

#initial states
check = "Nope"
toprint = "Nope"
name = "name"
screenName = "scrnm"
tweet = "chirp"
count = 1
flag = 0
#open file
f = open('birdfood.txt','a')

#tweet info loop nest
for item in responce:
    if flag == 1:
        print("End of new tweets")
        break
    for sec in item:
        if time.clock() > 5:
            flag = 1
            break
        #remove emoji
        tweet = str(item[sec])
        tweet = tweet.encode("ascii",errors='ignore')
        #find tweet text
        if "text" in sec:
            tweet = str(tweet)
            tweet = tweet[2:]
            tweet = tweet[:-1]
            #remove newlines
            while "\\n" in tweet:
                line = tweet.index("\\n")
                tweet = tweet[:-(len(tweet)-line)]+"\n"+tweet[line+2:]
            #if not already printed
            if check not in tweet:
                f.write(tweet+"\n")
                print("tweet "+str(count)+" complete")
                count = count + 1
                f.flush()
                check = tweet
