---
type: protein-evaluation
gene: "HDGFL2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HDGFL2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HDGFL2 / HDGF2, HDGFRP2, HRP2 |
| 蛋白名称 | Hepatoma-derived growth factor-related protein 2 |
| 蛋白大小 | 671 aa / 74.3 kDa |
| UniProt ID | Q7Z4V5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Mitochondria, Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 671 aa / 74.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.9; PDB: 3EAE, 3QBY, 3QJ6, 6T3I, 7HG0, 7HG1, 7HG2 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036218, IPR021567, IPR000313, IPR035441; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.5/180** | |
| **归一化总分** | | | **73.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Mitochondria, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HDGF2, HDGFRP2, HRP2 |

**关键文献**:
1. A fluid biomarker reveals loss of TDP-43 splicing repression in presymptomatic ALS-FTD.. *Nature medicine*. PMID: 38278991
2. Loss of TDP-43 Splicing Repression Occurs in Myonuclei of Inclusion Body Myositis Patients.. *Annals of neurology*. PMID: 39757935
3. TDP-43 Cryptic RNAs in Perry Syndrome: Differences across Brain Regions and TDP-43 Proteinopathies.. *Movement disorders : official journal of the Movement Disorder Society*. PMID: 39788898
4. A fluid biomarker reveals loss of TDP-43 splicing repression in pre-symptomatic ALS.. *bioRxiv : the preprint server for biology*. PMID: 36789434
5. HDGFL2 cryptic proteins report presence of TDP-43 pathology in neurodegenerative diseases.. *Molecular neurodegeneration*. PMID: 38539264

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.9 |
| 高置信度残基 (pLDDT>90) 占比 | 20.0% |
| 置信残基 (pLDDT 70-90) 占比 | 11.6% |
| 中等置信 (pLDDT 50-70) 占比 | 16.2% |
| 低置信 (pLDDT<50) 占比 | 52.2% |
| 有序区域 (pLDDT>70) 占比 | 31.6% |
| 可用 PDB 条目 | 3EAE, 3QBY, 3QJ6, 6T3I, 7HG0, 7HG1, 7HG2, 7HG3, 7HG4, 7HG5 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=59.9），有序残基占 31.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036218, IPR021567, IPR000313, IPR035441; Pfam: PF11467, PF00855 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| H3-3B | 0.952 | 0.905 | — |
| H3C14 | 0.949 | 0.948 | — |
| H3C1 | 0.945 | 0.945 | — |
| H3C12 | 0.923 | 0.908 | — |
| H3C13 | 0.921 | 0.905 | — |
| H3-4 | 0.919 | 0.905 | — |
| H3-3A | 0.909 | 0.905 | — |
| H3C10 | 0.905 | 0.905 | — |
| H3C2 | 0.905 | 0.905 | — |
| H3C4 | 0.905 | 0.905 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ARRB1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CSNK2A1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22113938|imex:IM-16640 |
| ARRB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17620599 |
| CSNK2A2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| PARK7 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| H3C1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| PLGRKT | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| CDK7 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| LMNA | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| Dld | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | doi:10.1016/j.cels.2017.10.010 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.9 + PDB: 3EAE, 3QBY, 3QJ6, 6T3I, 7HG0,  | pLDDT=59.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Mitochondria, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HDGFL2 — Hepatoma-derived growth factor-related protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小671 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=59.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z4V5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167674-HDGFL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HDGFL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z4V5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HDGFL2/IF_images/U-251MG_1.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HDGFL2/IF_images/NIH-3T3_1.jpg]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HDGFL2/HDGFL2-PAE.png]]
