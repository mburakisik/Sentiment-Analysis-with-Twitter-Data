import pandas as pd 
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score

data = pd.read_excel("etiketlenmis.xlsx",index_col=0)


print(data.tweet)
  
vectorizer = CountVectorizer()
vectorizer.fit(data["tweet"])
vector = vectorizer.transform(data["tweet"]).toarray()

X = vector[:306,]

print(X)

etiketlenmis_veri = data.iloc[:306,:]
etiketlenmemis_veri = data.iloc[306:,:]

# Kategori
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,etiketlenmis_veri["Kategori"], test_size=0.33, random_state=42)


# Lojistik Regresyon
from sklearn.linear_model import LogisticRegression

model = LogisticRegression().fit(X_train,y_train)
y_pred = model.predict(X_test)
print("Lojistik Regresyon:\t",accuracy_score(y_test,y_pred))


# Karar Ağacı 
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier().fit(X_train,y_train)
y_pred = model.predict(X_test)
print("Karar Ağacı:\t",accuracy_score(y_test,y_pred))


# Random Forest
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier().fit(X_train,y_train)
y_pred = model.predict(X_test)
print("Ratgele Orman:\t",accuracy_score(y_test,y_pred))


# SVM
from sklearn.svm import SVC

model = SVC().fit(X_train,y_train)
y_pred = model.predict(X_test)
print("SVM:\t",accuracy_score(y_test,y_pred))


# KNN 
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier().fit(X_train,y_train)
y_pred = model.predict(X_test)
print("KNN:\t",accuracy_score(y_test,y_pred))



# Lojistik Regresyon
from sklearn.linear_model import LogisticRegression

model = LogisticRegression().fit(X_train,y_train)
data["Kategori"][306:] = model.predict(vector[306:])
data["Kategori_Olasılık"] = [max(i) for i in model.predict_proba(vector)]






#Duygu Analizi

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,etiketlenmis_veri["Duygu"], test_size=0.33, random_state=42)


# Lojistik regresyon
from sklearn.linear_model import LogisticRegression

model = LogisticRegression().fit(X_train,y_train)
y_pred = model.predict(X_test)
print("Lojistik Regresyon:\t",accuracy_score(y_test,y_pred))



# Decision Tree 
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier().fit(X_train,y_train)
y_pred = model.predict(X_test)
print("Karar Ağacı:\t",accuracy_score(y_test,y_pred))



# Random Forest
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier().fit(X_train,y_train)
y_pred = model.predict(X_test)
print("Ratgele Orman:\t",accuracy_score(y_test,y_pred))



# SVM
from sklearn.svm import SVC

model = SVC().fit(X_train,y_train)
y_pred = model.predict(X_test)
print("SVM:\t",accuracy_score(y_test,y_pred))


# KNN 
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier().fit(X_train,y_train)
y_pred = model.predict(X_test)
print("KNN:\t",accuracy_score(y_test,y_pred))





# Tahmin
from sklearn.linear_model import LogisticRegression

model = LogisticRegression().fit(X_train,y_train)
data["Duygu"][306:] = model.predict(vector[306:])
data["Duygu_Olasılık"] = [max(i) for i in model.predict_proba(vector)]

data.to_excel("sonuc.xlsx")














