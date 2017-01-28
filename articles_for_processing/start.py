from nytimesarticle import articleAPI
import simplejson as json
import csv
import requests
from bs4 import BeautifulSoup
import urllib2
import nltk
import lxml
import lxml.etree

api = articleAPI('5bbdbc5c0c324194aea9f13ae835bf4d')

articles = api.search( page = 0, q = 'school', 
     fq = {'headline':'attack', 'source':['Reuters','AP', 'The New York Times']}, 
     begin_date = 20141231,
     fl='web_url')

with open('data.txt', 'w') as outfile:
     json.dump(articles, outfile, sort_keys = True, indent = 4,
ensure_ascii=False)


#print articles['response']['docs'][0]['web_url']

total_items =  len(articles['response']['docs'])

articles_array = []

for i in range(0, total_items):
    articles_array.append(articles['response']['docs'][i]['web_url'])



fixed_articles_array = []

def fixed_array(arr):
    for i in range(0, total_items):
        s = arr[i].decode('ascii', 'ignore')
        fixed_articles_array.append(s)

fixed_array(articles_array)


#print articles_array
for i in range (0,len(fixed_articles_array)):
    print fixed_articles_array[i]

# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
# response = opener.open(fixed_articles_array[0]).read()
# print fixed_articles_array[0]
# soup = BeautifulSoup(response, 'html.parser')
# text = soup.find("span", {"class": "summary"}).get_text()
# print text
# response.close()


################For creating a new file#####################
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
# response = opener.open("http://www.nytimes.com/2016/06/12/world/asia/china-higher-education-for-the-poor-protests.html")
# #soup = BeautifulSoup(response, "html.parser")
# #print response.read()


# soup = BeautifulSoup(response.read(),"lxml")

# all_text = soup.find_all('p')
# new_file = open("file_china_education.txt",'w')
# new_file.write(str(all_text))
# new_file.close()
# print "Done creating new file"
################For creating a new file#####################




#print soup.find_all('p')
#'class="story-body-text story-content"'


# for i in range(0, len(fixed_articles_array)):
#     opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
#     response = opener.open(fixed_articles_array[i])
#     print response.read()
#     response.close()



#Education
#Attacks
#Sports
#Obama
#Conflict
#Humanitarian
#Technology
#
#
#