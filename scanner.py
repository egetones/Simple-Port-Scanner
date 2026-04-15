#!/usr/bin/env python3
import socket
import sys
from datetime import datetime

# Hedef IP'yi belirle
# Kullanıcıdan input alalım veya statik verelim.
# Gelişmiş versiyonda 'argparse' kullanabiliriz ama şimdilik mantığı görelim.

def scan_target(target):
    try:
        # Hostname'i IP adresine çevir (DNS Çözümleme)
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Hata: Hostname çözümlenemedi.")
        sys.exit()

    print("-" * 50)
    print(f"Hedef Taranıyor: {target_ip}")
    print(f"Başlangıç Zamanı: {str(datetime.now())}")
    print("-" * 50)

    try:
        # 1'den 100'e kadar olan portları tara (Test için kısa tuttuk)
        # İstersen range(1, 65535) yapabilirsin ama çok uzun sürer.
        # Genelde kritik portlar: 21, 22, 80, 443, 3306 vs.
        for port in range(1, 101): 
            
            # IPv4 ve TCP kullanacağımızı belirtiyoruz
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Hızlanmak için timeout (zaman aşımı) koyuyoruz.
            # 1 saniye içinde cevap gelmezse kapalı varsay.
            s.settimeout(1)
            
            # Bağlantı denemesi (connect_ex hata kodu döndürür, connect hata fırlatır)
            # 0 dönerse bağlantı başarılı (Port AÇIK) demektir.
            result = s.connect_ex((target_ip, port))
            
            if result == 0:
                print(f"Port {port}: AÇIK")
            
            s.close() # Bağlantıyı kapat

    except KeyboardInterrupt:
        print("\nKullanıcı işlemi iptal etti.")
        sys.exit()
    
    except socket.error:
        print("\nSunucuya bağlanılamadı.")
        sys.exit()

    print("-" * 50)
    print("Tarama Tamamlandı.")

if __name__ == "__main__":
    # Kullanıcıdan hedef iste
    host = input("Taranacak IP veya Adres girin (Örn: scanme.nmap.org): ")
    scan_target(host)
