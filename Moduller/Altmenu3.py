def hava_durumu():
    print("\n╔══════════════════════╗")
    print("║     HAVA DURUMU      ║")
    print("╠══════════════════════╣")
    print("║ 1 - Şehir 1          ║")
    print("║ 2 - Şehir 2          ║")
    print("║ 3 - Ana Menüye Dön   ║")
    print("╚══════════════════════╝")
    secim = input("Seçiminizi yapınız: ")
    if secim == "1":
        print("Şehir 1 hava durumu gösteriliyor...")
    elif secim == "2":
        print("Şehir 2 hava durumu gösteriliyor...")
    elif secim == "3":
        return
    else:
        print("Geçersiz seçim!")
        hava_durumu()