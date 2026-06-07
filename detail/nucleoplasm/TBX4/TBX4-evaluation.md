---
type: protein-evaluation
gene: "TBX4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TBX4 — REJECTED (研究热度过高 (PubMed strict=165，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TBX4 |
| 蛋白名称 | T-box transcription factor TBX4 |
| 蛋白大小 | 545 aa / 60.2 kDa |
| UniProt ID | P57082 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 545 aa / 60.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=165 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008967, IPR046360, IPR036960, IPR001699, IPR018 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.0/180** | |
| **归一化总分** | | | **46.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 165 |
| PubMed broad count | 285 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Defining the clinical validity of genes reported to cause pulmonary arterial hypertension.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 37422716
2. Novel risk genes and mechanisms implicated by exome sequencing of 2572 individuals with pulmonary arterial hypertension.. *Genome medicine*. PMID: 31727138
3. Molecular Function and Contribution of TBX4 in Development and Disease.. *American journal of respiratory and critical care medicine*. PMID: 36367783
4. TBX4 variants and pulmonary diseases: getting out of the 'Box'.. *Current opinion in pulmonary medicine*. PMID: 32195678
5. Human genome meeting 2016 : Houston, TX, USA. 28 February - 2 March 2016.. *Human genomics*. PMID: 27294413

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.2 |
| 高置信度残基 (pLDDT>90) 占比 | 30.6% |
| 置信残基 (pLDDT 70-90) 占比 | 4.0% |
| 中等置信 (pLDDT 50-70) 占比 | 5.1% |
| 低置信 (pLDDT<50) 占比 | 60.2% |
| 有序区域 (pLDDT>70) 占比 | 34.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.2），有序残基占 34.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008967, IPR046360, IPR036960, IPR001699, IPR018186; Pfam: PF00907 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PITX1 | 0.923 | 0.054 | — |
| HOXC10 | 0.905 | 0.076 | — |
| HOXC11 | 0.847 | 0.076 | — |
| FGF10 | 0.737 | 0.000 | — |
| PDLIM7 | 0.700 | 0.091 | — |
| BCAS3 | 0.697 | 0.000 | — |
| LMX1B | 0.689 | 0.071 | — |
| ATP13A3 | 0.666 | 0.045 | — |
| KCNK3 | 0.634 | 0.051 | — |
| NKX2-5 | 0.626 | 0.075 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Ncoa3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.2 + PDB: 无 | pLDDT=60.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TBX4 — T-box transcription factor TBX4，研究基础较多，新颖性有限。
2. 蛋白大小545 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 165 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 165 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P57082
- Protein Atlas: https://www.proteinatlas.org/search/TBX4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TBX4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P57082
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000121075-TBX4/subcellular

![](https://images.proteinatlas.org/44457/1533_D3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/44457/1533_D3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/44457/1548_E2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/44457/1548_E2_7_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P57082-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P57082 |
| SMART | SM00425; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR008967;IPR046360;IPR036960;IPR001699;IPR018186; |
| Pfam | PF00907; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000121075-TBX4/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
