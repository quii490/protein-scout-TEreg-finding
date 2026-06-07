---
type: protein-evaluation
gene: "CDCA7"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CDCA7 — REJECTED (研究热度过高 (PubMed strict=128，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CDCA7 |
| 蛋白名称 | Cell division cycle associated 7 |
| 蛋白大小 | 449 aa / 51.3 kDa |
| UniProt ID | A0A8Q3WKV4 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CDCA7/IF_images/A-431_1.jpg|A 431]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/CDCA7/IF_images/U-251MG_1.jpg|U 251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 449 aa / 51.3 kDa |
| 🆕 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=128 篇 (>100→REJECTED) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.0; PDB: 无 |
| 🧬 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 11 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.0/180** | |
| **归一化总分** | | | **42.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已嵌入

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 128 |
| PubMed broad count | 130 |
| 别名(未计入scoring) |  |

**关键文献**:
1. CDCA7 Promotes Proliferation and Suppresses Apoptosis in Gastric Cancer via HELLS-Mediated Chromatin Remodeling.. *Oncol Res*. PMID: 42065057
2. CDCA7 Promotes Neuroblastoma Proliferation via Regulating the Cell Cycle.. *Iran J Biotechnol*. PMID: 42145973
3. Structure of human lymphoid-specific helicase HELLS in its autoinhibited state.. *Nucleic Acids Res*. PMID: 41954988
4. CDCA7 promotes chemoresistance of drug-tolerant persister cells in breast cancer by upregulating the expression of autophagy-related protein genes.. *Front Immunol*. PMID: 41890763
5. Missense substitutions in the BTB domain of ZBTB24 can lead to protein instability and cause ICF2 syndrome.. *Hum Mol Genet*. PMID: 41359419

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.0 |
| 高置信度残基 (pLDDT>90) 占比 | 24.5% |
| 置信残基 (pLDDT 70-90) 占比 | 11.4% |
| 中等置信 (pLDDT 50-70) 占比 | 13.6% |
| 低置信 (pLDDT<50) 占比 | 50.6% |
| 有序区域 (pLDDT>70) 占比 | 35.9% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CDCA7/CDCA7-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=60.0），有序残基占 35.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HELLS | 0.000 | 0.000 | — |
| ZBTB24 | 0.000 | 0.000 | — |
| YWHAZ | 0.000 | 0.000 | — |
| CDCA2 | 0.000 | 0.000 | — |
| CDCA5 | 0.000 | 0.000 | — |
| YWHAQ | 0.000 | 0.000 | — |
| CDCA8 | 0.000 | 0.000 | — |
| NUF2 | 0.000 | 0.000 | — |
| SFN | 0.000 | 0.000 | — |
| CDC45 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P61981 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P63104 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q04917 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O76024 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9BWT1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 11
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.0 + PDB: 无 | pLDDT=60.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 11 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CDCA7 — Cell division cycle associated 7，研究基础较多，新颖性有限。
2. 蛋白大小449 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 128 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 128 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A0A8Q3WKV4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144354-CDCA7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CDCA7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A8Q3WKV4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/CDCA7/CDCA7-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BWT1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR040221;IPR018866; |
| Pfam | PF10497; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000144354-CDCA7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HTT | Intact | false |
| WFS1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
