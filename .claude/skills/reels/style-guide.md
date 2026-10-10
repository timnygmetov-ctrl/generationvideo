# Визуальный стиль и герои Qadam Reels

Этот файл задаёт то, что одинаково во всех роликах. Блоки в рамках `text` вставляются
в промпты **дословно**, слово в слово: только так нейросеть рисует одних и тех же героев
в одном стиле от кадра к кадру.

## Якорь стиля (STYLE)

Каждый промпт начинается с этой строки:

```text
Stylized 3D animated film still, soft rounded character design, expressive friendly faces, gentle subsurface skin shading, warm cinematic lighting, shallow depth of field, clean uncluttered background, muted warm palette with deep navy and soft aqua accents, high-detail render, vertical 9:16 composition.
```

## Постоянные герои

Внешность героя в промпте повторяется полностью, в каждой сцене, где он есть.
Сервисы генерации не помнят прошлые кадры.

**Айгерим** (из Казахстана). Главная героиня по умолчанию.

```text
Aigerim, a 28-year-old Kazakh woman with warm light-brown skin, almond-shaped dark eyes and straight black hair in a low ponytail, wearing a mustard-yellow knitted cardigan over a white t-shirt, dark blue jeans, white sneakers and small silver earrings
```

**Азиз** (из Узбекистана). Второй герой: друг из сообщества или герой отдельного ролика.

```text
Aziz, a 34-year-old Uzbek man with tan skin, short black hair, a neat short beard and kind tired eyes, wearing a navy hooded jacket over a grey sweater, dark trousers and a black backpack
```

Второстепенные персонажи (врачи, администраторы, соседи) — британцы разного
происхождения, приветливые, в нейтральной одежде без логотипов. Описывать коротко:
`a friendly receptionist in a plain teal uniform`.

## Британская среда

Узнаваемо, но без брендов: красный кирпич, террасные дома, мокрый асфальт после дождя,
двухэтажный красный автобус вдали, бело-голубые вывески клиники **без читаемого текста**.
Временное жильё — маленькая, но чистая комната, без убогости.

## Негативный промпт (по умолчанию)

```text
text, letters, words, captions, subtitles, watermark, logo, brand names, readable signs, flags, national symbols, police, border force uniforms, handcuffs, distorted hands, extra fingers, deformed face, photorealistic, live-action photo, horror, gloomy dark mood, caricature, stereotypical costume, blurry, low quality
```

## Почему так

- **Без текста в кадре.** Нейросети рисуют буквы криво. Субтитры и надписи
  накладываются при монтаже из `scenario.md`.
- **Без флагов, полиции, логотипов Home Office и NHS.** Зрители могут быть в уязвимом
  положении: кадр не должен пугать или выдавать страну героя. Настоящие логотипы
  к тому же чужая торговая марка.
- **Английский язык промпта.** Модели генерации картинок понимают английский
  заметно лучше русского.
- **Палитра словами, не кодами.** Фирменные цвета `#0E2438` и `#7BE0F2` модели не читают
  как цвета, поэтому в STYLE они записаны как «deep navy» и «soft aqua».
