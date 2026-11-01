# Pronova English Studio — A2, B1 & B2

All English learning content lives in this folder. The home and progress screens provide an A2/B1/B2 selector. There are 28 lessons: 8 A2, 12 B1 and 8 B2, with Turkish explanations, translated examples, vocabulary and explained quizzes. This study collection does not cover the entire CEFR curriculum.

From the repository root run `python3 -m http.server 8787 --bind 127.0.0.1`, then open http://localhost:8787/english-studio/. No build or installation is required. Open through HTTP, not file://.

Edit `content.json` directly. It is loaded as UTF-8 JSON without compression or a packing step. Schema version is 1. Lessons have stable unique id, level (A2/B1/B2), title, subtitle, category, icon, minutes, words, sections and quiz fields. Quiz answers use zero-based indexes. Do not change existing lesson IDs, because progress uses them.

Progress and the shared vocabulary notebook are stored in localStorage under pronova-english-studio-v1. On the first visit, the old pronova-b1-v1 and pronova-b2-v1 records are merged without deleting the original keys. Migration applies only on the same browser and origin. Existing Studio records take precedence. Completion and latest quiz scores are tracked per lesson; words are deduplicated by spelling. Open-ended practice is not automatically scored.

The homepage links to /english-studio/. The former b1-english and b2-english folders have been removed; update any external bookmarks to the new address.
