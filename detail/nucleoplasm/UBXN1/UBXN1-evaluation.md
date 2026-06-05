---
type: protein-evaluation
gene: "UBXN1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## UBXN1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | UBXN1 / SAKS1 |
| 蛋白名称 | UBX domain-containing protein 1 |
| 蛋白大小 | 297 aa / 33.3 kDa |
| UniProt ID | Q04323 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 297 aa / 33.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=37 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR015940, IPR009060, IPR041923, IPR029071, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- VCP-NPL4-UFD1 AAA ATPase complex (GO:0034098)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 37 |
| PubMed broad count | 43 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SAKS1 |

**关键文献**:
1. Therapeutic targeting of the USP2-E2F4 axis inhibits autophagic machinery essential for zinc homeostasis in cancer progression.. *Autophagy*. PMID: 35253629
2. p53 promotes antiviral innate immunity by driving hexosamine metabolism.. *Cell reports*. PMID: 38294905
3. SUB1 promotes colorectal cancer metastasis by activating NF-κB signaling via UBR5-mediated ubiquitination of UBXN1.. *Science China. Life sciences*. PMID: 38240906
4. The p97-UBXN1 complex regulates aggresome formation.. *Journal of cell science*. PMID: 33712450
5. The many faces of p97/Cdc48 in mitochondrial homeostasis.. *Essays in biochemistry*. PMID: 41498289

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.4 |
| 高置信度残基 (pLDDT>90) 占比 | 40.4% |
| 置信残基 (pLDDT 70-90) 占比 | 29.6% |
| 中等置信 (pLDDT 50-70) 占比 | 10.1% |
| 低置信 (pLDDT<50) 占比 | 19.9% |
| 有序区域 (pLDDT>70) 占比 | 70.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.4，有序区 70.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015940, IPR009060, IPR041923, IPR029071, IPR001012; Pfam: PF22562, PF00789 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UBXN7 | 0.999 | 0.994 | — |
| VCP | 0.999 | 0.995 | — |
| FAF1 | 0.999 | 0.994 | — |
| FAF2 | 0.999 | 0.994 | — |
| TNFAIP1 | 0.995 | 0.994 | — |
| BAG6 | 0.995 | 0.994 | — |
| KCTD10 | 0.995 | 0.994 | — |
| MAGED1 | 0.994 | 0.994 | — |
| BTBD9 | 0.994 | 0.994 | — |
| NSFL1C | 0.981 | 0.397 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000303991.5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ASF1B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CDK4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CASP4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Vcp | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| VCPIP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| NPLOC4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| PLAA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| UFD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.4 + PDB: 无 | pLDDT=76.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. UBXN1 — UBX domain-containing protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小297 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 37 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q04323
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162191-UBXN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=UBXN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q04323
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000162191-UBXN1/subcellular

![](https://images.proteinatlas.org/76932/1803_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/76932/1803_F1_3_red_green.jpg)
![](https://images.proteinatlas.org/76932/1836_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/76932/1836_D12_2_red_green.jpg)
![](https://images.proteinatlas.org/76932/1893_G6_15_cr5bbf025c9c6ab_red_green.jpg)
![](https://images.proteinatlas.org/76932/1893_G6_17_cr5bbf025c9d595_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q04323-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
