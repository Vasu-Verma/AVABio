from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import chi2
from sklearn import preprocessing

def transform(x,y, percentage=20):
	min_max_scaler = preprocessing.MinMaxScaler()
	x = min_max_scaler.fit_transform(x)
	return SelectPercentile(chi2, percentage).fit_transform(x, y)