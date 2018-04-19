from sklearn.externals import joblib

def save(model, filename="model.pkl"):
	joblib.dump(model, filename)

def load(filename):
	return joblib.load(filename) 