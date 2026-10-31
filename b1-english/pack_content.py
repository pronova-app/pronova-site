"""Düzenlenen JSON içeriğini uygulamanın okuduğu gzip dosyasına dönüştürür."""
import gzip
import json
from pathlib import Path
base = Path(__file__).resolve().parent
raw = (base / 'content.json').read_bytes()
content = json.loads(raw)
assert content['schemaVersion'] == 1
assert content['lessons'], 'En az bir ders gerekli'
ids = set()
for lesson in content['lessons']:
    assert lesson['id'] not in ids, 'Ders kimlikleri benzersiz olmalı'
    ids.add(lesson['id'])
    assert lesson['sections'] and lesson['quiz']
    for question in lesson['quiz']:
        assert 0 <= question['answer'] < len(question['choices'])
with gzip.open(base / 'content.json.gz', 'wb') as output:
    output.write(raw)
print(f"{len(ids)} ders paketlendi: content.json.gz")
