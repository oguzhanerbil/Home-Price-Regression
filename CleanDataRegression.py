import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split,GridSearchCV,cross_val_score
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv("CleanData.csv")
# Sütunların bilgilerini verir
# print(data.info())
# Sütunlardaki verilerin min maks değerleri, ortalamaları gibi veriler
# print(data.describe().T)
# İlk 5 veriyi getirmek için, n parametresi ile kaç tane istiyorsan o kadar veri getirtebilirsin.
# print(data.head())
# Sondan veri getirmek için
# print(data.tail())
# Hangi veriden kaç adet bulunduğunu gösterir.
# print(data["sehir"].value_counts())
data["sehir"].value_counts().plot.barh()
data["Bulunduğu Kat"].value_counts().plot.barh()
data["Oda Sayısı"].value_counts().plot.barh()
fig = plt.figure(figsize=(5,15))
data["Bina Yaş"].value_counts().plot(kind="pie")
plt.ylabel("Yaş")
data.drop(labels="Tür", inplace=True,axis=1)


fiyat = data["fiyat"].values
sehir = data["sehir"].values
metrekare = data["metrekare"].values
bulundugu_kat = data["Bulunduğu Kat"].values
oda_sayisi = data["Oda Sayısı"].values
# plt.show()

# Etiketleme için sklearn kütüphanesi içerisinden LabelEncoder kullanacağız

from sklearn.preprocessing import LabelEncoder,OneHotEncoder


le = LabelEncoder()
ohe = OneHotEncoder()

newData = data.copy()
newData["sehir"] = le.fit_transform(data["sehir"])
newData["Isıtma Tipi"] = le.fit_transform(data["Isıtma Tipi"])

newData.drop("Unnamed: 0",axis=1,inplace=True)

X = newData.drop(["fiyat","sehir"],axis=1).head(200)
y = newData["fiyat"].head(200)
print(type(X))

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=144)
r_dt = DecisionTreeRegressor(random_state=0)
r_dt.fit(X_train,y_train)
print(r_dt.predict(X_test)[15:20])
print(y_test[15:20])

print("Modelin skoru: "+str(r_dt.score(X_test,y_test)))