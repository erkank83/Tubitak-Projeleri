from _dosya import Dosya
from _quiz  import Soru,Quiz
dosyaAdi="sorular.txt"
d=Dosya(dosyaAdi)


def _varsayilanSoruYukle():
    # Sorular
    s1=Soru("Adil olma, eşit davranma, paylaşma",["Adalet","Dostluk","Dürüstlük","Öz Denetim"],"adalet")
    s2=Soru("Diğergamlık, Güven duyma, sadık olma, vefalı olma, yardımlaşma",["Öz Denetim","Dostluk","Dürüstlük","Adalet"],"dostluk")
    s3=Soru("Açık ve anlaşılır olma, doğru sözlü olma, etik davranma, güvenilir olma, sözünde durma",["Adalet","Dostluk","Öz Denetim","Dürüstlük"],"dürüstlük")
    s4=Soru("Davranışlarını kontrol etme, davranışlarının sorumluluğunu alabilme, öz güven sahibi olma",["Adalet","Öz Denetim","Dostluk","Dürüstlük"],"öz denetim")
    s5=Soru("Azimli olma, tahammül etme",["Sabır","Saygı","Sevgi","Sorumluluk"],"sabır")
    s6=Soru("Alçak gönüllü olma, başkalarına kendisine davranılmasını istediği şekilde davranma, diğer insanların kişiliklerine değer verme",["Sabır","Saygı","Sevgi","Sorumluluk"],"saygı")
    s7=Soru("Aile birliğine önem verme, fedakarlık yapma",["Sabır","Saygı","Sevgi","Sorumluluk"],"sevgi")
    s8=Soru("Kendine, çevresine, vatanına, ailesine karşı sorumlu olma",["Sabır","Saygı","Sevgi","Sorumluluk"],"sorumluluk")
    s9=Soru("Çalışkan olma, dayanışma, kurallara ve kanunlara uyma, tarihsel ve doğal mirasa duyarlı olma, toplumu önemseme",["Sabır","Vatanseverlik","Sevgi","Sorumluluk"],"vatanseverlik")
    s10=Soru("Cömert olma, fedakar olma, iş birliği yapma, merhametli olma, misafirperver olma, paylaşma",["Vatanseverlik","Yardımseverlik","Sevgi","Sorumluluk"],"yardımseverlik")

    return [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]

def yarisma():
    ad=input("Adınızı giriniz :")
    print("".center(50,"*"))
    print("Bilgi yarışmasına hoş geldin, {}".format(ad).center(50,"*"))
    #eğer sorular.txt yoksa oluştur..
    try:
        sorular=soruOku()
    except Exception as ex:
        varsayilanSoruYukle(_varsayilanSoruYukle())
    sorular=soruOku()
    quiz=Quiz(sorular)
    quiz.soruYukle()

def varsayilanSoruYukle(liste):
    
    metin=""
    global dosyaAdi
    for soru in liste:
        secenekMetin=""
        for sececek in soru.secenekler:
            secenekMetin+=sececek+","
        secenekMetin=secenekMetin[:-1]
        metin+=soru.sorumetni+"|"+soru.cevap+":"+secenekMetin+"\n"

    d.yeniOlustur(metin)
    print("Varsayılan sorular {} dosyasına yazıldı".format(dosyaAdi))

def soruEkle():
    soru=soruGir()
    secenekMetin=""
    for sececek in soru.secenekler:
        secenekMetin+=sececek+","
    secenekMetin=secenekMetin[:-1]
    metin=soru.sorumetni+"|"+soru.cevap+":"+secenekMetin
    d.veriEkle(metin)


def soruOku():
  
    listeSorular=list()
    liste=d.listehalindeOku()
    
    for satir in liste:
        parcalar=satir.split("|")
        bolumler=parcalar[1].split(":")
        secenekler=bolumler[1].split(",")
        listeSorular.append(Soru(parcalar[0],secenekler,bolumler[0]))

    return listeSorular
def soruListe(liste):
    sayac=0
    print("Liste Başı".center(50,"*"))
    for soru in liste:
        print("{}-{}(cevap: {})".format((sayac+1),soru.sorumetni,soru.cevap))
        sayac+=1
    print("Liste Sonu".center(50,"*"))
 
def tamsayiKontrol(metin):
        deger=input(metin)
        if deger.isdigit():
            return int(deger)
        else:
            return 0
        
def metinKontrol(metin):
        _metin=input(metin)
        _metin=_metin.strip()
        if _metin.isalpha():
            return _metin.capitalize().strip()
        else:
            return _metin.lstrip().rstrip()
def soruGir():

    soru=metinKontrol("Soru :")
    cevap=metinKontrol("Cevap :").lower()
    secenekler=list()
    durum=False
    while not durum:
        secenek=metinKontrol("Seçenek")
        secenekler.append(secenek.capitalize().strip())
        secim=input("Çıkmak için(h) tuşuna basınız!\nDevam etmek için herhangi bir tuşa basınız")
        if secim.lower().strip()=="h": durum=True

    return Soru(soru,secenekler,cevap)

def listedenSinifaDonustur(liste):
    yeniListe=list()
    for soru in liste:
        yeniListe.append(Soru(soru.sorumetni,soru.secenekler,soru.cevap))
    return yeniListe
    

def soruSil(liste):
    sayac=0
    print("Silme işlemi için liste başı".center(50,"*"))
    for soru in liste:
        print("{}-{}(cevap: {})".format((sayac+1),soru.sorumetni,soru.cevap))
        sayac+=1
    secim=input("Silmek istediğiniz sorunun numarasını giriniz: ").strip()
    sec=input("{} nolu kaydı silmek istiyor musunuz?(e/h)".format(secim))
    if sec.lower().strip()=="e":
        del liste[int(secim)-1]
        print("{} nolu kaydı sildiniz...".format(secim))
        varsayilanSoruYukle(listedenSinifaDonustur(liste))
    print("Silme işlemi için liste sonu".center(50,"*"))
    
def ayarlar():
    print("Ayarlar sayfasına geldiniz".center(50,"*"))
    durum=False
    while not durum:
        metin="1- Varsayılan soruları yükle\n2- Soru Gir\n3- Soru Sil\n4- Soruları Listele\nÜst Menüye dönmek için enter tuşuna basın\nSeçimini giriniz :"
        secim=input(metin)
        if   secim.strip()=="1":varsayilanSoruYukle(_varsayilanSoruYukle())
        elif secim.strip()=="2":soruEkle()
        elif secim.strip()=="3":soruSil(soruOku())
        elif secim.strip()=="4":soruListe(soruOku())
        else: durum=True
    print("Ayarlar sayfa sonu".center(50,"*"))

def main():
    print("Ana sayfaya hoş geldiniz".center(50,"*"))
    durum=False
    while not durum:
        metin="1- Bilgi yarışması\n2- Ayarlar\n3- Çıkış\n\nSeçimini giriniz :"
        secim=input(metin)
        if   secim.strip()=="1":yarisma()
        elif secim.strip()=="2":ayarlar()
        else: durum=True
    print("Ana sayfa sonu".center(50,"*"))
main()

