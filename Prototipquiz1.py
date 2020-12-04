#soru Sınıfı
class Soru:
    def __init__(self,sorumetni,secenekler,cevap):
        self.sorumetni=sorumetni
        self.secenekler=secenekler
        self.cevap=cevap
        
    def cevapKontrol(self,cevap):
        return self.cevap==cevap

# Quiz sınıfı
class Quiz:
    def __init__(self,sorular):
        self.sorular=sorular
        self.skor=0
        self.soruIndex=0

    def getirSoru(self):
        return self.sorular[self.soruIndex]

    def gosterSoru(self):
        soru=self.getirSoru()
        print("Soru {}: {}".format((self.soruIndex+1),soru.sorumetni))
        for q in soru.secenekler:
            print("-",q)
        cevap=input("cevap:")
        self.tahmin(cevap.lower().strip())
        self.soruYukle()

    def tahmin(self,cevap):
        soru=self.getirSoru()
        if soru.cevapKontrol(cevap):
            self.skor+=1
        self.soruIndex+=1
        
    def soruYukle(self):
        if len(self.sorular)==self.soruIndex:
            self.gosterSkor()
        else:
            self.gosterilerleme()
            self.gosterSoru()

    def gosterSkor(self):
        print("Skor : {}".format(self.skor))

    def gosterilerleme(self):
        toplamSoru=len(self.sorular)
        soruSayisi=self.soruIndex+1

        if soruSayisi > toplamSoru:
            print("Quiz bitti")
        else:
            print(" {}. sorunun {}. sorusu ".format(toplamSoru,soruSayisi).center(50,"*"))
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

sorular=[s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]

quiz=Quiz(sorular)
quiz.soruYukle()

