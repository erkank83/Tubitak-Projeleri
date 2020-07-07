class Dosya:
    hata=""
    satirlar=""
   
    def __init__(self,dosyaadi=""):
        self.dosyaadi=dosyaadi

    def dosyaYolu(self,dosyaadi):
        self.dosyaadi=dosyaadi
        self.yeniOlustur()
    
    def yeniOlustur(self,veri=""):
        self.dosya=open(self.dosyaadi,"w",encoding="utf-8")
        if veri:
            self.dosya.write(veri)
        self.kapat()

    def varMi(self):
        mevcut=False
        try:
            self.dosya=open(self.dosyaadi,"x",encoding="utf-8")
        except FileExistsError:
            mevcut=True

        return mevcut
  
    def veriEkle(self,veri=""):
        self.dosya=open(self.dosyaadi,"a",encoding="utf-8")
        if veri:
            veri+="\n"
            self.dosya.write(veri)
        self.kapat()
        
    def veriOku(self):
        try:
            self.dosya=open(self.dosyaadi,"r",encoding="utf-8")
            self.satirlar=self.dosya.read()
            self.kapat()
        except FileNotFoundError:
            self.hata="Dosya yok"
        finally:
            return self.satirlar

    def satirSatirOku(self):
        try:
            self.dosya=open(self.dosyaadi,"r",encoding="utf-8")
            for satir in self.dosya:
                self.satirlar+=satir
            self.kapat()
        except FileNotFoundError:
            self.hata="Dosya yok"
        finally:
            return self.satirlar

    def listehalindeOku(self):
        try:
            self.dosya=open(self.dosyaadi,"r",encoding="utf-8")
            satirlar=self.dosya.readlines()
            yeniSatirlar=list()
            sayac=0
            while(len(satirlar)>sayac):
                yeniSatirlar.append(satirlar[sayac][:len(satirlar[sayac])-1])
                self.satirlar+=yeniSatirlar[sayac]+"\n"
                sayac+=1
           
            self.kapat()
        except FileNotFoundError:
            self.hata="Dosya yok"
        finally:
            return yeniSatirlar

    def veriOkuW(self):
        try:
            with open(self.dosyaadi,"r",encoding="utf-8")as file:
                self.dosya=file
                self.satirlar=self.dosya.read()
        except FileNotFoundError:
            self.hata="Dosya yok"
        finally:
            return self.satirlar

    def imleciGetir(self):
        return self.dosya.tell()

    def imleciKonumlandir(self,konum):
        return self.dosya.seek(konum)
    
    def sayfaBasiGuncelleme(self,guncellemeVerisi):
        try:
            with open(self.dosyaadi,"r+",encoding="utf-8")as file:
                self.dosya=file
                icerik=self.dosya.read()
                icerik=guncellemeVerisi+"\n"+icerik
                self.imleciKonumlandir(0)
                self.dosya.write(icerik)

        except FileNotFoundError:
            self.hata="Dosya yok"

    def sayfaOrtasiGuncelleme(self,index,guncellemeVerisi):
        try:
            with open(self.dosyaadi,"r+",encoding="utf-8")as file:
                self.dosya=file
                liste=self.dosya.readlines()
                liste.insert(index,guncellemeVerisi+"\n")
                self.imleciKonumlandir(0)
                #for i in liste:
                #    self.dosya.write(i)
                self.dosya.writelines(liste)

        except FileNotFoundError:
            self.hata="Dosya yok"
      
    def kapat(self):
        self.dosya.close()
        



