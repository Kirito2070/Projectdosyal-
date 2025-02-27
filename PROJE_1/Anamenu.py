import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Moduller.Altmenu1 as Altmenu1
import Moduller.Altmenu2 as Altmenu2
import Moduller.Altmenu3 as Altmenu3
import sys

def anamenu():
    while True:
        print("\n╔════════════════════════════════╗")
        print("║      PYTHON PROJE MENÜSÜ       ║")
        print("╠════════════════════════════════╣")
        print("║ 1 - HESAP MAKİNESİ             ║")
        print("║ 2 - OYUNLAR                    ║")
        print("║ 3 - ÇİZİM ARAÇLARI             ║")
        print("║ 4 - TAKVİM                     ║")
        print("║ 5 - NOT HESAPLAMA              ║")
        print("║ 6 - DÖVİZ ÇEVİRİCİ             ║")
        print("║ 7 - SICAKLIK DÖNÜŞTÜRME        ║")
        print("║ 8 - HARİTALAR                  ║")
        print("║ 9 - HAVA DURUMU                ║")
        print("║ 10 - ÇIKIŞ                     ║")
        print("╚════════════════════════════════╝")
        secim = input("Lütfen seçiminizi yapınız: ")
        if secim == "1":
            Altmenu1.hesap_makinesi()
        elif secim == "2":
            Altmenu1.oyunlar()
        elif secim == "3":
            Altmenu1.cizim_araclari()
        elif secim == "4":
            Altmenu1.takvim()
        elif secim == "5":
            Altmenu1.not_hesaplama()
        elif secim == "6":
            Altmenu1.doviz_cevirici()
        elif secim == "7":
            Altmenu1.sicaklik_donusturme()
        elif secim == "8":
            Altmenu2.haritalar()
        elif secim == "9":
            Altmenu3.hava_durumu()
        elif secim == "10":
            print("Çıkış yapılıyor...")
            sys.exit()
        else:
            print("Geçersiz seçim, tekrar deneyin.")

anamenu()