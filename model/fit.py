import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()

from sklearn import tree
iris_df = (pd.read_excel("lessons.xlsx"))
iris_df['Название предмета'] = labelencoder.fit_transform(iris_df['Название предмета'])
X = iris_df.drop(["Метка"], axis=1)
Y = iris_df["Метка"]
labelencoder = LabelEncoder()


X_train1, X_test1, Y_train1, Y_test1 = train_test_split(X, Y, test_size=0.3, random_state=3)
model =  DecisionTreeClassifier()
model.fit(X_train1, Y_train1)
with open('tree', 'wb') as pkl:
    pickle.dump(model, pkl)
