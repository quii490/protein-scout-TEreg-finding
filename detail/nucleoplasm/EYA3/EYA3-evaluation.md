---
type: protein-evaluation
gene: "EYA3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EYA3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EYA3 |
| 蛋白名称 | Protein phosphatase EYA3 |
| 蛋白大小 | 573 aa / 62.7 kDa |
| UniProt ID | Q99504 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EYA3/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EYA3/IF_images/HEK293_1.jpg|HEK293]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Centrosome; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 573 aa / 62.7 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=62 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.2; PDB: 9C7T |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028472, IPR006545, IPR042577, IPR038102; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.5/180** | |
| **归一化总分** | | | **55.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Centrosome | Enhanced |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 62 |
| PubMed broad count | 112 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Cryo-EM structures of PP2A:B55 with p107 and Eya3 define substrate recruitment.. *Nature structural & molecular biology*. PMID: 40247147
2. Biochemical characterization of the Eya and PP2A-B55α interaction.. *The Journal of biological chemistry*. PMID: 38796066
3. Cryo-EM structures reveal the PP2A-B55α and Eya3 interaction that can be disrupted by a peptide inhibitor.. *The Journal of biological chemistry*. PMID: 40414499
4. Inhibitors of EYA3 Protein in Ewing Sarcoma.. *Asian Pacific journal of cancer prevention : APJCP*. PMID: 35633536
5. RBFOX2 regulated EYA3 isoforms partner with SIX4 or ZBTB1 to control transcription during myogenesis.. *iScience*. PMID: 38026174

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.2 |
| 高置信度残基 (pLDDT>90) 占比 | 44.2% |
| 置信残基 (pLDDT 70-90) 占比 | 0.9% |
| 中等置信 (pLDDT 50-70) 占比 | 3.3% |
| 低置信 (pLDDT<50) 占比 | 51.7% |
| 有序区域 (pLDDT>70) 占比 | 45.1% |
| 可用 PDB 条目 | 9C7T |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EYA3/EYA3-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=65.2），有序残基占 45.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028472, IPR006545, IPR042577, IPR038102; Pfam: PF00702 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SIX1 | 0.906 | 0.394 | — |
| SIX2 | 0.881 | 0.576 | — |
| SIX5 | 0.833 | 0.751 | — |
| H2AX | 0.808 | 0.292 | — |
| SIX4 | 0.754 | 0.394 | — |
| DACH1 | 0.706 | 0.300 | — |
| TSHB | 0.692 | 0.000 | — |
| MDC1 | 0.662 | 0.000 | — |
| SIX6 | 0.662 | 0.301 | — |
| ATM | 0.605 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dach1 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:14628042 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| TCEAL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SIX2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZDHHC17 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-21827|pubmed:24705354 |
| CRK | psi-mi:"MI:0397"(two hybrid array) | pubmed:25814554|imex:IM-22632 |
| UBE4B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| EEF1AKMT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| WFS1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| KIF1B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.2 + PDB: 9C7T | pLDDT=65.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Centrosome | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. EYA3 — Protein phosphatase EYA3，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小573 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 62 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=65.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99504
- Protein Atlas: https://www.proteinatlas.org/ENSG00000158161-EYA3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EYA3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99504
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/EYA3/EYA3-PAE.png]]




