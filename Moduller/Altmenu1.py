def hesap_makinesi():
    while True:
        print("\n╔═════════════════════════╗")
        print("║     HESAP MAKİNESİ      ║")
        print("╠═════════════════════════╣")
        print("║ 1 - Toplama             ║")
        print("║ 2 - Çıkarma             ║")
        print("║ 3 - Çarpma              ║")
        print("║ 4 - Bölme               ║")
        print("║ 5 - Üs Alma             ║")
        print("║ 6 - Ana Menüye Dön      ║")
        print("╚═════════════════════════╝")
        secim = input("Bir işlem seçiniz: ")
        if secim == "6":
            return
        try:
            sayi1 = float(input("Birinci sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))
            if secim == "1":
                print("Sonuç:", sayi1 + sayi2)
            elif secim == "2":
                print("Sonuç:", sayi1 - sayi2)
            elif secim == "3":
                print("Sonuç:", sayi1 * sayi2)
            elif secim == "4":
                print("Sonuç:", sayi1 / sayi2 if sayi2 != 0 else "Tanımsız")
            elif secim == "5":
                print("Sonuç:", sayi1 ** sayi2)
            else:
                print("Geçersiz seçim!")
        except ValueError:
            print("Lütfen geçerli bir sayı girin!")

def oyunlar():
    print("\n╔══════════════════════╗")
    print("║       OYUN          ║")
    print("╠══════════════════════╣")
    print("║ 1 - Sayı Tahmin Oyunu║")
    print("║ 2 - Ana Menüye Dön   ║")
    print("╚══════════════════════╝")
    secim = input("Seçiminizi yapınız: ")
    if secim == "1":
        import random
        sayi = random.randint(1, 10)
        tahmin = int(input("1 ile 10 arasında bir sayı tahmin edin: "))
        if tahmin == sayi:
            print("Tebrikler! Doğru tahmin ettiniz.")
        else:
            print(f"Üzgünüm, doğru sayı {sayi} idi.")
    return

def takvim():
    import calendar
    yil = int(input("Yılı girin: "))
    ay = int(input("Ayı girin (1-12): "))
    print(calendar.month(yil, ay))

def not_hesaplama():
    vize = float(input("Vize notunu girin: "))
    final = float(input("Final notunu girin: "))
    ortalama = (vize * 0.4) + (final * 0.6)
    print("Ders ortalamanız:", ortalama)

def doviz_cevirici():
    print("1 USD = 30 TL, 1 EUR = 32 TL, 1 GBP = 37 TL")
    miktar = float(input("Çevrilecek miktarı girin: "))
    print("1 - USD → TL\n2 - EUR → TL\n3 - GBP → TL")
    secim = input("Seçiminizi yapınız: ")
    if secim == "1":
        print("Sonuç:", miktar * 30, "TL")
    elif secim == "2":
        print("Sonuç:", miktar * 32, "TL")
    elif secim == "3":
        print("Sonuç:", miktar * 37, "TL")
    else:
        print("Geçersiz seçim!")

def sicaklik_donusturme():
    print("1 - Celsius → Fahrenheit\n2 - Fahrenheit → Celsius")
    secim = input("Seçiminizi yapınız: ")
    if secim == "1":
        c = float(input("Celsius değerini girin: "))
        print("Sonuç:", (c * 9/5) + 32, "Fahrenheit")
    elif secim == "2":
        f = float(input("Fahrenheit değerini girin: "))
        print("Sonuç:", (f - 32) * 5/9, "Celsius")
    else:
        print("Geçersiz seçim!")

def cizim_araclari():
    print("Bu menü henüz hazır değildir.")