import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

def evaluation(X, y):

	# Secure that all Inputvariables are floats
	X = X.astype('float32')

	# Encode the Target Variable
	y = LabelEncoder().fit_transform(y.astype('str'))

	# Define and configure the model
	model = KNeighborsClassifier()

	# Evaluate the model
	cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
	n_scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')

	# Report model performance
	print('Accuracy: %.3f (%.3f)' % (np.mean(n_scores), np.std(n_scores)))