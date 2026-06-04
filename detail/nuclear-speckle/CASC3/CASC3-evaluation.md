---
type: protein-evaluation
gene: "CASC3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CASC3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CASC3 / MLN51 |
| 蛋白名称 | Protein CASC3 |
| 蛋白大小 | 703 aa / 76.3 kDa |
| UniProt ID | O15234 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane; UniProt: Cytoplasm; Cytoplasm, perinuclear region; Nucleus; Nucleus s |
| 蛋白大小 | 10/10 | ×1 | 10 | 703 aa / 76.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.4; PDB: 2HYI, 2J0Q, 2J0S, 2J0U, 2XB2, 3EX7, 5XJC |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR018545, IPR028544; Pfam: PF09405 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.5/180** | |
| **归一化总分** | | | **73.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane | Supported |
| UniProt | Cytoplasm; Cytoplasm, perinuclear region; Nucleus; Nucleus speckle; Cytoplasm, Stress granule; Cytop... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasmic stress granule (GO:0010494)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- exon-exon junction complex (GO:0035145)
- nuclear membrane (GO:0031965)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 60 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MLN51 |

**关键文献**:
1. CASC3 Biomolecular Condensates Restrict Turnip Crinkle Virus by Limiting Host Factor Availability.. *Journal of molecular biology*. PMID: 36642157
2. Cell-Penetrating Peptides Predicted From CASC3, AKIP1, and AHRR Proteins.. *Frontiers in pharmacology*. PMID: 34504427
3. CASC3 promotes transcriptome-wide activation of nonsense-mediated decay by the exon junction complex.. *Nucleic acids research*. PMID: 32621609
4. Roles of the exon junction complex components in the central nervous system: a mini review.. *Reviews in the neurosciences*. PMID: 29791316
5. Identification of suitable reference genes in bone marrow stromal cells from osteoarthritic donors.. *Stem cell research*. PMID: 24080205

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.4 |
| 高置信度残基 (pLDDT>90) 占比 | 7.4% |
| 置信残基 (pLDDT 70-90) 占比 | 7.1% |
| 中等置信 (pLDDT 50-70) 占比 | 30.0% |
| 低置信 (pLDDT<50) 占比 | 55.5% |
| 有序区域 (pLDDT>70) 占比 | 14.5% |
| 可用 PDB 条目 | 2HYI, 2J0Q, 2J0S, 2J0U, 2XB2, 3EX7, 5XJC, 5YZG, 6ICZ, 7W59 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=53.4），有序残基占 14.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018545, IPR028544; Pfam: PF09405 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UPF3A | 0.999 | 0.994 | — |
| EIF4A3 | 0.999 | 0.999 | — |
| RBM8A | 0.999 | 0.998 | — |
| UPF3B | 0.999 | 0.998 | — |
| UPF1 | 0.999 | 0.994 | — |
| MAGOH | 0.999 | 0.999 | — |
| MAGOHB | 0.999 | 0.906 | — |
| UPF2 | 0.994 | 0.735 | — |
| CWC22 | 0.992 | 0.800 | — |
| SNRNP200 | 0.983 | 0.800 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MLN51 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| PAB2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| PAB8 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| TCP19 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| KINB1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:36376753|imex:IM-29283 |
| EIF4A3 | psi-mi:"MI:0096"(pull down) | pubmed:14973490 |
| MAGOH | psi-mi:"MI:0096"(pull down) | pubmed:14973490 |
| RBM8A | psi-mi:"MI:0114"(x-ray crystallography) | imex:IM-11860|pubmed:16923391 |
| GRB2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| CDK6 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22094256|imex:IM-16628 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.4 + PDB: 2HYI, 2J0Q, 2J0S, 2J0U, 2XB2,  | pLDDT=53.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, perinuclear region; Nucleus; / Nuclear membrane | 一致 |
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
1. CASC3 — Protein CASC3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小703 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=53.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15234
- Protein Atlas: https://www.proteinatlas.org/ENSG00000108349-CASC3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CASC3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15234
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/CASC3/IF_images/A-431_2.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/CASC3/IF_images/A-431_1.jpg]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/CASC3/CASC3-PAE.png]]
