# Qrange Public Skills

Qrange 的公开 Agent Skill 集合。每个 Skill 是一个独立文件夹，平台无关——任何兼容 `SKILL.md` 规范的 Agent 运行时（Claude Code、OpenClaw、Hermes、WorkBody 等）都可以直接加载；不支持技能包的 Agent 也可以把 SKILL.md 作为系统提示词使用。

## Skills 索引

| Skill | 一句话说明 | 版本 |
|---|---|---|
| [methodology-bsc](methodology-bsc/) | 平衡计分卡（BSC）业务复盘：把零散业务数据追问成有因果逻辑的结构化复盘文档 | v2.0 |
| [course-mainline-v2](course-mainline-v2/) | 课程/书籍/分享等任意材料 → 标准化 9 模块主线文档 | v0.2.0 |
| [tizhinei-writing](tizhinei-writing/) | 体制内文风写作：公文风格的改写与起草 | v0.2.0 |
| [chaishu](chaishu/) | 六步拆书法：非虚构书籍批判性拆解——查出作者的椅子，在盲区上长出你自己的认知 | v0.1.0 |

> 新 Skill 入库规则：一个 Skill 一个文件夹，加到这个索引表，注明版本。

## 使用方式

每个 Skill 文件夹自成一体，内含自己的 README（安装、触发方式、边界）。挑你要的那个，整个文件夹拿走即可。

## License

除各 Skill 另有说明外，本仓库内容均采用 **CC BY-NC 4.0**（署名-非商业性使用）许可，作者 Qrange。可自由使用、修改、分发，需署名，禁止商用。
