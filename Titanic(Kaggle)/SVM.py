#imports
from sklearn.svm import SVC
import pandas as pd

#Open CSV
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

#Normalize the data. Delete string(0-1) and unnecesary columns
##Train
male= pd.get_dummies(train["Sex"])
embarked= pd.get_dummies(train["Embarked"])
p_class= pd.get_dummies(train["Pclass"])
train.drop("Sex", axis = 1, inplace=True)
train.drop("Pclass", axis = 1, inplace=True)
train.drop("Embarked", axis = 1, inplace=True)
train.drop("Name", axis = 1, inplace=True)
train.drop("Ticket", axis = 1, inplace=True)
train.drop("Cabin", axis = 1, inplace=True)
train = pd.concat([train, male, embarked, p_class], axis=1)
train.drop("female", axis = 1, inplace=True)
train.drop("S", axis = 1, inplace=True)
train.drop(3, axis = 1, inplace=True)
train.dropna(inplace=True)


##Test
male= pd.get_dummies(test["Sex"])
embarked= pd.get_dummies(test["Embarked"])
p_class= pd.get_dummies(test["Pclass"])
test.drop("Sex", axis = 1, inplace=True)
test.drop("Pclass", axis = 1, inplace=True)
test.drop("Embarked", axis = 1, inplace=True)
test.drop("Name", axis = 1, inplace=True)
test.drop("Ticket", axis = 1, inplace=True)
test.drop("Cabin", axis = 1, inplace=True)
test = pd.concat([test, male, embarked, p_class], axis=1)
test.drop("female", axis = 1, inplace=True)
test.drop("S", axis = 1, inplace=True)
test.drop(3, axis = 1, inplace=True)

#test.dropna(inplace=True) -> Don't work
column_means = test.mean()
test = test.fillna(column_means)

#TRAIN. Separate X_train (no label) and Y_train (label)
X_train = train.loc[:, train.columns != "Survived"]
Y_train = train.loc[:, "Survived"].values

#TEST. X_test (all the columns)
X_test = test

#Scaler X_train and X_test
from sklearn.preprocessing import MinMaxScaler
scaling = MinMaxScaler(feature_range=(0,1)).fit(X_train)
X_train = scaling.transform(X_train)
X_test = scaling.transform(X_test)

#Crearte and fit the model
svm = SVC(kernel='poly', C=1, random_state=1)
svm.fit(X_train, Y_train)

y_pred = svm.predict(X_test)

output = pd.DataFrame({'PassengerId': test["PassengerId"], 'Survived': y_pred})
output.to_csv('submission.csv', index=False)

