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
        "`not_run`",
        "`needs_recheck`",
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


def check_evidence_contract() -> list[str]:
    errors: list[str] = []
    required_markers = {
        "SKILL.md": (
            "`pass`, `fail`, or `not_run`",
            "repository revision or other stable artifact identity",
            "`needs_recheck`",
        ),
        "references/artifacts.md": (
            "A `not_run` result does not prove code correctness.",
            "Applicable behavior, path, or subsystem:",
            "Repository revision",
            "`needs_recheck`",
        ),
        "references/coaching-and-review.md": (
            "a documented limitation does not turn `not_run` into evidence",
            "mark its validity `needs_recheck`",
        ),
        "examples/atomic-task-card.md": (
            "A `not_run` result does not prove that the code is correct.",
            "Repository revision or other stable artifact identity.",
            "`needs_recheck`",
        ),
        "examples/atomic-task-card.zh-CN.md": (
            "`not_run` 不能证明代码正确。",
            "仓库 revision 或其他稳定的产物标识。",
            "`needs_recheck`",
        ),
    }

    for relative_path, markers in required_markers.items():
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                errors.append(
                    f"{relative_path}: missing evidence-contract marker {marker!r}"
                )

    return errors


def main() -> int:
    errors = check_local_links() + check_readme_pair() + check_evidence_contract()
    if errors:
        print("Project validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print(
        "Project validation passed: local links, bilingual README coverage, "
        "and the evidence contract are intact."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
