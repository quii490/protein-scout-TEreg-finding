---
type: protein-evaluation
gene: "TNFSF4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TNFSF4 — REJECTED (研究热度过高 (PubMed strict=177，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TNFSF4 / TXGP1 |
| 蛋白名称 | Tumor necrosis factor ligand superfamily member 4 |
| 蛋白大小 | 183 aa / 21.1 kDa |
| UniProt ID | P23510 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles; UniProt: Membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 183 aa / 21.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=177 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=84.8; PDB: 2HEV |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR021184, IPR006052, IPR042338, IPR008983 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **75.0/180** | |
| **归一化总分** | | | **41.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell surface (GO:0009986)
- extracellular space (GO:0005615)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 177 |
| PubMed broad count | 634 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TXGP1 |

**关键文献**:
1. Single-cell profiling of response to neoadjuvant chemo-immunotherapy in surgically resectable esophageal squamous cell carcinoma.. *Genome medicine*. PMID: 38566201
2. Genome-wide association analyses define pathogenic signaling pathways and prioritize drug targets for IgA nephropathy.. *Nature genetics*. PMID: 37337107
3. Deciphering the generation of heterogeneity in esophageal squamous cell carcinoma metastasis via single-cell multiomics analysis.. *Journal of translational medicine*. PMID: 39905485
4. Associations between TNFSF4 and TRAF1-C5 gene polymorphisms and systemic lupus erythematosus: a meta-analysis.. *Human immunology*. PMID: 22820624
5. A multi-omics resource of B cell activation reveals genetic mechanisms for immune-mediated diseases.. *medRxiv : the preprint server for health sciences*. PMID: 40475139

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.8 |
| 高置信度残基 (pLDDT>90) 占比 | 62.8% |
| 置信残基 (pLDDT 70-90) 占比 | 18.0% |
| 中等置信 (pLDDT 50-70) 占比 | 9.8% |
| 低置信 (pLDDT<50) 占比 | 9.3% |
| 有序区域 (pLDDT>70) 占比 | 80.8% |
| 可用 PDB 条目 | 2HEV |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=84.8，有序区 80.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR021184, IPR006052, IPR042338, IPR008983 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TNFRSF4 | 0.999 | 0.971 | — |
| TNFRSF9 | 0.993 | 0.000 | — |
| CD27 | 0.986 | 0.000 | — |
| CD28 | 0.981 | 0.000 | — |
| CD40LG | 0.958 | 0.000 | — |
| ICOS | 0.942 | 0.000 | — |
| TNFSF9 | 0.907 | 0.000 | — |
| LOC102723996 | 0.904 | 0.000 | — |
| TNFRSF8 | 0.897 | 0.000 | — |
| TNFSF18 | 0.880 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Tnfrsf4 | psi-mi:"MI:0107"(surface plasmon resonance) | pubmed:8765008 |
| TCF7L2 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| MAFG | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| TGIF1 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| GFI1B | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| SOX14 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| GRHL2 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| HOXD10 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| IRX5 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| ZNF710 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.8 + PDB: 2HEV | pLDDT=84.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TNFSF4 — Tumor necrosis factor ligand superfamily member 4，研究基础较多，新颖性有限。
2. 蛋白大小183 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 177 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 177 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P23510
- Protein Atlas: https://www.proteinatlas.org/ENSG00000117586-TNFSF4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TNFSF4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P23510
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
