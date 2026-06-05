---
type: protein-evaluation
gene: "CSTF2T"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CSTF2T 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CSTF2T / KIAA0689 |
| 蛋白名称 | Cleavage stimulation factor subunit 2 tau variant |
| 蛋白大小 | 616 aa / 64.4 kDa |
| UniProt ID | Q9H0L4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Vesicles, Basal body; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 616 aa / 64.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR025742, IPR026896, IPR038192, IPR012677, IPR035 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Basal body | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- mRNA cleavage and polyadenylation specificity factor complex (GO:0005847)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 62 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0689 |

**关键文献**:
1. The gene CSTF2T, encoding the human variant CstF-64 polyadenylation protein tauCstF-64, lacks introns and may be associated with male sterility.. *Genomics*. PMID: 12408968
2. First Infertile Case with CSTF2TGene Mutation.. *Molecular syndromology*. PMID: 33224017
3. CSTF2T facilitates pancreatic adenocarcinoma growth and metastasis by elevating H3K4Me1 methylation of CALB2 via ASH2L.. *Cancer biology & therapy*. PMID: 37287122
4. Cstf2t Regulates expression of histones and histone-like proteins in male germ cells.. *Andrology*. PMID: 29673127
5. The τCstF-64 polyadenylation protein controls genome expression in testis.. *PloS one*. PMID: 23110235

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.0 |
| 高置信度残基 (pLDDT>90) 占比 | 12.8% |
| 置信残基 (pLDDT 70-90) 占比 | 19.0% |
| 中等置信 (pLDDT 50-70) 占比 | 17.9% |
| 低置信 (pLDDT<50) 占比 | 50.3% |
| 有序区域 (pLDDT>70) 占比 | 31.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.0），有序残基占 31.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR025742, IPR026896, IPR038192, IPR012677, IPR035979; Pfam: PF14327, PF14304, PF00076 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CSTF3 | 0.998 | 0.972 | — |
| CSTF1 | 0.996 | 0.938 | — |
| CSTF2 | 0.989 | 0.834 | — |
| FIP1L1 | 0.985 | 0.934 | — |
| SYMPK | 0.983 | 0.909 | — |
| CPSF3 | 0.978 | 0.871 | — |
| CPSF2 | 0.967 | 0.827 | — |
| CPSF1 | 0.964 | 0.788 | — |
| WDR33 | 0.956 | 0.768 | — |
| PCF11 | 0.954 | 0.756 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UBQLN1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| UBQLN4 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| acnA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| U2SURP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZNF571 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| PKNOX2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| STH | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| FOXJ2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.0 + PDB: 无 | pLDDT=59.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Vesicles, Basal body | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CSTF2T — Cleavage stimulation factor subunit 2 tau variant，非常新颖，仅有少数基础研究。
2. 蛋白大小616 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=59.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H0L4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177613-CSTF2T/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CSTF2T
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H0L4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CSTF2T/IF_images/A-431_2.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CSTF2T/IF_images/A-431_1.jpg]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000177613-CSTF2T/subcellular

![](https://images.proteinatlas.org/62021/2166_G6_19_blue_red_green.jpg)
![](https://images.proteinatlas.org/62021/2166_G6_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/62021/2176_D7_34_blue_red_green.jpg)
![](https://images.proteinatlas.org/62021/2176_D7_69_blue_red_green.jpg)
![](https://images.proteinatlas.org/62021/2201_B7_14_blue_red_green.jpg)
![](https://images.proteinatlas.org/62021/2201_B7_73_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H0L4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
