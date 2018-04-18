from sklearn.linear_model import LogisticRegression

def train(x,y):
	model = LogisticRegression()
	model = model.fit(x,y)
	return model

def score(model,x,y):
	return model.score(x,y)

def predict(model, x):
	return model.predict(x)