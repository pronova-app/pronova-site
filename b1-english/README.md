# Pronova English Studio — A2 & B1

Mavi-indigo temalı, Türkçe konu anlatımlı web uygulaması. Ana ekranda ve ilerleme ekranında A2/B1 seçimi vardır. Konular, süreler ve test sonuçları seçili seviyeye göre listelenir. Kelime defteri her iki seviye için ortaktır. Eski B1 ilerleme kayıtları korunur.

| Seviye | Konu | Anlatım bölümü | Açıklamalı soru | Kelime girdisi |
| --- | ---: | ---: | ---: | ---: |
| A2 | 8 | 32 | 40 | 48 |
| B1 | 12 | 72 | 84 | 96 |
| Toplam | 20 | 104 | 124 | 144 |

Kelime sayısı derslerdeki girdilerin toplamıdır; defter aynı kelimeyi iki kez kaydetmez. Bu bir eğitim prototipidir, seviyelerin tüm müfredatını kapsamaz.

## Yerel çalıştırma

```bash
cd /home/omers/Documents/workspace/pronova-b1
python3 -m http.server 8787 --bind 127.0.0.1
```

http://localhost:8787 adresini açın. Kurulum veya derleme gerekmez. Dosyaya çift tıklamak fetch erişimi nedeniyle çalışmaz. Google Fonts erişilemezse sistem yazı tipi kullanılır. İlerleme yalnızca aynı tarayıcı/origin içindeki localStorage alanında tutulur; sunucuya gönderilmez.

## İçerik ve düzenleme

Uygulama UTF-8 JSON içeren `content.json.gz` dosyasını okur ve DecompressionStream ile açar. Sunucu Content-Encoding: gzip eklerse tarayıcının açtığı düz JSON da desteklenir.

`content.json` dosyasını değiştirip çalıştırın:

```bash
python3 pack_content.py
```

Şema: `schemaVersion: 1`, `lessons: []`. Her ders `id`, `level` (A2/B1), `title`, `subtitle`, `category`, `icon`, `minutes`, `words`, `sections`, `quiz` içerir. Eski içerikte level yoksa B1 kabul edilir. Kimlikler benzersiz ve kalıcı olmalıdır; kayıtlı ilerleme id ile eşleşir. Bölümlerde title/text, isteğe bağlı formula/examples(en,tr)/tip bulunur. Sorularda prompt/choices/sıfır tabanlı answer/explanation vardır. Kelimeler word/meaning alanlarını taşır.

## A2 konuları

Be & Have Got; Present Simple; Present Continuous; Past Simple; Some, Any, Much & Many; A, An, The & No Article; Prepositions of Time & Place; Everyday Requests & Shopping.

## B1 konuları

Present Perfect; First & Second Conditional; Must, Have to & Should; Relative Clauses; Past Simple & Past Continuous; Will, Going to & Present Continuous; Passive Voice; Reported Speech; Gerunds & Infinitives; Comparatives & Superlatives; Linking Words; Travel English.

Her derste Türkçe anlatımlar, çevirili örnekler, hata ipuçları ve açıklamalı mini test bulunur. Uzun derslerde bölüm bağlantıları kullanılabilir. Mini testi bitirmek konuyu tamamlandı olarak işaretler. İlerleme ekranı seçili seviyedeki her dersin son denemesini gösterir. Konuşma/çeviri provalarında otomatik telaffuz veya serbest cevap puanlaması yoktur. Süreler tahminidir.

Bu klasör web sürümüdür. Ayrı native Java Android projesi ve APK bu klasöre dahil değildir.
