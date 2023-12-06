# Menü metinlerinin içeriği burada yer almaktadır
def anaMenuMetin():
    _menu="""
    --:::     Ana Menu     :::---
    1- Okul Bazında En Büyük Bulma
    2- Sınıf Bazında En Büyük Bulma
    3- Veri Girişi
    4- Çıkış (için enter tuşuna da basabilirisiniz)
    Seçim yapmak için (1-4) arasında değer giriniz:"""
    return input(_menu)

def menu1Metin():
    _menu="""
    ------ Okul Bazında En Büyük Bulma -------
    9.  sınıflar : isim - puan
    10. sınıflar : isim - puan
    11. sınırlar : isim - puan
    12. sınıflar : isim - puan
    Ana menüye dönmek için Enter tuşa tuşuna basınız."""
    return input(_menu)
def menu2Metin():
    _menu="""
    ------ Sınıf Bazında En Büyük Bulma -------
    1)  9. sınıflar içinde bulma
    2) 10. sınıflar içinde bulma
    3) 11. sınırlar içinde bulma
    4) 12. sınıflar içinde bulma
    Ana menüye dönmek için Enter tuşa tuşuna basınız.
    Seçiminizi yapınız(1-4):"""
    return input(_menu)
def menu2_1Metin():
    _menu="""
    ------ 9.Sınıflar Bazında En Büyük Bulma -------
    9/A  sınıfı  : isim - puan
    9/B  sınıfı  : isim - puan
    9/C  sınıfı  : isim - puan
    Ana menüye dönmek için Enter tuşa tuşuna basınız."""
    return input(_menu)
def menu2_2Metin():
    _menu="""
    ------ 10.Sınıflar Bazında En Büyük Bulma -------
    10/A  sınıfı  : isim - puan
    10/B  sınıfı  : isim - puan
    10/C  sınıfı  : isim - puan
    Ana menüye dönmek için Enter tuşa tuşuna basınız."""
    return input(_menu)
def menu2_3Metin():
    _menu="""
    ------ 11.Sınıflar Bazında En Büyük Bulma -------
    11/A  sınıfı  : isim - puan
    11/B  sınıfı  : isim - puan
    11/C  sınıfı  : isim - puan
    Ana menüye dönmek için Enter tuşa tuşuna basınız."""
    return input(_menu)
def menu2_4Metin():
    _menu="""
    ------ 12.Sınıflar Bazında En Büyük Bulma -------
    12/A  sınıfı  : isim - puan
    12/B  sınıfı  : isim - puan
    12/C  sınıfı  : isim - puan
    Ana menüye dönmek için Enter tuşa tuşuna basınız."""
    return input(_menu)
def menu3Metin():
    _menu="""
    ------ Veri Girişi   -------
    1- Okul Bilgileri
    2- Sınıf Bilgileri
    3- Öğrenci Bilgileri
    4- Ders Bilgileri
    5- Deneme Sınavı Bilgileri
    Ana menüye dönmek için Enter tuşa tuşuna basınız.
    Seçiminizi yapınız(1-5):"""
    return input(_menu)
def menu3_1Metin():
    _menu="""
    ------ Okul Bilgi Girişi -------
    Okul adı      : İbrahim Önal Fen Lisesi
    İl            : Bursa
    İlçe          : Mustafakemalpaşa
    Ana menüye dönmek için Enter tuşa tuşuna basınız."""
    return input(_menu)
def menu3_2Metin():
    _menu="""
    ------ Sınıf Bilgi Girişi -------
    Sınıf Adı     : ilgili sınıf adı
    Sınıfa ait öğrenci listeleri burada yer alacak    
    Ana menüye dönmek için Enter tuşa tuşuna basınız."""
    return input(_menu)
def menu3_3Metin():
    _menu="""
    ------ Öğrenci Bilgi Girişi -------
    1- Yeni Kayıt
    2- Kayit Silme/Güncelleme
    3- Kayit Listeleme
    Ana menüye dönmek için Enter tuşa tuşuna basınız.
    Seçiminizi yapınız(1-3):"""
    return input(_menu)
def menu3_4Metin():
    _menu="""
    ------ Ders Bilgi Girişi -------
    Ders Adı     : ders adı
    Doğru Sayısı : X tane
    Yanlış Sayısı: Y tane
    Net Sayısı   : Z tane
    Ana menüye dönmek için Enter tuşa tuşuna basınız."""
    return input(_menu)
def menu3_5Metin():
    _menu="""
    ------ Deneme Sınavı Bilgi Girişi -------
    Deneme Sınavı Adı     : deneme sınavı adı burada yer alacak..
    Ana menüye dönmek için Enter tuşa tuşuna basınız."""
    return input(_menu)

# Menüden gelen değere göre yapılan işlemler burada yer almaktadır
def anaMenuSecim():
    durum=False
    while not durum:
        secim=anaMenuMetin()
        if   secim=="1": altMenuSecim(menu1Metin())
        elif secim=="2": menu2Secim()
        elif secim=="3": menu3Secim()
        elif secim=="4" or not secim: durum=True
def altMenuSecim(gelenMenu):
    durum=False
    while not durum:
         secim=gelenMenu
         if not secim:
             durum=True
         else:
             print("\t!!!!!Çıkmak için enter tuşuna basınız!!!!!!!!")
             break
def menu2Secim():
    durum=False
    while not durum:
         secim=menu2Metin()
         if secim=="1":   altMenuSecim(menu2_1Metin())
         elif secim=="2": altMenuSecim(menu2_2Metin())
         elif secim=="3": altMenuSecim(menu2_3Metin())
         elif secim=="4": altMenuSecim(menu2_4Metin())
         if not secim:#enter tuşuna basılmış ise
             durum=True

def menu3Secim():
    durum=False
    while not durum:
         secim=menu3Metin()
         if secim=="1":   altMenuSecim(menu3_1Metin())
         elif secim=="2": altMenuSecim(menu3_2Metin())
         elif secim=="3": menu3_3Secim()
         elif secim=="4": altMenuSecim(menu3_4Metin())
         elif secim=="5": altMenuSecim(menu3_5Metin())
         if not secim:#enter tuşuna basılmış ise
             durum=True
def menu3_3Secim():
    durum=False
    while not durum:
         secim=menu3_3Metin()
         if secim=="1":   print("Yeni kayıt girişi yapılacak")
         elif secim=="2": print("Kayıt silme güncelleme işlemi yapılacak")
         elif secim=="3": print("Kayıt listeleme işlemi yapılacak")
         if not secim:
             #enter tuşuna basılmış ise
             durum=True                      
def main():
    anaMenuSecim()
    
main() 
