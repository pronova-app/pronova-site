# Pronova B1 English Studio

Mavi-indigo temalı, Türkçe konu anlatımlı yerel web uygulaması. 12 B1 konusu, 84 açıklamalı soru, 72 anlatım bölümü ve 96 kaydedilebilir kelime içerir. İlerleme yalnızca bu tarayıcının localStorage alanında tutulur. Harici hesap veya sunucu veritabanı yoktur.

## Çalıştırma

```bash
cd /home/omers/Documents/workspace/pronova-b1
python3 -m http.server 8787 --bind 127.0.0.1
```

Tarayıcıda http://localhost:8787 adresini açın. Sunucuyu durdurmak için Ctrl+C kullanın. Dosyaya çift tıklamak fetch erişimi nedeniyle çalışmaz. Kurulum veya derleme gerekmez. Google Fonts erişilemezse sistem yazı tipi kullanılır; dersler yereldir.

## İçerik

Uygulama içerikleri **content.json.gz** dosyasından okur. Bu dosya gzip ile sıkıştırılmış UTF-8 JSON'dur. Tarayıcı DecompressionStream API'si ile açar. Sunucu Content-Encoding: gzip başlığı eklerse tarayıcının açtığı düz JSON da desteklenir.

Düzenlemek için `content.json` kaynak dosyasını değiştirin ve çalıştırın:

```bash
python3 pack_content.py
```

Şema: `schemaVersion: 1`, `lessons: []`. Her derste `id`, `title`, `subtitle`, `category`, `icon`, `minutes`, `words`, `sections`, `quiz` alanları vardır. Her bölüm `title`, `text`, isteğe bağlı `formula`, `examples` (en/tr), `tip` taşır. Her soruda `prompt`, `choices`, **sıfırdan başlayan** `answer` ve `explanation` bulunur. Kelimeler `word` ve `meaning` alanlarından oluşur. Aynı şema ile yeni ders eklenebilir; arayüz kendiliğinden listeler.

## Kapsam

Present Perfect; First & Second Conditional; Must, Have to & Should; Relative Clauses. Bu bir çalışır tasarım prototipidir; tüm B1 müfredatı değildir. Soru yanıtı seçildikten sonra açıklama gösterilir. Mini testi bitirmek konuyu tamamlandı olarak işaretler; yanlış cevap varsa yeniden çözmek mümkündür. İlerleme ekranı her dersin son denemesini gösterir.


## Genişletilmiş kütüphane

Present Perfect; First & Second Conditional; Must, Have to & Should; Relative Clauses; Past Simple & Past Continuous; Will, Going to & Present Continuous; Passive Voice; Reported Speech; Gerunds & Infinitives; Comparatives & Superlatives; Linking Words; Travel English.


## İçerik v3

Her konu altı bölüm, yedi açıklamalı soru ve sekiz kelime içerir. Temel anlatıma bağlamlı diyalog/okuma, yaygın hata analizi ve üretim odaklı tekrar etkinliği eklenmiştir. Ders başında bölüm bağlantıları vardır. Toplam tahmini anlatım süresi 227 dakikadır; süreler okuma/çalışma tahminidir. Konuşma etkinlikleri kendi kendine prova içindir; ses kaydı veya otomatik telaffuz puanlaması yapılmaz.
