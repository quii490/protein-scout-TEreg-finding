---
type: protein-evaluation
gene: "BRF1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BRF1 — REJECTED (研究热度过高 (PubMed strict=171，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BRF1 / BRF, GTF3B, TAF3B2, TAF3C |
| 蛋白名称 | Transcription factor IIIB 90 kDa subunit |
| 蛋白大小 | 677 aa / 73.8 kDa |
| UniProt ID | Q92994 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nuclear bodies; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 677 aa / 73.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=171 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011665, IPR013763, IPR036915, IPR000812, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **87.5/180** | |
| **归一化总分** | | | **48.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription factor TFIIIB complex (GO:0000126)
- transcription preinitiation complex (GO:0097550)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 171 |
| PubMed broad count | 322 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BRF, GTF3B, TAF3B2, TAF3C |

**关键文献**:
1. Brf1 loss and not overexpression disrupts tissues homeostasis in the intestine, liver and pancreas.. *Cell death and differentiation*. PMID: 30858608
2. Alcohol Intake and Abnormal Expression of Brf1 in Breast Cancer.. *Oxidative medicine and cellular longevity*. PMID: 31781337
3. ROS Signaling-Mediated Novel Biological Targets: Brf1 and RNA Pol III Genes.. *Oxidative medicine and cellular longevity*. PMID: 34646425
4. Turnover of PPP1R15A mRNA encoding GADD34 controls responsiveness and adaptation to cellular stress.. *Cell reports*. PMID: 38602876
5. Exploring the Role and Mechanism of pAMPKα-Mediated Dysregulation of Brf1 and RNA Pol III Genes.. *Oxidative medicine and cellular longevity*. PMID: 33995823

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.1 |
| 高置信度残基 (pLDDT>90) 占比 | 29.1% |
| 置信残基 (pLDDT 70-90) 占比 | 24.7% |
| 中等置信 (pLDDT 50-70) 占比 | 16.0% |
| 低置信 (pLDDT<50) 占比 | 30.3% |
| 有序区域 (pLDDT>70) 占比 | 53.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.1），有序残基占 53.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011665, IPR013763, IPR036915, IPR000812, IPR013150; Pfam: PF07741, PF00382, PF08271 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TBP | 0.999 | 0.971 | — |
| BDP1 | 0.998 | 0.944 | — |
| GTF3C3 | 0.997 | 0.968 | — |
| POLR3F | 0.993 | 0.963 | — |
| GTF3C1 | 0.991 | 0.000 | — |
| POLR3B | 0.974 | 0.923 | — |
| GTF3C5 | 0.964 | 0.323 | — |
| POLR3A | 0.957 | 0.847 | — |
| POLR3C | 0.952 | 0.763 | — |
| CRCP | 0.942 | 0.824 | — |

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
| 三维结构 | AlphaFold pLDDT=69.1 + PDB: 无 | pLDDT=69.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BRF1 — Transcription factor IIIB 90 kDa subunit，研究基础较多，新颖性有限。
2. 蛋白大小677 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 171 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=69.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 171 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92994
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185024-BRF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BRF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92994
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000185024-BRF1/subcellular

![](https://images.proteinatlas.org/51918/766_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/51918/766_B10_2_red_green.jpg)
![](https://images.proteinatlas.org/51918/778_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/51918/778_B10_3_red_green.jpg)
![](https://images.proteinatlas.org/51918/910_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/51918/910_G2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92994-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q92994 |
| SMART | SM00385; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011665;IPR013763;IPR036915;IPR000812;IPR013150;IPR013137; |
| Pfam | PF07741;PF00382;PF08271; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000185024-BRF1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TBP | Intact, Biogrid, Opencell | true |
| CAPZB | Opencell | false |
| LMNA | Opencell | false |
| POLR1C | Opencell | false |
| POLR1D | Opencell | false |
| POLR2F | Opencell | false |
| POLR2H | Opencell | false |
| POLR2K | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
