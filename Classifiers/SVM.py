from sklearn import svm

def train(x,y):
	model = svm.SVC()
	model = model.fit(x,y)
	return model

def score(model,x,y):
	return model.score(x,y)

def predict(model, x):
	return model.predict(x)