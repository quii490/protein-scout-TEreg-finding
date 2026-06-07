---
type: protein-evaluation
gene: "FYB1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FYB1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FYB1 / FYB, SLAP130 |
| 蛋白名称 | FYN-binding protein 1 |
| 蛋白大小 | 783 aa / 85.4 kDa |
| UniProt ID | O15117 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; 额外: Nucleoplasm; UniProt: Cytoplasm; Nucleus; Cell junction |
| 蛋白大小 | 10/10 | ×1 | 10 | 783 aa / 85.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.6; PDB: 1RI9, 2GTJ, 2GTO |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043443, IPR035540, IPR029294, IPR036028, IPR001 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm; Nucleus; Cell junction | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- anchoring junction (GO:0070161)
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 92 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FYB, SLAP130 |

**关键文献**:
1. Proteomics reveal biomarkers for diagnosis, disease activity and long-term disability outcomes in multiple sclerosis.. *Nature communications*. PMID: 37903821
2. Recent advances in inherited platelet disorders.. *Current opinion in hematology*. PMID: 31348050
3. Transcriptomic analysis reveals shared gene signatures and molecular mechanisms between obesity and periodontitis.. *Frontiers in immunology*. PMID: 37063877
4. Spatially Resolved Single-Cell Transcriptome Analysis of Mycosis Fungoides Reveals Distinct Biomarkers GNLY and FYB1 Compared With Psoriasis and Chronic Spongiotic Dermatitis.. *Modern pathology : an official journal of the United States and Canadian Academy of Pathology, Inc*. PMID: 39675427
5. Super Enhancer Regulatory Gene FYB1 Promotes the Progression of T Cell Acute Lymphoblastic Leukemia by Activating IGLL1.. *Journal of immunology research*. PMID: 37767202

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.6 |
| 高置信度残基 (pLDDT>90) 占比 | 12.6% |
| 置信残基 (pLDDT 70-90) 占比 | 15.2% |
| 中等置信 (pLDDT 50-70) 占比 | 15.2% |
| 低置信 (pLDDT<50) 占比 | 57.0% |
| 有序区域 (pLDDT>70) 占比 | 27.8% |
| 可用 PDB 条目 | 1RI9, 2GTJ, 2GTO |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.6），有序残基占 27.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043443, IPR035540, IPR029294, IPR036028, IPR001452; Pfam: PF14603, PF07653 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| FYN | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| ABL1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| FASLG | psi-mi:"MI:0084"(phage display) | pubmed:19807924|imex:IM-20398 |
| GRB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19380743|imex:IM-20432 |
| SELENOH | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-12103|pubmed:19798671 |
| EVL | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-12103|pubmed:19798671 |
| DOCK2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-12103|pubmed:19798671 |
| SKAP1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-12103|pubmed:19798671 |
| ARHGEF2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-12103|pubmed:19798671 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.6 + PDB: 1RI9, 2GTJ, 2GTO | pLDDT=56.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cell junction / Plasma membrane; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FYB1 — FYN-binding protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小783 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=56.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15117
- Protein Atlas: https://www.proteinatlas.org/ENSG00000082074-FYB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FYB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15117
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000082074-FYB1/subcellular

![](https://images.proteinatlas.org/26796/1802_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/26796/1802_B1_4_red_green.jpg)
![](https://images.proteinatlas.org/26796/1813_A1_31_red_green.jpg)
![](https://images.proteinatlas.org/26796/1813_A1_32_red_green.jpg)
![](https://images.proteinatlas.org/26796/516_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/26796/516_D1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O15117-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O15117 |
| SMART | SM00326; |
| UniProt Domain [FT] | DOMAIN 511..572; /note="SH3 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00192"; DOMAIN 700..768; /note="SH3 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00192" |
| InterPro | IPR043443;IPR035540;IPR029294;IPR036028;IPR001452; |
| Pfam | PF14603;PF07653; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000082074-FYB1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FYN | Intact, Biogrid | true |
| LCP2 | Intact, Biogrid | true |
| SKAP1 | Intact, Biogrid | true |
| NCK1 | Intact | false |
| NCK2 | Intact | false |
| SH2D1A | Intact | false |
| SKAP2 | Biogrid | false |
| UBE2I | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
