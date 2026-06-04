---
type: protein-evaluation
gene: "ELP6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ELP6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ELP6 / ATP1, C3orf75, TMEM103 |
| 蛋白名称 | Elongator complex protein 6 |
| 蛋白大小 | 266 aa / 29.8 kDa |
| UniProt ID | Q0PNE2 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELP6/IF_images/PC-3_1.jpg|PC-3]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELP6/IF_images/SH-SY5Y_1.jpg|SH-SY5Y]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Centrosome; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 266 aa / 29.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR018627, IPR027417; Pfam: PF09807 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/180** | |
| **归一化总分** | | | **71.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Centrosome | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cytosol (GO:0005829)
- elongator holoenzyme complex (GO:0033588)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed broad count | 45 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ATP1, C3orf75, TMEM103 |

**关键文献**:
1. Developing and mature human granulocytes express ELP 6 in the cytoplasm.. *Human antibodies*. PMID: 24284306
2. Evolutionary Conservation in Protein-Protein Interactions and Structures of the Elongator Sub-Complex ELP456 from Arabidopsis and Yeast.. *International journal of molecular sciences*. PMID: 38673955
3. Structural insights into the function of Elongator.. *Cellular and molecular life sciences : CMLS*. PMID: 29332244
4. An early step in wobble uridine tRNA modification requires the Elongator complex.. *RNA (New York, N.Y.)*. PMID: 15769872
5. Role of ELP6 in tumour progression and impact on ERK1/2 signalling pathway inhibitors in skin cutaneous melanoma.. *Oncology letters*. PMID: 40177137

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.4 |
| 高置信度残基 (pLDDT>90) 占比 | 75.2% |
| 置信残基 (pLDDT 70-90) 占比 | 16.9% |
| 中等置信 (pLDDT 50-70) 占比 | 6.4% |
| 低置信 (pLDDT<50) 占比 | 1.5% |
| 有序区域 (pLDDT>70) 占比 | 92.1% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELP6/ELP6-PAE.png]]

**评价**: AlphaFold 极高置信度预测（pLDDT=90.4，有序区 92.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018627, IPR027417; Pfam: PF09807 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ELP5 | 0.999 | 0.854 | — |
| ELP4 | 0.999 | 0.841 | — |
| ELP3 | 0.996 | 0.429 | — |
| ELP2 | 0.992 | 0.228 | — |
| ELP1 | 0.990 | 0.292 | — |
| PIPOX | 0.835 | 0.835 | — |
| ABCA5 | 0.810 | 0.000 | — |
| ABCA7 | 0.761 | 0.000 | — |
| ABCA2 | 0.738 | 0.000 | — |
| MT-ATP6 | 0.729 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| D6W0D9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22556426|imex:IM-20530 |
| ELP3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| cg9025 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| IKI1 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |
| IKI3 | psi-mi:"MI:0091"(chromatography technology) | pubmed:11435442|imex:IM-19719 |
| ELP2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:11689709|imex:IM-19720 |
| ELP4 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:11689709|imex:IM-19720 |
| cg1316 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| MLH1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15124|pubmed:20706999 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.4 + PDB: 无 | pLDDT=90.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Cytosol; 额外: Centrosome | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. ELP6 — Elongator complex protein 6，非常新颖，仅有少数基础研究。
2. 蛋白大小266 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q0PNE2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163832-ELP6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ELP6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q0PNE2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELP6/ELP6-PAE.png]]




