---
type: protein-evaluation
gene: "EXOSC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EXOSC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EXOSC1 / CSL4 |
| 蛋白名称 | Exosome complex component CSL4 |
| 蛋白大小 | 195 aa / 21.5 kDa |
| UniProt ID | Q9Y3B2 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/EXOSC1/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/EXOSC1/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; 额外: Nucleoplasm; UniProt: Nucleus, nucleolus; Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 195 aa / 21.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=0; PDB: 2NN6, 6D6Q, 6D6R, 6H25, 9G8M, 9G8N, 9G8O |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039771, IPR019495, IPR025721, IPR012340, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies; 额外: Nucleoplasm | Approved |
| UniProt | Nucleus, nucleolus; Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic exosome (RNase complex) (GO:0000177)
- cytosol (GO:0005829)
- exosome (RNase complex) (GO:0000178)
- nuclear exosome (RNase complex) (GO:0000176)
- nucleolar exosome (RNase complex) (GO:0101019)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 20 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CSL4 |

**关键文献**:
1. Bi-allelic missense variant, p.Ser35Leu in EXOSC1 is associated with pontocerebellar hypoplasia.. *Clinical genetics*. PMID: 33463720
2. The mRNA export pathway licenses viral mimicry response and antitumor immunity by actively exporting nuclear retroelement transcripts.. *Science translational medicine*. PMID: 40203080
3. RNA exosome mutations in pontocerebellar hypoplasia alter ribosome biogenesis and p53 levels.. *Life science alliance*. PMID: 32527837
4. Comprehensive bioinformatics analysis of EXOSC family genes in lung adenocarcinoma.. *Discover oncology*. PMID: 42171853
5. Pontocerebellar hypoplasia associated with p.Arg183Trp homozygous variant in EXOSC1 gene: A case report.. *American journal of medical genetics. Part A*. PMID: 37024942

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 2NN6, 6D6Q, 6D6R, 6H25, 9G8M, 9G8N, 9G8O, 9G8P |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/EXOSC1/EXOSC1-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039771, IPR019495, IPR025721, IPR012340, IPR003029; Pfam: PF14382, PF10447 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EXOSC2 | 0.999 | 0.997 | — |
| EXOSC3 | 0.999 | 0.999 | — |
| MPHOSPH6 | 0.999 | 0.988 | — |
| C1D | 0.999 | 0.991 | — |
| EXOSC9 | 0.999 | 0.997 | — |
| EXOSC10 | 0.999 | 0.998 | — |
| DIS3 | 0.999 | 0.999 | — |
| EXOSC5 | 0.999 | 0.998 | — |
| EXOSC6 | 0.999 | 0.997 | — |
| EXOSC8 | 0.999 | 0.997 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EXOSC5 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| EXOSC4 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| EXOSC8 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| UPF2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| EXOSC7 | psi-mi:"MI:0018"(two hybrid) | pubmed:12419256 |
| MTMR3 | psi-mi:"MI:0018"(two hybrid) | pubmed:12419256 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| A2M | psi-mi:"MI:0397"(two hybrid array) | doi:10.1101/gr.114280.110|imex |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 2NN6, 6D6Q, 6D6R, 6H25, 9G8M,  | pLDDT=0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus; Nucleus; Cytoplasm / Nuclear bodies; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. EXOSC1 — Exosome complex component CSL4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小195 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y3B2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171311-EXOSC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EXOSC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y3B2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-body/EXOSC1/EXOSC1-PAE.png]]




