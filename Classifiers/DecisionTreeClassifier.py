from sklearn import tree
from sklearn.metrics import confusion_matrix

def train(x,y):
	model = tree.DecisionTreeClassifier()
	model = model.fit(x,y)
	return model

def score(model,x,y):
	return model.score(x,y)

def predict(model, x):
	return model.predict(x)

def generateConfusionMatrix(model, x, y):
	return confusion_matrix(model.predict(x),y)