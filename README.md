# Ev Fiyat Tahmini Projesi
 

Bu proje, Evlerin çeşitli özelliklerine (metrekare, bulunduğu kat, oda sayısı, tür, ısıtma tipi, vb) dayanarak evlerin fiyatlarını tahmin etmeyi amaçlamaktadır. Proje, Karar ağacı tekniği kullanılarak, veri setindeki mevcut ev özelliklerinden yola çıkarak ev fiyatlarını etkili bir şekilde tahmin edebilmektedir. Siz eğer isterseniz diğer teknikleri kullanarak modelin doğruluk oranında nasıl bir değişim olduğunu gözlemleyebilir ve buna göre kendi çıkarımlarınızı yapabilirsiniz.
Etkili bir şekilde tahmin yapabilen algoritma geliştirebilmek için elimizde olan veri setindeki bozuk verileri temizlemeliyiz veya kullanılabilir bir hale getirmeliyiz. Şehir bilgisi gibi kategorik veriler, model tarafından işlenebilir bir hale getirmek için sayısal formata dönüştürülmelidir.

## Veri Seti
Verileri nasıl elde ettiğim hakkındaki bilgiyi [buradan](https://github.com/oguzhanerbil/Web-Scraping) bulabilirsiniz.

Ev özellikleri verilerinin barındıran dosyamda şu bilgiler yer almaktadır:
* Fiyat
* Şehir
* Metrekare
* Bulunduğu Kat
* Isıtma Tipi
* Bine Yaşı
* Binanın Kat Sayısı

## Modelleme

Model, veri setindeki ev özelliklerini kullanarak fiyat tahminleri yapmaktadır. Model geliştirme sürecinde şu adımlar izlenmiştir:

1. Veri Temizleme: Bozuk veya eksik verilerin temizlenmesi.
2. Veri Ön İşleme: Kategorik verilerin sayısallaştırılması ve özellik mühendisliği.
3. Model Seçimi ve Eğitimi: Makine öğrenimi algoritmalarının seçilmesi ve eğitilmesi.
4. Model Değerlendirme: Modelin performansının değerlendirilmesi ve iyileştirilmesi.

## Teknolojiler

Ana kullanılan kütüphaneler:

* Pandas: Veri manipülasyonu ve analizi için kullanılmıştır.
* Scikit-learn: Makine öğrenimi modellemesi için kullanılmıştır.
* Matplotlib ve Seaborn: Veri görselleştirme için kullanılmıştır.

  ### Yardımlarından dolayı @yasinsahin0'a teşekkür ederim.

