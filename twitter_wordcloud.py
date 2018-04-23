
import twitter

import json

import sys
#sys.stdout = open("searchfile22.csv", "w")
#print ("searchtext" sys.stdout)

import numpy as np # linear algebra
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt
# %matplotlib inline

from subprocess import check_output
from wordcloud import WordCloud, STOPWORDS


api = twitter.Api(consumer_key="HdNFQ0YH52wyrwtUYiwalIp3b",
consumer_secret="dC6Uc13Xhrtsel92uBlD3r6QyEkWq8oCFR6psW8rCsURR4YQaY",
access_token_key="46344285-UOV7LAxBlelMHA59eYH1wteT4FssMjoBQJJIq1UPU",
access_token_secret="FXSMZSOZameYmsfbP2Gac2COGPPF8ZDJWoWyQniLxVQxz")

searchlist=api.GetSearch(term="run",  since='2017-07-01', geocode="1.350512,103.8722258,100mi",count=50)


#print([s.text for s in searchlist])
for s in searchlist:
	searchtext = s.text
	print (searchtext)
#	print (searchtext, file= sys.stdout)	


#mpl.rcParams['figure.figsize']=(8.0,6.0)    #(6.0,4.0)
mpl.rcParams['font.size']=12                #10 
mpl.rcParams['savefig.dpi']=100             #72 
mpl.rcParams['figure.subplot.bottom']=.1 


stopwords = set(STOPWORDS)

#data = pd.read_csv("searchfile.csv")
data=searchtext

wordcloud = WordCloud(
                          background_color='green',
                          stopwords=stopwords,
                          max_words=200,
                          max_font_size=40, 
                          random_state=42
                         ).generate(str(data))


print(wordcloud)
fig = plt.figure(1)
fig.savefig("word2.png", dpi=900)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

fig.savefig("word2.png", dpi=900)
