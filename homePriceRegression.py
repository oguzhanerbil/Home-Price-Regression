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
# EŞYA DURUMUNDA 7398 veri nan
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
def bina_yas_format(yas):
   if str(yas) == "0 (Yeni)":
      return 0
   if str(yas) == "1":
      return 1
   if str(yas) == "11-15":
      return 13
   if str(yas) == "16-20":
      return 18
   if str(yas) == "21 Ve Üzeri":
      return 25
   if str(yas) == "3":
      return 3
   if str(yas) == "4":
      return 4
   if str(yas) == "5-10":
      return 7
data = pd.read_csv("TopluVeriler.csv")




isitma_tipi = data["Isıtma Tipi"]
isitma_tipi = isitma_tipi.astype(str)
bina_yas = data["Binanın Yaşı"].values
fiyat = data["Fiyat"].values
metrekare = data["Net Metrekare"].values
bulundugu_kat = data["Bulunduğu Kat"].values
oda_sayisi = data["Oda Sayısı"].values

bina_yas = [bina_yas_format(yas) for yas in bina_yas]
fiyat_veri = [fiyat_format(s) for s in fiyat]
metrekare = [metinden_sayi_cikarma(metin) for metin in metrekare]
kacinci_kat = [metinden_kat_cikarma(kat) for kat in bulundugu_kat]
oda_sayisi = [oda_sayisi_format(oda) for oda in oda_sayisi]
isitma_tipi = [s.strip() for s in isitma_tipi]

bina_yas = np.array(bina_yas)
fiyat = np.array(fiyat_veri)
metrekare = np.array(metrekare)
kacinci_kat = np.array(kacinci_kat)
oda_sayisi = np.array(oda_sayisi)
sehir = np.array(data["Şehir"].values)
tur = np.array(data["Türü"].values)
isitma_tipi = np.array(isitma_tipi)

data = {"fiyat":fiyat,"sehir":sehir,"metrekare":metrekare,"Bulunduğu Kat": kacinci_kat,"Oda Sayısı":oda_sayisi,"Tür":tur,"Isıtma Tipi":isitma_tipi,"Bina Yaş":bina_yas}# 
data = pd.DataFrame(data)

data.to_csv("CleanData.csv")
