import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
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
# data["sehir"].value_counts().plot.barh()
# data["Bulunduğu Kat"].value_counts().plot.barh()
# data["Oda Sayısı"].value_counts().plot.barh()
# fig = plt.figure(figsize=(5,15))
# data["Bina Yaş"].value_counts().plot(kind="pie")
# plt.ylabel("Yaş")

data.drop(labels="Tür", inplace=True,axis=1)

data.drop("Unnamed: 0",axis=1,inplace=True)

# Etiketleme için sklearn kütüphanesi içerisinden LabelEncoder kullanacağız
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
"""
newData = data.copy()
data["sehir"] = le.fit_transform(data["sehir"])
data["Isıtma Tipi"] = le.fit_transform(data["Isıtma Tipi"])

fiyat = float(input("Fiyat bilgisi giriniz: "))
metrekare = float(input("Metrekareyi giriniz: "))
kat = int(input("Bulunduğu katı giriniz: "))
oda_sayisi = int(input("Oda sayısını giriniz: "))
isitma_tipi = int(input("Isıtma tipini giriniz (0: Doğalgaz, 1: Kombi, 2: Elektrik): "))
bina_yasi = int(input("Bina yaşını giriniz: "))
sehir = int(input("Lütfen şehir giriniz: "))
# Tahmin için veriyi hazırlama

yeni_veri = pd.DataFrame({
    "fiyat": [fiyat],
    "sehir":[sehir],
    "metrekare": [metrekare],
    "Bulunduğu Kat": [kat],
    "Oda Sayısı": [oda_sayisi],
    "Isıtma Tipi": [isitma_tipi],
    "Bina Yaş": [bina_yasi]
})

# X = yeni_veri.drop(["fiyat","sehir"],axis=1).head(200)
# y = yeni_veri["fiyat"].head(200)


# r_dt = DecisionTreeRegressor(random_state=0)
# r_dt.fit(data.drop(["fiyat"],axis=1),data["fiyat"])
# print(r_dt.predict(yeni_veri.drop("fiyat",axis=1)))
# print(y_test[15:20])

# print("Modelin skoru: "+str(r_dt.score(X_test,y_test)))
"""

newData = data.copy()
newData["sehir"] = le.fit_transform(newData["sehir"])
newData["Isıtma Tipi"] = le.fit_transform(newData["Isıtma Tipi"])

X = newData.drop(["fiyat"],axis=1)
y = newData["fiyat"]

r_dt = DecisionTreeRegressor(random_state=0)
r_dt.fit(X,y)
print(r_dt.predict(X))

print("Modelin skoru: "+str(r_dt.score(X,y)))