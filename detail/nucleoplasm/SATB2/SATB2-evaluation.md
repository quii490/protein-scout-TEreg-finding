---
type: protein-evaluation
gene: "SATB2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SATB2 — REJECTED (研究热度过高 (PubMed strict=573，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SATB2 / KIAA1034 |
| 蛋白名称 | DNA-binding protein SATB2 |
| 蛋白大小 | 733 aa / 82.6 kDa |
| UniProt ID | Q9UPW6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Centrosome, Basal body, Cytosol; UniProt: Nucleus matrix |
| 蛋白大小 | 10/10 | ×1 | 10 | 733 aa / 82.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=573 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.1; PDB: 1WI3, 1WIZ, 2CSF |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003350, IPR032355, IPR001356, IPR009057, IPR010 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.0/180** | |
| **归一化总分** | | | **49.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Centrosome, Basal body, Cytosol | Supported |
| UniProt | Nucleus matrix | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- histone deacetylase complex (GO:0000118)
- nuclear matrix (GO:0016363)
- nucleoplasm (GO:0005654)
- transcription regulator complex (GO:0005667)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 573 |
| PubMed broad count | 1018 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1034 |

**关键文献**:
1. SATB2-Associated Syndrome.. **. PMID: 29023086
2. Integrative functional genomic analysis of human brain development and neuropsychiatric risks.. *Science (New York, N.Y.)*. PMID: 30545854
3. Immunohistochemistry in the diagnosis and classification of neuroendocrine neoplasms: what can brown do for you?. *Human pathology*. PMID: 31857137
4. Astrocyte layers in the mammalian cerebral cortex revealed by a single-cell in situ transcriptomic map.. *Nature neuroscience*. PMID: 32203496
5. Protein translation rate determines neocortical neuron fate.. *Nature communications*. PMID: 38849354

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.1 |
| 高置信度残基 (pLDDT>90) 占比 | 28.6% |
| 置信残基 (pLDDT 70-90) 占比 | 23.7% |
| 中等置信 (pLDDT 50-70) 占比 | 7.4% |
| 低置信 (pLDDT<50) 占比 | 40.2% |
| 有序区域 (pLDDT>70) 占比 | 52.3% |
| 可用 PDB 条目 | 1WI3, 1WIZ, 2CSF |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.1），有序残基占 52.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003350, IPR032355, IPR001356, IPR009057, IPR010982; Pfam: PF02376, PF16557, PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TBR1 | 0.898 | 0.000 | — |
| RUNX2 | 0.882 | 0.081 | — |
| BCL11B | 0.848 | 0.053 | — |
| SATB1 | 0.810 | 0.693 | — |
| CUX1 | 0.755 | 0.052 | — |
| FEZF2 | 0.750 | 0.053 | — |
| HDAC1 | 0.742 | 0.452 | — |
| FOXG1 | 0.735 | 0.164 | — |
| PAX6 | 0.731 | 0.000 | — |
| FOXP1 | 0.729 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.1 + PDB: 1WI3, 1WIZ, 2CSF | pLDDT=66.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus matrix / Nucleoplasm; 额外: Centrosome, Basal body, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SATB2 — DNA-binding protein SATB2，研究基础较多，新颖性有限。
2. 蛋白大小733 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 573 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=66.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 573 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UPW6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119042-SATB2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SATB2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UPW6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000119042-SATB2/subcellular

![](https://images.proteinatlas.org/1042/2250_A3_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/1042/2250_A3_9_blue_red_green.jpg)
![](https://images.proteinatlas.org/1042/2251_B2_54_blue_red_green.jpg)
![](https://images.proteinatlas.org/1042/2251_B2_80_blue_red_green.jpg)
![](https://images.proteinatlas.org/29543/2248_C4_35_blue_red_green.jpg)
![](https://images.proteinatlas.org/29543/2248_C4_78_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UPW6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UPW6 |
| SMART | SM01109;SM00389; |
| UniProt Domain [FT] | DOMAIN 57..158; /note="CMP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01326"; DOMAIN 161..234; /note="CUTL"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01327" |
| InterPro | IPR003350;IPR032355;IPR001356;IPR009057;IPR010982;IPR039673;IPR038216;IPR038224;IPR032392; |
| Pfam | PF02376;PF16557;PF00046;PF16534; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000119042-SATB2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HDAC1 | Biogrid, Opencell | true |
| TP63 | Intact, Biogrid | true |
| TRIM47 | Biogrid, Bioplex | true |
| FOXF1 | Biogrid | false |
| FOXL1 | Biogrid | false |
| FOXP1 | Biogrid | false |
| FOXP2 | Biogrid | false |
| FOXP4 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
