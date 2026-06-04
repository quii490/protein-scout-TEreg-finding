你是 Claude Code 中的 protein-scout 执行主 agent。继续执行 Sheet3 缺口评估，准确性和完整性优先。只在以下两个项目路径内读写：
- `/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested`
- `/Users/quii/Desktop/projects/TE-regulated proteins finding`

必须遵守：
- `/Users/quii/Documents/Obsidian Vault/.claude/skills/protein-scout/SKILL.md`
- 项目内 `skills.md`
- `validate.py`, `validate_strict.py`, `protein_gate.py`, `rebuild_summary.py`
- 上一批 log：`log/claude_sheet3_gap_next5_20260601_030214.md`

本批任务来源：`Final_TE_finding.xlsx` 的 `研究很多`

处理 Excel 行：
- row 124: C11orf42
- row 125: C11orf71
- row 126: C11orf96
- row 127: C12orf57
- row 128: C12orf60

硬性流程，不能跳步：
1. 创建 log：`log/claude_sheet3_gap_next5b_YYYYMMDD_HHMMSS.md`
2. 对每个 gene 单独执行完整流程：
   - 先用 `/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/protein_scout_harvest.py` 生成/更新 packet。
   - 基于 packet + 必要独立补查写报告。
   - PubMed 必须通过 PubMed/E-utils 独立搜索；不能只读 Excel 值。
   - HPA 是核定位核心证据：必须写 reliability、subcellular location/main/additional。无 IF 原图不失败，但必须写标准缺失说明。能嵌入 IF display/缩略图就嵌入。
   - 有 `<GENE>-PAE.png` 必须嵌入；没有则写明确缺失原因。
   - PPI 必须有表格，展示 Partner、来源、score/PMID/方法、功能类别、是否调控相关。无结果也要写 `0 条/无结果`。
   - 分类必须严格：核仁主定位才进 `nucleolus`；核斑进 `nuclear-speckle`；核膜进 `nuclear-envelope`; 弥漫核质进 `nucleoplasm`; 核+胞质进 `nucleus-cytoplasm`; 不合格进 `rejected`。
   - 小鼠 only 也评估，不跳过；本批如遇到非人/小鼠条目，写物种限制。
3. 每完成一个 gene，立即追加 log，内容包括：
   - gene、row、分类、报告路径、是否 rejected
   - HPA 定位和 IF 状态
   - PAE 状态
   - PubMed strict/broad 和 novelty
   - PPI 来源覆盖
   - targeted strict 结果
4. 每个 gene 完成后运行：
   `python3 validate_strict.py --gene <GENE>`
   必须 0 error 后才能进入下一个 gene。
5. 5 个全部完成后运行：
   `python3 protein_gate.py --all`
   必须 `Errors: 0`。

评分规则：
- 新颖性：≤20=10, 21-40=8, 41-60=6, 61-80=4, 81-100=2, >100=rejected。
- 核定位：≤3=rejected。必须综合 HPA、UniProt、GO-CC、GeneCards/文献。
- 公式：`(核定位*4 + 蛋白大小*1 + 新颖性*5 + 三维结构*3 + 结构域*2 + PPI*3 + 互证加分) / 1.83`。
- 总表只能通过 `protein_gate.py --all` 或 `rebuild_summary.py` 更新。

如果你卡住超过一个 gene，不要继续空转：写入 log 说明已完成/未完成、当前阻塞点，然后停止。

完成后只输出：
- log 路径
- 5 个报告路径
- rejected 列表
- targeted strict 摘要
- full gate 摘要
- 需要 Codex 判断的问题
