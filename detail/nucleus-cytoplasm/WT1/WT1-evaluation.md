---
type: protein-evaluation
gene: "WT1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## WT1 — REJECTED (研究热度过高 (PubMed strict=4426，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WT1 |
| 蛋白名称 | Wilms tumor protein |
| 蛋白大小 | 449 aa / 49.2 kDa |
| UniProt ID | P19544 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Nucleus, nucleolus; Cytoplasm; Nucleus speckle; Nuc |
| 蛋白大小 | 10/10 | ×1 | 10 | 449 aa / 49.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=4426 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=50.8; PDB: 1XF7, 2JP9, 2JPA, 2PRT, 3HPJ, 3MYJ, 4R2E |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000976, IPR036236, IPR013087; Pfam: PF02165, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Enhanced |
| UniProt | Nucleus; Nucleus, nucleolus; Cytoplasm; Nucleus speckle; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear speck (GO:0016607)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4426 |
| PubMed broad count | 8062 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Epg5 deficiency leads to primary ovarian insufficiency due to WT1 accumulation in mouse granulosa cells.. *Autophagy*. PMID: 35786405
2. WT1(+) glomerular parietal epithelial progenitors promote renal proximal tubule regeneration after severe acute kidney injury.. *Theranostics*. PMID: 36923529
3. DNA and RNA binding by the Wilms' tumour gene 1 (WT1) protein +KTS and -KTS isoforms-From initial observations to recent global genomic analyses.. *European journal of haematology*. PMID: 29240258
4. WT1 and kidney progenitor cells.. *Organogenesis*. PMID: 20885852
5. [WT1-targeting cancer vaccine].. *Nihon rinsho. Japanese journal of clinical medicine*. PMID: 23259381

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 50.8 |
| 高置信度残基 (pLDDT>90) 占比 | 9.1% |
| 置信残基 (pLDDT 70-90) 占比 | 19.2% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 65.0% |
| 有序区域 (pLDDT>70) 占比 | 28.3% |
| 可用 PDB 条目 | 1XF7, 2JP9, 2JPA, 2PRT, 3HPJ, 3MYJ, 4R2E, 4R2P, 4R2Q, 4R2R |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=50.8），有序残基占 28.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000976, IPR036236, IPR013087; Pfam: PF02165, PF00096 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WTAP | 0.997 | 0.614 | — |
| TP53 | 0.983 | 0.626 | — |
| NR5A1 | 0.969 | 0.060 | — |
| SRY | 0.938 | 0.095 | — |
| NPHS1 | 0.935 | 0.000 | — |
| GATA4 | 0.935 | 0.091 | — |
| NPHS2 | 0.921 | 0.064 | — |
| SOX9 | 0.908 | 0.095 | — |
| NR0B1 | 0.907 | 0.067 | — |
| PAWR | 0.906 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MDM2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| DVL3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-11695|pubmed:19447967 |
| KRTAP10-3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| KRTAP10-8 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| KRT40 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| OSBPL3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CYSRT1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| IPO8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| WTAP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| BHLHE40 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=50.8 + PDB: 1XF7, 2JP9, 2JPA, 2PRT, 3HPJ,  | pLDDT=50.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus; Cytoplasm; Nucleus sp / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. WT1 — Wilms tumor protein，研究基础较多，新颖性有限。
2. 蛋白大小449 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4426 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=50.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 4426 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P19544
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184937-WT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P19544
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000184937-WT1/subcellular

![](https://images.proteinatlas.org/35717/1030_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/35717/1030_F12_2_red_green.jpg)
![](https://images.proteinatlas.org/35717/1472_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/35717/1472_E1_4_red_green.jpg)
![](https://images.proteinatlas.org/35717/574_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/35717/574_E9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P19544-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P19544 |
| SMART | SM00355; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000976;IPR036236;IPR013087; |
| Pfam | PF02165;PF00096; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000184937-WT1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DVL3 | Intact, Biogrid | true |
| CIAO1 | Biogrid | false |
| DVL2 | Biogrid | false |
| HMBOX1 | Biogrid | false |
| KRT40 | Intact | false |
| KRTAP10-3 | Biogrid | false |
| KRTAP10-7 | Biogrid | false |
| KRTAP10-8 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
