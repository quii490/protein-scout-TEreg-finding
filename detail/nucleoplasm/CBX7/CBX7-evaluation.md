---
type: protein-evaluation
gene: "CBX7"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CBX7 — REJECTED (研究热度过高 (PubMed strict=262，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CBX7 |
| 蛋白名称 | Chromobox protein homolog 7 |
| 蛋白大小 | 251 aa / 28.3 kDa |
| UniProt ID | O95931 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CBX7/IF_images/U2OS_1.jpg|U2OS]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/CBX7/IF_images/NIH-3T3_1.jpg|NIH 3T3]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 251 aa / 28.3 kDa |
| 🆕 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=262 篇 (>100→REJECTED) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.2; PDB: 无 |
| 🧬 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已嵌入

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 262 |
| PubMed broad count | 270 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Discovery of novel 4-aminobenzamide derivatives as small molecule CBX2 inhibitors.. *Bioorg Med Chem Lett*. PMID: 41478308
2. Histone H3.3 phosphorylation facilitates H3K9me3-heterochromatin formation during retrotransposon silencing and X-chromosome inactivation via H3.3K27me3-CBX7-KAP1 axis.. *Sci Bull (Beijing)*. PMID: 41582043
3. CBX7 functions as a methylation-dependent inducer of gene transcription and regulator of cytosolic signaling in lymphoid cells.. *Sci Adv*. PMID: 41686891
4. Engineered Multifunctional Hydrogel Delivering Novel CBX7 Inhibitor Modulates Cuproptosis Via Liquid-Liquid Phase Separation to Restore Cardiac Function in Aged Myocardial Infarction.. *Adv Sci (Weinh)*. PMID: 41117088
5. Chromobox protein homolog 7 (CBX7) deficiency inhibits osteoblast ferroptosis by activating the Nrf2 function in type 2 diabetic osteoporosis.. *Int J Biochem Cell Biol*. PMID: 40998236

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.2 |
| 高置信度残基 (pLDDT>90) 占比 | 24.7% |
| 置信残基 (pLDDT 70-90) 占比 | 9.2% |
| 中等置信 (pLDDT 50-70) 占比 | 43.0% |
| 低置信 (pLDDT<50) 占比 | 23.1% |
| 有序区域 (pLDDT>70) 占比 | 33.9% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CBX7/CBX7-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=66.2），有序残基占 33.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RING1 | 0.000 | 0.000 | — |
| RNF2 | 0.000 | 0.000 | — |
| BMI1 | 0.000 | 0.000 | — |
| PCGF2 | 0.000 | 0.000 | — |
| EZH2 | 0.000 | 0.000 | — |
| PHC2 | 0.000 | 0.000 | — |
| SUZ12 | 0.000 | 0.000 | — |
| CBX8 | 0.000 | 0.000 | — |
| PHC1 | 0.000 | 0.000 | — |
| COMMD3-BMI1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:O95931 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q8VDS3 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9CQJ4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P23798 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q64028 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8CCI5 | psi-mi:"MI:0071"(molecular sieving) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q99NA9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P35226 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q3KNV8-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q6W2J9-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.2 + PDB: 无 | pLDDT=66.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CBX7 — Chromobox protein homolog 7，研究基础较多，新颖性有限。
2. 蛋白大小251 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 262 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=66.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 262 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95931
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100307-CBX7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CBX7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95931
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/CBX7/CBX7-PAE.png]]




