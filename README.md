# binance-spot-trade-bot

FED faizi sonucu LUNA coinin çöküşünden sonra botu kapatmak zorunda kaldım ve yayınlamak istedim,

Botun algoritması 200 coinin 1 yıllık verisi indirilerek hazırlanmıştır, uzun vadede(1 yıllık bir süreç) %2300-%10000 kar getirmektedir,

Gerekli moduller:

pip install python-binance

pip install pandas

Log kısmını silmek istemedim fakat LUNA coinin ani düşüşü sebebiyle log yazılarında çok fazla stop yazıldı, çoğunu sildim.

Şu an sadece BTC kullanılıyor fakat yeni coin eklemek isterseniz, dbcreate.py bulunan coinName kısmına coinin adını yazıp 1 kez çalıştırırsanız veritabanına ekleyecektir ve çalışmasını sağlayacaktır.

Apilere spot yetkisi vermeniz gerekmektedir, apiler BTC.py dosyasının içine yazılacaktır.

Son olarak başlatmak için BTC.py dosyasını çalıştırabilirsiniz.(apisiz çalışmaz nasıl api alacağınızı bilmiyorsanız https://www.binance.com/tr/support/faq/360002502072)

Daha fazla detay almak isterseniz Discord: Sezar#6699
