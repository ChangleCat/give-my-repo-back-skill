#!/usr/bin/env python3
"""Validate repository-local links and bilingual README coverage."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent.parent
LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def check_local_links() -> list[str]:
    errors: list[str] = []
    for document in sorted(ROOT.rglob("*.md")):
        if ".git" in document.parts:
            continue
        text = document.read_text(encoding="utf-8")
        for raw_target in LINK_PATTERN.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            relative_path = unquote(target.split("#", 1)[0])
            resolved = (document.parent / relative_path).resolve()
            if not resolved.exists():
                errors.append(
                    f"{document.relative_to(ROOT)}: missing local link target {target!r}"
                )
    return errors


def check_readme_pair() -> list[str]:
    errors: list[str] = []
    english = (ROOT / "README.md").read_text(encoding="utf-8")
    chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")

    shared_markers = (
        "ChangleCat/give-my-repo-back-skill --skill give-my-repo-back-skill",
        "skills-ref==0.1.1",
        "actions/workflows/validate.yml",
        "docs/repo-ownership/",
    )
    for marker in shared_markers:
        if marker not in english:
            errors.append(f"README.md: missing shared marker {marker!r}")
        if marker not in chinese:
            errors.append(f"README.zh-CN.md: missing shared marker {marker!r}")

    mirrored_sections = (
        ("## Install", "## 安装"),
        ("## Start your first session", "## 开始第一次学习"),
        ("## How a session works", "## 一轮任务如何进行"),
        ("## Documents and resuming work", "## 生成文档与跨会话续接"),
        ("## Harness compatibility", "## Harness 兼容性"),
        ("## Validation", "## 校验"),
        ("## Project contents", "## 项目结构"),
        ("## Contribute", "## 参与贡献"),
        ("## License", "## 许可证"),
    )
    for english_heading, chinese_heading in mirrored_sections:
        if english_heading not in english:
            errors.append(f"README.md: missing section {english_heading!r}")
        if chinese_heading not in chinese:
            errors.append(f"README.zh-CN.md: missing section {chinese_heading!r}")

    return errors


def main() -> int:
    errors = check_local_links() + check_readme_pair()
    if errors:
        print("Project validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print("Project validation passed: local links and bilingual README coverage are intact.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
