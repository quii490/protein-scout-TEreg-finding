---
type: protein-evaluation
gene: "HMGA2/BNC2"
uniprot: "N/A (chimeric fusion, not a normal gene)"
date: 2026-06-28
tags: [protein-scout, rejected, somatic-fusion, readthrough-artifact, not-a-normal-protein]
status: rejected
---

## HMGA2/BNC2 — 拒绝报告: 体细胞融合假象

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 标识符 | HMGA2/BNC2 (亦标注为 HMGA2-BNC2 fusion) |
| 原始 Excel 分类 | Tier 3; HPA nuclear=True; PPI=0; Hotness=0 |
| 基因座 | HMGA2 (chr12q14.3) + BNC2 (chr9p22.2) — **不同染色体** |
| UniProt 条目 | A0A9E7V733 (TrEMBL, unreviewed, added 2023-05-03) |
| UniProt 证据等级 | 2: Evidence at transcript level only (无蛋白水平证据) |
| UniProt 注释得分 | 1.0 / 5.0 |
| 声明蛋白长度 | 42 aa |
| Ensembl 注释 | **未收录** (ENSG 查询无结果) |

### 2. 拒绝原因

#### 2.1 非基因通读事件 — 体细胞染色体易位

HMGA2 位于 **chr12** (65.8 Mb)，BNC2 位于 **chr9** (16.4 Mb)。两个基因位点不在同一染色体上，**物理上不可能发生顺式通读转录**。该融合来自 Panagopoulos et al. (2022, PMID: 36309352) 在一例 **子宫肌瘤 (uterine leiomyoma)** 中检测到的获得性 t(9;12)(p22;q14) 体细胞易位，是**单个体细胞肿瘤事件**，而非正常人类基因组编码的产物。

#### 2.2 不产生融合蛋白

UniProt 条目声称的 42-aa "蛋白" 序列 `AEATGEKRPRGRPRKWPQQVVQKKPAQEETEETSSQESAEED` 与**野生型 HMGA2 第 68-109 位残基完全一致**——这仅是 HMGA2 蛋白的 C 端片段，不含任何 BNC2 来源的氨基酸序列。

融合的分子结构为: **HMGA2 3'-UTR (终止密码子后核苷酸 1035) 与 BNC2 3'-UTR (外显子 7 核苷酸 9284) 融合**。两个融合伙伴均贡献非翻译区。GenBank 提交 (ON989351) 中的 CDS 注释为提交流程假象 — "partial cds" 标签和 `codon_start=2` 表明其为正常 HMGA2 ORF 的片段，而非新型融合蛋白。

**UniProt 条目 A0A9E7V733 不应该标注为独立的蛋白产物。** 条目以 TrEMBL 自动注释方式添加，flag 为 "Fragment"，不存在独立证据支持该序列代表一个稳定的体内蛋白。

#### 2.3 生物学机制: HMGA2 转录上调，非新蛋白

Panagopoulos et al. 论文的明确结论: 致瘤机制为**野生型 HMGA2 的转录上调**，通过缺失 3'-UTR 中的 Let-7 miRNA 结合位点实现。引用原文: *"Regardless of the exact mechanism, transcriptional upregulation of HMGA2 seems to be the important result."* 该融合不产生嵌合蛋白。

#### 2.4 无独立验证

- 仅一篇文献 (2022)，无后续独立复制
- 无蛋白水平证据 (PE=2; 无质谱, 无 western blot, 无免疫组化)
- Ensembl 未收录 (不是真实基因)
- AlphaFold 预测模型 (AF-A0A9E7V733-F1, mean pLDDT=63.34) 为自动生成的无意义片段

### 3. 综合判断

HMGA2/BNC2 **不符合蛋白评估标准**，在任何核蛋白筛选中都应被排除:

| 标准 | 判定 |
|---|---|
| 是否为正常人类基因产物? | **否** — 体细胞肿瘤特异性易位 |
| 是否产生嵌合蛋白? | **否** — UTR-UTR 融合, 不产生新蛋白 |
| 是否有蛋白水平证据? | **否** — PE=2, 无质谱/抗体证据 |
| 是否被 Ensembl 收录? | **否** — 人参考基因组中不存在 |
| 是否符合核蛋白筛选条件? | **否** — 无蛋白产物可评估 |
| 原始 Excel 中的 Nucleoplasm 标注 | 误标 — 该条目不应出现在筛选中 |

### 4. 处置建议

**完全拒绝，从候选清单中移除。** HMGA2/BNC2 不适用于:
- 核蛋白候选筛选
- TE 调控蛋白评估
- 任何基于正常人类蛋白质组的分析

该条目在来源 Excel sheet 中的存在本身即为错误，需在数据清洗阶段去除。

### 5. 数据来源

| 来源 | 查询 | 结论 |
|---|---|---|
| UniProt | A0A9E7V733, P52926 (HMGA2), Q6ZN30 (BNC2) | TrEMBL 条目, PE=2, Fragment |
| PubMed | PMID:36309352 (Panagopoulos 2022) | 子宫肌瘤体细胞易位, 单病例 |
| Ensembl | HMGA2-BNC2 / ON989351 | 未收录 |
| AlphaFold DB | AF-A0A9E7V733-F1 | 自动生成片段, pLDDT=63.34 |
| 染色体定位 | HMGA2: chr12; BNC2: chr9 | 通读不可能 (需同染色体) |
