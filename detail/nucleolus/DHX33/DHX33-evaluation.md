---
type: protein-evaluation
gene: "DHX33"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DHX33 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DHX33 |
| 蛋白名称 | ATP-dependent RNA helicase DHX33 |
| 蛋白大小 | 707 aa / 78.9 kDa |
| UniProt ID | Q9H6R0 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/DHX33/IF_images/A-549_1.jpg|A-549]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/DHX33/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; UniProt: Nucleus, nucleolus; Nucleus, nucleoplasm; Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 707 aa / 78.9 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=41 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.3; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.5/180** | |
| **归一化总分** | | | **63.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Enhanced |
| UniProt | Nucleus, nucleolus; Nucleus, nucleoplasm; Cytoplasm; Nucleus; Inflammasome | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 41 |
| PubMed broad count | 41 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Ubiquitin Ligases in Control: Regulating NLRP3 Inflammasome Activation.. *Front Biosci (Landmark Ed)*. PMID: 40152367
2. An RNA Helicase DHX33 Inhibitor Shows Broad Anticancer Activity via Inducing Ferroptosis in Cancer Cells.. *ACS Omega*. PMID: 38973855
3. Formation of the NLRP3 inflammasome inhibits stress granule assembly by multiple mechanisms.. *J Biochem*. PMID: 38299728
4. The anticancer potential of the CLK kinases inhibitors 1C8 and GPS167 revealed by their impact on the epithelial-mesenchymal transition and the antiviral immune response.. *Oncotarget*. PMID: 38753413
5. DHX33 mediates p53 to regulate mevalonate pathway gene transcription in human cancers.. *Biochim Biophys Acta Gen Subj*. PMID: 38143011

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.3 |
| 高置信度残基 (pLDDT>90) 占比 | 58.4% |
| 置信残基 (pLDDT 70-90) 占比 | 30.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.7% |
| 低置信 (pLDDT<50) 占比 | 7.1% |
| 有序区域 (pLDDT>70) 占比 | 89.2% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/DHX33/DHX33-PAE.png]]

**评价**: AlphaFold 极高置信度预测（pLDDT=85.3，有序区 89.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NLRP3 | 0.000 | 0.000 | — |
| MAVS | 0.000 | 0.000 | — |
| RNASEL | 0.000 | 0.000 | — |
| NLRP6 | 0.000 | 0.000 | — |
| CASP1 | 0.000 | 0.000 | — |
| AIM2 | 0.000 | 0.000 | — |
| NLRP9 | 0.000 | 0.000 | — |
| PYCARD | 0.000 | 0.000 | — |
| NLRP1 | 0.000 | 0.000 | — |
| CARD8 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9H6R0 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P0CG38 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q09019 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q7L099 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.3 + PDB: 无 | pLDDT=85.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus, nucleolus; Nucleus, nucleoplasm; Cytoplas / Nucleoli | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DHX33 — ATP-dependent RNA helicase DHX33，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小707 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 41 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H6R0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000005100-DHX33/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DHX33
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H6R0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/DHX33/DHX33-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H6R0 |
| SMART | SM00487;SM00847;SM00490; |
| UniProt Domain [FT] | DOMAIN 84..252; /note="Helicase ATP-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00541"; DOMAIN 277..450; /note="Helicase C-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00542" |
| InterPro | IPR011709;IPR011545;IPR002464;IPR048333;IPR007502;IPR014001;IPR001650;IPR027417; |
| Pfam | PF00270;PF21010;PF00271;PF07717;PF04408; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000005100-DHX33/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| USP36 | Intact, Biogrid, Opencell | true |
| FKBP5 | Opencell | false |
| MRPL38 | Bioplex | false |
| MYC | Biogrid | false |
| NOP56 | Biogrid | false |
| NUDCD1 | Biogrid | false |
| POLR3K | Bioplex | false |
| RPS6 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
