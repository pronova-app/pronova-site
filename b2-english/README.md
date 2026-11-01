# Pronova English Studio — B2

Türkçe açıklamalar, çevirili örnekler ve açıklamalı mini testler içeren üst orta seviye modül.
8 ders, 16 anlatım bölümü, 32 soru ve 32 kelime girdisi içerir. Tahmini toplam çalışma süresi 120 dakikadır.
Bu bir çalışma modülüdür; tüm B2 müfredatını kapsadığı veya sertifika sağladığı iddia edilmez.

## Çalıştırma

Depo kökünde `python3 -m http.server 8787 --bind 127.0.0.1` çalıştırın ve
http://localhost:8787/b2-english/ adresini açın. Derleme veya paket kurulumu gerekmez.

## İçerik

`content.json` doğrudan yüklenir; gzip üretmek gerekmez. Şema mevcut English Studio ile aynıdır:
`schemaVersion: 1`; her derste benzersiz `id`, `level: B2`, `title`, `subtitle`, `category`,
`icon`, `minutes`, `words`, `sections`, `quiz` alanları bulunur. Soruların `answer` alanı sıfır tabanlıdır.

Dersler: Perfect Simple & Continuous; Third & Mixed Conditionals; Modals of Deduction;
Advanced Passive & Causative; Relative & Participle Clauses; Reported Speech & Reporting Verbs;
Linking Ideas & Arguments; Workplace Discussions & Collocations.

İlerleme ve kelimeler `pronova-b2-v1` localStorage anahtarında yalnızca bu tarayıcıda saklanır.
A2/B1 kayıtlarından bağımsızdır. Her test bitince tamamlanma ve son sonuç kaydedilir;
kelimeler eklenip kaldırılabilir. Açık uçlu prova otomatik puanlanmaz.
Ana sayfa ve A2/B1 Studio bu modüle bağlantı verir. Modül de her ikisine geri bağlantı içerir.
