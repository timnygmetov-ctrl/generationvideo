#!/usr/bin/env python3
"""Проверяет scenario.md и prompts/scene-NN.md и собирает prompts/prompts.json.

Запуск: python3 tools/check_prompts.py [папка_проекта]
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
STYLE_GUIDE = ROOT / ".claude" / "skills" / "reels" / "style-guide.md"

MIN_SCENES, MAX_SCENES = 4, 6
MIN_WORDS, MAX_WORDS = 90, 220
FORBIDDEN = [
    r"[Ѐ-ӿ]",            # кириллица
    r"<[^>]*>", r"\[[^\]]*\]",     # плейсхолдеры
    r"\bTODO\b", r"\binsert\b",
    r"\bNHS\b", r"\bHome Office\b",  # модель нарисует логотип
]


def text_block(md: str, heading: str) -> str | None:
    """Содержимое первого блока ```text после заголовка ## heading."""
    m = re.search(rf"^## {re.escape(heading)}\s*\n+```text\n(.*?)\n```", md, re.S | re.M)
    return m.group(1).strip() if m else None


def style_anchor() -> str:
    md = STYLE_GUIDE.read_text(encoding="utf-8")
    return text_block(md, "Якорь стиля (STYLE)") or ""


def main() -> int:
    errors: list[str] = []

    if not (ROOT / "scenario.md").is_file():
        errors.append("нет scenario.md")

    scenes = sorted((ROOT / "prompts").glob("scene-*.md"))
    if not MIN_SCENES <= len(scenes) <= MAX_SCENES:
        errors.append(f"сцен {len(scenes)}, нужно {MIN_SCENES}–{MAX_SCENES}")

    expected = [f"scene-{i:02d}.md" for i in range(1, len(scenes) + 1)]
    if [p.name for p in scenes] != expected:
        errors.append(f"номера сцен идут не подряд: {[p.name for p in scenes]}")

    anchor = style_anchor()
    out = []
    for path in scenes:
        md = path.read_text(encoding="utf-8")
        prompt = text_block(md, "Prompt")
        negative = text_block(md, "Negative prompt")
        if not prompt:
            errors.append(f"{path.name}: нет блока Prompt")
            continue
        if not negative:
            errors.append(f"{path.name}: нет блока Negative prompt")
        if anchor and not prompt.startswith(anchor):
            errors.append(f"{path.name}: промпт не начинается с якоря стиля")
        if "\n" in prompt:
            errors.append(f"{path.name}: промпт должен быть одним абзацем")
        words = len(prompt.split())
        if not MIN_WORDS <= words <= MAX_WORDS:
            errors.append(f"{path.name}: {words} слов, нужно {MIN_WORDS}–{MAX_WORDS}")
        for pattern in FORBIDDEN:
            hit = re.search(pattern, prompt, re.I)
            if hit:
                errors.append(f"{path.name}: недопустимое в промпте: {hit.group(0)!r}")
        title = re.search(r"^# (.+)$", md, re.M)
        shot = re.search(r"^\*\*Что в кадре:\*\*\s*(.+)$", md, re.M)
        out.append({
            "scene": int(path.stem.split("-")[1]),
            "title": title.group(1).strip() if title else path.stem,
            "shot_ru": shot.group(1).strip() if shot else "",
            "prompt": prompt,
            "negative_prompt": negative or "",
            "aspect_ratio": "9:16",
            "size": "1080x1920",
        })

    if errors:
        print("ОШИБКИ:")
        for e in errors:
            print(" -", e)
        return 1

    target = ROOT / "prompts" / "prompts.json"
    target.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"OK: {len(out)} сцен, собрано в {target.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
