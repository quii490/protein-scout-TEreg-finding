---
type: protein-evaluation
gene: "CPNE1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CPNE1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CPNE1 / CPN1 |
| 蛋白名称 | Copine-1 |
| 蛋白大小 | 537 aa / 59.1 kDa |
| UniProt ID | Q99829 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Nuclear membrane; UniProt: Nucleus; Cytoplasm; Cell membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 537 aa / 59.1 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=48 篇 (<=60->6) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=91.9; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR000008, IPR035892, IPR037768, IPR045052, IPR010 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear membrane | Supported |
| UniProt | Nucleus; Cytoplasm; Cell membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- azurophil granule membrane (GO:0035577)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- membrane (GO:0016020)
- nuclear membrane (GO:0031965)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 48 |
| PubMed broad count | 73 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CPN1 |

**关键文献**:
1. Integrated ubiquitomics characterization of hepatocellular carcinomas.. *Hepatology (Baltimore, Md.)*. PMID: 39348425
2. Expression and Significance of MTA2 and CPNE1 in Cervical Squamous Cell Carcinoma.. *Applied immunohistochemistry & molecular morphology : AIMM*. PMID: 37399268
3. Copine 1 predicts poor clinical outcomes by promoting M2 macrophage activation in ovarian cancer.. *Carcinogenesis*. PMID: 37747823
4. Role of CPNE1 in Odontoblastic Differentiation of Rat Stem Cells from Apical Papilla.. *Advanced biology*. PMID: 37132099
5. 14-3-3γ regulates Copine1-mediated neuronal differentiation in HiB5 hippocampal progenitor cells.. *Experimental cell research*. PMID: 28412242

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.9 |
| 高置信度残基 (pLDDT>90) 占比 | 80.3% |
| 置信残基 (pLDDT 70-90) 占比 | 16.2% |
| 中等置信 (pLDDT 50-70) 占比 | 0.9% |
| 低置信 (pLDDT<50) 占比 | 2.6% |
| 有序区域 (pLDDT>70) 占比 | 96.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.9，有序区 96.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000008, IPR035892, IPR037768, IPR045052, IPR010734; Pfam: PF00168, PF07002 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| REPS1 | 0.570 | 0.000 | — |
| C20orf27 | 0.541 | 0.000 | — |
| IRGQ | 0.535 | 0.052 | — |
| AFTPH | 0.527 | 0.000 | — |
| AP1G2 | 0.519 | 0.000 | — |
| TOR4A | 0.515 | 0.000 | — |
| AATF | 0.511 | 0.000 | — |
| ERGIC3 | 0.494 | 0.000 | — |
| ADPGK | 0.459 | 0.000 | — |
| SWAP70 | 0.455 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| STK3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| BUB3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ARRB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17620599 |
| UIMC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| EBI-1257121 | psi-mi:"MI:0400"(affinity technology) | pubmed:19367725|imex:IM-20587 |
| FN1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-14135|pubmed:19738201 |
| CFTR | psi-mi:"MI:0096"(pull down) | pubmed:29924966|imex:IM-27204 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| LHX6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.9 + PDB: 无 | pLDDT=91.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cell membrane / Nucleoplasm, Nuclear membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. CPNE1 -- Copine-1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小537 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 48 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99829
- Protein Atlas: https://www.proteinatlas.org/ENSG00000214078-CPNE1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CPNE1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99829
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
