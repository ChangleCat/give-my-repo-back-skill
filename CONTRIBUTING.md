# Contributing / 参与贡献

Contributions should help people understand their own repositories through work they perform. Keep the instructions portable and the task design concrete.

欢迎帮助人通过亲手实践掌握仓库的贡献。请保持指令可移植，让任务设计具体、可执行。

## Useful changes / 欢迎的改进

- Improve task scope, evidence requirements, hints, or review questions.
- Correct instructions that cause English-only artifacts or accidental AI takeover.
- Document observed harness behavior without claiming untested support.
- Keep English and Simplified Chinese READMEs and examples in sync.

- 改进任务粒度、证据要求、提示方式和验收问题。
- 修复导致文档只用英文或 AI 不经意代做的指令。
- 记录实际观察到的 harness 行为，避免声称未经测试的支持。
- 同步维护中英文 README 和示例。

## Before opening a pull request / 提交 PR 前

Read `SKILL.md` and the affected references. Explain the concrete behavior your change improves and include a small example when useful. Keep tool-specific integrations optional. Do not add a runtime dependency just to express a workflow in Markdown.

请阅读 `SKILL.md` 及受影响的参考文档，说明修改改善了什么具体行为，必要时提供小例子。工具专属适配应保持可选；用 Markdown 即可表达的流程无需增加运行时依赖。

Check relative links, YAML frontmatter, and consistency between the entrypoint and references. If you run an agent session, report the harness/version, request language, observed result, and limits of the check. Static document review and runtime evaluation are different forms of evidence; describe what you actually did. Cross-harness testing is welcome but not required for documentation contributions.

Before submitting, run `agentskills validate` as documented in the README and `python scripts/validate_project.py`.

检查相对链接、YAML 元数据以及入口与参考文件的一致性。如果实际运行了 agent 会话，请记录 harness 及版本、请求语言、观察结果和验证范围。静态文档检查与运行验证是不同证据，应如实说明做过的检查。欢迎跨 harness 测试，但文档贡献不要求执行此类测试。

提交前，请按 README 说明运行 `agentskills validate`，并执行 `python scripts/validate_project.py`。

## Report a problem / 报告问题

Use the issue template. Include a minimal prompt and relevant output, with private project details removed. Describe what the agent did, what the person was supposed to do, and whether hints or implementation were explicitly requested.

请使用 Issue 模板，提供最小提示词与相关输出，并移除私有项目信息。说明 agent 做了什么、原本应该由人做什么，以及是否明确要求过提示或代写。

## License / 许可

Contributions are provided under this project's [MIT license](LICENSE).

贡献内容沿用本项目的 [MIT 许可证](LICENSE)。
