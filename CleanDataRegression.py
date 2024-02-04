import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

data = pd.read_csv("CleanData.csv")
fiyat = data["fiyat"].values
sehir = data["sehir"].values
metrekare = data["metrekare"].values
bulundugu_kat = data["Bulunduğu Kat"].values
oda_sayisi = data["Oda Sayısı"].values

print(data["sehir"].value_counts())