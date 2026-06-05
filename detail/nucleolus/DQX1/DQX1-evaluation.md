---
type: protein-evaluation
gene: "DQX1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DQX1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DQX1 |
| 蛋白名称 | ATP-dependent RNA helicase homolog DQX1 |
| 蛋白大小 | 717 aa / 79.5 kDa |
| UniProt ID | Q8TE96 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoli fibrillar center; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 717 aa / 79.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011709, IPR048333, IPR007502, IPR014001, IPR027 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **142.0/180** | |
| **归一化总分** | | | **78.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- spliceosomal complex (GO:0005681)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. DQX1, an RNA-dependent ATPase homolog with a novel DEAQ box: expression pattern and genomic sequence comparison of the human and mouse genes.. *Mammalian genome : official journal of the International Mammalian Genome Society*. PMID: 11353393
2. Monitoring methylation-driven genes as prognostic biomarkers in patients with lung squamous cell cancer.. *Oncology letters*. PMID: 31897186
3. DeepCBS: shedding light on the impact of mutations occurring at CTCF binding sites.. *Frontiers in genetics*. PMID: 38463168
4. Integrative analysis of DNA methylation-driven genes for the prognosis of lung squamous cell carcinoma using MethylMix.. *International journal of medical sciences*. PMID: 32218699
5. Genome-wide identification of alternative splicing associated with histone deacetylase inhibitor in cutaneous T-cell lymphomas.. *Frontiers in genetics*. PMID: 36147491

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.2 |
| 高置信度残基 (pLDDT>90) 占比 | 64.7% |
| 置信残基 (pLDDT 70-90) 占比 | 25.4% |
| 中等置信 (pLDDT 50-70) 占比 | 4.7% |
| 低置信 (pLDDT<50) 占比 | 5.2% |
| 有序区域 (pLDDT>70) 占比 | 90.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.2，有序区 90.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011709, IPR048333, IPR007502, IPR014001, IPR027417; Pfam: PF21010, PF07717, PF04408 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UTP3 | 0.909 | 0.782 | — |
| ABT1 | 0.820 | 0.782 | — |
| EFTUD2 | 0.820 | 0.754 | — |
| SART1 | 0.812 | 0.782 | — |
| TFIP11 | 0.809 | 0.777 | — |
| CDC5L | 0.807 | 0.782 | — |
| BUD31 | 0.802 | 0.783 | — |
| BMS1 | 0.797 | 0.239 | — |
| PRPF19 | 0.793 | 0.778 | — |
| NOP58 | 0.783 | 0.413 | — |

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
| 三维结构 | AlphaFold pLDDT=87.2 + PDB: 无 | pLDDT=87.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DQX1 — ATP-dependent RNA helicase homolog DQX1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小717 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TE96
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144045-DQX1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DQX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TE96
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (approved)。来源: https://www.proteinatlas.org/ENSG00000144045-DQX1/subcellular

![](https://images.proteinatlas.org/46763/1816_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/46763/1816_A2_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/46763/2038_H5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/46763/2038_H5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/46763/2056_E6_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/46763/2056_E6_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TE96-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
