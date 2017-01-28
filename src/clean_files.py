import os
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups
import numpy as np
import sys
import json

def enter_to_space(s):
	if s == '\n':
		return ' '
	else:
		return s


stops = stopwords.words('english');

files_to_clean = os.listdir('./pages');
files_to_clean = filter(lambda x: '.txt' in x, files_to_clean);

res = []
for file in files_to_clean:
	with open('./pages/%s' % (file)) as f:
		raw = list(f.read().lower());
	raw = map(enter_to_space, raw);
	raw = filter(lambda x: (ord(x) < 58 and ord(x) > 47) or (ord(x) >= 97 and ord(x) <= 122) or ord(x) == 32, raw);
	raw = ''.join(raw);
	raw = ' '.join(filter(lambda x: x not in stops, raw.split()));
	res.append(raw);


newsgroups_train = fetch_20newsgroups(subset='train')
np.random.shuffle(newsgroups_train.data);

for name in newsgroups_train.data[:698]:
	raw = list(name.lower());
	raw = map(enter_to_space, raw);
	raw = filter(lambda x: (ord(x) < 58 and ord(x) > 47) or (ord(x) >= 97 and ord(x) <= 122) or ord(x) == 32, raw);
	raw = ''.join(raw);
	raw = ' '.join(filter(lambda x: x not in stops, raw.split()));
	res.append(raw);





v = TfidfVectorizer('content');
r = v.fit_transform(res);
# with open('vocab.txt', "w") as f:
# 	f.write(json.dumps(v.vocabulary_));
# sys.exit()

# print r
answer = r.toarray()
new_array_1 = np.array(map(lambda _: [1], range(answer.shape[0] / 2)));
new_array_2 = np.array(map(lambda _: [0], range(answer.shape[0] / 2)));
new_array = np.r_[new_array_1, new_array_2]


# print answer[:10]
# print new_array.shape;
# answer = np.insert(answer, 0, new_array, axis = 1);



answer = np.c_[new_array, answer]

top = answer[:141];
bot = answer[-141:];

answer = answer[141:-142];
test = np.r_[top, bot];
print top.shape, bot.shape, answer.shape
np.savetxt('min_test.txt',test,delimiter=',',fmt='%s')
np.savetxt('min_training.txt',answer,delimiter=',',fmt='%s')
print test.shape
# print test[0]
# print len(test[0]), len(test[1])
# print top[:10], bot[:10]
# np.savetxt('YES_VALS.txt', answer, delimiter = ',')
# with open('min_test.txt', "w") as f:
# 	test = np.r_[top, bot];
# 	for row in test:
# 		new_row = map(lambda x: '' if x == 0 else x, row);
# 		print len(new_row)
# 		new_row = reduce(lambda x, y: str(x) + ',' + str(y), new_row);
# 		print new_row.count(',')
# 		# f.write("%s\n" % new_row);
# 		break

# with open('min_training.txt', "w") as f:
# 	for row in answer:
# 		new_row = map(lambda x: '' if x == 0 else x, row);
# 		print len(new_row)
# 		new_row = reduce(lambda x, y: str(x) + ',' + str(y), new_row);
# 		print new_row.count(',')
		# f.write("%s\n" % new_row);
# np.savetxt('training.txt', answer, delimiter = ',')
# np.savetxt('test.txt', test, delimiter = ',')

