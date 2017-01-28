import cPickle as pickle
import numpy as np 
from sklearn.svm import SVC
from sklearn.metrics.pairwise import chi2_kernel
from sklearn.metrics.pairwise import pairwise_kernels
import os
import sys
def classify(filename, SVMfile, resultsFolder):
	with open(filename, 'r') as f_feat:
			lines = f_feat.readlines()
	lines = map(lambda x : map(lambda x2 : float(x2), x.split(',')), lines)
	labels = map(lambda x: x[0], lines)
	lines = map(lambda x: x[1:], lines)
	svm = pickle.load(open(SVMfile, 'r'))
	results = svm.predict(lines)
	diff = sum(abs(np.array(labels) - np.array(results)))
	print (1 - float(diff)/len(labels))

	if not os.path.exists(resultsFolder):
		os.makedirs(resultsFolder)
	resfl = open(resultsFolder+"results.txt",'w')
	for i in range(len(results)):
		resfl.write("%s %d" % (labels[i], results[i]))
	return results[i]

def test(fileList, SVMfile, label, resultsFolder):
	svm = load(open(SVMfile, 'r'))

	fl = open(fileList, 'r')
	lines = fl.readlines()
	fl.close()

	alldata = np.array([])
	for fname in lines:
		data = np.loadtxt(fname.strip(),delimiter=',')
		alldata = np.concatenate((alldata, data), axis=0)

	results = svm.predict(alldata)
	
	if not os.path.exists(resultsFolder):
		os.makedirs(resultsFolder)
	resfl = open(resultsFolder+"results.txt",'w')
	for i in range(len(results)):
		resfl.write("%s %d" % (line[i], results[i]))

if __name__ == '__main__':
	if len(sys.argv) >= 4:
		classify(sys.argv[1], sys.argv[2],sys.argv[3])