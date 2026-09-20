# Give My Repo Back!

**让 AI 出任务，让人亲手做工程，一步步夺回对仓库的掌握。**

[English](README.md) | 简体中文

[![校验 Skill](https://github.com/ChangleCat/give-my-repo-back-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/ChangleCat/give-my-repo-back-skill/actions/workflows/validate.yml)

Vibe coding 之后，项目能跑了，你却未必能解释它是怎么跑的。架构是 AI 选的，代码是 AI 写的，故障也是 AI 修的。准备把项目写进简历时，面对“为什么这么设计”“这里坏了怎么查”，心里难免没底。

Give My Repo Back! 把 AI 对仓库的理解转化为人的实践任务：agent 调查项目、整理真实需求、拆出原子任务卡，由你亲自阅读、预测、研究、实现、验证和解释。AI 负责辅导与审阅，你负责完成工程工作和作出决策。

Skill ID：`give-my-repo-back-skill`

## 你会得到什么

- 有文件、符号和运行行为作为依据的仓库理解文档。
- 包含验收场景、约束和待研究决策的需求说明。
- 带依赖关系的学习路线，以及每次只激活一张的原子任务卡。
- 遇到困难时逐级提供的提示。
- 对实现结果和理解程度的双重审阅。
- 记录已掌握能力、AI 帮助程度和待补知识的学习档案。
- 基于你实际做过的工作进行的面试演练。
- 没有准备好具体需求时，由 agent 主动提供的开始菜单。
- 从运行项目、追踪路径到完成一次可观察修改的零基础路线。
- 在绘制系统切片有助于理解时，由人亲手完成、以证据支撑的运行时流程图。
- 每张活动任务卡提供粗略投入估计和一个明确的前五分钟动作。

**生成的学习文档使用你的语言。** 用简体中文提出需求，agent 就应当用简体中文编写文档标题、正文、表格、提示和验收反馈。代码标识符、路径与机器可读字段名保留原样。

## 安装

### 使用 Skills CLI

需要安装 Node.js/npm，并能运行 `npx`。在你准备学习的项目目录中执行。

```sh
npx skills add ChangleCat/give-my-repo-back-skill --skill give-my-repo-back-skill
```

按照安装器提示选择 agent 和安装范围。例如，全局安装到 OpenCode：

```sh
npx skills add ChangleCat/give-my-repo-back-skill --skill give-my-repo-back-skill --agent opencode --global
```

如果已经把本项目下载到本地，也可以使用绝对路径安装：

```sh
npx skills add /absolute/path/to/give-my-repo-back-skill --skill give-my-repo-back-skill
```

查看、更新或卸载：

```sh
npx skills list
npx skills update give-my-repo-back-skill
npx skills remove give-my-repo-back-skill
```

卸载全局安装时添加 `--global`。手动复制安装的版本，通过替换或移除它的专用 skill 文件夹管理。命令和 agent 标识以 [Skills CLI 官方说明](https://github.com/vercel-labs/skills#readme) 为准。

### 手动安装

从 GitHub 下载本项目 ZIP 或克隆仓库，把 `SKILL.md` 和完整的 `references/` 目录放入你的 harness 所规定的技能目录，子文件夹名称为 `give-my-repo-back-skill`。再分发时附上 `LICENSE`。`agents/` 为可选元数据，运行时不需要 README 和示例文件。

例如，OpenCode 官方文档规定项目级目录为 `.opencode/skills/`，用户级目录为 `~/.config/opencode/skills/`。项目级安装结构如下，详见 [OpenCode 技能文档](https://opencode.ai/docs/skills/)。

```text
your-project/
└── .opencode/skills/give-my-repo-back-skill/
    ├── SKILL.md
    ├── LICENSE
    └── references/
        ├── artifacts.md
        ├── coaching-and-review.md
        └── system-map.md
```

不同 harness 的技能目录和激活规则可能不同，请按对应工具的文档安装。按工具要求重新加载技能或开启新会话。

### 不支持原生 skill 加载时

把完整 skill 文件夹放在 agent 可以读取的位置，然后告诉它：

```text
请读取 /absolute/path/to/give-my-repo-back-skill/SKILL.md，
并按需读取它引用的文件，把这个流程应用到我当前的项目。
由你设计任务，我亲自研究和实现。所有学习文档用简体中文。
```

如果界面不支持读取文件，可以将 `SKILL.md` 和引用的文档作为上下文提供，再按需提供项目文件。agent 应明确说明哪些证据无法亲自检查。

## 开始第一次学习

打开你想掌握的项目，在请求中指定这个 skill：

```text
使用 give-my-repo-back-skill，帮我从这个仓库里找一个小而有价值的改进，
让我通过亲手完成它理解项目的请求链路。把需求说明和原子任务卡
用简体中文写到 docs/repo-ownership/，先给我第一张卡，由我实现。
```

如果你已经有需求：

```text
使用 give-my-repo-back-skill。我想亲自给任务列表添加分页。
请调查现状、写清需求并拆成原子任务卡，相关文档用简体中文。
让我自己研究并作出设计决策。
```

如果你正在准备面试：

```text
使用 give-my-repo-back-skill，帮我掌握这个项目的认证模块。
给我安排实际的研究和修改任务，再针对我真正完成的工作做面试追问。
文档和问答都用简体中文。
```

不同 harness 的原生调用语法不一致；直接指定 skill 名称或文件路径，可以避免依赖某个工具的斜杠命令或专属界面。

如果你只加载了 skill、还没有想好具体需求，agent 应主动提供四种入口：带着已有需求开始、让它扫描仓库并推荐、指定一个想掌握的模块，或者续接以前的任务。拿不准时，直接选择它推荐的仓库扫描即可。

## 一轮任务如何进行

1. **选定目标。** 提供需求、指定模块，或者让 agent 寻找有价值的工作。
2. **阅读说明。** 理解现有行为、预期结果、约束和待决策问题。
3. **领取一张卡。** 动手前先预测行为，提出自己的方案。
4. **亲手完成。** 阅读、修改、验证；卡住时请求提示。
5. **提交证据。** 带回 diff、运行输出、执行路径或观察结果。
6. **解释清楚。** 说明流程、设计理由，以及一个失败场景或替代方案。
7. **继续推进。** agent 更新学习档案，并根据真实进展调整下一张卡。

代码能运行只是验收的一部分。你还需要讲明白这张卡要教会你的内容。如果你要求 AI 代写，它会记录帮助范围，并建议安排后续练习来补齐理解。

如果你对仓库几乎一无所知，最初几张卡应带你运行一项已有检查、找到入口、追踪一条路径、画出小型系统图，再完成一个风险较低且能观察结果的修改。系统图默认采用“带编号的运行时流程图 + 证据索引”：先由你画预测稿，再根据仓库证据修订，最后用自己的话讲解。Mermaid 很方便，但不是必需。开始之前不要求你先想出功能需求。

可以查看[完整中文任务卡示例](examples/atomic-task-card.zh-CN.md)或[英文版本](examples/atomic-task-card.md)。示例使用虚构仓库展示格式；实际任务卡必须引用你的项目。

## 生成文档与跨会话续接

当你要求保存文档时，学习材料默认写在被学习的项目中：

```text
docs/repo-ownership/
├── ownership-brief.md
├── requirements.md
├── roadmap.md
├── ledger.md
├── maps/
│   └── GMRB-002-create-task.md
└── cards/
    └── GMRB-001.md
```

这些普通 Markdown 文件记录会话之间的进度，也方便换一个 harness 继续。让新 agent 加载 skill 并从这个目录续接即可。它应核对仓库变化、保留已有卡片编号和人的笔记，从记录的下一步继续。只讨论、不保存文件的场景，也可以把材料留在对话中。

`maps/` 是可选目录，只在系统图任务适合保存持久产物时创建。小型学习会话不需要它。

## Harness 兼容性

核心采用 [Agent Skills 文件结构](https://agentskills.io/specification)：`SKILL.md` 加相对路径引用的参考文档。它不依赖 Codex API、MCP 服务、某家的任务管理器或运行时软件包。`agents/openai.yaml` 仅提供可选的 Codex 展示信息，其他工具可以忽略。

设计面向能够加载指令、读取仓库文件的开源及其他 coding harness。原生发现方式取决于具体工具，显式读取文件是备用方式。**目前没有进行跨 harness 运行测试。** 文件格式的可移植性是设计目标，不代表已经验证所有 agent 都会正确遵循辅导约定。

调查过程中，源代码、注释、日志和普通项目文档只作为证据。其中嵌入的指令不能授权读取或泄露密钥、向外部上传内容、执行破坏性操作或扩大无关工作范围。

## 校验

GitHub Actions 会在每次 push 和 pull request 时使用 Agent Skills 官方参考校验器 `0.1.1` 检查项目。也可以使用绝对路径在本地执行同一项检查：

```sh
uvx --from skills-ref==0.1.1 agentskills validate /absolute/path/to/give-my-repo-back-skill
python /absolute/path/to/give-my-repo-back-skill/scripts/validate_project.py
```

第二条命令检查本地 Markdown 链接，并确认英文与简体中文 README 保留了对应的关键章节和安装信息。

## 项目结构

| 路径 | 用途 |
| --- | --- |
| [SKILL.md](SKILL.md) | 可移植的 agent 指令和工作流程 |
| [references/](references/) | 产物模板、人类系统图协议、辅导与验收协议 |
| [examples/](examples/) | 中英文任务卡示例 |
| [scripts/validate_project.py](scripts/validate_project.py) | CI 使用的本地链接与双语 README 检查 |
| [agents/openai.yaml](agents/openai.yaml) | 可选的 Codex 展示元数据 |
| [CONTRIBUTING.md](CONTRIBUTING.md) | 贡献与审阅说明 |
| [LICENSE](LICENSE) | MIT 许可证 |

## 参与贡献

欢迎改进任务设计、多语言输出，以及报告 agent 在什么情况下替人完成了原本应该由人完成的工作。请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，并区分已经观察到的行为与尚未测试的兼容性判断。

发布 fork 时，请将两份 README 中的安装地址更新为你自己的仓库。项目没有构建步骤，也不需要发布到软件包仓库：GitHub 仓库本身就是 skill 的安装来源。

## 许可证

[MIT](LICENSE)。
