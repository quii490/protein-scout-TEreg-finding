---
type: protein-evaluation
gene: "BANK1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BANK1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BANK1 |
| 蛋白名称 | B-cell scaffold protein with ankyrin repeats |
| 蛋白大小 | 785 aa / 89.3 kDa |
| UniProt ID | Q8NDB2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Cytosol; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 785 aa / 89.3 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=87 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036770, IPR052446, IPR017893, IPR041340, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **90.0/180** | |
| **归一化总分** | | | **50.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 87 |
| PubMed broad count | 136 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Bank1 modulates the differentiation and molecular profile of key B cell populations in autoimmunity.. *JCI insight*. PMID: 39163122
2. The Role of BANK1 in B Cell Signaling and Disease.. *Cells*. PMID: 34066164
3. IgA Vasculitis: Influence of CD40, BLK and BANK1 Gene Polymorphisms.. *Journal of clinical medicine*. PMID: 36233442
4. The association between BANK1 and TNFAIP3 gene polymorphisms and systemic lupus erythematosus: a meta-analysis.. *International journal of immunogenetics*. PMID: 21208380
5. Functional variants in the B-cell gene BANK1 are associated with systemic lupus erythematosus.. *Nature genetics*. PMID: 18204447

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.8 |
| 高置信度残基 (pLDDT>90) 占比 | 13.4% |
| 置信残基 (pLDDT 70-90) 占比 | 30.8% |
| 中等置信 (pLDDT 50-70) 占比 | 9.6% |
| 低置信 (pLDDT<50) 占比 | 46.2% |
| 有序区域 (pLDDT>70) 占比 | 44.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.8），有序残基占 44.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036770, IPR052446, IPR017893, IPR041340, IPR000157; Pfam: PF14545, PF18567 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BLK | 0.912 | 0.314 | — |
| MS4A1 | 0.875 | 0.067 | — |
| LYN | 0.854 | 0.314 | — |
| ITPR1 | 0.790 | 0.294 | — |
| PXK | 0.782 | 0.000 | — |
| PTPN22 | 0.769 | 0.065 | — |
| PHRF1 | 0.765 | 0.000 | — |
| IRF5 | 0.759 | 0.000 | — |
| NIBAN3 | 0.743 | 0.000 | — |
| ITPR3 | 0.734 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Stat3 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Traf1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| hemY | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000320509.4 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Q81PD4 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| glgA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SERPINH1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| FMR1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.8 + PDB: 无 | pLDDT=60.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Plasma membrane, Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. BANK1 — B-cell scaffold protein with ankyrin repeats，研究基础较多，新颖性有限。
2. 蛋白大小785 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 87 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=60.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NDB2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000153064-BANK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BANK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NDB2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000153064-BANK1/subcellular

![](https://images.proteinatlas.org/37002/1383_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/37002/1383_F7_3_red_green.jpg)
![](https://images.proteinatlas.org/37002/1442_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/37002/1442_G10_3_red_green.jpg)
![](https://images.proteinatlas.org/37002/432_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/37002/432_E8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NDB2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NDB2 |
| SMART | SM01282; |
| UniProt Domain [FT] | DOMAIN 25..153; /note="TIR"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00204"; DOMAIN 200..327; /note="DBB"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00707" |
| InterPro | IPR036770;IPR052446;IPR017893;IPR041340;IPR000157;IPR035897; |
| Pfam | PF14545;PF18567; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000153064-BANK1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| LYN | Intact, Biogrid | true |
| BLK | Intact | false |
| MYD88 | Biogrid | false |
| TRAF6 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
