---
type: protein-evaluation
gene: "C2orf66"
uniprot: "Q6UXQ4"
date: 2026-06-28
tags: [protein-scout, nucleoplasm, evaluation, rejected]
status: rejected
---

## C2orf66 评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | C2orf66 |
| 蛋白全称 | Uncharacterized protein C2orf66 |
| UniProt ID | Q6UXQ4 (Swiss-Prot, reviewed) |
| 蛋白大小 | 117 aa (mature chain: 79 aa) |
| UniProt 证据等级 | 3: Inferred from homology |
| 亚细胞定位 | **Secreted** (分泌蛋白, 含信号肽 1-38 aa) |

### 2. 评分总览
| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 0/10 | x4 | 0.0 | Secreted (UniProt); 核定位无证据 |
| 蛋白大小 | 1/10 | x1 | 1.0 | 117 aa (极小型蛋白) |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=1; 完全未鉴定功能 |
| 三维结构 | 1/10 | x3 | 3.0 | 无 AlphaFold 高置信结构; 仅 DUF4720 |
| 调控结构域 | 0/10 | x2 | 0.0 | 仅 Pfam DUF4720 (未知功能域) |
| PPI | 2/10 | x3 | 6.0 | PPI degree=3; 无显著相互作用 |
| **加权总分** | | | **45.0/180** | |
| **归一化总分** | | | **25.0/100** | |

### 3. 详细分析

**核定位: 不成立 (FAIL)**。C2orf66 是一个**分泌蛋白**，UniProt 明确标注 "Secreted"，含信号肽(1-38 aa)，mature chain 仅 79 个氨基酸。该蛋白被设计为分泌到胞外，不具备核定位信号。HPA 标注 "Cytosol; Nucleoplasm" 可能是基于过表达或抗体非特异性结合的人工信号，与 Swiss-Prot 的 curated 定位直接矛盾。

**功能**: 完全未知。属于 Pfam DUF4720 (Domain of Unknown Function)，2003 年通过大型分泌蛋白发现计划 (SPDI) 被鉴定。在睾丸及 85+ 种组织中表达。

**结构**: 蛋白极小 (79 aa mature chain)，仅含一个功能未知的结构域 (DUF4720)。不具备 DNA 结合或染色质调控相关结构域。作为分泌蛋白，其折叠由信号肽引导至 ER/分泌途径。

**文献**: 仅 1 篇 PubMed 文献 (PMID 26428916)，为分泌蛋白组发现研究。无任何功能研究。

### 4. 总体评价
**25.0/100** | **REJECTED**

**拒绝理由**: C2orf66 是一个**极小型分泌蛋白** (mature chain 仅 79 aa)，功能完全未知。HPA 标注的 "Nucleoplasm" 定位与 UniProt curated 定位 "Secreted" 矛盾。蛋白不含任何已知功能域 (仅 DUF4720)，不具备作为转录/染色质调控因子的基本条件。文献极度缺乏，无开发价值。
