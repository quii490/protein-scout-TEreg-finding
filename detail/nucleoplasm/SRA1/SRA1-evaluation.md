---
type: protein-evaluation
gene: "SRA1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SRA1 — REJECTED (研究热度过高 (PubMed strict=165，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SRA1 |
| 蛋白名称 | Steroid receptor RNA activator 1 |
| 蛋白大小 | 224 aa / 24.4 kDa |
| UniProt ID | Q9HD15 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Microtubules, Cytokinetic bridge, Primary c; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 224 aa / 24.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=165 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=76.1; PDB: 2MGX, 4NBO |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009917, IPR040243; Pfam: PF07304 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **90.0/180** | |
| **归一化总分** | | | **50.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Microtubules, Cytokinetic bridge, Primary cilium, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cilium (GO:0005929)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- intercellular bridge (GO:0045171)
- microtubule cytoskeleton (GO:0015630)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 165 |
| PubMed broad count | 286 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Gsα Regulates Macrophage Foam Cell Formation During Atherosclerosis.. *Circulation research*. PMID: 38375634
2. Mechanisms of foam cell formation in atherosclerosis.. *Journal of molecular medicine (Berlin, Germany)*. PMID: 28785870
3. Mycobacterium tuberculosis suppresses host DNA repair to boost its intracellular survival.. *Cell host & microbe*. PMID: 37848028
4. Combined proteomics and single cell RNA-sequencing analysis to identify biomarkers of disease diagnosis and disease exacerbation for systemic lupus erythematosus.. *Frontiers in immunology*. PMID: 36524113
5. Fucoidan reduces NET accumulation and alleviates chemotherapy-induced peripheral neuropathy via the gut-blood-DRG axis.. *Journal of neuroinflammation*. PMID: 40186245

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.1 |
| 高置信度残基 (pLDDT>90) 占比 | 42.9% |
| 置信残基 (pLDDT 70-90) 占比 | 12.9% |
| 中等置信 (pLDDT 50-70) 占比 | 35.7% |
| 低置信 (pLDDT<50) 占比 | 8.5% |
| 有序区域 (pLDDT>70) 占比 | 55.8% |
| 可用 PDB 条目 | 2MGX, 4NBO |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2MGX, 4NBO）+ AlphaFold高质量预测（pLDDT=76.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009917, IPR040243; Pfam: PF07304 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ABI1 | 0.901 | 0.000 | — |
| WASF2 | 0.900 | 0.000 | — |
| ABI2 | 0.900 | 0.000 | — |
| NCKAP1 | 0.900 | 0.000 | — |
| BRK1 | 0.900 | 0.000 | — |
| NCKAP1L | 0.900 | 0.000 | — |
| RARG | 0.818 | 0.000 | — |
| DDX5 | 0.795 | 0.000 | — |
| DDX17 | 0.791 | 0.000 | — |
| DMBT1 | 0.767 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BCY1 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |
| TPK2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| TPK1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| UBE2Z | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ESS1 | psi-mi:"MI:0089"(protein array) | pubmed:16606443|imex:IM-19627| |
| CALM1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:16512683|imex:IM-19867 |
| SAM35 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| GPI14 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| UBQLN4 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| Cyfip1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12126|pubmed:18805096 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.1 + PDB: 2MGX, 4NBO | pLDDT=76.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Microtubules, Cytokinetic bridge, | 一致 |
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
1. SRA1 — Steroid receptor RNA activator 1，研究基础较多，新颖性有限。
2. 蛋白大小224 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 165 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 165 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HD15
- Protein Atlas: https://www.proteinatlas.org/ENSG00000213523-SRA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SRA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HD15
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000213523-SRA1/subcellular

![](https://images.proteinatlas.org/50153/2120_H10_10_red_green.jpg)
![](https://images.proteinatlas.org/50153/2120_H10_21_red_green.jpg)
![](https://images.proteinatlas.org/50153/2128_F11_16_red_green.jpg)
![](https://images.proteinatlas.org/50153/2128_F11_36_red_green.jpg)
![](https://images.proteinatlas.org/50153/2169_F6_15_red_green.jpg)
![](https://images.proteinatlas.org/50153/2169_F6_38_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HD15-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H7N4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR042841;IPR057031; |
| Pfam | PF23030; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000213523-SRA1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HDAC2 | Intact | false |
| SPEN | Biogrid | false |
| UBE2T | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
