---
type: protein-evaluation
gene: "CDK2AP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CDK2AP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CDK2AP2 |
| 蛋白名称 | Cyclin-dependent kinase 2-associated protein 2 |
| 蛋白大小 | 126 aa / 13.1 kDa |
| UniProt ID | O75956 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CDK2AP2/IF_images/SK-MEL-30_1.jpg|SK MEL 30]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CDK2AP2/IF_images/OE19_1.jpg|OE19]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 126 aa / 13.1 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.2; PDB: 无 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 8 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已嵌入

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 43 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Candidate Biomarkers for Hard-to-Heal Wounds Revealed by Single-Cell RNA Sequencing of Wound Fluid in Murine Wound Models.. *Wound Repair Regen*. PMID: 40444294
2. Novel circular RNA hsa_circ_0036683 suppresses proliferation and migration by mediating the miR-4664-3p/CDK2AP2 axis in non-small cell lung cancer.. *Thorac Cancer*. PMID: 39113208
3. Cigarette smoking, by accelerating the cell cycle, promotes the progression of non-small cell lung cancer through an HIF-1α-METTL3-m(6)A/CDK2AP2 axis.. *J Hazard Mater*. PMID: 37156046
4. Whole-genome resequencing reveals genetic diversity, differentiation, and selection signatures of yak breeds/populations in Qinghai, China.. *Front Genet*. PMID: 36704337
5. Cross-linking mass spectrometry reveals the structural topology of peripheral NuRD subunits relative to the core complex.. *FEBS J*. PMID: 33283408

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.2 |
| 高置信度残基 (pLDDT>90) 占比 | 34.9% |
| 置信残基 (pLDDT 70-90) 占比 | 15.1% |
| 中等置信 (pLDDT 50-70) 占比 | 38.1% |
| 低置信 (pLDDT<50) 占比 | 11.9% |
| 有序区域 (pLDDT>70) 占比 | 50.0% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CDK2AP2/CDK2AP2-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=74.2，有序区 50.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDK2AP1 | 0.000 | 0.000 | — |
| HDAC2 | 0.000 | 0.000 | — |
| CDK2 | 0.000 | 0.000 | — |
| MANF | 0.000 | 0.000 | — |
| MTA3 | 0.000 | 0.000 | — |
| HDAC1 | 0.000 | 0.000 | — |
| MRFAP1L1 | 0.000 | 0.000 | — |
| TMEM217 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P23381 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q5NET3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:O75956 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q96HT8 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q6IAV4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| intact:EBI-25847655 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| intact:EBI-54262435 | psi-mi:"MI:2195"(clash) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 8，IntAct interactions: 15
- 调控相关比例: 0 / 8 = 0%

**评价**: STRING 8 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.2 + PDB: 无 | pLDDT=74.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 8 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CDK2AP2 — Cyclin-dependent kinase 2-associated protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小126 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75956
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167797-CDK2AP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CDK2AP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75956
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CDK2AP2/CDK2AP2-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O75956 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR017266; |
| Pfam | PF09806; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000167797-CDK2AP2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HDAC2 | Biogrid, Opencell | true |
| CDK2AP1 | Biogrid | false |
| CHD4 | Biogrid | false |
| MRFAP1L1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
