import random
def Divide_into_training_testing(x,y, training_set = 0.8):
	length = len(x)
	if len(x)!=len(y):
		print "Error: Length of X and Y datasets is different: Using lesser length"
		length = min(len(x),len(y))
	length = int(length*training_set)
	combined = list(zip(x, y))
	random.shuffle(combined)
	x[:], y[:] = zip(*combined)
	trainX = x[:length:]
	trainY = y[:length:]
	testX = x[length::]
	testY = y[length::]
	return trainX,trainY, testX, testY