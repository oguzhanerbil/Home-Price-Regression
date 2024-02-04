import pandas as pd
import numpy as np
from sklearn import preprocessing
import re
# TOPLAM VERİ 20324
# Müstakil ev sayısı 154
# Yüksek Giriş sayısı 1215
# Düz Giriş (Zemin) sayısı 616
# Çatı Katı sayısı 131
# Bahçe Katı sayısı 414
def metinden_sayi_cikarma(metin):
  sayi = re.findall(r"\d+", metin)
  if sayi:
    return int(sayi[0])
  else:
    return None
def metinden_kat_cikarma(metin):
   kat = str(metin).split(".")
   if kat and kat[0].isdigit():
      return int(kat[0])
   else:
      if metin == "nan":
        return None
      elif metin == "Yüksek Giriş":
         return 1
      elif metin == "Bahçe Dublex":
         return None
      elif metin == "Müstakil":
         return None
      elif metin == "Düz Giriş (Zemin)":
         return 1
      elif metin == "Bahçe Katı":
         return None
      elif metin == "Çatı Katı":
         return None
      
      return None

def fiyat_format(s):
    return int(re.sub(r"[^0-9]","",s))

def oda_sayisi_format(oda):
    liste = str(oda).split("+")
    if liste and liste[0].isdigit() and liste[1].isdigit():
        return int(liste[0])+int(liste[1])
    else:
       return None
data = pd.read_csv("TopluVeriler.csv")

fiyat = data["Fiyat"].values
metrekare = data["Net Metrekare"].values
bulundugu_kat = data["Bulunduğu Kat"].values
oda_sayisi = data["Oda Sayısı"].values

metrekare = [metinden_sayi_cikarma(metin) for metin in metrekare]
kacinci_kat = [metinden_kat_cikarma(kat) for kat in bulundugu_kat]
fiyat_veri = [fiyat_format(s) for s in fiyat]
oda_sayisi = [oda_sayisi_format(oda) for oda in oda_sayisi]

oda_sayisi = np.array(oda_sayisi)
kacinci_kat = np.array(kacinci_kat)
sehir = np.array(data["Şehir"].values)
fiyat = np.array(fiyat_veri)
metrekare = np.array(metrekare)
tur = np.array(data["Türü"].values)

data = {"fiyat":fiyat,"sehir":sehir,"metrekare":metrekare,"Bulunduğu Kat": kacinci_kat,"Oda Sayısı":oda_sayisi,"Tür":tur}
data = pd.DataFrame(data)

data.to_csv("CleanData.csv")
print(data)