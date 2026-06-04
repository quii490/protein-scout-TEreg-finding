---
type: protein-evaluation
gene: "MTMR10"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MTMR10 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MTMR10 |
| 蛋白名称 | Myotubularin-related protein 10 |
| 蛋白大小 | 777 aa / 88.3 kDa |
| UniProt ID | Q9NXD2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Nuclear bodies; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 777 aa / 88.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036004, IPR030573, IPR022587, IPR030564, IPR010 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Common and rare variant analyses implicate late-infancy cerebellar development and immune genes in ADHD.. *Journal of neurodevelopmental disorders*. PMID: 40542392
2. Identification and Validation of Prognostic Risk Model for Female-Specific Lung Adenocarcinoma.. *Alternative therapies in health and medicine*. PMID: 39038326
3. Histone modification-based functional characterization and genetic association of polymorphisms in LRRC6 and MTMR10 within CRC susceptibility regions 8q24 and 15q13.3.. *Gene*. PMID: 39875006
4. miR-149-3p Is a Potential Prognosis Biomarker and Correlated with Immune Infiltrates in Uterine Corpus Endometrial Carcinoma.. *International journal of endocrinology*. PMID: 35719192
5. Molecular, physiological and behavioral characterization of the heterozygous Df[h15q13]/+ mouse model associated with the human 15q13.3 microdeletion syndrome.. *Brain research*. PMID: 32712126

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.8 |
| 高置信度残基 (pLDDT>90) 占比 | 54.8% |
| 置信残基 (pLDDT 70-90) 占比 | 18.4% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 20.2% |
| 有序区域 (pLDDT>70) 占比 | 73.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=78.8，有序区 73.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036004, IPR030573, IPR022587, IPR030564, IPR010569; Pfam: PF12578, PF06602 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MTMR2 | 0.968 | 0.442 | — |
| FAN1 | 0.949 | 0.000 | — |
| TRPM1 | 0.933 | 0.000 | — |
| OTUD7A | 0.808 | 0.000 | — |
| IFT80 | 0.763 | 0.000 | — |
| KLF13 | 0.731 | 0.103 | — |
| ARHGAP11B-2 | 0.673 | 0.050 | — |
| ARHGAP11B | 0.667 | 0.050 | — |
| FMN1 | 0.654 | 0.068 | — |
| DYNC2H1 | 0.648 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| A0A1J9UYI5 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MEOX2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-24135|pubmed:24722188| |
| PSMB4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-23318|pubmed:25416956 |
| Mtmr2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| PLEKHG3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SVIL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NEXN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MPRIP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PBRM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.8 + PDB: 无 | pLDDT=78.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Nuclear bodies; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. MTMR10 — Myotubularin-related protein 10，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小777 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NXD2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166912-MTMR10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MTMR10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NXD2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
