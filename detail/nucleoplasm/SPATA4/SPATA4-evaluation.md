---
type: protein-evaluation
gene: "SPATA4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPATA4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPATA4 / TSARG2 |
| 蛋白名称 | Spermatogenesis-associated protein 4 |
| 蛋白大小 | 305 aa / 34.8 kDa |
| UniProt ID | Q8NEY3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 305 aa / 34.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR010441, IPR001715, IPR036872, IPR052111; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axoneme (GO:0005930)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 27 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TSARG2 |

**关键文献**:
1. Cloning and characterization of chicken SPATA4 gene and analysis of its specific expression.. *Molecular and cellular biochemistry*. PMID: 17673952
2. Increased DNA methylation in the spermatogenesis-associated (SPATA) genes correlates with infertility.. *Andrology*. PMID: 31838782
3. Cloning and characterization of zebra fish SPATA4 gene and analysis of its gonad specific expression.. *Biochemistry. Biokhimiia*. PMID: 16038605
4. Molecular cloning and bioinformatic analysis of SPATA4 gene.. *Journal of biochemistry and molecular biology*. PMID: 16336790
5. SPATA4 improves aging-induced metabolic dysfunction through promotion of preadipocyte differentiation and adipose tissue expansion.. *Aging cell*. PMID: 33314576

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.7 |
| 高置信度残基 (pLDDT>90) 占比 | 44.6% |
| 置信残基 (pLDDT 70-90) 占比 | 16.1% |
| 中等置信 (pLDDT 50-70) 占比 | 16.7% |
| 低置信 (pLDDT<50) 占比 | 22.6% |
| 有序区域 (pLDDT>70) 占比 | 60.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.7，有序区 60.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010441, IPR001715, IPR036872, IPR052111; Pfam: PF06294 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WDR90 | 0.754 | 0.754 | — |
| SPATA17 | 0.738 | 0.000 | — |
| PGK2 | 0.625 | 0.401 | — |
| ASB5 | 0.562 | 0.111 | — |
| FANK1 | 0.559 | 0.111 | — |
| PLAAT5 | 0.543 | 0.000 | — |
| ELMOD2 | 0.535 | 0.000 | — |
| SPATA20 | 0.532 | 0.000 | — |
| ZMYND10 | 0.521 | 0.000 | — |
| SPAG6 | 0.515 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SIAH1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| FAT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LCN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.7 + PDB: 无 | pLDDT=74.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Vesicles, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SPATA4 — Spermatogenesis-associated protein 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小305 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NEY3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000150628-SPATA4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPATA4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NEY3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000150628-SPATA4/subcellular

![](https://images.proteinatlas.org/30791/2183_E3_23_blue_red_green.jpg)
![](https://images.proteinatlas.org/30791/2183_E3_49_blue_red_green.jpg)
![](https://images.proteinatlas.org/30791/2217_E4_10_blue_red_green.jpg)
![](https://images.proteinatlas.org/30791/2217_E4_13_blue_red_green.jpg)
![](https://images.proteinatlas.org/30791/2096_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/30791/2096_E9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NEY3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
