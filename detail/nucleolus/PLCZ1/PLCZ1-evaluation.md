---
type: protein-evaluation
gene: "PLCZ1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLCZ1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLCZ1 |
| 蛋白名称 | 1-phosphatidylinositol 4,5-bisphosphate phosphodiesterase zeta-1 |
| 蛋白大小 | 608 aa / 70.4 kDa |
| UniProt ID | Q86YW0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Cytoplasm, perinuclear region |
| 蛋白大小 | 10/10 | ×1 | 10 | 608 aa / 70.4 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=66 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000008, IPR035892, IPR011992, IPR002048, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)
- pronucleus (GO:0045120)
- sperm head (GO:0061827)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 66 |
| PubMed broad count | 197 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genetic mechanisms of fertilization failure and early embryonic arrest: a comprehensive review.. *Human reproduction update*. PMID: 37758324
2. Total fertilization failure after ICSI: insights into pathophysiology, diagnosis, and management through artificial oocyte activation.. *Human reproduction update*. PMID: 36977357
3. SPERM FACTORS AND EGG ACTIVATION: Phospholipase C zeta (PLCZ1) and the clinical diagnosis of oocyte activation deficiency.. *Reproduction (Cambridge, England)*. PMID: 35312629
4. SPERM FACTORS AND EGG ACTIVATION: The structure and function relationship of sperm PLCZ1.. *Reproduction (Cambridge, England)*. PMID: 35521907
5. Phospholipase C Zeta 1 (PLCZ1): The Function and Potential for Fertility Assessment and In Vitro Embryo Production in Cattle and Horses.. *Veterinary sciences*. PMID: 38133249

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.0 |
| 高置信度残基 (pLDDT>90) 占比 | 81.2% |
| 置信残基 (pLDDT 70-90) 占比 | 13.8% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 2.6% |
| 有序区域 (pLDDT>70) 占比 | 95.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.0，有序区 95.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000008, IPR035892, IPR011992, IPR002048, IPR001192; Pfam: PF00168, PF09279, PF00388 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ITPR1 | 0.950 | 0.000 | — |
| ITPR3 | 0.943 | 0.000 | — |
| ITPR2 | 0.921 | 0.000 | — |
| PRKCA | 0.916 | 0.000 | — |
| IPMK | 0.915 | 0.093 | — |
| INPP5A | 0.914 | 0.000 | — |
| CDIPT | 0.910 | 0.000 | — |
| PRKCG | 0.908 | 0.000 | — |
| PRKCB | 0.908 | 0.000 | — |
| PIKFYVE | 0.904 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PRKCSH | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| NPM1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ACTC1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SEMG1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HAL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KLK7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CST6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ECM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SERPINA12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ALOX12B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.0 + PDB: 无 | pLDDT=92.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, perinuclear region / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PLCZ1 — 1-phosphatidylinositol 4,5-bisphosphate phosphodiesterase zeta-1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小608 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 66 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86YW0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139151-PLCZ1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLCZ1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86YW0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86YW0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
