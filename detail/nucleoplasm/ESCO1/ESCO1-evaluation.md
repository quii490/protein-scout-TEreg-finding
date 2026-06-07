---
type: protein-evaluation
gene: "ESCO1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ESCO1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ESCO1 / EFO1, KIAA1911 |
| 蛋白名称 | N-acetyltransferase ESCO1 |
| 蛋白大小 | 840 aa / 95.0 kDa |
| UniProt ID | Q5FWF5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 8/10 | ×1 | 8 | 840 aa / 95.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=52.4; PDB: 4MXE, 5T53 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028005, IPR028009; Pfam: PF13880, PF13878 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **122.5/180** | |
| **归一化总分** | | | **68.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromosome (GO:0005694)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 64 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EFO1, KIAA1911 |

**关键文献**:
1. Altered Cohesin Dynamics During Cellular Differentiation.. *bioRxiv : the preprint server for biology*. PMID: 41509300
2. Esco1 and Esco2 regulate distinct cohesin functions during cell cycle progression.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 28847955
3. The intrinsically disordered tail of ESCO1 binds DNA in a charge-dependent manner.. *bioRxiv : the preprint server for biology*. PMID: 38106185
4. ESCO1 and CTCF enable formation of long chromatin loops by protecting cohesin(STAG1) from WAPL.. *eLife*. PMID: 32065581
5. HPV E6/E7-Induced Acetylation of a Peptide Encoded by a Long Non-Coding RNA Inhibits Ferroptosis to Promote the Malignancy of Cervical Cancer.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39836502

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 52.4 |
| 高置信度残基 (pLDDT>90) 占比 | 20.0% |
| 置信残基 (pLDDT 70-90) 占比 | 7.5% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 67.0% |
| 有序区域 (pLDDT>70) 占比 | 27.5% |
| 可用 PDB 条目 | 4MXE, 5T53 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ESCO1/ESCO1-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=52.4），有序残基占 27.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028005, IPR028009; Pfam: PF13880, PF13878 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMC3 | 0.997 | 0.836 | — |
| PDS5A | 0.994 | 0.516 | — |
| WAPL | 0.982 | 0.000 | — |
| CHTF18 | 0.964 | 0.306 | — |
| RAD21 | 0.959 | 0.410 | — |
| STAG1 | 0.952 | 0.204 | — |
| CHTF8 | 0.904 | 0.189 | — |
| PDS5B | 0.891 | 0.500 | — |
| DSCC1 | 0.889 | 0.117 | — |
| GLYATL1 | 0.880 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| B9EKQ9 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| PDIA3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SMC6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Racgap1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Crebbp | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Cct4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Nrip3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CDK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Cct8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CEP43 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=52.4 + PDB: 4MXE, 5T53 | pLDDT=52.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. ESCO1 — N-acetyltransferase ESCO1，非常新颖，仅有少数基础研究。
2. 蛋白大小840 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=52.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5FWF5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000141446-ESCO1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ESCO1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5FWF5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ESCO1/ESCO1-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5FWF5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR028005;IPR028009; |
| Pfam | PF13880;PF13878; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000141446-ESCO1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CALM1 | Opencell | false |
| CALM2 | Opencell | false |
| CALM3 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
