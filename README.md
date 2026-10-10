Проект Qadam London: генерация видео для Instagram.

Сайт с последним прогоном: https://timnygmetov-ctrl.github.io/generationvideo/

## Как пользоваться

Напишите в чате Claude в этой папке:

```
/reels как открыть bank account в UK
```

Получите:

- `scenario.md` — сценарий Reels на 30–45 секунд: кадры, закадровый голос, текст на экране, подпись к посту;
- `prompts/scene-01.md` … — готовый промпт для 3D-кадра на каждую сцену (копировать блок **Prompt**);
- `prompts/prompts.json` — все промпты одним файлом для API.

Прошлый прогон при этом не пропадает: он переносится в `archive/`.

## Что где лежит

- `.claude/skills/reels/SKILL.md` — правила помощника: тон, структура, границы проекта;
- `.claude/skills/reels/style-guide.md` — стиль картинок и внешность героев (Айгерим, Азиз);
- `tools/check_prompts.py` — проверка промптов и сборка `prompts.json`.
