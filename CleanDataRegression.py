import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv("DataSon.csv")

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
# data["sehir"].value_counts().plot.barh()
# data["Bulunduğu Kat"].value_counts().plot.barh()
# data["Oda Sayısı"].value_counts().plot.barh()
# fig = plt.figure(figsize=(5,15))
# data["Bina Yaş"].value_counts().plot(kind="pie")
# plt.ylabel("Yaş")


# Etiketleme için sklearn kütüphanesi içerisinden LabelEncoder kullanacağız
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

le = LabelEncoder()
ohe = OneHotEncoder()

newData = data.copy()
newData["sehir"] = le.fit_transform(newData["sehir"])
newData["Bulunduğu Kat"] = le.fit_transform(newData["Bulunduğu Kat"])
newData["Bina Yaş"] = le.fit_transform(newData["Bina Yaş"])
newData["Isıtma Tipi"] = le.fit_transform(newData["Isıtma Tipi"])

sehir = ohe.fit_transform(newData["sehir"].values.reshape(-1,1)).toarray()
sonuc = pd.DataFrame(data=sehir,index=range(len(sehir)),columns=["antalya","bursa","canakkale","denizli","eskisehir","gaziantep","kirklareli","kocaeli"])


newData.drop("Unnamed: 0",axis=1,inplace=True)
newData.drop("sehir",axis=1,inplace=True)
sonuc.drop("antalya",axis=1,inplace=True)
newData = pd.concat([newData,sonuc],axis=1)

X = newData.iloc[:,1:]
y = newData["fiyat"]

r_dt = DecisionTreeRegressor(random_state=1)
r_dt.fit(X,y)

# print(r_dt.predict(X))
# print(newData.value_counts())
print("Modelin skoru: "+str(r_dt.score(X,y)))

from sklearn.metrics import mean_squared_error
from math import sqrt

import statsmodels.api as sm
model = sm.OLS(y,X).fit()
print(model.summary())