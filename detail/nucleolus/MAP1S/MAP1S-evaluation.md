---
type: protein-evaluation
gene: "MAP1S"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAP1S 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAP1S / BPY2IP1, C19orf5, MAP8, VCY2IP1 |
| 蛋白名称 | Microtubule-associated protein 1S |
| 蛋白大小 | 1059 aa / 112.2 kDa |
| UniProt ID | Q66K74 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol, Principal piece; 额外: Nucleoplasm, Nucleoli; UniProt: Nucleus; Cytoplasm, cytosol; Cytoplasm, cytoskeleton; Cytopl |
| 蛋白大小 | 8/10 | ×1 | 8 | 1059 aa / 112.2 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=55 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026074, IPR057480, IPR056617; Pfam: PF23415, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.0/180** | |
| **归一化总分** | | | **60.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol, Principal piece; 额外: Nucleoplasm, Nucleoli | Supported |
| UniProt | Nucleus; Cytoplasm, cytosol; Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, spindle | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell projection (GO:0042995)
- centrosome (GO:0005813)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- microtubule (GO:0005874)
- microtubule associated complex (GO:0005875)
- microtubule organizing center (GO:0005815)
- mitotic spindle microtubule (GO:1990498)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 55 |
| PubMed broad count | 69 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BPY2IP1, C19orf5, MAP8, VCY2IP1 |

**关键文献**:
1. HBx-induced upregulation of MAP1S drives hepatocellular carcinoma proliferation and migration via MAP1S/Smad/TGF-β1 loop.. *International journal of biological macromolecules*. PMID: 39374711
2. Spermidine Prolongs Lifespan and Prevents Liver Fibrosis and Hepatocellular Carcinoma by Activating MAP1S-Mediated Autophagy.. *Cancer research*. PMID: 28386016
3. MAP1S Protein Regulates the Phagocytosis of Bacteria and Toll-like Receptor (TLR) Signaling.. *The Journal of biological chemistry*. PMID: 26565030
4. Prioritization of Drug Targets for Neurodegenerative Diseases by Integrating Genetic and Proteomic Data From Brain and Blood.. *Biological psychiatry*. PMID: 36759259
5. Whole-genome sequencing analysis reveals new susceptibility loci and structural variants associated with progressive supranuclear palsy.. *Molecular neurodegeneration*. PMID: 39152475

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.4 |
| 高置信度残基 (pLDDT>90) 占比 | 31.2% |
| 置信残基 (pLDDT 70-90) 占比 | 21.0% |
| 中等置信 (pLDDT 50-70) 占比 | 2.9% |
| 低置信 (pLDDT<50) 占比 | 44.9% |
| 有序区域 (pLDDT>70) 占比 | 52.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=65.4），有序残基占 52.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026074, IPR057480, IPR056617; Pfam: PF23415, PF25281 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RASSF1 | 0.989 | 0.785 | — |
| LRPPRC | 0.977 | 0.474 | — |
| SQSTM1 | 0.974 | 0.070 | — |
| MAP1LC3B | 0.943 | 0.185 | — |
| MAP1LC3A | 0.934 | 0.436 | — |
| ATG12 | 0.923 | 0.046 | — |
| BECN1 | 0.910 | 0.000 | — |
| ATG5 | 0.886 | 0.000 | — |
| GABARAPL1 | 0.865 | 0.053 | — |
| ATG7 | 0.864 | 0.098 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| MAP1LC3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| BPY2C | psi-mi:"MI:0018"(two hybrid) | pubmed:14627543|imex:IM-19270 |
| RASSF5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| Rassf1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| STK4 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| STK3 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| RASSF3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-20985|pubmed:24366813 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.4 + PDB: 无 | pLDDT=65.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytosol; Cytoplasm, cytoskelet / Cytosol, Principal piece; 额外: Nucleoplasm, Nucleol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MAP1S — Microtubule-associated protein 1S，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1059 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 55 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=65.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q66K74
- Protein Atlas: https://www.proteinatlas.org/ENSG00000130479-MAP1S/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAP1S
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q66K74
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
