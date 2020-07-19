#imports
from sklearn.svm import SVC
import pandas as pd

#Open CSV
train = pd.read_csv("/content/drive/My Drive/Claudia y Lidia/Competition & Projects/Titanic/train.csv")
test = pd.read_csv("/content/drive/My Drive/Claudia y Lidia/Competition & Projects/Titanic/test.csv")

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
