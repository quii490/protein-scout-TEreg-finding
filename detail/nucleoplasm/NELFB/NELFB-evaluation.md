---
type: protein-evaluation
gene: "NELFB"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NELFB 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NELFB / COBRA1, KIAA1182 |
| 蛋白名称 | Negative elongation factor B |
| 蛋白大小 | 580 aa / 65.7 kDa |
| UniProt ID | Q8WX92 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 580 aa / 65.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=89.2; PDB: 6GML, 7PKS, 7YCX, 8JJ6, 8RBX, 8UHA, 8UHD |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR010405; Pfam: PF06209 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **146.0/180** | |
| **归一化总分** | | | **81.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- NELF complex (GO:0032021)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: COBRA1, KIAA1182 |

**关键文献**:
1. NELF focuses sites of initiation and maintains promoter architecture.. *Nucleic acids research*. PMID: 38197272
2. Identification of mitophagy-related biomarkers in human osteoporosis based on a machine learning model.. *Frontiers in physiology*. PMID: 38260098
3. Negative Elongation Factor (NELF) Inhibits Premature Granulocytic Development in Zebrafish.. *International journal of molecular sciences*. PMID: 35409193
4. Nelfb promotes dermal white adipose tissue formation through RNA polymerase II-mediated adipogenic gene regulation.. *Development (Cambridge, England)*. PMID: 40960263
5. Identification of proteins in semen-derived extracellular vesicles that bind to Tat and NF-κB and that may impair HIV replication.. *Science signaling*. PMID: 40924817

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.2 |
| 高置信度残基 (pLDDT>90) 占比 | 71.6% |
| 置信残基 (pLDDT 70-90) 占比 | 22.1% |
| 中等置信 (pLDDT 50-70) 占比 | 1.9% |
| 低置信 (pLDDT<50) 占比 | 4.5% |
| 有序区域 (pLDDT>70) 占比 | 93.7% |
| 可用 PDB 条目 | 6GML, 7PKS, 7YCX, 8JJ6, 8RBX, 8UHA, 8UHD, 8UHG, 8UI0, 8W8E |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6GML, 7PKS, 7YCX, 8JJ6, 8RBX, 8UHA, 8UHD, 8UHG, 8UI0, 8W8E）+ AlphaFold极高置信度预测（pLDDT=89.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010405; Pfam: PF06209 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NELFE | 0.999 | 0.926 | — |
| NELFA | 0.999 | 0.975 | — |
| SUPT5H | 0.999 | 0.887 | — |
| NELFCD | 0.999 | 0.973 | — |
| SUPT4H1 | 0.996 | 0.507 | — |
| NCBP1 | 0.959 | 0.599 | — |
| CDK9 | 0.956 | 0.000 | — |
| CTR9 | 0.949 | 0.000 | — |
| POLR2E | 0.948 | 0.871 | — |
| POLR2A | 0.948 | 0.860 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NELFE | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| 40038273 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| FYN | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| ABL1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| PIK3R1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| PLCG1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| TCEAL2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.2 + PDB: 6GML, 7PKS, 7YCX, 8JJ6, 8RBX,  | pLDDT=89.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NELFB — Negative elongation factor B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小580 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WX92
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188986-NELFB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NELFB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WX92
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000188986-NELFB/subcellular

![](https://images.proteinatlas.org/20259/234_C4_12_red_green.jpg)
![](https://images.proteinatlas.org/20259/234_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/20259/235_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/20259/235_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/20259/535_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/20259/535_C4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WX92-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WX92 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR010405; |
| Pfam | PF06209; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000188986-NELFB/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BRCA1 | Intact, Biogrid | true |
| NELFA | Biogrid, Bioplex | true |
| NELFE | Intact, Biogrid, Bioplex | true |
| SUPT5H | Biogrid, Opencell | true |
| YWHAB | Biogrid, Opencell | true |
| YWHAE | Biogrid, Opencell | true |
| YWHAG | Biogrid, Opencell | true |
| YWHAZ | Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
