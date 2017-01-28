from sklearn import cluster
import numpy as np

def learn(trainFile, K, binary=False):
	with open(trainFile,'r') as f:
		lines = f.readlines()
	lines = filter(lambda x : x.find("NaN") == -1 and x.find('nan') == -1, lines)
	lines = map(lambda x : map(lambda x2 : float(x2), x.split(',')), lines)
	if binary:
		l0 = filter(lambda x: x[0] == 0.0, lines)
		l0 = map(lambda x: x[1:], l0)
		l1 = filter(lambda x: x[0] == 1.0, lines)
		l1 = map(lambda x: x[1:], l1)
		kmc0 = cluster.KMeans(n_clusters=1, n_jobs= -1)
		kmc0.fit(l0)
		kmc1 = cluster.KMeans(n_clusters=1, n_jobs= -1)
		kmc1.fit(l1)
		clusters = np.array([kmc0.cluster_centers_.flatten(),kmc1.cluster_centers_.flatten()])
		np.savetxt(trainFile+".2cents", clusters,delimiter=',')
	else:
		labels = map(lambda x: x[0], lines)
		lines = map(lambda x: x[1:], lines)
		# kmc = cluster.MiniBatchKMeans(n_clusters=K, batch_size = 10000, init_size=len(lines), reassignment_ratio=0.1, verbose=1)
		kmc = cluster.KMeans(n_clusters=K, n_jobs= -1)
		kmc.fit(lines)
		np.savetxt(trainFile+(".%dcents"%K), kmc.cluster_centers_, delimiter=',')
		return kmc
def quantizeFile(filename, centroid_file, transform=False):	
	with open(centroid_file,'r') as f:
		lines = f.readlines()
	lines = filter(lambda x : x.find("NaN") == -1 and x.find('nan') == -1, lines)
	cents = map(lambda x : map(lambda x2 : float(x2), x.split(',')), lines)
	cents = np.array(cents)
	K = len(cents)
	kmc = cluster.KMeans(n_clusters=K, n_jobs= -1)
	kmc.cluster_centers_ = cents
	with open(filename, 'r') as f_feat:
			lines = f_feat.readlines()
	lines = map(lambda x : map(lambda x2 : float(x2), x.split(',')), lines)
	labels = map(lambda x: x[0], lines)
	lines = map(lambda x: x[1:], lines)
	if transform:
		res = kmc.transform(lines)
		labels = np.array(map(lambda x: [x], labels))
		res = np.c_[labels,res]
		np.savetxt(filename+'.quant', res, delimiter=',')
		return filename+'.quant'
	else:
		res = kmc.predict(lines)
		labels = np.array(labels)
		np.savetxt(filename+'.results', res, delimiter=',')
		diff = (abs(res - labels))
		print 1 - float(sum(diff))/labels.shape[0]
		return res

# learn('src/min_training.txt', 32)
# quantizeFile('src/min_training.txt', 'src/min_training.txt.32cents', transform=True)
