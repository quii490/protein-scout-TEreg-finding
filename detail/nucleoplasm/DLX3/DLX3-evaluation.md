---
type: protein-evaluation
gene: "DLX3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DLX3 — REJECTED (研究热度过高 (PubMed strict=245，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DLX3 |
| 蛋白名称 | Homeobox protein DLX-3 |
| 蛋白大小 | 287 aa / 31.7 kDa |
| UniProt ID | O60479 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 287 aa / 31.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=245 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.1; PDB: 4XRS |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050460, IPR022135, IPR001356, IPR020479, IPR017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 245 |
| PubMed broad count | 313 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Protein kinase a phosphorylates Dlx3 and regulates the function of Dlx3 during osteoblast differentiation.. *Journal of cellular biochemistry*. PMID: 24924519
2. DLX3 negatively regulates osteoclastic differentiation through microRNA-124.. *Experimental cell research*. PMID: 26836061
3. Regulation and function of Dlx3 in vertebrate development.. *Developmental dynamics : an official publication of the American Association of Anatomists*. PMID: 10906774
4. Estrogen Receptor α Regulates Dlx3-Mediated Osteoblast Differentiation.. *Molecules and cells*. PMID: 26674964
5. miR-9-5p promotes myogenic differentiation via the Dlx3/Myf5 axis.. *PeerJ*. PMID: 35529491

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.1 |
| 高置信度残基 (pLDDT>90) 占比 | 19.5% |
| 置信残基 (pLDDT 70-90) 占比 | 2.8% |
| 中等置信 (pLDDT 50-70) 占比 | 35.5% |
| 低置信 (pLDDT<50) 占比 | 42.2% |
| 有序区域 (pLDDT>70) 占比 | 22.3% |
| 可用 PDB 条目 | 4XRS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.1），有序残基占 22.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050460, IPR022135, IPR001356, IPR020479, IPR017970; Pfam: PF12413, PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MEIS1 | 0.955 | 0.903 | — |
| MEIS2 | 0.922 | 0.903 | — |
| RUNX2 | 0.797 | 0.000 | — |
| BGLAP | 0.787 | 0.000 | — |
| FAM83H | 0.707 | 0.000 | — |
| ENAM | 0.682 | 0.000 | — |
| GCM1 | 0.676 | 0.292 | — |
| SP7 | 0.673 | 0.054 | — |
| COL10A1 | 0.632 | 0.000 | — |
| IBSP | 0.627 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TBL1X | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| TDP2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| POU4F2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| BANP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:26871637|imex:IM-25013| |
| URS00000A07C1_10090 | psi-mi:"MI:0096"(pull down) | pubmed:29867223|imex:IM-24989 |
| GCM1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28515447|imex:IM-26805 |
| HTT | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| UBQLN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| PRPF40A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| ATXN1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.1 + PDB: 4XRS | pLDDT=60.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DLX3 — Homeobox protein DLX-3，研究基础较多，新颖性有限。
2. 蛋白大小287 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 245 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 245 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60479
- Protein Atlas: https://www.proteinatlas.org/ENSG00000064195-DLX3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DLX3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60479
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000064195-DLX3/subcellular

![](https://images.proteinatlas.org/31164/2030_E4_1_red_green.jpg)
![](https://images.proteinatlas.org/31164/2030_E4_2_red_green.jpg)
![](https://images.proteinatlas.org/31164/321_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/31164/321_E5_3_red_green.jpg)
![](https://images.proteinatlas.org/31164/326_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/31164/326_E5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60479-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O60479 |
| SMART | SM00389; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR050460;IPR022135;IPR001356;IPR020479;IPR017970;IPR009057;IPR000047; |
| Pfam | PF12413;PF00046; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000064195-DLX3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATXN1 | Intact | false |
| CASP6 | Intact | false |
| FGFR3 | Intact | false |
| HTT | Intact | false |
| POU4F2 | Intact | false |
| SNCA | Intact | false |
| UBQLN1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
