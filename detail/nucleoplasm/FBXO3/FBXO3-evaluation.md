---
type: protein-evaluation
gene: "FBXO3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXO3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO3 / FBX3 |
| 蛋白名称 | F-box only protein 3 |
| 蛋白大小 | 471 aa / 54.6 kDa |
| UniProt ID | Q9UK99 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 471 aa / 54.6 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=45 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=88.7; PDB: 5HDW, 9KBD, 9KBF |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR007474, IPR036767, IPR036047, IPR001810, IPR052 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- SCF ubiquitin ligase complex (GO:0019005)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 45 |
| PubMed broad count | 53 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBX3 |

**关键文献**:
1. Phosphorylation regulates cullin-based ubiquitination in tumorigenesis.. *Acta pharmaceutica Sinica. B*. PMID: 33643814
2. Rift Valley fever virus coordinates the assembly of a programmable E3 ligase to promote viral replication.. *Cell*. PMID: 39366381
3. High-throughput diversification of protein-ligand surfaces to discover chemical inducers of proximity.. *bioRxiv : the preprint server for biology*. PMID: 40950085
4. Diverse Roles of F-BoxProtein3 in Regulation of Various Cellular Functions.. *Frontiers in cell and developmental biology*. PMID: 35127719
5. FBXO3 stabilizes USP4 and Twist1 to promote PI3K-mediated breast cancer metastasis.. *PLoS biology*. PMID: 38134227

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.7 |
| 高置信度残基 (pLDDT>90) 占比 | 82.4% |
| 置信残基 (pLDDT 70-90) 占比 | 4.0% |
| 中等置信 (pLDDT 50-70) 占比 | 4.7% |
| 低置信 (pLDDT<50) 占比 | 8.9% |
| 有序区域 (pLDDT>70) 占比 | 86.4% |
| 可用 PDB 条目 | 5HDW, 9KBD, 9KBF |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（5HDW, 9KBD, 9KBF）+ AlphaFold高质量预测（pLDDT=88.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007474, IPR036767, IPR036047, IPR001810, IPR052121; Pfam: PF04379, PF12937, PF09346 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.994 | 0.881 | — |
| CUL1 | 0.989 | 0.833 | — |
| KIAA1549L | 0.872 | 0.000 | — |
| FBXL2 | 0.860 | 0.510 | — |
| RBX1 | 0.822 | 0.750 | — |
| POLD2 | 0.669 | 0.000 | — |
| NUDCD1 | 0.626 | 0.619 | — |
| C11orf91 | 0.604 | 0.000 | — |
| FBXL15 | 0.597 | 0.000 | — |
| CEACAM1 | 0.596 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SkpA | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| Prosbeta3 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| tat | psi-mi:"MI:0096"(pull down) | imex:IM-17346|pubmed:22190034| |
| TNIP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| Ogdh1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| skl | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG14053 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Idgf4 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| elm | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dysb | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.7 + PDB: 5HDW, 9KBD, 9KBF | pLDDT=88.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FBXO3 — F-box only protein 3，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小471 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 45 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UK99
- Protein Atlas: https://www.proteinatlas.org/ENSG00000110429-FBXO3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UK99
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
