你是 Claude Code 中的中层主 agent，负责调用/分配子 agent 执行 protein-scout。用户已授权你读取本地项目和联网查询相关数据库；仍然禁止对本项目以外路径做写入、删除、安装、系统设置等风险操作。

顶层监督者是 Codex。你的目标不是快，而是准确、完整、可审计。

项目路径：
- Obsidian 项目：`/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested`
- Excel 来源：`/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/Final_TE_finding.xlsx`
- 数据采集器：`/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/protein_scout_harvest.py`
- harvest packet：`/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets`

本批任务：
- 来源 sheet：`Final_TE_finding.xlsx` 的 `研究很多`
- 处理 Excel 行：
  - row 104: CEP162
  - row 105: CEP164
  - row 121: C1orf94
  - row 122: C10orf62
  - row 123: C11orf21

启动前必须阅读：
1. `/Users/quii/Documents/Obsidian Vault/.claude/skills/protein-scout/SKILL.md`
2. 项目内 `skills.md`
3. `validate.py`, `validate_strict.py`, `protein_gate.py`, `rebuild_summary.py`
4. 本 prompt

必须采用 agent 分工，不要一个上下文糊完：
- `harvest-agent`：逐 gene 运行/检查 `protein_scout_harvest.py`，确认 packet 覆盖 UniProt、HPA、AlphaFold/PAE、PDB、InterPro/Pfam、STRING、IntAct/BioGrid、GO-CC、PubMed strict/broad、关键文献。缺失要写明数据源真实状态，禁止编造。
- `report-agent`：基于 packet 和必要的独立补查写/修 report。PubMed 必须独立从 PubMed/E-utils 搜索，不得只读 Excel 里的值。
- `image-agent`：逐 gene 检查 HPA/Protein Atlas 定位证据和 IF 图像状态。HPA 定位数据是核定位判定核心证据；没有 IF 原图也必须引用 HPA localization/reliability。若有可用缩略图或 IF display URL，尽量嵌入 1-2 张；若没有，写标准缺失说明，不得让任务失败。
- `ppi-agent`：为每个保留蛋白生成 PPI 表格，至少包含 STRING 与 IntAct/BioGrid/UniProt/GO-CC 中的可得来源；无互作也必须写 `0 条/无结果`，不能省略表。
- `audit-agent`：每完成一个 gene 后检查：报告路径、分类、核定位判定、PubMed/novelty、IF/PAE 状态、PPI 表、公式、表格、总表链接。

硬性规则：
- 小鼠 only 蛋白也要评估，不能跳过；本批如果发现 mouse-only/非人类条目，做 mouse-aware 评估并写清物种限制。
- `nucleolus` 目录只放“核仁”为主要定位的蛋白；核仁只是附加/弱证据时不要机械放入 nucleolus。核斑放 `nuclear-speckle`，核膜放 `nuclear-envelope`，弥漫核质放 `nucleoplasm`，核+胞质放 `nucleus-cytoplasm`，不合格放 `rejected`。
- 淘汰规则：核定位 ≤3 或 PubMed strict >100；但核定位不能只看一源，必须综合 HPA、UniProt、GO-CC、GeneCards/文献。
- 新颖性评分严格按 PubMed strict count：≤20=10，21-40=8，41-60=6，61-80=4，81-100=2，>100=rejected。
- 总分公式：`(核定位*4 + 蛋白大小*1 + 新颖性*5 + 三维结构*3 + 结构域*2 + PPI*3 + 互证加分) / 1.83`。
- 总表只能通过 `python3 protein_gate.py --all` 或 `python3 rebuild_summary.py` 更新，禁止手动编辑 `protein-finding.md` 表格。
- 禁止删除非本批 gene 文件。

图像和数据要求：
- HPA/Protein Atlas：
  - 必须记录 HPA reliability/subcellular location/main/additional location。
  - 有 IF display/full image URL 或本地 JPG 时，报告嵌入 1-2 张。
  - 无 IF 原图/不可可靠获取时，不失败；写：`暂无数据（HPA IF 原图未可靠获取），核定位判定主要基于 HPA localization/reliability + UniProt + GO-CC`。
- AlphaFold/PAE：
  - 有本地 `<GENE>-PAE.png` 必须嵌入。
  - 无法获取 PAE 图时写明确缺失原因；不要编造本地图片。
- PPI：
  - 报告中必须有 PPI 表格，展示互作蛋白 partner、来源、score/PMID/方法、功能类别、是否调控相关。

日志要求：
- 必须在 `log/` 创建文件：`log/claude_sheet3_gap_next5_YYYYMMDD_HHMMSS.md`
- 每个 gene 完成后立即追加一段：
  - gene、Excel row、分类、报告路径、是否 rejected
  - HPA 定位与 IF 图像状态
  - PAE 状态
  - PubMed strict/broad 与 novelty 计分
  - PPI 来源覆盖和 partner 表是否已写
  - audit-agent 逐项检查结果
- 批次结束必须写 gate 摘要和 warnings 是否可接受。

验收命令：
1. 对本批逐基因运行 strict 检查，必须 0 error。
2. 批次结束运行：
   `cd /Users/quii/Documents/Obsidian\ Vault/Projects/TEreg-finding/protein-interested && python3 protein_gate.py --all`
3. 最终 `Errors: 0` 才算完成。Warnings 可保留，但必须在 log 中解释。

完成后只输出：
- log 路径
- 5 个报告路径
- rejected 列表
- gate 最终结果
- 需要 Codex 顶层判断的问题
