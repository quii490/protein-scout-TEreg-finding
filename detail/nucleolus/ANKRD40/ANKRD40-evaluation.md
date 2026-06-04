---
type: protein-evaluation
gene: "ANKRD40"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ANKRD40 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANKRD40 |
| 蛋白名称 | Ankyrin repeat domain-containing protein 40 |
| 蛋白大小 | 368 aa / 41.1 kDa |
| UniProt ID | Q6AI12 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; 额外: Nucleoli fibrillar center, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 368 aa / 41.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039195, IPR002110, IPR036770; Pfam: PF13637 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.5/180** | |
| **归一化总分** | | | **65.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoli fibrillar center, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Discovery of myeloid zinc finger (MZF) 1 nuclear bodies.. *Biochemical and biophysical research communications*. PMID: 39954358
2. LAMC1 is a prognostic factor and a potential therapeutic target in endometrial cancer.. *Journal of gynecologic oncology*. PMID: 31912669
3. Comprehensive analysis of dysregulated circular RNAs and construction of a ceRNA network involved in the pathology of Alzheimer's disease in a 5 × FAD mouse model.. *Frontiers in aging neuroscience*. PMID: 36466608
4. Single symbiotic cell transcriptome sequencing of coral.. *Genomics*. PMID: 33096259

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.5 |
| 高置信度残基 (pLDDT>90) 占比 | 37.5% |
| 置信残基 (pLDDT 70-90) 占比 | 11.7% |
| 中等置信 (pLDDT 50-70) 占比 | 14.7% |
| 低置信 (pLDDT<50) 占比 | 36.1% |
| 有序区域 (pLDDT>70) 占比 | 49.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=68.5），有序残基占 49.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039195, IPR002110, IPR036770; Pfam: PF13637 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AHCY | 0.828 | 0.827 | — |
| SEC13 | 0.808 | 0.743 | — |
| SAR1A | 0.654 | 0.471 | — |
| SEC23A | 0.639 | 0.480 | — |
| SEC23B | 0.636 | 0.480 | — |
| SEC24B | 0.607 | 0.314 | — |
| SEC24A | 0.606 | 0.314 | — |
| SUPT20H | 0.590 | 0.044 | — |
| SAR1B | 0.577 | 0.471 | — |
| SUMF2 | 0.489 | 0.461 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000285243.6 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| adP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CTRL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LTA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ULK4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RCBTB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MSX2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| H1-2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| LAMA2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2AC21 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.5 + PDB: 无 | pLDDT=68.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Golgi apparatus; 额外: Nucleoli fibrillar center, Cy | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. ANKRD40 — Ankyrin repeat domain-containing protein 40，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小368 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=68.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6AI12
- Protein Atlas: https://www.proteinatlas.org/ENSG00000154945-ANKRD40/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANKRD40
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6AI12
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
