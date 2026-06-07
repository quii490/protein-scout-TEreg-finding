---
type: protein-evaluation
gene: "EXOSC3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EXOSC3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EXOSC3 / RRP40 |
| 蛋白名称 | Exosome complex component RRP40 |
| 蛋白大小 | 275 aa / 29.6 kDa |
| UniProt ID | Q9NQT5 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/EXOSC3/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/EXOSC3/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus, nucleolus; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 275 aa / 29.6 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=65 篇 (≤80→4) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=79.3; PDB: 2NN6, 6D6Q, 6D6R, 6H25, 9G8M, 9G8N, 9G8O |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026699, IPR004088, IPR036612, IPR012340, IPR049 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.0/180** | |
| **归一化总分** | | | **63.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Cytoplasm; Nucleus, nucleolus; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic exosome (RNase complex) (GO:0000177)
- cytosol (GO:0005829)
- euchromatin (GO:0000791)
- exosome (RNase complex) (GO:0000178)
- nuclear exosome (RNase complex) (GO:0000176)
- nucleolar exosome (RNase complex) (GO:0101019)
- nucleolus (GO:0005730)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 65 |
| PubMed broad count | 89 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RRP40 |

**关键文献**:
1. The RNA Exosome and Human Disease.. *Methods in molecular biology (Clifton, N.J.)*. PMID: 31768969
2. A Chemical Biology Approach to Model Pontocerebellar Hypoplasia Type 1B (PCH1B).. *ACS chemical biology*. PMID: 30141626
3. EXOSC3 S1-domain variants implicated in PCH1b alter RNA exosome cap subunit abundance and thermal stability disrupting rRNA processing and targeting of AU-rich mRNA.. *bioRxiv : the preprint server for biology*. PMID: 40501579
4. Pontocerebellar Hypoplasia Type 1 and Associated Neuronopathies.. *Genes*. PMID: 40428407
5. The RNA exosome and RNA exosome-linked disease.. *RNA (New York, N.Y.)*. PMID: 29093021

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.3 |
| 高置信度残基 (pLDDT>90) 占比 | 35.6% |
| 置信残基 (pLDDT 70-90) 占比 | 46.2% |
| 中等置信 (pLDDT 50-70) 占比 | 4.4% |
| 低置信 (pLDDT<50) 占比 | 13.8% |
| 有序区域 (pLDDT>70) 占比 | 81.8% |
| 可用 PDB 条目 | 2NN6, 6D6Q, 6D6R, 6H25, 9G8M, 9G8N, 9G8O, 9G8P |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/EXOSC3/EXOSC3-PAE.png]]

**评价**: PDB实验结构（2NN6, 6D6Q, 6D6R, 6H25, 9G8M, 9G8N, 9G8O, 9G8P）+ AlphaFold极高置信度预测（pLDDT=79.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026699, IPR004088, IPR036612, IPR012340, IPR049469; Pfam: PF15985, PF21261, PF21262 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EXOSC9 | 0.999 | 0.997 | — |
| EXOSC10 | 0.999 | 0.998 | — |
| DIS3 | 0.999 | 0.999 | — |
| MPHOSPH6 | 0.999 | 0.991 | — |
| EXOSC1 | 0.999 | 0.999 | — |
| C1D | 0.999 | 0.972 | — |
| EXOSC2 | 0.999 | 0.998 | — |
| DIS3L | 0.999 | 0.998 | — |
| EXOSC4 | 0.999 | 0.999 | — |
| EXOSC7 | 0.999 | 0.998 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000323046.4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21255825|imex:IM-15741 |
| EXOSC4 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| EXOSC5 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| EXOSC8 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| HDGF | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21907836|imex:IM-17230 |
| GABARAPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| Aicda | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21255825|imex:IM-15741 |
| EXOSC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21255825|imex:IM-15741 |
| EXOSC6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21255825|imex:IM-15741 |
| EXOSC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21255825|imex:IM-15741 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.3 + PDB: 2NN6, 6D6Q, 6D6R, 6H25, 9G8M,  | pLDDT=79.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus, nucleolus; Nucleus / Nucleoplasm | 一致 |
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
1. EXOSC3 — Exosome complex component RRP40，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小275 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 65 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NQT5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000107371-EXOSC3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EXOSC3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NQT5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/EXOSC3/EXOSC3-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NQT5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026699;IPR004088;IPR036612;IPR012340;IPR049469;IPR048541;IPR037319; |
| Pfam | PF15985;PF21261;PF21262; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000107371-EXOSC3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DIS3 | Intact, Biogrid, Bioplex | true |
| DIS3L | Intact, Biogrid, Bioplex | true |
| EXOSC1 | Intact, Biogrid, Bioplex | true |
| EXOSC2 | Intact, Biogrid, Bioplex | true |
| EXOSC4 | Intact, Biogrid, Bioplex | true |
| EXOSC5 | Intact, Biogrid, Bioplex | true |
| EXOSC6 | Biogrid, Bioplex | true |
| EXOSC7 | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
