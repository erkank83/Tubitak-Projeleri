public class Students {
    private int ogrenciNo;
    private String ogrenciAdi;
    private double matematik;
    private double edebiyat;
    private double tarih;
    private double cografya;
    private double din;
    private double felsefe;
    private double kimya;
    private double fizik;
    private double biyoloji;
    private double puan;

    public Students(int ogrenciNo,String ogrenciAdi,double matematik,double edebiyat,double tarih,double cografya,double din,double felsefe,double kimya,double fizik,double biyoloji,double puan){
      this.ogrenciNo = ogrenciNo;
      this.ogrenciAdi = ogrenciAdi;
      this.matematik = matematik;
      this.edebiyat = edebiyat;
      this.tarih = tarih;
      this.cografya = cografya;
      this.din = din;
      this.felsefe =felsefe;
      this.kimya = kimya;
      this.fizik = fizik;
      this.biyoloji = biyoloji;
      this.puan = puan;
    }
    public int getOgrenciNo() {
        return ogrenciNo;
    }

    public void setOgrenciNo(int ogrenciNo) {
        this.ogrenciNo = ogrenciNo;
    }

    public String getOgrenciAdi() {
        return ogrenciAdi;
    }

    public void setOgrenciAdi(String ogrenciAdi) {
        this.ogrenciAdi = ogrenciAdi;
    }

    public double getMatematik() {
        return matematik;
    }

    public void setMatematik(double matematik) {
        this.matematik = matematik;
    }

    public double getEdebiyat() {
        return edebiyat;
    }

    public void setEdebiyat(double edebiyat) {
        this.edebiyat = edebiyat;
    }

    public double getTarih() {
        return tarih;
    }

    public void setTarih(double tarih) {
        this.tarih = tarih;
    }

    public double getCografya() {
        return cografya;
    }

    public void setCografya(double cografya) {
        this.cografya = cografya;
    }

    public double getDin() {
        return din;
    }

    public void setDin(double din) {
        this.din = din;
    }

    public double getFelsefe() {
        return felsefe;
    }

    public void setFelsefe(double felsefe) {
        this.felsefe = felsefe;
    }

    public double getKimya() {
        return kimya;
    }

    public void setKimya(double kimya) {
        this.kimya = kimya;
    }

    public double getFizik() {
        return fizik;
    }

    public void setFizik(double fizik) {
        this.fizik = fizik;
    }

    public double getBiyoloji() {
        return biyoloji;
    }

    public void setBiyoloji(double biyoloji) {
        this.biyoloji = biyoloji;
    }

    public double getPuan() {
        return puan;
    }

    public void setPuan(double puan) {
        this.puan = puan;
    }
}
