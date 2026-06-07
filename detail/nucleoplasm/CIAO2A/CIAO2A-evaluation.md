---
type: protein-evaluation
gene: "CIAO2A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CIAO2A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CIAO2A / CIA2A, FAM96A |
| 蛋白名称 | Cytosolic iron-sulfur assembly component 2A |
| 蛋白大小 | 160 aa / 18.4 kDa |
| UniProt ID | Q9H5X1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 8/10 | x1 | 8 | 160 aa / 18.4 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=86.6; PDB: 2M5H, 3UX2, 3UX3 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR034904, IPR039796, IPR002744; Pfam: PF01883 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.0/180** | |
| **归一化总分** | | | **78.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Enhanced |
| UniProt | Cytoplasm | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- cytosolic [4Fe-4S] assembly targeting complex (GO:0097361)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CIA2A, FAM96A |

**关键文献**:
1. Fam96a is essential for the host control of Toxoplasma gondii infection by fine-tuning macrophage polarization via an iron-dependent mechanism.. *PLoS neglected tropical diseases*. PMID: 38713713
2. The Cia1 and Cia2 subunits of the CTC mediate recognition of apo-FeS proteins with a C-terminal targeting complex recognition motif.. *bioRxiv : the preprint server for biology*. PMID: 40196589
3. FAM96A is essential for maintaining organismal energy balance and adipose tissue homeostasis in mice.. *Free radical biology & medicine*. PMID: 36150559
4. Long-read sequencing and proteomics reveal blood transcriptome and protein expression profiles in multiple primary lung cancers.. *BMC cancer*. PMID: 41761147

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.6 |
| 高置信度残基 (pLDDT>90) 占比 | 68.8% |
| 置信残基 (pLDDT 70-90) 占比 | 13.1% |
| 中等置信 (pLDDT 50-70) 占比 | 16.9% |
| 低置信 (pLDDT<50) 占比 | 1.2% |
| 有序区域 (pLDDT>70) 占比 | 81.9% |
| 可用 PDB 条目 | 2M5H, 3UX2, 3UX3 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2M5H, 3UX2, 3UX3）+ AlphaFold高质量预测（pLDDT=86.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR034904, IPR039796, IPR002744; Pfam: PF01883 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CIAO1 | 0.999 | 0.972 | — |
| MMS19 | 0.996 | 0.696 | — |
| CIAO3 | 0.991 | 0.744 | — |
| CIAO2B | 0.965 | 0.359 | — |
| IREB2 | 0.855 | 0.583 | — |
| NUBP1 | 0.791 | 0.071 | — |
| CIAPIN1 | 0.620 | 0.000 | — |
| NDOR1 | 0.534 | 0.071 | — |
| ABCB7 | 0.527 | 0.000 | — |
| APAF1 | 0.524 | 0.078 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CIAO1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| eef1a1o.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |
| RHBDD2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| MEST | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| PLPP6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ERGIC3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FKBP7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| APOA2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PLP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DERL1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.6 + PDB: 2M5H, 3UX2, 3UX3 | pLDDT=86.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CIAO2A -- Cytosolic iron-sulfur assembly component 2A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小160 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H5X1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166797-CIAO2A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CIAO2A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H5X1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000166797-CIAO2A/subcellular

![](https://images.proteinatlas.org/40459/412_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/40459/412_D10_3_red_green.jpg)
![](https://images.proteinatlas.org/40459/419_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/40459/419_D10_5_red_green.jpg)
![](https://images.proteinatlas.org/40459/471_D10_3_red_green.jpg)
![](https://images.proteinatlas.org/40459/471_D10_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H5X1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H5X1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR034904;IPR039796;IPR002744; |
| Pfam | PF01883; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000166797-CIAO2A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CIAO1 | Intact, Biogrid, Bioplex | true |
| CIAO3 | Intact, Biogrid, Bioplex | true |
| IREB2 | Biogrid, Bioplex | true |
| POLE | Biogrid, Bioplex | true |
| AAAS | Bioplex | false |
| ABCD1 | Bioplex | false |
| ANAPC5 | Bioplex | false |
| ANKLE2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
