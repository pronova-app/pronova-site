# Business English — İlk Ay

A responsive static web module inspired by the supplied mobile design. Source content is adapted from Business_English_Ilk_Ay_Rehberi.docx: 19 topics, 481 bilingual phrase entries, explanatory notes, dialogues, email samples, grammar and the four-week / 30-day plan. Two-column reference tables remain available in the reading view; only three-column English/Turkish/usage rows are turned into flashcards. The document’s mini exam and answer key remain a reading exercise; the Practice tab separately generates 10-question meaning quizzes.

Run `python3 -m http.server 8787 --bind 127.0.0.1` from the repository root and open http://localhost:8787/business-english/. No dependencies or build step. Content loads from content.json via HTTP.

Navigation: Today (real learned counts and seven-day activity), Topics (search/category filter, full reading), Practice (20 flashcards or 10 shuffled questions, selectable topic), Plan (four weekly checkboxes and day-30 review), More (goal, start date, speech accent/rate and confirmed reset).

State is stored only in localStorage under pronova-business-v1. Clicking “Biliyorum” or answering correctly marks an expression learned; repeat answers do not increment learning counts again. Repeat cards advance without marking knowledge. Weekly completion is manual, independent of phrase learning. Activity records new learning events, not current mastery. Other English Studio progress is separate.

Speech uses the browser’s speechSynthesis with en-GB/en-US and normal/slow speed. Availability depends on the device; errors and unsupported browsers display a message. No audio assets or external speech API are used. Open-ended speaking/writing is not automatically evaluated. Source examples are educational, not employment-policy guidance; titles and workplace customs vary.

The source tense label for “How long have you been with the company?” is corrected to Present Perfect Simple. The reference document and preview image are not included in the repository.

Validation: JavaScript syntax; source schema and unique IDs; all 19 topic routes, search, cards, generated quiz completion, learned-item deduplication and persistence, week completion, unsupported-speech fallback. Browser smoke checks cover mobile home, card flip/learn, quiz feedback and plan rendering. Actual audio output was not verified.
