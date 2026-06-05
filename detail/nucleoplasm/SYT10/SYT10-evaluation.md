---
type: protein-evaluation
gene: "SYT10"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SYT10 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SYT10 |
| 蛋白名称 | Synaptotagmin-10 |
| 蛋白大小 | 523 aa / 59.1 kDa |
| UniProt ID | Q6XYQ8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles; UniProt: Cytoplasmic vesicle, secretory vesicle membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 523 aa / 59.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000008, IPR035892, IPR001565; Pfam: PF00168 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Approved |
| UniProt | Cytoplasmic vesicle, secretory vesicle membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- exocytic vesicle (GO:0070382)
- glutamatergic synapse (GO:0098978)
- plasma membrane (GO:0005886)
- presynapse (GO:0098793)
- transport vesicle membrane (GO:0030658)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of Synaptotagmin 10 as Effector of NPAS4-Mediated Protection from Excitotoxic Neurodegeneration.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 26936998
2. Genome-wide case-only analysis of gene-gene interactions with known Parkinson's disease risk variants reveals link between LRRK2 and SYT10.. *NPJ Parkinson's disease*. PMID: 37386035
3. Genetics and the heart rate response to exercise.. *Cellular and molecular life sciences : CMLS*. PMID: 30919020
4. Identification of potential new T cell activation molecules: a Bioinformatic Approach.. *Scientific reports*. PMID: 39333573
5. Synaptotagmin10-Cre, a driver to disrupt clock genes in the SCN.. *Journal of biological rhythms*. PMID: 21921292

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.1 |
| 高置信度残基 (pLDDT>90) 占比 | 40.9% |
| 置信残基 (pLDDT 70-90) 占比 | 19.1% |
| 中等置信 (pLDDT 50-70) 占比 | 11.9% |
| 低置信 (pLDDT<50) 占比 | 28.1% |
| 有序区域 (pLDDT>70) 占比 | 60.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.1，有序区 60.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000008, IPR035892, IPR001565; Pfam: PF00168 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SYT3 | 0.804 | 0.790 | — |
| SYT6 | 0.803 | 0.791 | — |
| NPAS4 | 0.643 | 0.000 | — |
| ARNTL | 0.613 | 0.000 | — |
| NRXN1 | 0.599 | 0.042 | — |
| SNAP25 | 0.561 | 0.091 | — |
| RPH3AL | 0.544 | 0.062 | — |
| KIAA1755 | 0.542 | 0.000 | — |
| UNC13A | 0.528 | 0.000 | — |
| NRXN3 | 0.525 | 0.042 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000029441.4 | psi-mi:"MI:0808"(comigration in sds page) | pubmed:10531343|imex:IM-16892 |
| Syt6 | psi-mi:"MI:0808"(comigration in sds page) | pubmed:10531343|imex:IM-16892 |
| Syt3 | psi-mi:"MI:0808"(comigration in sds page) | pubmed:10531343|imex:IM-16892 |
| Syt9 | psi-mi:"MI:0808"(comigration in sds page) | pubmed:10531343|imex:IM-16892 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.1 + PDB: 无 | pLDDT=73.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasmic vesicle, secretory vesicle membrane / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

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
1. SYT10 — Synaptotagmin-10，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小523 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6XYQ8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000110975-SYT10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SYT10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6XYQ8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000110975-SYT10/subcellular

![](https://images.proteinatlas.org/55426/1353_D1_5_red_green.jpg)
![](https://images.proteinatlas.org/55426/1353_D1_6_red_green.jpg)
![](https://images.proteinatlas.org/55426/1363_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/55426/1363_D1_2_red_green.jpg)
![](https://images.proteinatlas.org/55426/1395_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/55426/1395_E11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6XYQ8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
