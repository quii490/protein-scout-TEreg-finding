---
type: protein-evaluation
gene: "CPA4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CPA4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CPA4 |
| 蛋白名称 | Carboxypeptidase A4 |
| 蛋白大小 | 421 aa / 47.4 kDa |
| UniProt ID | Q9UI42 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoplasm, Plasma membrane; 额外: Centriolar satellite; UniProt: Secreted |
| 蛋白大小 | 10/10 | x1 | 10 | 421 aa / 47.4 kDa |
| 研究新颖性 | 4/10 | x5 | 20 | PubMed strict=70 篇 (≤80→4) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=93.7; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.5/180** | |
| **归一化总分** | | | **51.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane; 额外: Centriolar satellite | Approved |
| UniProt | Secreted | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 70 |
| PubMed broad count | 74 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Integrating plasma proteomes with genome-wide association data for causal protein identification in hepatocellular carcinoma: A bidirectional Mendelian randomization study.. *Medicine (Baltimore)*. PMID: 41578465
2. Comprehensive analysis of DNA methylation patterns in recurrent miscarriage: imprinted/non-imprinted genes and their regulation across sperm and fetal-maternal tissues.. *PeerJ*. PMID: 41081108
3. Druggable genome-wide Mendelian randomization integrating GWAS and eQTL/pQTL data identifies targets for lung squamous cell carcinoma.. *Sci Rep*. PMID: 40820226
4. Retraction Note: Circular RNA circ-CPA4/ let-7 miRNA/PD-L1 axis regulates cell growth, stemness, drug resistance and immune evasion in non-small cell lung cancer (NSCLC).. *J Exp Clin Cancer Res*. PMID: 40796894
5. Carboxypeptidase A4: A Biomarker for Cancer Aggressiveness and Drug Resistance.. *Cancers (Basel)*. PMID: 40805261

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.7 |
| 高置信度残基 (pLDDT>90) 占比 | 87.4% |
| 置信残基 (pLDDT 70-90) 占比 | 8.8% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 3.8% |
| 有序区域 (pLDDT>70) 占比 | 96.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.7，有序区 96.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LXN | 0.000 | 0.000 | — |
| CMA1 | 0.000 | 0.000 | — |
| TPSAB1 | 0.000 | 0.000 | — |
| MEST | 0.000 | 0.000 | — |
| CTSG | 0.000 | 0.000 | — |
| SRGN | 0.000 | 0.000 | — |
| TPSB2 | 0.000 | 0.000 | — |
| FCER1A | 0.000 | 0.000 | — |
| CELA3B | 0.000 | 0.000 | — |
| CELA3A | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9UI42 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q14249 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.7 + PDB: 无 | pLDDT=93.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Secreted / Nucleoplasm, Plasma membrane; 额外: Centriolar satel | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CPA4 -- Carboxypeptidase A4，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小421 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 70 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UI42
- Protein Atlas: https://www.proteinatlas.org/ENSG00000128510-CPA4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CPA4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UI42
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UI42-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
