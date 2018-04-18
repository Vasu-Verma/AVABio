from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix

def train(x,y, layers=(5,2)):
	model = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=layers, random_state=1)
	model = model.fit(x,y)
	return model

def score(model,x,y):
	return model.score(x,y)

def predict(model, x):
	return model.predict(x)

def generateConfusionMatrix(model, x, y):
	return confusion_matrix(model.predict(x),y)