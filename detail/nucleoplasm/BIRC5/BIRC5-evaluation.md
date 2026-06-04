---
type: protein-evaluation
gene: "BIRC5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BIRC5 — REJECTED (研究热度过高 (PubMed strict=1005，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BIRC5 / API4, IAP4 |
| 蛋白名称 | Baculoviral IAP repeat-containing protein 5 |
| 蛋白大小 | 142 aa / 16.4 kDa |
| UniProt ID | O15392 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytokinetic bridge; UniProt: Cytoplasm; Nucleus; Chromosome; Chromosome, centromere; Cyto |
| 蛋白大小 | 8/10 | ×1 | 8 | 142 aa / 16.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1005 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=94.8; PDB: 1E31, 1F3H, 1XOX, 2QFA, 2RAW, 2RAX, 3UEC |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR051190, IPR001370; Pfam: PF00653 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytokinetic bridge | Supported |
| UniProt | Cytoplasm; Nucleus; Chromosome; Chromosome, centromere; Cytoplasm, cytoskeleton, spindle; Chromosome... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centriole (GO:0005814)
- chromosome passenger complex (GO:0032133)
- chromosome, centromeric region (GO:0000775)
- cytoplasm (GO:0005737)
- cytoplasmic microtubule (GO:0005881)
- cytosol (GO:0005829)
- interphase microtubule organizing center (GO:0031021)
- kinetochore (GO:0000776)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1005 |
| PubMed broad count | 6177 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: API4, IAP4 |

**关键文献**:
1. A CRISPR/Cas9-Engineered ARID1A-Deficient Human Gastric Cancer Organoid Model Reveals Essential and Nonessential Modes of Oncogenic Transformation.. *Cancer discovery*. PMID: 33451982
2. IGF2BP1 induces neuroblastoma via a druggable feedforward loop with MYCN promoting 17q oncogene expression.. *Molecular cancer*. PMID: 37246217
3. Survivin at a glance.. *Journal of cell science*. PMID: 30948431
4. Exosomal Gene Biomarkers in Osteosarcoma: Mifepristone as a Targeted Therapeutic Revealed by Multi-Omics Analysis.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 40616392
5. Survivin (BIRC5): Implications in cancer therapy.. *Life sciences*. PMID: 38848940

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.8 |
| 高置信度残基 (pLDDT>90) 占比 | 90.8% |
| 置信残基 (pLDDT 70-90) 占比 | 6.3% |
| 中等置信 (pLDDT 50-70) 占比 | 2.1% |
| 低置信 (pLDDT<50) 占比 | 0.7% |
| 有序区域 (pLDDT>70) 占比 | 97.1% |
| 可用 PDB 条目 | 1E31, 1F3H, 1XOX, 2QFA, 2RAW, 2RAX, 3UEC, 3UED, 3UEE, 3UEF |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1E31, 1F3H, 1XOX, 2QFA, 2RAW, 2RAX, 3UEC, 3UED, 3UEE, 3UEF）+ AlphaFold极高置信度预测（pLDDT=94.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051190, IPR001370; Pfam: PF00653 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AURKB | 0.999 | 0.944 | — |
| INCENP | 0.999 | 0.928 | — |
| CDCA8 | 0.999 | 0.943 | — |
| CDK1 | 0.997 | 0.510 | — |
| CDC20 | 0.995 | 0.045 | — |
| AURKA | 0.993 | 0.492 | — |
| CCNB1 | 0.993 | 0.098 | — |
| CCNB2 | 0.993 | 0.098 | — |
| UBE2C | 0.992 | 0.091 | — |
| BUB1B | 0.987 | 0.095 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-518838 | psi-mi:"MI:0096"(pull down) | imex:IM-14437|pubmed:16291752 |
| EBI-518842 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-14437|pubmed:16291752 |
| A2SUH6 | psi-mi:"MI:0096"(pull down) | pubmed:23251006|imex:IM-22982 |
| AURKB | psi-mi:"MI:0096"(pull down) | imex:IM-14437|pubmed:16291752 |
| CDCA8 | psi-mi:"MI:0096"(pull down) | imex:IM-14437|pubmed:16291752 |
| USF2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| AURKC | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| CDK1 | psi-mi:"MI:0416"(fluorescence microscopy) | pubmed:17681274|imex:IM-19740 |
| INCENP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12018|pubmed:17956729 |
| Birc6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11898|pubmed:18329369 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.8 + PDB: 1E31, 1F3H, 1XOX, 2QFA, 2RAW,  | pLDDT=94.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Chromosome; Chromosome, centro / Cytokinetic bridge | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. BIRC5 — Baculoviral IAP repeat-containing protein 5，研究基础较多，新颖性有限。
2. 蛋白大小142 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 1005 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1005 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15392
- Protein Atlas: https://www.proteinatlas.org/ENSG00000089685-BIRC5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BIRC5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15392
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
