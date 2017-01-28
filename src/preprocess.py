from nltk.corpus import stopwords
import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import re

def striphtml(data):
    p = re.compile(r"<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[\^'\">\s]+))?)+\s*|\s*)\/?>")
    return p.sub('', data)

def enter_to_space(s):
	if s == '\n':
		return ' '
	else:
		return s

stops = stopwords.words('english');

files_to_clean = os.listdir('../articles_for_processing/');
files_to_clean = filter(lambda x: '.txt' in x, files_to_clean);
res = []
with open('vocab.txt') as f:
	vocabulary = json.loads(f.read());
# truth_vector = []
for file in files_to_clean:
	with open('../articles_for_processing/%s' % (file)) as f:
		raw = list(striphtml(f.read()).lower());
	raw = map(enter_to_space, raw);
	raw = filter(lambda x: (ord(x) < 58 and ord(x) > 47) or (ord(x) >= 97 and ord(x) <= 122) or ord(x) == 32, raw);
	raw = ''.join(raw);
	raw = ' '.join(filter(lambda x: x not in stops, raw.split()));
	if 'irfile' in file:
		truth_val = [0]
	else:
		truth_val = [1]

	v = TfidfVectorizer('content', vocabulary = vocabulary);
	r = v.fit_transform([raw]);
	answer = np.c_[np.array(truth_val), r.toarray()];
	np.savetxt('../articles_for_processing/%s_VEC.txt' % (file),answer,delimiter=',',fmt='%s')

	# res.append(raw);

	# if 'irfile' in file:
	# 	truth_vector.append([0]);
	# else:
	# 	truth_vector.append(([1]));


# print res[0];
# with open('vocab.txt') as f:
# 	vocabulary = json.loads(f.read());

# v = TfidfVectorizer('content', vocabulary = vocabulary);
# r = v.fit_transform(res);
# truth_vector = np.array(truth_vector);

# print r.shape, truth_vector.shape

# answer = np.c_[truth_vector, r.toarray()];

# print answer;