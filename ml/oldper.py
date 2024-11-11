import pandas as pd
from math import exp
from sklearn import preprocessing
from sklearn import model_selection

# Activation logic
# If activation >= 0.0 then return 1.0, else return 0.0
def predict(row):
    global weights
    activation = weights[0]  # Bias value is set so it will be further added
    for i in range(len(row)-1):
        activation += weights[i + 1] * row[i]  # Calculating summation of weights and input
    if activation >= 0.0:
        return 1.0
    else:
        return 0.0

# Applying perceptron learning rule
def train_weights(train):
    global epochs, weights, learningRate

    for epoch in range(epochs):
        sum_error = 0.0
        for row in train:
            predictionValue = predict(row)
            error = row[-1] - predictionValue  # row[-1] is the target output
            sum_error += error**2  # Error sum value

            # Updating the weights and bias
            weights[0] = weights[0] + learningRate * error  # Bias update
            for i in range(len(row)-1):
                weights[i + 1] = weights[i + 1] + learningRate * error * row[i]  # Weight update

        print('epoch number={}, learning rate={}, error (sum of squares)={}'.format(epoch, learningRate, sum_error))

# Reading the csv file
csvFile = pd.read_csv("SAHeart.csv")
x = csvFile[['obesity', 'alcohol', 'sbp', 'tobacco', 'ldl', 'adiposity']]
y = csvFile['famhist']

# Converting 'famhist' column to binary values (1 for Present, 0 for Absent)
csvFile.loc[csvFile.famhist == 'Present', 'famhist'] = 1
csvFile.loc[csvFile.famhist == 'Absent', 'famhist'] = 0

print("".center(80, "-"), "\nDataset Dimensions\nTotal numbers of rows in dataset: ", x.shape[0], 
      "\nTotal numbers of columns in dataset: ", x.shape[1] + 1, "\n", "".center(80, "-"))

# Splitting the data for training and testing
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2, shuffle=True)

# Initializing variables
epochs = 10
learningRate = 0.1
weights = [0.0] * (x_train.shape[1] + 1)  # Initialize weights with zeros (including bias)

# Train the perceptron model
train_weights(x_train.values)  # Assuming x_train is a DataFrame, we convert it to a numpy array for iteration

# Make predictions on the test set
right = 0
for row, actual in zip(x_test.values, y_test):
    predictionVal = predict(row)
    if predictionVal == actual:
        right += 1
    print("Expected={}, Predicted={}".format(actual, predictionVal))

# Print accuracy of prediction
print(f"{right} values Predicted correctly.\nAccuracy of Prediction is: {right / len(y_test):.4f}")

