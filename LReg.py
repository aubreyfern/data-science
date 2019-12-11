import math

NUM_ATTRIBUTES = 2
TRAIN_DATA_FILE = "reg_train.csv"


#read the train file and return the data as two lists (ind and dep variables)
def readData(fname):
	data = []
	x = []
	y = []
	f = open(fname,"r")
	for i in f:
		instance = i.split(",")
		x.append(float(instance[0].strip()))
		y.append(float(instance[1].strip()))

	f.close()
	data.append(x)
	data.append(y)
	return data

def printParams(params):
	print("The value of B0 (intercept) is: ", params[0])
	print("The value of B1 (slope) is: ", params[1])

#The linear regression algorithm. Takes a list of lists as input
def lreg(ind_variable,dep_variable):
	params = []
	B0 = 0.0
	B1 = 0.0
	x_sum =0
	x_counter=0

	y_sum=0
	y_counter=0
    #estimate the linear regression parameters (B0 and B1) here
	for i in ind_variable:
		x_sum+=float(ind_variable[i])
		x_counter+=1

	for i in dep_variable:
		y_sum+=float(dep_variable[i])
		y_counter+=1

	x_mean = 0.0
	y_mean = 0.0

	x_mean = x_sum/x_counter
	y_mean = y_sum/y_counter

	print('x:'x_mean)
	print('y:'y_mean)
	params.append(B0)
	params.append(B1)
	return params


#this is the main routine of the program. You should not have to modify anything here
if __name__ == "__main__":
	train_matrix = readData(TRAIN_DATA_FILE)
	parameters = lreg(train_matrix[0],train_matrix[1])
	printParams(parameters)
