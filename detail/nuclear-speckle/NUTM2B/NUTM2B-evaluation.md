---
type: protein-evaluation
gene: "NUTM2B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NUTM2B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NUTM2B / FAM22B |
| 蛋白名称 | NUT family member 2B |
| 蛋白大小 | 878 aa / 94.0 kDa |
| UniProt ID | A6NNL0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 878 aa / 94.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=33 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=45.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024310, IPR024309; Pfam: PF12881 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117/180** | |
| **归一化总分** | | | **65.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 33 |
| PubMed broad count | 61 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM22B |

**关键文献**:
1. CGG repeat expansions in Charcot-Marie-Tooth disease: insights from the 100 000 Genomes Project.. *Journal of neurology, neurosurgery, and psychiatry*. PMID: 40645757
2. Genetic variation of YWHAE gene-"Switch" of disease control.. *Zhong nan da xue xue bao. Yi xue ban = Journal of Central South University. Medical sciences*. PMID: 35545369
3. Targeted RNA sequencing in diagnostically challenging head and neck carcinomas identifies novel MON2::STAT6, NFATC2::NUTM2B, POC5::RAF1, and NSD3::NCOA2 gene fusions.. *Histopathology*. PMID: 39628352
4. KDM2B-Rearranged Soft Tissue Sarcomas Expand the Concept of BCOR-Associated Sarcoma.. *Modern pathology : an official journal of the United States and Canadian Academy of Pathology, Inc*. PMID: 37634866
5. m(6)A-Methylated NUTM2B-AS1 Promotes Hepatocellular Carcinoma Stemness Feature via Epigenetically Activating BMPR1A Transcription.. *Journal of hepatocellular carcinoma*. PMID: 39649245

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 45.3 |
| 高置信度残基 (pLDDT>90) 占比 | 4.9% |
| 置信残基 (pLDDT 70-90) 占比 | 9.9% |
| 中等置信 (pLDDT 50-70) 占比 | 9.6% |
| 低置信 (pLDDT<50) 占比 | 75.6% |
| 有序区域 (pLDDT>70) 占比 | 14.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=45.3），有序残基占 14.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024310, IPR024309; Pfam: PF12881 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| YWHAE | 0.788 | 0.093 | — |
| NUTM2A | 0.768 | 0.000 | — |
| CCNB3 | 0.668 | 0.100 | — |
| ZC3H7B | 0.624 | 0.092 | — |
| JAZF1 | 0.550 | 0.046 | — |
| BCOR | 0.493 | 0.079 | — |
| BOLA2-SMG1P6 | 0.446 | 0.000 | — |
| MEAF6 | 0.422 | 0.000 | — |
| PHF1 | 0.403 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 9，IntAct interactions: 0
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=45.3 + PDB: 无 | pLDDT=45.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear bodies | 待确认 |
| PPI | STRING + IntAct | 9 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. NUTM2B — NUT family member 2B，非常新颖，仅有少数基础研究。
2. 蛋白大小878 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 33 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=45.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NNL0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188199-NUTM2B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NUTM2B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NNL0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
