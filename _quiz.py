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
