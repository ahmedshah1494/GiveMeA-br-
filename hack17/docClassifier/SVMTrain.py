import numpy as np 
from sklearn.svm import SVC
from sklearn.metrics.pairwise import chi2_kernel
from sklearn.metrics.pairwise import pairwise_kernels
import os
import sys
import grid
import matplotlib.pyplot as plt
import cPickle as pickle
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV


def parseSVM(filename):
	with open(filename, 'r') as f:
		lines = f.readlines()
	lines = map(lambda x: map(lambda y: y.split(':')[-1],x.split()), lines)
	lines = map(lambda x : map(float,x),lines)
	return lines

def fast_hik(x, y):
	return np.minimum(x, y).sum()

def intersectionKernel(x,y):
	return pairwise_kernels(x,y,metric=fast_hik,n_jobs=-1)

def train(filename, SVMdir, Kernel='linear'):
	with open(filename, 'r') as f_feat:
			lines = f_feat.readlines()
	lines = map(lambda x : map(lambda x2 : float(x2), x.split(',')), lines)
	labels = map(lambda x: x[0], lines)
	lines = map(lambda x: x[1:], lines)
	svm = SVC(kernel = Kernel, C=1000)
	svm.fit(lines, labels)
	pickle.dump(svm, open(SVMdir+"SVM.pkl", 'wb'))

def learn(fileList, SVMdir, Kernel="linear"):
	fl = open(fileList, 'r')
	lines = fl.readlines()
	fl.close()

	allData = []
	labels = []
	for l in lines:
		[label, fname] = l.split()
		labels.append(int(label))
		fl = open(fname,'r')
		dataStr = fl.readlines()
		fl.close()
		data = map(float, dataStr)
		alldata.append(data)

	if Kernel=="intersection":
		Kernel = intersectionKernel
		
	(best_rate,best_params) = grid.find_parameters('files/DataSets/'+filename, options='-log2c -1,2,1 -log2g 1,1,1 -t 0')
	svm = SVC(kernel = Kernel)
	svm.fit(alldata, labels)
	pickle.dump(svm, open(SVMdir+"SVM.pkl", 'wb'))

if __name__ == "__main__":
	if len(sys.argv) < 4:
		print "-arg1 inFileList -arg2 SVMdir [-arg3 kernel]"
	if len(sys.argv) == 3:
		train(sys.argv[1], sys.argv[2])
	if len(sys.argv) == 4:
		train(sys.argv[1], sys.argv[2], Kernel=sys.argv[3])