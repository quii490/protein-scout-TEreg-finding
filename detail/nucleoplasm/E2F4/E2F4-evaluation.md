---
type: protein-evaluation
gene: "E2F4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## E2F4 — REJECTED (研究热度过高 (PubMed strict=611，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | E2F4 |
| 蛋白名称 | Transcription factor E2F4 |
| 蛋白大小 | 413 aa / 44.0 kDa |
| UniProt ID | Q16254 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 413 aa / 44.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=611 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.2; PDB: 1CF7, 5TUU |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR015633, IPR037241, IPR032198, IPR003316, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 611 |
| PubMed broad count | 866 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Therapeutic targeting of the USP2-E2F4 axis inhibits autophagic machinery essential for zinc homeostasis in cancer progression.. *Autophagy*. PMID: 35253629
2. p27(Kip1) regulates alpha-synuclein expression.. *Oncotarget*. PMID: 29662651
3. USP24-i-101 targeting of USP24 activates autophagy to inhibit drug resistance acquired during cancer therapy.. *Cell death and differentiation*. PMID: 38491202
4. mTOR controls ependymal cell differentiation by targeting the alternative cell cycle and centrosomal proteins.. *EMBO reports*. PMID: 40307619
5. Interplay between NRF1, E2F4 and MYC transcription factors regulating common target genes contributes to cancer development and progression.. *Cellular oncology (Dordrecht, Netherlands)*. PMID: 30047092

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.2 |
| 高置信度残基 (pLDDT>90) 占比 | 21.1% |
| 置信残基 (pLDDT 70-90) 占比 | 20.8% |
| 中等置信 (pLDDT 50-70) 占比 | 21.1% |
| 低置信 (pLDDT<50) 占比 | 37.0% |
| 有序区域 (pLDDT>70) 占比 | 41.9% |
| 可用 PDB 条目 | 1CF7, 5TUU |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.2），有序残基占 41.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015633, IPR037241, IPR032198, IPR003316, IPR036388; Pfam: PF16421, PF02319 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TFDP2 | 0.999 | 0.990 | — |
| SMAD3 | 0.999 | 0.292 | — |
| RB1 | 0.999 | 0.921 | — |
| TFDP1 | 0.999 | 0.991 | — |
| RBL2 | 0.999 | 0.939 | — |
| RBL1 | 0.998 | 0.941 | — |
| SMAD4 | 0.997 | 0.000 | — |
| HDAC1 | 0.996 | 0.736 | — |
| LIN9 | 0.994 | 0.832 | — |
| E2F5 | 0.992 | 0.329 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRRAP | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:11418595 |
| AP3S2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| PCM1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| E2FA | psi-mi:"MI:0413"(electrophoretic mobility shift as | pubmed:11891240|imex:IM-20317 |
| DPB | psi-mi:"MI:0018"(two hybrid) | pubmed:11891240|imex:IM-20317 |
| CHMP2A | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| POLR1D | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| LIN54 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17531812 |
| LIN9 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17531812 |
| LIN37 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17531812 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.2 + PDB: 1CF7, 5TUU | pLDDT=64.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. E2F4 — Transcription factor E2F4，研究基础较多，新颖性有限。
2. 蛋白大小413 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 611 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=64.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 611 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q16254
- Protein Atlas: https://www.proteinatlas.org/ENSG00000205250-E2F4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=E2F4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q16254
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000205250-E2F4/subcellular

![](https://images.proteinatlas.org/54128/2147_E4_14_red_green.jpg)
![](https://images.proteinatlas.org/54128/2147_E4_79_red_green.jpg)
![](https://images.proteinatlas.org/54128/2161_A11_29_red_green.jpg)
![](https://images.proteinatlas.org/54128/2161_A11_4_red_green.jpg)
![](https://images.proteinatlas.org/54128/2268_C11_13_red_green.jpg)
![](https://images.proteinatlas.org/54128/2268_C11_38_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q16254-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
