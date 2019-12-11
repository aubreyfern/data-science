import math

NUM_ATTRIBUTES = 4
TRAIN_DATA_FILE = "sample_train.csv"
TEST_DATA_FILE = "sample_test.csv"

#read the train file and return the data matrix and the target variable to predict
def readData(fname):
	data = []
	labels = []
	f = open(fname,"r")
	for i in f:
		instance = i.split(",")
		vector = []
		for j in range(NUM_ATTRIBUTES):
			vector.append(float(instance[j]))
		data.append(vector)
		labels.append(instance[NUM_ATTRIBUTES])
	f.close()
	return [data,labels]

#compute the dot product of vectors represented as lists
def dotProduct(vecA,vecB):
	sum = 0.0
	for i in range(NUM_ATTRIBUTES):
		sum += vecA[i]*vecB[i]
	return sum

#compute the cosine similarity of 2 vectors represented as lists
def cosDistance(vecA,vecB):
	normA = math.sqrt(dotProduct(vecA,vecA))
	normB = math.sqrt(dotProduct(vecB,vecB))
	return dotProduct(vecA,vecB)/(normA*normB)

#compare predicted labels to truth labels. Identify errors and print accuracy
def printAccuracy(pred,truth):
	total = 0.0
	correct= 0.0
	for i in range(len(pred)):
		total += 1.0
		if pred[i]==truth[i]:
			correct += 1.0
		else:
			print("Predicted that test point ",i," was ",pred[i], "but it is actually ",truth[i])
	print("The accuracy is: ", 100*(correct/total), " percent")

#The KNN algorithm. Predicts the label for each test data set instance and adds to a list. Returns the list as output
def knn(train_data,train_labels,test_data):
	predictions = []
	for i nin test_data:
		c=-1
		closest_distance = -2
		for j in range(len(train_data)):
			point = train_data[j]
			cos_dist = cosDistance(i,point)
			y_train = train_data[j]
			if cos_dist > closest_distance:
				closest_distance = cos_dist
				c=j
		predictions.append(train_labels[c])
	return predictions
	#implement KNN here
	#for each test data point predict the label and add your prediction to the preditions list
	#compare to every data point in train_data using cosDistance by making a call to the above function
	#find the index, c, of the closest data point
def cleanData(train_data, train_labels):
	attrList = []

	#separate data into the different classifications
	for type in range(len(CATEGORY)):
		for col in range(NUM_ATTRIBUTES):
			attrList.append([])
			attrList[col].append([])
			for row in range(len(train_data)):
				if CATEGORY[type] == train_labels[row]:
					attrList[col][type].append(train_data[row][col])
				#elif row % 50 == 0:
				#	attrList[col][type].append(train_data[row+1][col])

	#filter out outliers (outside 3 standard dev)
	for type in range(len(CATEGORY)):
		for col in range(NUM_ATTRIBUTES):
			stdev = 0
			values = []
			for row in range(len(attrList[col][type])):
				values.append(attrList[col][type][row])
			mean = stats.mean(values)
			stdev = stats.stdev(values)
			noOutliers = []
			#exclude data point if further than 3 stdev away from mean
			for dataPoint in values:
				if dataPoint < (mean+(stdev*3)):
					noOutliers.append(dataPoint)
			trueMean = round(stats.mean(noOutliers),1)
			#replace empty values and outliers with mean
			for row in range(len(attrList[col][type])):
				if attrList[col][type][row] == 0.0 or attrList[col][type][row] >= mean+(stdev*3):
					attrList[col][type][row] = trueMean

	#condense data into single list
	vector = []
	numRows = len(attrList[0][0])
	count = 0
	for type in range(len(CATEGORY)):
		for index in range(numRows-1):
			row = []
			for col in range(NUM_ATTRIBUTES):
				row.append(attrList[col][type][index])
			vector.append(row)
			count += 1
			print("Row :", count)
			print(vector[index])
			print(train_data[index])


	return predictions


#this is the main routine of the program. You should not have to modify anything here
if __name__ == "__main__":
	train_matrix = readData(TRAIN_DATA_FILE)
	train_data = train_matrix[0]
	train_labels = train_matrix[1]
	test_matrix = readData(TEST_DATA_FILE)
	test_data = test_matrix[0]
	test_labels = test_matrix[1]
	predictions = knn(train_data,train_labels,test_data)
	printAccuracy(predictions,test_labels)
