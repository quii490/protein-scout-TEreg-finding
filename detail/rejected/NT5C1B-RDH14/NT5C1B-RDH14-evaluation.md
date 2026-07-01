---
type: protein-evaluation
gene: "NT5C1B-RDH14"
date: 2026-06-28
tags: [protein-scout, rejected, uncharacterized-accession]
status: rejected
---

## NT5C1B-RDH14 — 自动拒绝

### 拒绝原因

NT5C1B-RDH14 为 UniProtKB 未审查条目（非 reviewed Swiss-Prot 条目）的 accession number，而非标准人类基因符号。该条目在 `unclassified_core_nuclear` sheet 中缺乏核心证据：

- **无实验核定位证据**: HPA nuclear=False, 无 GO-CC IDA, 无 ChIP-Seq
- **无 PPI 数据**: Combined_BS_Human_Degree=0
- **蛋白长度异常**: nan aa（部分条目为碎片/部分序列）
- **Tier=3**: 证据质量极低

此类条目代表 UniProt 中未映射到标准基因符号的蛋白序列，不具备 TE 调控研究价值。

### 基本信息

| 项目 | 内容 |
|---|---|
| 标识符 | NT5C1B-RDH14 |
| 蛋白长度 | nan aa |
| Tier | 3 |
| HPA 核定位 | True |

### 深度机制分析

NT5C1B-RDH14为UniProtKB未审查条目（非Swiss-Prot审查蛋白），蛋白长度标注为nan aa，属于Tier=3的低质量证据蛋白。该条目缺乏标准基因符号映射（为read-through融合转录本产物），在核蛋白筛选流程中因无实验核定位证据（HPA nuclear=False）、无PPI数据（Combined_BS_Human_Degree=0）和UniProt注释极不完整而被自动拒收。

从序列分析角度，NT5C1B-RDH14为NT5C1B（5'-核苷酸酶胞质1B）和RDH14（视黄醇脱氢酶14）基因间通读转录产生的融合蛋白编码序列。Read-through融合被认为在很大程度上是转录机制的渗漏扫描产物，多数不产生稳定的功能蛋白。该序列缺乏已定义的结构域注释、无实验验证的蛋白互作、无GO-CC定位信息，不具备任何可进行功能机制分析的蛋白特征。

从TE调控角度，NT5C1B-RDH14作为未表征的融合序列，不具备TE调控研究价值。即使其亲本基因NT5C1B（嘧啶核苷酸酶）和RDH14（视黄醇脱氢酶）在核苷酸代谢和视黄酸代谢中具有明确功能，融合蛋白本身因缺乏独立的结构域保守性和实验表达证据，无法推断其在TE调控通路中的任何贡献。
