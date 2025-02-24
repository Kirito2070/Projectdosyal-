def haritalar():
    print("\n╔══════════════════════╗")
    print("║       HARİTALAR      ║")
    print("╠══════════════════════╣")
    print("║ 1 - Harita 1         ║")
    print("║ 2 - Harita 2         ║")
    print("║ 3 - Ana Menüye Dön   ║")
    print("╚══════════════════════╝")
    secim = input("Seçiminizi yapınız: ")
    if secim == "1":
        print("Harita 1 gösteriliyor...")
    elif secim == "2":
        print("Harita 2 gösteriliyor...")
    elif secim == "3":
        return
    else:
        print("Geçersiz seçim!")
        haritalar()