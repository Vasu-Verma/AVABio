from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn import preprocessing

def transform(x,y, features=2):
	min_max_scaler = preprocessing.MinMaxScaler()
	x = min_max_scaler.fit_transform(x)
	return SelectKBest(chi2, features).fit_transform(x, y)