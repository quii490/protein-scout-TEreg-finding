---
type: protein-evaluation
gene: "ASB2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ASB2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ASB2 |
| 蛋白名称 | Ankyrin repeat and SOCS box protein 2 |
| 蛋白大小 | 635 aa / 70.2 kDa |
| UniProt ID | Q96Q27 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli fibrillar center; 额外: Nucleoplasm, Cytosol; UniProt: Cytoplasm, cytoskeleton, stress fiber; Cytoplasm, myofibril, |
| 蛋白大小 | 10/10 | ×1 | 10 | 635 aa / 70.2 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=70 篇 (≤80→4) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002110, IPR036770, IPR037330, IPR001496, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.5/180** | |
| **归一化总分** | | | **58.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center; 额外: Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm, cytoskeleton, stress fiber; Cytoplasm, myofibril, sarcomere, Z line | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- stress fiber (GO:0001725)
- ubiquitin ligase complex (GO:0000151)
- Z disc (GO:0030018)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 70 |
| PubMed broad count | 130 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Skeletal Muscle-Specific Deletion of E3 Ligase Asb2 Enhances Muscle Mass and Strength.. *Journal of cachexia, sarcopenia and muscle*. PMID: 40641155
2. Notch-induced Asb2 expression promotes protein ubiquitination by forming non-canonical E3 ligase complexes.. *Cell research*. PMID: 21119685
3. Discovery of a potent PROTAC degrader for RNA demethylase FTO as antileukemic therapy.. *Acta pharmaceutica Sinica. B*. PMID: 39807332
4. YTHDF2 governs muscle size through a targeted modulation of proteostasis.. *Nature communications*. PMID: 38467649
5. Meta-analysis identifies key genes and pathways implicated in Benzo[a]pyrene exposure response.. *Chemosphere*. PMID: 39154768

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.7 |
| 高置信度残基 (pLDDT>90) 占比 | 67.7% |
| 置信残基 (pLDDT 70-90) 占比 | 15.0% |
| 中等置信 (pLDDT 50-70) 占比 | 2.2% |
| 低置信 (pLDDT<50) 占比 | 15.1% |
| 有序区域 (pLDDT>70) 占比 | 82.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=83.7，有序区 82.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR037330, IPR001496, IPR036036; Pfam: PF12796, PF13606, PF13637 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL5 | 0.982 | 0.785 | — |
| RNF7 | 0.956 | 0.644 | — |
| ELOC | 0.865 | 0.731 | — |
| ASB17 | 0.863 | 0.000 | — |
| FLNA | 0.836 | 0.742 | — |
| ELOB | 0.825 | 0.630 | — |
| CISH | 0.811 | 0.000 | — |
| CAND1 | 0.689 | 0.292 | — |
| FTO | 0.662 | 0.045 | — |
| UBC | 0.661 | 0.648 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ESR2 | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-13781|pubmed:21182203 |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| NFKB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DCUN1D3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CUL5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NDUFA10 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| Rab40b | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:26885862|imex:IM-24977 |
| PRKN | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.7 + PDB: 无 | pLDDT=83.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, stress fiber; Cytoplasm,  / Nucleoli fibrillar center; 额外: Nucleoplasm, Cytoso | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. ASB2 — Ankyrin repeat and SOCS box protein 2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小635 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 70 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96Q27
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100628-ASB2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ASB2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96Q27
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
