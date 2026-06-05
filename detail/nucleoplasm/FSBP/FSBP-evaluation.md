---
type: protein-evaluation
gene: "FSBP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FSBP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FSBP |
| 蛋白名称 | Fibrinogen silencer-binding protein |
| 蛋白大小 | 299 aa / 34.8 kDa |
| UniProt ID | O95073 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 299 aa / 34.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR042383, IPR028002; Pfam: PF13873 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.0/180** | |
| **归一化总分** | | | **76.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 64 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Structural features and anti-neuroinflammatory activity of a glucan, FSBP-2, from Ferula sinkiangensis.. *International journal of biological macromolecules*. PMID: 40692052
2. Foetal steroid binding protein in British and Japanese women.. *Acta endocrinologica*. PMID: 3107299
3. Inferring circadian gene regulatory relationships from gene expression data with a hybrid framework.. *BMC bioinformatics*. PMID: 37752445
4. Amino acid digestibility and protein quality of fermented soybean-based ingredients using the precision-fed cecectomized rooster assay.. *Journal of animal science*. PMID: 40974165
5. Interactions of foetal steroid binding protein with other binding proteins in human serum.. *Clinica chimica acta; international journal of clinical chemistry*. PMID: 3123101

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.5 |
| 高置信度残基 (pLDDT>90) 占比 | 38.1% |
| 置信残基 (pLDDT 70-90) 占比 | 15.4% |
| 中等置信 (pLDDT 50-70) 占比 | 9.7% |
| 低置信 (pLDDT<50) 占比 | 36.8% |
| 有序区域 (pLDDT>70) 占比 | 53.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=69.5），有序残基占 53.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042383, IPR028002; Pfam: PF13873 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAD51 | 0.978 | 0.638 | — |
| ATRX | 0.964 | 0.000 | — |
| RAD52 | 0.957 | 0.402 | — |
| BRCA1 | 0.874 | 0.000 | — |
| VAC14 | 0.858 | 0.067 | — |
| BRCA2 | 0.838 | 0.073 | — |
| WRN | 0.797 | 0.309 | — |
| RAD51D-2 | 0.740 | 0.420 | — |
| RAD51B | 0.740 | 0.420 | — |
| RAD51D | 0.740 | 0.420 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000420405.2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:19060904|imex:IM-20259 |
| CD2BP2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PSMA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:19060904|imex:IM-20259 |
| NIF3L1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:19060904|imex:IM-20259 |
| ELOA | psi-mi:"MI:0397"(two hybrid array) | pubmed:19060904|imex:IM-20259 |
| NUDT18 | psi-mi:"MI:0397"(two hybrid array) | pubmed:19060904|imex:IM-20259 |
| HNRNPM | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HNRNPCL2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HNRNPC | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| LNX1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.5 + PDB: 无 | pLDDT=69.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FSBP — Fibrinogen silencer-binding protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小299 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95073
- Protein Atlas: https://www.proteinatlas.org/ENSG00000265817-FSBP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FSBP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95073
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000265817-FSBP/subcellular

![](https://images.proteinatlas.org/25059/1484_H11_1_red_green.jpg)
![](https://images.proteinatlas.org/25059/1484_H11_3_red_green.jpg)
![](https://images.proteinatlas.org/25059/1518_B9_2_red_green.jpg)
![](https://images.proteinatlas.org/25059/1518_B9_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
