---
type: protein-evaluation
gene: "DHCR24"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DHCR24 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=392，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DHCR24 |
| 蛋白名称 | Delta(24)-sterol reductase |
| 蛋白大小 | 528 aa / 61.4 kDa |
| UniProt ID | A0A0A0MTI1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum membrane; Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 528 aa / 61.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=392 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.1; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **64.0/180** | |
| **归一化总分** | | | **35.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Endoplasmic reticulum membrane; Golgi apparatus membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 392 |
| PubMed broad count | 427 |
| 别名(未计入scoring) |  |

**关键文献**:
1. The phytosterol 24(S)-saringosterol alters lipid homeostasis and inflammatory pathways in a cell-specific manner.. *Biomed Pharmacother*. PMID: 42107911
2. Hepatic transcriptomics reveals immuno-metabolic interactions in juvenile channel catfish (Ictalurus punctatus) after Aeromonas hydrophila infection.. *BMC Genomics*. PMID: 42210080
3. The Selective DHCR24 Blocker SH42 Inhibits ACE2 Binding and Cellular Entry of SARS-CoV-2 Spike Proteins More Efficiently Than Atorvastatin.. *Research (Wash D C)*. PMID: 42146763
4. Altered lipid profile in mice lacking the DNA repair protein ERCC1.. *DNA Repair (Amst)*. PMID: 41962388
5. Identification of a genetic locus responsible for the dominant white-spotting coat phenotype in mice spontaneously isolated from a Japanese wild-derived inbred strain.. *J Vet Med Sci*. PMID: 41882906

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.1 |
| 高置信度残基 (pLDDT>90) 占比 | 63.3% |
| 置信残基 (pLDDT 70-90) 占比 | 24.1% |
| 中等置信 (pLDDT 50-70) 占比 | 10.8% |
| 低置信 (pLDDT<50) 占比 | 1.9% |
| 有序区域 (pLDDT>70) 占比 | 87.4% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/DHCR24/DHCR24-PAE.png]]

**评价**: AlphaFold 极高置信度预测（pLDDT=88.1，有序区 87.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DHCR7 | 0.000 | 0.000 | — |
| CYP51A1 | 0.000 | 0.000 | — |
| MSMO1 | 0.000 | 0.000 | — |
| SC5D | 0.000 | 0.000 | — |
| LSS | 0.000 | 0.000 | — |
| EBP | 0.000 | 0.000 | — |
| HSD17B7 | 0.000 | 0.000 | — |
| TM7SF2 | 0.000 | 0.000 | — |
| LBR | 0.000 | 0.000 | — |
| SOAT2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q15392 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O00264 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:P01112 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P54707-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P62736 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q86V48-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9BWH2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9NZ08-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.1 + PDB: 无 | pLDDT=88.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Golgi apparatus me / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DHCR24 — Delta(24)-sterol reductase，研究基础较多，新颖性有限。
2. 蛋白大小528 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 392 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A0A0A0MTI1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116133-DHCR24/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DHCR24
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A0A0MTI1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/DHCR24/DHCR24-PAE.png]]
