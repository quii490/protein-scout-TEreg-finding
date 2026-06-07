---
type: protein-evaluation
gene: "FAM214A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM214A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM214A / FAM214A, KIAA1370 |
| 蛋白名称 | Atos homolog protein A |
| 蛋白大小 | 1076 aa / 121.7 kDa |
| UniProt ID | Q32MH5 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM214A/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM214A/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 1076 aa / 121.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033473, IPR025261, IPR051506; Pfam: PF13889, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.0/180** | |
| **归一化总分** | | | **75.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM214A, KIAA1370 |

**关键文献**:
1. Placental genomics mediates genetic associations with complex health traits and disease.. *Nature communications*. PMID: 35121757
2. Identification of miRNA, lncRNA and circRNA associated with gastric cancer metabolism through sequencing and bioinformatics analysis.. *Pathology, research and practice*. PMID: 38290402
3. Predicted SARS-CoV-2 miRNAs Associated with Epigenetic Viral Pathogenesis and the Detection of New Possible Drugs for Covid-19.. *Current drug delivery*. PMID: 33645482

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.9 |
| 高置信度残基 (pLDDT>90) 占比 | 19.8% |
| 置信残基 (pLDDT 70-90) 占比 | 15.4% |
| 中等置信 (pLDDT 50-70) 占比 | 7.9% |
| 低置信 (pLDDT<50) 占比 | 56.9% |
| 有序区域 (pLDDT>70) 占比 | 35.2% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM214A/FAM214A-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=54.9），有序残基占 35.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033473, IPR025261, IPR051506; Pfam: PF13889, PF13915 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LMBRD2 | 0.573 | 0.000 | — |
| RSL24D1 | 0.544 | 0.000 | — |
| MBLAC1 | 0.488 | 0.000 | — |
| ZFAND2B | 0.481 | 0.000 | — |
| ONECUT1 | 0.476 | 0.000 | — |
| WDR72 | 0.459 | 0.000 | — |
| ZC3H6 | 0.451 | 0.000 | — |
| PIGO | 0.426 | 0.000 | — |
| BTBD2 | 0.419 | 0.000 | — |
| KBTBD4 | 0.416 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ATOSA | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| CASS4 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| MAGEA6 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| KRT40 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| MID2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| SSX2IP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| GOLGA2 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 7
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.9 + PDB: 无 | pLDDT=54.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 11 + 7 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FAM214A — Atos homolog protein A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1076 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=54.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q32MH5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000047346-ATOSA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM214A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q32MH5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM214A/FAM214A-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q32MH5 |
| SMART | SM01177; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR033473;IPR025261;IPR051506; |
| Pfam | PF13889;PF13915; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000047346-ATOSA/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
