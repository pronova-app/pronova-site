# Pronova English Studio — A2, B1 & B2

All English learning content lives in this folder. The home and progress screens provide an A2/B1/B2 selector. There are 28 lessons: 8 A2, 12 B1 and 8 B2, with Turkish explanations, translated examples, vocabulary and explained quizzes. This study collection does not cover the entire CEFR curriculum.

From the repository root run `python3 -m http.server 8787 --bind 127.0.0.1`, then open http://localhost:8787/english-studio/. No build or installation is required. Open through HTTP, not file://.

Edit `content.json` directly. It is loaded as UTF-8 JSON without compression or a packing step. Schema version is 1. Lessons have stable unique id, level (A2/B1/B2), title, subtitle, category, icon, minutes, words, sections and quiz fields. Quiz answers use zero-based indexes. Do not change existing lesson IDs, because progress uses them.

Progress and the shared vocabulary notebook are stored in localStorage under pronova-english-studio-v1. On the first visit, the old pronova-b1-v1 and pronova-b2-v1 records are merged without deleting the original keys. Migration applies only on the same browser and origin. Existing Studio records take precedence. Completion and latest quiz scores are tracked per lesson; words are deduplicated by spelling. Open-ended practice is not automatically scored.

The homepage links to /english-studio/. The former b1-english and b2-english folders have been removed; update any external bookmarks to the new address.


## B1 lesson format

The 12 B1 lessons use Turkish explanations, English models with Turkish translations, form/comparison tables and 8 vocabulary entries per lesson. Each lesson follows sections 1, 2, 3, 4, 7, 8 and 9 as requested. Each has a 120–180 word English reading passage with highlighted target forms and three English comprehension questions. Lessons are approximately 1,800–2,100 words including bilingual examples and reading translations. Lesson IDs remain stable. B1 quizzes now contain eight original five-option questions per lesson, replacing the former quiz items. Existing progress remains stored; a new quiz attempt updates that lesson’s latest result.

A section may provide `markdown` in place of plain `text`. The built-in renderer supports level-three headings, paragraphs, bold text, unordered lists and pipe tables. Model translations can use a literal <br> in a table cell. All content is escaped before rendering; arbitrary HTML is not accepted. Wide tables scroll within a keyboard-focusable region on small screens. A2/B2 retain their existing section rendering.


## B1 YÖKDİL-style practice

96 original questions: 48 sentence gaps, 12 sentence completions, 12 paragraph completions and 24 reading questions. Each B1 lesson has eight questions with five choices, Turkish explanations for all choices, and a learning note. Reading passages are the original lesson texts. The activity is adapted to B1 general English; it is not an official YÖKDİL paper or a complete exam simulation.

Question fields: stable `id`, `type`, `instruction`, `typeLabel`, `prompt`, five `choices`, zero-based `answer`, `explanation`, five aligned `choiceExplanations`, `tip`, and optional plain-text `passage`. A2/B2 questions retain their original rendering.

Format reference only: https://dokuman.osym.gov.tr/pdfdokuman/2025/YOKDIL-1/ing_sos_bil16022025.pdf. No exam questions or passages were copied.
