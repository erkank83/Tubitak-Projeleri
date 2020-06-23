# Veri girişi işlemleri burada yer almaktadır
liste12C,liste12B,liste12A=list(),list(),list()
liste11C,liste11B,liste11A=list(),list(),list()
liste10C,liste10B,liste10A=list(),list(),list()
liste9C,liste9B,liste9A=list(),list(),list()
pliste12C,pliste12B,pliste12A=list(),list(),list()
pliste11C,pliste11B,pliste11A=list(),list(),list()
pliste10C,pliste10B,pliste10A=list(),list(),list()
pliste9C,pliste9B,pliste9A=list(),list(),list()

sinifIsimListe={
    "9a":liste9A,
    "9b":liste9B,
    "9c":liste9C,
    "10a":liste10A,
    "10b":liste10B,
    "10c":liste10C,
    "11a":liste11A,
    "11b":liste11B,
    "11c":liste11C,
    "12a":liste12A,
    "12b":liste12B,
    "12c":liste12C
    }
sinifPuanListe={
    "9a":pliste9A,
    "9b":pliste9B,
    "9c":pliste9C,
    "10a":pliste10A,
    "10b":pliste10B,
    "10c":pliste10C,
    "11a":pliste11A,
    "11b":pliste11B,
    "11c":pliste11C,
    "12a":pliste12A,
    "12b":pliste12B,
    "12c":pliste12C
}
def _ogrenciEkle(sinifDeger):
   
    print("{} Sınıfı için veri girişi".format(sinifDeger.upper()))
    kimlik={
        "Ad":"",
        "Soyad":"",
        "No":"",
        "Sınıf":""
        }   
    dersTurkce={
        "D":0,
        "Y":0,
        "N":0.0
        }
    dersSosyal={
        "D":0,
        "Y":0,
        "N":0.0
        }
    dersMatematik={
        "D":0,
        "Y":0,
        "N":0.0
        }
    dersFen={
        "D":0,
        "Y":0,
        "N":0.0
        }
    denemeDersler={
        "Kimlik":kimlik,
        "Turkce":dersTurkce,
        "Sosyal":dersSosyal,
        "Matematik":dersMatematik,
        "Fen":dersFen
        }
    katsayiDersler={
        "Turkce":3.3,
        "Sosyal":3.4,
        "Matematik":3.3,
        "Fen":3.4
        }
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
            return _metin.capitalize().lstrip().rstrip()
    
    dogru,yanlis,net,katsayi,puan=0,0,0,0,0
    for ders,sutun in denemeDersler.items():
        if ders=="Kimlik":
            sutun["Ad"]   =metinKontrol("Öğrenci adını giriniz :")
            sutun["Soyad"]=metinKontrol("Öğrenci soyadını giriniz :")
            sutun["No"]   =tamsayiKontrol("Öğrenci nosunu giriniz :")
            sutun["Sınıf"]=sinifDeger.upper().strip()
        else:
            print("{} dersi için veri girişi:".format(ders))
            
            sutun["D"]=tamsayiKontrol("Doğru sayısını giriniz  :")
            sutun["Y"]=tamsayiKontrol("Yanlış sayısını giriniz :")
            sutun["N"]=float(int(sutun["D"])-int(sutun["Y"])/4)
            dogru+=sutun["D"]
            yanlis+=sutun["Y"]
            net+=sutun["N"]
            puan+=sutun["N"]*katsayiDersler[ders]
    puan+=100
    denemeDersler["Toplam"]={
        "D":dogru,
        "Y":yanlis,
        "N":net
        }
    denemeDersler["Puan"]={
        "isim":denemeDersler["Kimlik"].get("Ad"),
        "puan":puan
        }
    

    return denemeDersler

def ogrenciListele(liste):
    if len(liste)>0:
        for ogrenci in liste:
            ogrenciYaz(ogrenci)
    else:
        print("Liste boş..".center(50))
            

def ogrenciEkle(sinif):
    durum=False
    secim=""
    while not durum:
        ogrenci=_ogrenciEkle(sinif)
        secim=input("(k)aydet || i(p)tal . Seçiminiz(k|p):")
        if secim.lower().strip()=="k":
            sinifIsimListe.get(sinif).append(ogrenci)
            sinifPuanListe.get(sinif).append(ogrenci["Puan"])
            secim=input("Devam etmek istiyor musunuz?(e/h)")
            if secim.lower().strip()=="h":
                durum=True
            else:
                print("e yada h harfine basın")
        elif secim.casefold().strip()=="p":
            print("Kayıt ekleme işlemi iptal edildi.".center(50))
            durum=True
 #basla
def ogrenciYaz(ogrenci):
    print("{}".format("------------------------------------------------\t--------------".expandtabs(4)))
    print("----{:^40}----\t{}".expandtabs(23).format("Kimlik Bilgileri","Puan"))
    print("{}".format("------------------------------------------------\t--------------".expandtabs(4)))
#sütun bilgisi
    for bolum in ogrenci:
        for sutun in ogrenci[bolum].keys():
            if sutun=="Ad" or sutun=="Soyad":
                print("{:^10}\t".format(sutun),end=" ")
            elif sutun=="No":
                print("{:^3}\t".format(sutun),end=" ")
            elif sutun=="Sınıf":
                print("{:^3}\t".format(sutun),end="\n")

#veriler
    for bolum in ogrenci:
        for sutun,v in ogrenci[bolum].items():
            if sutun=="Ad" or sutun=="Soyad":
                print("{:^10}\t".format(v),end=" ")
            elif sutun=="No":
                print("{:3}\t".format(v),end=" ")
            elif sutun=="Sınıf":
                print("{:^6}\t".format(v),end="\t")
    print("{p:1.3f}".format(p=ogrenci["Puan"].get("puan")))
    print("{}".format("------------------------------------------------"))
    print("----{:^40}----".format("Dersler"))
    print("{}".format("------------------------------------------------"))
#ders bilgileri          
    for bolum in ogrenci:
        if bolum=="Kimlik" or bolum=="Puan":
            pass
        else:
            print("{:^8}\t".format(bolum),end="")
# D Y N sütun bilgileri
    for bolum in ogrenci:
        for sutun in ogrenci[bolum].keys():
            if sutun=="D" or sutun=="Y":
                print("{:2}".format(sutun),end=" ")
            elif sutun=="N":
                print("{:^3}\t".format(sutun),end="")
# D Y N sütun verileri
    for bolum in ogrenci:
        for sutun,v in ogrenci[bolum].items():
            if sutun=="D" or sutun=="Y":
                print("{:<2}".format(v),end=" ")
            elif sutun=="N":
                print("{:<3}\t".format(v),end="")
def puanaGoreSirala(liste):
    def getirPuan(e):
        return e['puan']
    if len(liste)>0:
        liste.sort(reverse=True,key=getirPuan)
        isim=liste[0].get("isim")
        puan=liste[0].get("puan")
        return "{} - {}".format(isim,puan)
    else:
        return "Liste boş..."
def ogrenciListele2(liste,sinif):
    def indexBul(isim,puan):
        index=0
        for kayit in sinifPuanListe[sinif]:
            if kayit.get("isim")==isim and kayit.get("puan")==puan:
                return index
            index+=1    
                   
        
    if len(liste)>0:
        sayac=0
        print("{:^3}\t{:^10}\t{:^10}\t{:^3}\t{:^3}\t{:^10}".format("Sıra No","Ad","Soyad","No","Sınıf","Puan"))
        for ogrenci in liste:
            sayac+=1
            ogrenciYaz2(ogrenci,sayac)
        secim=input("Silinmek istenen kaydın sıra nosu giriniz:")
        if not secim:
            exit
        else:
            silinecekOgrenci=liste[int(secim)-1]
            isim=silinecekOgrenci["Puan"].get("isim")
            puan=silinecekOgrenci["Puan"].get("puan")
            del liste[int(secim)-1]
            del sinifPuanListe[sinif][indexBul(isim,puan)]
            print(secim+" nolu kayıt silindi..")
            
    else:
        print("Liste boş..")
        
def ogrenciYaz2(ogrenci,sayac):
    #veriler
    print("{:^3}\t".format(sayac),end=" ")
    for sutun,v in ogrenci["Kimlik"].items():
        if sutun=="Ad" or sutun=="Soyad":
            print("{:^10}\t".format(v),end=" ")
        elif sutun=="No":
            print("{:3}\t".format(v),end=" ")
        elif sutun=="Sınıf":
            print("{:^6}\t".format(v),end=" ")
    print("{:^10}".format(ogrenci["Puan"].get("puan")))

# Menü metinlerinin içeriği burada yer almaktadır
def menuBoslukKontrol(menuEleman):
    _deger=menuEleman.strip()
    if _deger.isdigit():
        return int(_deger)
    else:
        return menuEleman

def anaMenuMetin():
    _menu="""
    --:::     Ana Menu     :::---
    1- Okul Bazında En Büyük Bulma
    2- Sınıf Bazında En Büyük Bulma
    3- Veri Girişi
    4- Çıkış 
    Seçim yapmak için (1-4) arasında değer giriniz:"""
    return input(_menu)

def menu1Metin():
    global pliste12C,pliste12B,pliste12A,pliste11C,pliste11B,pliste11A,pliste10C,pliste10B,pliste10A,pliste9A,pliste9B,pliste9C
    liste12ler=pliste12C+pliste12B+pliste12A
    liste11ler=pliste11C+pliste11B+pliste11A
    liste10lar=pliste10C+pliste10B+pliste10A
    liste9lar =pliste9C+pliste9B+pliste9A
   
    _9lar =puanaGoreSirala(liste9lar)
    _10lar=puanaGoreSirala(liste10lar)
    _11ler=puanaGoreSirala(liste11ler)
    _12ler=puanaGoreSirala(liste12ler)

    _menu="""
    ------ Okul Bazında En Büyük Bulma -------
    9.  sınıflar : {0}
    10. sınıflar : {1}
    11. sınırlar : {2}
    12. sınıflar : {3}
    Ana menüye dönmek için Enter tuşa tuşuna basınız.""".format(_9lar,_10lar,_11ler,_12ler)
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
    _9a=puanaGoreSirala(sinifPuanListe["9a"])
    _9b=puanaGoreSirala(sinifPuanListe["9b"])
    _9c=puanaGoreSirala(sinifPuanListe["9c"])

    _menu="""
    ------ 9.Sınıflar Bazında En Büyük Bulma -------
    9/A  sınıfı  : {0}
    9/B  sınıfı  : {1}
    9/C  sınıfı  : {2}
    Üst menüye dönmek için Enter tuşa tuşuna basınız.""".format(_9a,_9b,_9c)
    return input(_menu)
def menu2_2Metin():
    _10a=puanaGoreSirala(sinifPuanListe["10a"])
    _10b=puanaGoreSirala(sinifPuanListe["10b"])
    _10c=puanaGoreSirala(sinifPuanListe["10c"])

    _menu="""
    ------ 10.Sınıflar Bazında En Büyük Bulma -------
    10/A  sınıfı  : {0}
    10/B  sınıfı  : {1}
    10/C  sınıfı  : {2}
    Üst menüye dönmek için Enter tuşa tuşuna basınız.""".format(_10a,_10b,_10c)
    return input(_menu)
def menu2_3Metin():
    _11a=puanaGoreSirala(sinifPuanListe["11a"])
    _11b=puanaGoreSirala(sinifPuanListe["11b"])
    _11c=puanaGoreSirala(sinifPuanListe["11c"])

    _menu="""
    ------ 11.Sınıflar Bazında En Büyük Bulma -------
    11/A  sınıfı  : {0}
    11/B  sınıfı  : {1}
    11/C  sınıfı  : {2}
    Üst menüye dönmek için Enter tuşa tuşuna basınız.""".format(_11a,_11b,_11c)
    return input(_menu)
def menu2_4Metin():
    _12a=puanaGoreSirala(sinifPuanListe["12a"])
    _12b=puanaGoreSirala(sinifPuanListe["12b"])
    _12c=puanaGoreSirala(sinifPuanListe["12c"])

    _menu="""
    ------ 12.Sınıflar Bazında En Büyük Bulma -------
    12/A  sınıfı  : {0}
    12/B  sınıfı  : {1}
    12/C  sınıfı  : {2}
    Üst menüye dönmek için Enter tuşa tuşuna basınız.""".format(_12a,_12b,_12c)
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
    okulBilgileri = ("İbrahim Önal Fen Lisesi", "Bursa", "Mustafakemalpaşa")
    _menu="""
    ------ Okul Bilgi Girişi -------
    Okul adı      : {}
    İl            : {}
    İlçe          : {}
    Üst menüye dönmek için Enter tuşa tuşuna basınız.""".format(
        okulBilgileri[0],okulBilgileri[1],okulBilgileri[2])
    return input(_menu)
def menu3_2Metin():
    sinifBilgileri=("9a","9b","9c","10a","10b","10c","11a","11b","11c","12a","12b","12c")
    listem=""
    for sinif in sinifBilgileri:
        listem+=sinif+" "
    _menu="""
    ------ Kayit Listeleme -------
    Sınıflar     : {}
    Toplam Sınıf : {}
    Üst menüye dönmek için Enter tuşa tuşuna basınız.
    Listeleme yapmak için bir sınıf ismi giriniz:""".format(listem,len(sinifBilgileri))
    return input(_menu)
def menu3_3Metin():
    _menu="""
    ------ Öğrenci Bilgi Girişi -------
    1- Yeni Kayıt
    2- Kayit Silme
    3- Kayit Listeleme
    Üst menüye dönmek için Enter tuşa tuşuna basınız.
    Seçiminizi yapınız(1-3):"""
    return input(_menu)
def menu3_4Metin():
    _menu="""
    ------ Ders Bilgi Girişi -------
    Dersler     : Türkçe, Sosyal, Matematik, Fen
    Ana menüye dönmek için Enter tuşa tuşuna basınız."""
    return input(_menu)
def menu3_5Metin():
    _menu="""
    ------ Deneme Sınavı Bilgi Girişi -------
    Deneme Sınavı Adı     : 9-10-11-12 TARAMA - 1
    Ana menüye dönmek için Enter tuşa tuşuna basınız."""
    return input(_menu)

# Menüden gelen değere göre yapılan işlemler burada yer almaktadır
def anaMenuSecim():
    durum=False
    while not durum:
        secim=menuBoslukKontrol(anaMenuMetin())
        if   secim==1: altMenuSecim(menu1Metin())
        elif secim==2: menu2Secim()
        elif secim==3: menu3Secim()
        elif secim==4: durum=True
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
         secim=menuBoslukKontrol(menu2Metin())
         if   secim==1:   altMenuSecim(menu2_1Metin())
         elif secim==2:   altMenuSecim(menu2_2Metin())
         elif secim==3:   altMenuSecim(menu2_3Metin())
         elif secim==4:   altMenuSecim(menu2_4Metin())
         if not secim:#enter tuşuna basılmış ise
             durum=True

def menu3Secim():
    durum=False
    while not durum:
         secim=menuBoslukKontrol(menu3Metin())
         if   secim==1: altMenuSecim(menu3_1Metin())
         elif secim==2: menu3_2Secim()
         elif secim==3: menu3_3Secim()
         elif secim==4: altMenuSecim(menu3_4Metin())
         elif secim==5: altMenuSecim(menu3_5Metin())
         if not secim:#enter tuşuna basılmış ise
             durum=True
             
def menu3_2Secim():
    durum=False
    while not durum:
         secim=menu3_2Metin()
         if secim in sinifIsimListe.keys():
             ogrenciListele(sinifIsimListe.get(secim))
         if not secim:
             #enter tuşuna basılmış ise
             durum=True    
def menu3_3Secim():
    durum=False
    while not durum:
        secim=menuBoslukKontrol(menu3_3Metin())
        if secim==1:
            sinif=input("Sınıflar     : 9a,9b,9c,10a,10b,10c,11a,11b,11c,12a,12b,12c\nYeni kayıt için sınıf giriniz:")
            if sinif in sinifIsimListe.keys():
                ogrenciEkle(sinif)
        elif secim==2:
            sinif=input("Sınıflar     : 9a,9b,9c,10a,10b,10c,11a,11b,11c,12a,12b,12c\nYeni kayıt için sınıf giriniz:")
            if sinif in sinifIsimListe.keys():
                ogrenciListele2(sinifIsimListe.get(sinif),sinif)
        elif secim==3: menu3_2Secim()
        if not secim:
             #enter tuşuna basılmış ise
             durum=True                      
def main():
    anaMenuSecim()
    
main() 
