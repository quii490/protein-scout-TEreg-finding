---
type: protein-evaluation
gene: "FBXO2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXO2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO2 / FBX2 |
| 蛋白名称 | F-box only protein 2 |
| 蛋白大小 | 296 aa / 33.3 kDa |
| UniProt ID | Q9UK22 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXO2/IF_images/80_C8_1_blue_red_green.jpg|80 C8 1 blue red green]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXO2/IF_images/80_C8_2_blue_red_green.jpg|80 C8 2 blue red green]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Microsome membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 296 aa / 33.3 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=53 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR007397, IPR036047, IPR001810, IPR039752, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **106.5/180** | |
| **归一化总分** | | | **59.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm; Microsome membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已嵌入

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendritic spine (GO:0043197)
- extrinsic component of postsynaptic membrane (GO:0098890)
- glutamatergic synapse (GO:0098978)
- SCF ubiquitin ligase complex (GO:0019005)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 53 |
| PubMed broad count | 80 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBX2 |

**关键文献**:
1. Muscle-derived small extracellular vesicles induce liver fibrosis during overtraining.. *Cell metabolism*. PMID: 39879982
2. Single-Cell RNA-Seq Analysis of Cells from Degenerating and Non-Degenerating Intervertebral Discs from the Same Individual Reveals New Biomarkers for Intervertebral Disc Degeneration.. *International journal of molecular sciences*. PMID: 35409356
3. FBXO2 Alleviates Intervertebral Disc Degeneration via Dual Mechanisms: Activating PINK1-Parkin Mitophagy and Ubiquitinating LCN2 to Suppress Ferroptosis.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40791152
4. FBXO2-mediated KPTN ubiquitination promotes amino acid-dependent mTORC1 signaling and tumor growth.. *The Journal of clinical investigation*. PMID: 41401028
5. FBXO2 promotes hepatocellular carcinoma progression and sorafenib resistance by targeting USP49 for proteasomal degradation.. *Frontiers in immunology*. PMID: 41035649

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.0 |
| 高置信度残基 (pLDDT>90) 占比 | 75.0% |
| 置信残基 (pLDDT 70-90) 占比 | 9.1% |
| 中等置信 (pLDDT 50-70) 占比 | 10.1% |
| 低置信 (pLDDT<50) 占比 | 5.7% |
| 有序区域 (pLDDT>70) 占比 | 84.1% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXO2/FBXO2-PAE.png]]

**评价**: AlphaFold 极高置信度预测（pLDDT=88.0，有序区 84.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007397, IPR036047, IPR001810, IPR039752, IPR008979; Pfam: PF12937, PF04300 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.997 | 0.943 | — |
| BTRC | 0.981 | 0.000 | — |
| CUL1 | 0.973 | 0.836 | — |
| FBXO6 | 0.962 | 0.000 | — |
| SKP2 | 0.952 | 0.000 | — |
| FBXW7 | 0.945 | 0.000 | — |
| FBXO4 | 0.942 | 0.000 | — |
| FBXW11 | 0.919 | 0.000 | — |
| STUB1 | 0.880 | 0.295 | — |
| DISP3 | 0.877 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IQCB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| Dlg4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11694|pubmed:19455133 |
| CHST12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RNASET2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BOC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Syngap1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| CBLIF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SNCA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| CAV2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| SLAMF7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.0 + PDB: 无 | pLDDT=88.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Microsome membrane / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. FBXO2 — F-box only protein 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小296 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 53 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UK22
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116661-FBXO2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UK22
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXO2/FBXO2-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UK22 |
| SMART | SM01198; |
| UniProt Domain [FT] | DOMAIN 44..91; /note="F-box"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00080"; DOMAIN 113..296; /note="FBA"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00482" |
| InterPro | IPR007397;IPR036047;IPR001810;IPR039752;IPR008979; |
| Pfam | PF12937;PF04300; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000116661-FBXO2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SKP1 | Intact, Biogrid, Bioplex | true |
| ACP2 | Bioplex | false |
| ADAM17 | Bioplex | false |
| ADAM9 | Bioplex | false |
| ADAMTS7 | Bioplex | false |
| ADGRF1 | Bioplex | false |
| AGRN | Bioplex | false |
| AHSG | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
