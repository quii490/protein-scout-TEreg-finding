---
type: protein-evaluation
gene: "EXOSC5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EXOSC5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EXOSC5 / CML28, RRP46 |
| 蛋白名称 | Exosome complex component RRP46 |
| 蛋白大小 | 235 aa / 25.2 kDa |
| UniProt ID | Q9NQT4 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/EXOSC5/IF_images/CACO-2_1.jpg|CACO-2]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/EXOSC5/IF_images/MCF-7_1.jpg|MCF-7]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Nucleoplasm; UniProt: Nucleus, nucleolus; Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 235 aa / 25.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=84.4; PDB: 2NN6, 6D6Q, 6D6R, 6H25, 9G8M, 9G8N, 9G8O |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001247, IPR015847, IPR036345, IPR027408, IPR020 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.0/180** | |
| **归一化总分** | | | **75.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm | Enhanced |
| UniProt | Nucleus, nucleolus; Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

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
| PubMed strict count | 22 |
| PubMed broad count | 43 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CML28, RRP46 |

**关键文献**:
1. The plasma peptides of Alzheimer's disease.. *Clinical proteomics*. PMID: 34182925
2. Comparative analyses of disease-linked missense mutations in the RNA exosome modeled in budding yeast reveal distinct functional consequences in translation.. *RNA (New York, N.Y.)*. PMID: 40246537
3. Biallelic variants in the RNA exosome gene EXOSC5 are associated with developmental delays, short stature, cerebellar hypoplasia and motor weakness.. *Human molecular genetics*. PMID: 32504085
4. EXOSC5 promotes proliferation of gastric cancer through regulating AKT/STAT3 signaling pathways.. *Journal of Cancer*. PMID: 35371329
5. Comprehensive bioinformatics analysis of EXOSC family genes in head and neck squamous cell carcinoma.. *Scientific reports*. PMID: 40830179

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.4 |
| 高置信度残基 (pLDDT>90) 占比 | 63.8% |
| 置信残基 (pLDDT 70-90) 占比 | 24.7% |
| 中等置信 (pLDDT 50-70) 占比 | 0.9% |
| 低置信 (pLDDT<50) 占比 | 10.6% |
| 有序区域 (pLDDT>70) 占比 | 88.5% |
| 可用 PDB 条目 | 2NN6, 6D6Q, 6D6R, 6H25, 9G8M, 9G8N, 9G8O, 9G8P |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/EXOSC5/EXOSC5-PAE.png]]

**评价**: PDB实验结构（2NN6, 6D6Q, 6D6R, 6H25, 9G8M, 9G8N, 9G8O, 9G8P）+ AlphaFold极高置信度预测（pLDDT=84.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001247, IPR015847, IPR036345, IPR027408, IPR020568; Pfam: PF01138, PF03725 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EXOSC1 | 0.999 | 0.998 | — |
| MPHOSPH6 | 0.999 | 0.972 | — |
| C1D | 0.999 | 0.992 | — |
| DIS3 | 0.999 | 0.999 | — |
| EXOSC9 | 0.999 | 0.997 | — |
| EXOSC10 | 0.999 | 0.999 | — |
| EXOSC3 | 0.999 | 0.999 | — |
| EXOSC2 | 0.999 | 0.997 | — |
| EXOSC7 | 0.999 | 0.997 | — |
| EXOSC4 | 0.999 | 0.998 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000221233.3 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-30059|pubmed:39251607 |
| Pik3cb | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| EXOSC3 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| EXOSC8 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| EXOSC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| EXOSC10 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| KIAA1217 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| DHRS2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Aicda | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21255825|imex:IM-15741 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.4 + PDB: 2NN6, 6D6Q, 6D6R, 6H25, 9G8M,  | pLDDT=84.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus; Cytoplasm; Nucleus / Nucleoli; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. EXOSC5 — Exosome complex component RRP46，非常新颖，仅有少数基础研究。
2. 蛋白大小235 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NQT4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000077348-EXOSC5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EXOSC5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NQT4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/EXOSC5/EXOSC5-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NQT4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001247;IPR015847;IPR036345;IPR027408;IPR020568;IPR050080; |
| Pfam | PF01138;PF03725; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000077348-EXOSC5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| C1D | Biogrid, Bioplex | true |
| DIS3L | Biogrid, Bioplex | true |
| EXOSC1 | Intact, Biogrid, Bioplex | true |
| EXOSC10 | Intact, Biogrid | true |
| EXOSC2 | Biogrid, Bioplex | true |
| EXOSC3 | Intact, Biogrid, Bioplex | true |
| EXOSC4 | Biogrid, Bioplex | true |
| EXOSC6 | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
