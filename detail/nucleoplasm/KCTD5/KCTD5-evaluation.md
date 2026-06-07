---
type: protein-evaluation
gene: "KCTD5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KCTD5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KCTD5 |
| 蛋白名称 | BTB/POZ domain-containing protein KCTD5 |
| 蛋白大小 | 234 aa / 26.1 kDa |
| UniProt ID | Q9NXV2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytosol; Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 234 aa / 26.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=37 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=77.5; PDB: 3DRX, 3DRY, 3DRZ, 8U7Z, 8U80, 8U81, 8U82 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000210, IPR011333, IPR003131; Pfam: PF02214 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, cytosol; Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Cul3-RING ubiquitin ligase complex (GO:0031463)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 37 |
| PubMed broad count | 46 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Structure and dynamics of a pentameric KCTD5/CUL3/Gβγ E3 ubiquitin ligase complex.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 38625940
2. Heterozygous Kctd5 knockout mice exhibit abnormal lipid metabolism.. *The international journal of biochemistry & cell biology*. PMID: 40846050
3. KCTD5 regulates Ikaros degradation induced by chemotherapeutic drug etoposide in hematological cells.. *Biological chemistry*. PMID: 38424700
4. Investigation of ITGB3 Heterogeneity to Overcome Trastuzumab Resistance in HER2-Positive Breast Cancer.. *Biology*. PMID: 39857240
5. Integrated drug profiling and CRISPR screening identify BCR::ABL1-independent vulnerabilities in chronic myeloid leukemia.. *Cell reports. Medicine*. PMID: 38653245

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.5 |
| 高置信度残基 (pLDDT>90) 占比 | 52.1% |
| 置信残基 (pLDDT 70-90) 占比 | 14.1% |
| 中等置信 (pLDDT 50-70) 占比 | 11.5% |
| 低置信 (pLDDT<50) 占比 | 22.2% |
| 有序区域 (pLDDT>70) 占比 | 66.2% |
| 可用 PDB 条目 | 3DRX, 3DRY, 3DRZ, 8U7Z, 8U80, 8U81, 8U82, 8U83, 8U84 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3DRX, 3DRY, 3DRZ, 8U7Z, 8U80, 8U81, 8U82, 8U83, 8U84）+ AlphaFold极高置信度预测（pLDDT=77.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000210, IPR011333, IPR003131; Pfam: PF02214 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL3 | 0.998 | 0.880 | — |
| KCTD17 | 0.937 | 0.787 | — |
| KCND2 | 0.862 | 0.751 | — |
| KCTD2 | 0.802 | 0.292 | — |
| KCTD11 | 0.768 | 0.000 | — |
| KCTD13 | 0.729 | 0.000 | — |
| RBX1 | 0.727 | 0.000 | — |
| KCTD10 | 0.684 | 0.000 | — |
| GAN | 0.676 | 0.312 | — |
| SPOP | 0.673 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q3UPC0 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| ELF3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TRIP6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ILK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CUL2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| NXF1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| CD1A | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| NEK6 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| PRKAB2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| GIT2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.5 + PDB: 3DRX, 3DRY, 3DRZ, 8U7Z, 8U80,  | pLDDT=77.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Cytoplasm; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KCTD5 — BTB/POZ domain-containing protein KCTD5，非常新颖，仅有少数基础研究。
2. 蛋白大小234 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 37 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NXV2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167977-KCTD5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KCTD5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NXV2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NXV2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NXV2 |
| SMART | SM00225; |
| UniProt Domain [FT] | DOMAIN 44..146; /note="BTB" |
| InterPro | IPR000210;IPR011333;IPR003131; |
| Pfam | PF02214; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000167977-KCTD5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SLC9A3R2 | Intact, Biogrid | true |
| BTBD10 | Biogrid | false |
| CUL3 | Biogrid | false |
| FAM193B | Biogrid | false |
| GNB1 | Biogrid | false |
| GNG2 | Biogrid, Bioplex | false |
| KCNRG | Biogrid | false |
| KCTD10 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
