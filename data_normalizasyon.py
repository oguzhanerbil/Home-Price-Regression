import pandas as pd
import numpy as np

data = pd.read_csv("data.csv")
data1 = pd.read_csv("CleanData.csv")
data2 = pd.read_csv("TopluVeriler.csv")
data3 = pd.read_csv("DataSon.csv")
data = data[~data["fiyat"].isin([3960000100,45500006,46000007,3250000000,215000010,53000004,50000009,52000005,52500005,150000025,61200002,64900004,65000003,85000004,85000013,125000016,90000090,112000015,120000013,114000004,125000014,135000011,145000012,135000090,159900014,145000041,155000013,158000011,160000011,166500090,162500010,165000011,166500090,167500090,195000015,175000010,185000011,185000035,192500010,195000013,195000024,200000013,208900028,257500090,220000010,2100000000,227000012,239500039,1400000000,259000022,500000012,265000018,419500010,410000014,270000017,270000010,370000090,365000022,275000010,285000016,360000020,300000014,350000010,300000090,111111,320000099])]
data = data[~data["Binanın Kat Sayısı"].isin([22,20,23,21,19,18,17,16,15,14,13,12,11,10,9,1,8,25,24,28,85,35,43,32,27,30])]
data = data[~data["Oda Sayısı"].isin([6,5,4,3,0])]
data = data[~data["Bulunduğu Kat"].isin([4,3])]
data = data[~data["Bina Yaş"].isin([3,2])]
data = data[~data["Isıtma Tipi"].isin(["Doğalgaz Sobalı","Merkezi Kömür","Güneş Enerjisi","Jeotermal","Isı Pompası","Şömine","Kombi Fueloil","Elektrikli Radyatör","VRV","Fancoil Ünitesi","Kombi Katı Yakıt","Merkezi Fueloil","Kombi Kömür","Kat Kaloriferi","Isıtma Yok","Merkezi (Pay Ölçer)"])]
print(data["Isıtma Tipi"].unique())
print(data["Isıtma Tipi"].value_counts())
# print(data["fiyat"].sort_values())
data.drop("Unnamed: 0",axis=1,inplace=True)
# data.drop("Isıtma Tipi.1",axis=1,inplace=True)
# data1.drop("Tür",axis=1,inplace=True)
# data = data.drop("Isıtma Tipi", axis=1)

# binanin_kat_sayisi = data2["Binanın Kat Sayısı"]
# binanin_kat_sayisi = binanin_kat_sayisi.astype(str)
# binanin_kat_sayisi = [s.strip() for s in binanin_kat_sayisi]
# binanin_kat_sayisi = np.array(binanin_kat_sayisi)
# binanin_kat_sayisi = pd.DataFrame(data=binanin_kat_sayisi,columns=["Binanın Kat Sayısı"],index= range(len(binanin_kat_sayisi)))
# print(data2["Binanın Kat Sayısı"].value_counts())
# sonuc = pd.concat([data,binanin_kat_sayisi])
data.to_csv("DataSon.csv")