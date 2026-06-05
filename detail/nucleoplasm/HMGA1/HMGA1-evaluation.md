---
type: protein-evaluation
gene: "Hmga1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## Hmga1 — REJECTED (研究热度过高 (PubMed strict=663，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Hmga1 / HMGIY |
| 蛋白名称 | High mobility group protein HMG-I/HMG-Y |
| 蛋白大小 | 107 aa / 11.7 kDa |
| UniProt ID | P17096 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear membrane; 额外: Cytosol; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 8/10 | ×1 | 8 | 107 aa / 11.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=663 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.0; PDB: 2EZD, 2EZE, 2EZF, 2EZG, 8CPG |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR017956, IPR000116, IPR000637 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear membrane; 额外: Cytosol | Supported |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- focal adhesion (GO:0005925)
- nuclear membrane (GO:0031965)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)
- senescence-associated heterochromatin focus (GO:0035985)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 663 |
| PubMed broad count | 908 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HMGIY |

**关键文献**:
1. HMGA1-pseudogenes and cancer.. *Oncotarget*. PMID: 26895108
2. High mobility group A1 (HMGA1) promotes the tumorigenesis of colorectal cancer by increasing lipid synthesis.. *Nature communications*. PMID: 39548107
3. Mediterranean Diet Nutrients to Turn the Tide against Insulin Resistance and Related Diseases.. *Nutrients*. PMID: 32290535
4. High mobility group A1 (HMGA1) promotes esophageal squamous cell carcinoma progression by inhibiting STING-mediated anti-tumor immunity.. *Nature communications*. PMID: 40456764
5. HMGA1 orchestrates chromatin compartmentalization and sequesters genes into 3D networks coordinating senescence heterogeneity.. *Nature communications*. PMID: 39134516

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.0 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 27.1% |
| 中等置信 (pLDDT 50-70) 占比 | 72.0% |
| 低置信 (pLDDT<50) 占比 | 0.9% |
| 有序区域 (pLDDT>70) 占比 | 27.1% |
| 可用 PDB 条目 | 2EZD, 2EZE, 2EZF, 2EZG, 8CPG |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.0），有序残基占 27.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017956, IPR000116, IPR000637 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| JUN | 0.964 | 0.474 | — |
| HMGA2 | 0.902 | 0.000 | — |
| HMGCR | 0.882 | 0.000 | — |
| SMIM29 | 0.876 | 0.000 | — |
| IRF1 | 0.826 | 0.292 | — |
| PRMT6 | 0.797 | 0.510 | — |
| FDPS | 0.775 | 0.000 | — |
| GGPS1 | 0.773 | 0.000 | — |
| PMVK | 0.763 | 0.000 | — |
| IRF3 | 0.741 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EWSR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PRMT6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-14484|pubmed:16293633 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| CSNK2A1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22113938|imex:IM-16640 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| ANXA1 | psi-mi:"MI:0049"(filter binding) | imex:IM-12160|pubmed:18850631 |
| PCBP1 | psi-mi:"MI:0049"(filter binding) | imex:IM-12160|pubmed:18850631 |
| XRCC6 | psi-mi:"MI:0049"(filter binding) | imex:IM-12160|pubmed:18850631 |
| PTBP1 | psi-mi:"MI:0049"(filter binding) | imex:IM-12160|pubmed:18850631 |
| PA2G4 | psi-mi:"MI:0049"(filter binding) | imex:IM-12160|pubmed:18850631 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.0 + PDB: 2EZD, 2EZE, 2EZF, 2EZG, 8CPG | pLDDT=65.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm, Nuclear membrane; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. Hmga1 — High mobility group protein HMG-I/HMG-Y，研究基础较多，新颖性有限。
2. 蛋白大小107 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 663 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=65.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 663 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P17096
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137309-HMGA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Hmga1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P17096
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000137309-HMGA1/subcellular

![](https://images.proteinatlas.org/65612/1244_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/65612/1244_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/65612/1247_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/65612/1247_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/65612/2224_G8_3_red_green.jpg)
![](https://images.proteinatlas.org/65612/2224_G8_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P17096-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
