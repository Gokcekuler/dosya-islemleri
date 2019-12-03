from collections import namedtuple
import sys

tampon=0
cikis="g"
while cikis != "e":
    kimlik=input("Lütfen kullanıcı mı yoksa sistem yöntecisi mi olduğunuzu belirtiniz\n" ) 

    if kimlik=='kullanıcı': #eğer kullanıcıysa listede aradığı kaydın olup olmadığını kontrol ediyor
        kitap=input("Lütfen aradığınız kitabın adını giriniz     \n")
        yazar=input("Lütfen aradığınız kitabın yazarını giriniz \n")
        ISBN=int(input("Lütfen aradığınız k,tabın ISBN numarasını giriniz \n"))
        aranan= kitap +","  +  yazar + "," +  str(ISBN)
        dosya=open("kitap.txt","r")

        if aranan in open('kitap.txt').read(): #aranan kayıt bulunduysa çalışır
            print("Aradığınız kitap listede mevcut")

        else:
            print("Aradığınız kitap bulunamadı")

        dosya.close()

    else: #Sistem yönetici ise bu kısım çalıştırılır
        Kitap=namedtuple('Kitap',("isim","yazar","ISBN")) #struct yapısına denk gelir
        islem=input("ekleme yapmak için a'ya silme için d'ye güncellemek için u'ya basınız") 
        girdi=Kitap(input("kitap adi"),input("yazar adi"),int(input("ISBN numarası"))) #kayıt bilgileri girilir
        kitap_adi=girdi.isim
        kitap_yazari=girdi.yazar
        ISBN_numarasi=girdi.ISBN
        kayit=kitap_adi+","+kitap_yazari+","+str(ISBN_numarasi)
        if len(kayit) >100:
            print("Lütfen 100  karakterden uzun kayıt girmeyin")
            sys.exit()

        if islem== 'a': #ekleme işlemi
            dosya = open("kitap.txt","r")
            aranan=kayit.lower()
            aranan_varmi = dosya.read().find(aranan) #dosyada arama yapar
        
            if aranan_varmi != -1 : #Sonuç -1 dönmüyorsa kayıt bulunmuştur
                print("eklemek istediğiniz kayıt mevcuttur")

                dosya.close()
            else: #kayıt bulunamadığı durum için ekleme yapılır
                if tampon >0 :
                    dosya=open("kitap.txt")
                    source=dosya.read().splitlines()
                    a=source.index("")
                    dosya.close()
                    with open("kitap.txt", "r+") as f:
                        veri = f.readlines()
                        veri.insert(a, kayit)
                        f.seek(0)
                        f.writelines(veri)
                        tampon=tampon-1
                    with open('silinecekler.txt', 'r') as fin:
                        data = fin.read().splitlines(True)
                    with open('silinecekler.txt', 'w') as fout:
                        fout.writelines(data[1:])
                else:
                    dosya=open("kitap.txt","a")
                    dosya.write(kayit + "\n")
                    dosya.close()



        if islem== 'd': #silme işlemi
            dosya = open("kitap.txt","r+")
            aranan=kayit.lower()
            aranan_varmi = dosya.read().find(aranan)
            if aranan_varmi == -1 :
                print("silmek istediğiniz kayıt mevcut değil") 
                dosya.close()

            else:
                tampon=tampon+1

                inp = open('kitap.txt').read()
                out = open('kitap.txt', 'w')
                replacements = {kayit:'*'+kayit} #seçtiğimiz kaydın başına işaretçi koyar
                for i in replacements.keys():
                      inp = inp.replace(i, replacements[i])
                out.write(inp)
                out.close()

                silinecekler=open('silinecekler.txt','a')
                silinecekler.write(str(ISBN_numarasi) ) #seçilen kaydın ISBN numarasını silinecekler.txt dosyasına yazar 
                silinecekler.write("\n")
                silinecekler.close()


                inp = open('kitap.txt').read() 
                out = open('kitap.txt', 'w')
                replacements = {'*'+kayit: ""} #kitap.txt dosyasındaki silinecek kaydı sildik
                for i in replacements.keys():
                     inp = inp.replace(i, replacements[i])
                out.write(inp)
                out.close()

        if islem == 'u':#güncelleme yapar
                dosya=open("kitap.txt").read()
                if kayit in dosya:

                    inp = open('kitap.txt').read()
                    out = open('kitap.txt', 'w')
                    yeni_numara=input("Yeni ISBN numarasını giriniz")  #güncellemek istediğimiz yeni ISBN numarasını alır
                    replacements = {kayit:kitap_adi+"," + kitap_yazari+ "," + yeni_numara} #güncel kayıt
                    for i in replacements.keys():
                        inp = inp.replace(i, replacements[i])
                    out.write(inp)
                    out.close()
                else:
                    print("Güncellemek istediğiniz kayıt bulunamadı")


        cikis=input("Çıkmak için e ye devam etmek için her hangi bir tuşa basınız")
