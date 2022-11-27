import pandas as pd
from sklearn import preprocessing, linear_model
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import svm


class MachineLearningAlgorithm:

    XData = pd.read_csv('../Dataset/ProcessedData/CTD_chemicals_diseases_Processed.csv',nrows=100000)
    yData = XData['DiseaseID']
    label_encoder = preprocessing.LabelEncoder()
    yData = label_encoder.fit_transform(yData)
    XData.pop('DiseaseID')
    X_train, X_test, y_train, y_test = train_test_split(XData, yData, test_size=0.4, random_state = 42)

    def KNeighborsClassifier(self):
        print("-----------KNeighborsClassifier----------------")
        model = KNeighborsClassifier(n_neighbors=5)
        model.fit(self.X_train, self.y_train)
        y_predict = model.predict(self.X_test)
        print(self.y_test)
        print(y_predict)
        print("Accuracy Score = ", accuracy_score(self.y_test,y_predict))
        print("-----------------------------------------------")

    def GaussianNB(self):
        print("-----------GaussianNB----------------")
        model = GaussianNB()
        model.fit(self.X_train, self.y_train)
        y_predict = model.predict(self.X_test)
        print(self.y_test)
        print(y_predict)
        print("Accuracy Score = ", accuracy_score(self.y_test,y_predict))
        print("-----------------------------------------------")


    def SVC(self):
        print("-----------SVC----------------")
        model = SVC(kernel= 'linear', random_state=1, C=0.1)
        model.fit(self.X_train, self.y_train)
        y_predict = model.predict(self.X_test)
        print(self.y_test)
        print(y_predict)
        print("Accuracy Score = ", accuracy_score(self.y_test,y_predict))
        print("-----------------------------------------------")

    def SGDClassifier(self):
        print("-----------SGDClassifier----------------")
        model = SGDClassifier(loss='hinge')
        model.fit(self.X_train, self.y_train)
        y_predict = model.predict(self.X_test)
        print(self.y_test)
        print(y_predict)
        print("Accuracy Score = ", accuracy_score(self.y_test,y_predict))
        print("-----------------------------------------------")

