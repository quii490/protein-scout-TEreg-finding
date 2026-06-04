---
type: protein-evaluation
gene: "GLMN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GLMN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GLMN / FAP48, FAP68, VMGLOM |
| 蛋白名称 | Glomulin |
| 蛋白大小 | 594 aa / 68.2 kDa |
| UniProt ID | Q92990 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 594 aa / 68.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=32 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.5; PDB: 4F52 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR019516, IPR013877; Pfam: PF08568 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.0/180** | |
| **归一化总分** | | | **65.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Cul2-RING ubiquitin ligase complex (GO:0031462)
- Cul3-RING ubiquitin ligase complex (GO:0031463)
- Cul4A-RING E3 ubiquitin ligase complex (GO:0031464)
- cullin-RING ubiquitin ligase complex (GO:0031461)
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 75 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAP48, FAP68, VMGLOM |

**关键文献**:
1. FKBP51 and FKBP12.6-Novel and tight interactors of Glomulin.. *PloS one*. PMID: 31490997
2. Beneath the surface: delineating the subtypes of Dowling-Degos disease.. *The British journal of dermatology*. PMID: 40674458
3. NR3C1/GLMN-Mediated FKBP12.6 Ubiquitination Disrupts Calcium Homeostasis and Impairs Mitochondrial Quality Control in Stress-Induced Myocardial Damage.. *International journal of molecular sciences*. PMID: 40943170
4. Glomuvenous malformations.. *Dermatology online journal*. PMID: 17511950
5. Loss-of-function variants in GLMN are associated with generalized skin hyperpigmentation with or without glomuvenous malformation.. *The British journal of dermatology*. PMID: 38489583

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.5 |
| 高置信度残基 (pLDDT>90) 占比 | 72.6% |
| 置信残基 (pLDDT 70-90) 占比 | 15.5% |
| 中等置信 (pLDDT 50-70) 占比 | 7.9% |
| 低置信 (pLDDT<50) 占比 | 4.0% |
| 有序区域 (pLDDT>70) 占比 | 88.1% |
| 可用 PDB 条目 | 4F52 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.5，有序区 88.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019516, IPR013877; Pfam: PF08568 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RBX1 | 0.999 | 0.968 | — |
| CUL1 | 0.993 | 0.958 | — |
| CUL7 | 0.992 | 0.601 | — |
| FKBP4 | 0.983 | 0.848 | — |
| FBXW8 | 0.979 | 0.000 | — |
| SKP1 | 0.960 | 0.292 | — |
| NLRC4 | 0.922 | 0.000 | — |
| NLRP3 | 0.914 | 0.000 | — |
| FKBP1A | 0.901 | 0.647 | — |
| CUL4A | 0.895 | 0.421 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NSFL1C | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EBI-1257123 | psi-mi:"MI:0096"(pull down) | pubmed:19367725|imex:IM-20587 |
| STING1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |
| HSPB1 | psi-mi:"MI:0097"(reverse ras recruitment system) | imex:IM-20864|pubmed:25277244 |
| CUL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CUL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CUL4A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CUL4B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CUL7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KLHDC10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.5 + PDB: 4F52 | pLDDT=88.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GLMN — Glomulin，非常新颖，仅有少数基础研究。
2. 蛋白大小594 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 32 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92990
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174842-GLMN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GLMN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92990
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
