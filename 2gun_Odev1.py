# Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.

# Bu öğrenci kayıt sistemine;

# Aldığı isim soy isim ile listeye öğrenci ekleyen
# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
# Listeye birden fazla öğrenci eklemeyi mümkün kılan
# Listedeki tüm öğrencileri tek tek ekrana yazdıran
# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
# fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.

# Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir.


ogrenciListesi= []
    
def ogrenciEkle():
    ogrenci = (input("\tIsim ve Soyisim giriniz:\n "))
    ogrenciListesi.append(ogrenci)
    print("\tOgrenci Kaydedildi")

def ogrenciSil():
    if len(ogrenciListesi) !=0 :
        ogrenci = (input("\tIsim ve Soyisim Giriniz:\n "))
        if ogrenci in ogrenciListesi:
            ogrenciListesi.remove(ogrenci)
            print("\tOgrenci silindi.")
        else :
            print("Ogrenci Kaydi Bulunamadi!")
    else : 
        print("\tHenuz Kayit Yok!")

def ogrenciCokluEkle():
    while True:
        ogrenci = input("\tKayit için Isim ve Soyisim giriniz! \n\tKayittan cikmak icin 0'a basiniz!: \n")
        if ogrenci == "0":
            break
        ogrenciListesi.append(ogrenci)
    print("\tKayitlar tamamlandi")

def ogrenciListe():
    if len(ogrenciListesi) !=0 :
      for ogrenci in ogrenciListesi:
          print("\t",ogrenci)
    else : 
        print("\tHenuz Kayit Yok!")

def ogrenciCokluSil():
    if len(ogrenciListesi) !=0 :
        while True:
            ogrenci = input("\tSilmek icin Isim ve Soyisim giriniz! \n\tCikmak icin 0'a basiniz!:\n")
            if ogrenci == "0" :
                break
            elif ogrenci in ogrenciListesi:
                ogrenciListesi.remove(ogrenci)
            else:
                print("\tOgrenci Kaydi Bulunamadi!")
    else : 
        print("\tHenuz Kayit Yok!")
   
while True:
    print("Ogrenci Kayit Programi :\n1- Ogrenci Ekle\n2- Ogrenci Kayit Silme\n3- Coklu Ogrenci Ekleme\n4- Coklu Ogrenci Kaydi Silme\n5- Ogrenci listesi\n0-Programdan cikis")
    islem = int(input("Yapmak Istediğiniz Islemi Seciniz : "))

    if islem == 1: ogrenciEkle()
    elif islem == 2: ogrenciSil()
    elif islem == 3: ogrenciCokluEkle()
    elif islem == 4: ogrenciCokluSil()    
    elif islem == 5: ogrenciListe() 
    elif islem == 0: break
    else : print("\tGeçersiz Islem!!!, \n\tLutfen Tekrar Deneyin.")
