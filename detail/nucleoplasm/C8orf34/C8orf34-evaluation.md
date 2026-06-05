---
type: protein-evaluation
gene: "C8orf34"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C8orf34 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C8orf34 |
| 蛋白名称 | Uncharacterized protein C8orf34 |
| 蛋白大小 | 538 aa / 59.4 kDa |
| UniProt ID | Q49A92 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/C8orf34/IF_images/HEK293_1.jpg|HEK293]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/C8orf34/IF_images/Rh30_1.jpg|Rh30]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; 额外: Golgi apparatus; UniProt: 无注释 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 538 aa / 59.4 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.6; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR040687; Pfam: PF17824 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 8 partners; IntAct 3 interactions |
| ➕ 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli; 额外: Golgi apparatus | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 9 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Transcriptome of the human C2 dorsal root ganglia in C1-2 arthrodesis surgery: insight for neck pain.. *Brain : a journal of neurology*. PMID: 41032656
2. The plasma peptides of breast versus ovarian cancer.. *Clinical proteomics*. PMID: 31889940
3. Single-cell characterization of the human C2 dorsal root ganglion recovered from C1-2 arthrodesis surgery: implications for neck pain.. *bioRxiv : the preprint server for biology*. PMID: 40196625
4. Identification of a Novel Cancer Stemness-Associated ceRNA Axis in Lung Adenocarcinoma via Stemness Indices Analysis.. *Oncology research*. PMID: 33106209
5. Detection of novel fusion genes by next-generation sequencing-based targeted RNA sequencing analysis in adenoid cystic carcinoma of head and neck.. *Oral surgery, oral medicine, oral pathology and oral radiology*. PMID: 34413003

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.6 |
| 高置信度残基 (pLDDT>90) 占比 | 8.2% |
| 置信残基 (pLDDT 70-90) 占比 | 15.1% |
| 中等置信 (pLDDT 50-70) 占比 | 28.4% |
| 低置信 (pLDDT<50) 占比 | 48.3% |
| 有序区域 (pLDDT>70) 占比 | 23.3% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.6），有序残基占 23.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040687; Pfam: PF17824 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| C1orf194 | 0.607 | 0.000 | — |
| TEX55 | 0.510 | 0.000 | — |
| ASB7 | 0.508 | 0.508 | — |
| C19orf18 | 0.447 | 0.000 | — |
| ANKUB1 | 0.443 | 0.000 | — |
| EFCAB10 | 0.441 | 0.000 | — |
| OR1E2 | 0.418 | 0.000 | — |
| PREX2 | 0.417 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CNDP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ASB7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| S100P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 8，IntAct interactions: 3
- 调控相关比例: 0 / 8 = 0%

**评价**: STRING 8 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.6 + PDB: 无 | pLDDT=56.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Nucleoli; 额外: Golgi apparatus | 待确认 |
| PPI | STRING + IntAct | 8 + 3 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. C8orf34 — Uncharacterized protein C8orf34，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小538 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=56.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q49A92
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165084-C8orf34/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C8orf34
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q49A92
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:27:01

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q49A92-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
