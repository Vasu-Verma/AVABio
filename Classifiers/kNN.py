from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

def train(x,y, neighbors=5):
	model = KNeighborsClassifier(n_neighbors=neighbors)
	model = model.fit(x,y)
	return model

def score(model,x,y):
	return model.score(x,y)

def predict(model, x):
	return model.predict(x)

def generateConfusionMatrix(model, x, y):
	return confusion_matrix(model.predict(x),y)