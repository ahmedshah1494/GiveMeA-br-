from nltk.corpus import stopwords
import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import re
import time
import urllib2
import csv
import requests
from bs4 import BeautifulSoup
import lxml
import lxml.etree

def retrieve(url):
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
	response = opener.open(url)
	#soup = BeautifulSoup(response, "html.parser")
	#print response.read()


	soup = BeautifulSoup(response.read(),"lxml")

	all_text = soup.find_all('p')
	return str(all_text)

def striphtml(data):
    p = re.compile(r"<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[\^'\">\s]+))?)+\s*|\s*)\/?>")
    return p.sub('', data)

def enter_to_space(s):
	if s == '\n':
		return ' '
	else:
		return s

def clean(text):
	stops = stopwords.words('english');
	raw = list(striphtml(text.lower()));
	raw = map(enter_to_space, raw);
	raw = filter(lambda x: (ord(x) < 58 and ord(x) > 47) or (ord(x) >= 97 and ord(x) <= 122) or ord(x) == 32, raw);
	raw = ''.join(raw);
	raw = ' '.join(filter(lambda x: x not in stops, raw.split()));
	return raw;

def vectorize(text):
	with open('vocab.txt') as f:
		vocabulary = json.loads(f.read());
	v = TfidfVectorizer('content', vocabulary = vocabulary);
	r = v.fit_transform([text]);
	answer = np.c_[np.array([0]), r.toarray()];
	np.savetxt('temp_VEC_%f.txt' % time.time(), answer, delimiter=',', fmt='%s')


def retrieve_and_vectorize(url):
	vectorize(clean(retrieve(url)));

retrieve_and_vectorize('https://www.nytimes.com/2017/01/27/opinion/the-trump-war-on-public-schools.html?_r=0')