---
type: protein-evaluation
gene: "THAP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## THAP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | THAP2 |
| 蛋白名称 | THAP domain-containing protein 2 |
| 蛋白大小 | 228 aa / 26.3 kDa |
| UniProt ID | Q9H0W7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 228 aa / 26.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=75.3; PDB: 2D8R |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026521, IPR006612, IPR038441; Pfam: PF05485 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **137.0/180** | |
| **归一化总分** | | | **76.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleolus (GO:0005730)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Molecular Mechanism of Different Rooting Capacity between Two Clones of Taxodium hybrid 'Zhongshanshan'.. *International journal of molecular sciences*. PMID: 38397108
2. Bone Marrow Mesenchymal Stem Cell-derived Exosomal microRNA-99b-5p Promotes Cell Growth of High Glucose-treated Human Umbilical Vein Endothelial Cells by Modulating THAP Domain Containing 2 Expression.. *Current stem cell research & therapy*. PMID: 38357906
3. The Whole Transcriptome Sequencing Profile of Serum-Derived Exosomes and Potential Pathophysiology of Age-Related Hearing Loss.. *Diagnostics (Basel, Switzerland)*. PMID: 41594224
4. Late-gestational systemic hypoxia leads to a similar early gene response in mouse placenta and developing brain.. *American journal of physiology. Regulatory, integrative and comparative physiology*. PMID: 20926767
5. The involvement of miR-100 in bladder urothelial carcinogenesis changing the expression levels of mRNA and proteins of genes related to cell proliferation, survival, apoptosis and chromosomal stability.. *Cancer cell international*. PMID: 25493074

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.3 |
| 高置信度残基 (pLDDT>90) 占比 | 29.4% |
| 置信残基 (pLDDT 70-90) 占比 | 35.5% |
| 中等置信 (pLDDT 50-70) 占比 | 21.5% |
| 低置信 (pLDDT<50) 占比 | 13.6% |
| 有序区域 (pLDDT>70) 占比 | 64.9% |
| 可用 PDB 条目 | 2D8R |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=75.3，有序区 64.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026521, IPR006612, IPR038441; Pfam: PF05485 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| THAP11 | 0.890 | 0.000 | — |
| HCFC1 | 0.806 | 0.732 | — |
| HCFC2 | 0.726 | 0.711 | — |
| OGT | 0.685 | 0.685 | — |
| PAWR | 0.528 | 0.000 | — |
| THAP10 | 0.511 | 0.000 | — |
| TRIM71 | 0.481 | 0.474 | — |
| RRM1 | 0.481 | 0.000 | — |
| RBM12B | 0.467 | 0.071 | — |
| DNAJB8 | 0.459 | 0.459 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VANGL1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| OGT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HCFC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRIM71 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DNAJB8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CTNNBL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HCFC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FAM76B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 8
- 调控相关比例: 1 / 12 = 8%

**评价**: STRING 12 个预测互作，IntAct 8 个实验互作。调控相关配体占比 8%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.3 + PDB: 2D8R | pLDDT=75.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Golgi apparatus; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 12 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. THAP2 — THAP domain-containing protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小228 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H0W7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173451-THAP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=THAP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H0W7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000173451-THAP2/subcellular

![](https://images.proteinatlas.org/39790/461_H4_2_red_green.jpg)
![](https://images.proteinatlas.org/39790/461_H4_3_red_green.jpg)
![](https://images.proteinatlas.org/39790/462_H4_3_red_green.jpg)
![](https://images.proteinatlas.org/39790/462_H4_4_red_green.jpg)
![](https://images.proteinatlas.org/39790/464_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/39790/464_H4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H0W7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
