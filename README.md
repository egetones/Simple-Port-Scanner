# Simple Python Port Scanner 📡

Bu proje, Python'un yerel `socket` kütüphanesini kullanarak hedef IP üzerindeki açık portları tespit eden bir ağ keşif aracıdır.

## 🎯 Amaç
Bilişim güvenliği eğitimim kapsamında;
- **TCP/IP** bağlantı mantığını (3-way handshake),
- **Socket** programlamayı,
- Ağ üzerindeki servislerin nasıl dinlendiğini anlamak amacıyla geliştirilmiştir.

## ⚙️ Özellikler
- Belirtilen hedef IP adresini tarar.
- Yaygın portları (veya belirtilen aralığı) kontrol eder.
- Bağlantı zamanını (Timestamp) gösterir.
- Açık portları ve servisleri raporlar.

## ⚠️ Yasal Uyarı (Disclaimer)
Bu araç yalnızca eğitim ve test amaçlıdır. Sadece sahibi olduğunuz veya izniniz olan ağlarda kullanınız. İzinsiz port taraması yasal suç teşkil edebilir.

## 🚀 Kullanım

```bash
git clone [https://github.com/KULLANICI_ADIN/simple-port-scanner.git](https://github.com/KULLANICI_ADIN/simple-port-scanner.git)
cd simple-port-scanner
python3 scanner.py
