---
type: protein-evaluation
gene: "GPS1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GPS1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPS1 / COPS1, CSN1 |
| 蛋白名称 | COP9 signalosome complex subunit 1 |
| 蛋白大小 | 491 aa / 55.5 kDa |
| UniProt ID | Q13098 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 491 aa / 55.5 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=54 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=84.6; PDB: 4D10, 4D18, 4WSN, 6R6H, 6R7F, 6R7H, 6R7I |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR048624, IPR000717, IPR019585, IPR045135, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分** | | | **70.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Enhanced |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- COP9 signalosome (GO:0008180)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 54 |
| PubMed broad count | 117 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: COPS1, CSN1 |

**关键文献**:
1. Proteome asymmetry in mouse and human embryos before fate specification.. *bioRxiv : the preprint server for biology*. PMID: 39253500
2. Bioinformatics analysis of GPS1 expression and biological function in breast cancer.. *Journal of cancer research and clinical oncology*. PMID: 38289496
3. G Protein Pathway Suppressor 1 Promotes Influenza Virus Polymerase Activity by Activating the NF-κB Signaling Pathway.. *mBio*. PMID: 31848286
4. Ankyrin repeat and SOCS box containing protein 4 (Asb-4) interacts with GPS1 (CSN1) and inhibits c-Jun NH2-terminal kinase activity.. *Cellular signalling*. PMID: 17276034
5. Prognostic features of bladder cancer based on five neddylation-related genes.. *American journal of clinical and experimental urology*. PMID: 39584004

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.6 |
| 高置信度残基 (pLDDT>90) 占比 | 68.4% |
| 置信残基 (pLDDT 70-90) 占比 | 15.5% |
| 中等置信 (pLDDT 50-70) 占比 | 4.5% |
| 低置信 (pLDDT<50) 占比 | 11.6% |
| 有序区域 (pLDDT>70) 占比 | 83.9% |
| 可用 PDB 条目 | 4D10, 4D18, 4WSN, 6R6H, 6R7F, 6R7H, 6R7I, 6R7N, 8H38, 8H3A |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（4D10, 4D18, 4WSN, 6R6H, 6R7F, 6R7H, 6R7I, 6R7N, 8H38, 8H3A）+ AlphaFold极高置信度预测（pLDDT=84.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR048624, IPR000717, IPR019585, IPR045135, IPR036390; Pfam: PF21151, PF01399, PF10602 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COPS8 | 0.999 | 0.996 | — |
| COPS4 | 0.999 | 0.997 | — |
| COPS5 | 0.999 | 0.995 | — |
| COPS7B | 0.999 | 0.987 | — |
| COPS3 | 0.999 | 0.997 | — |
| COPS2 | 0.999 | 0.999 | — |
| COPS7A | 0.999 | 0.991 | — |
| COPS6 | 0.999 | 0.993 | — |
| RBX1 | 0.982 | 0.953 | — |
| NEDD8 | 0.981 | 0.924 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TBC1D17 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| WRAP73 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:18850735|imex:IM-20477 |
| vpr | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| COPS6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| Ddb1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| A0A384LH97 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000302873.6 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| DCUN1D1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.6 + PDB: 4D10, 4D18, 4WSN, 6R6H, 6R7F,  | pLDDT=84.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GPS1 — COP9 signalosome complex subunit 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小491 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 54 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13098
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169727-GPS1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPS1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13098
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
