---
type: protein-evaluation
gene: "SMYD4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SMYD4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SMYD4 / KIAA1936 |
| 蛋白名称 | Protein-lysine N-methyltransferase SMYD4 |
| 蛋白大小 | 804 aa / 89.2 kDa |
| UniProt ID | Q8IYR2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus, Vesicles; 额外: Nucleoplasm, Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 804 aa / 89.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR052097, IPR001214, IPR046341, IPR044421, IPR011 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.5/180** | |
| **归一化总分** | | | **75.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Vesicles; 额外: Nucleoplasm, Cytosol | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 27 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1936 |

**关键文献**:
1. SMYD4 monomethylates PRMT5 and forms a positive feedback loop to promote hepatocellular carcinoma progression.. *Cancer science*. PMID: 38438251
2. SMYD4 promotes MYH9 ubiquitination through lysine monomethylation modification to inhibit breast cancer progression.. *Breast cancer research : BCR*. PMID: 39930544
3. The roles of SMYD4 in epigenetic regulation of cardiac development in zebrafish.. *PLoS genetics*. PMID: 30110327
4. Functions of SMYD proteins in biological processes: What do we know? An updated review.. *Archives of biochemistry and biophysics*. PMID: 34555372
5. SMYD proteins: key regulators in skeletal and cardiac muscle development and function.. *Anatomical record (Hoboken, N.J. : 2007)*. PMID: 25125178

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.0 |
| 高置信度残基 (pLDDT>90) 占比 | 66.7% |
| 置信残基 (pLDDT 70-90) 占比 | 17.5% |
| 中等置信 (pLDDT 50-70) 占比 | 5.7% |
| 低置信 (pLDDT<50) 占比 | 10.1% |
| 有序区域 (pLDDT>70) 占比 | 84.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.0，有序区 84.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052097, IPR001214, IPR046341, IPR044421, IPR011990; Pfam: PF00856, PF01753 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMYD5 | 0.845 | 0.000 | — |
| PRDM15 | 0.647 | 0.095 | — |
| SETD4 | 0.588 | 0.000 | — |
| HDAC1 | 0.537 | 0.127 | — |
| SMYD3 | 0.536 | 0.000 | — |
| EHMT1 | 0.520 | 0.000 | — |
| KMT2E | 0.517 | 0.115 | — |
| PRDM4 | 0.509 | 0.095 | — |
| L3MBTL2 | 0.500 | 0.069 | — |
| METTL8 | 0.495 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| Smyd4-2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ATP5PO | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H3-4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| GYPB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PpD3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| NPAS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GMCL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CCT8L2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PRKY | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 13
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.0 + PDB: 无 | pLDDT=85.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Golgi apparatus, Vesicles; 额外: Nucleoplasm, Cytoso | 一致 |
| PPI | STRING + IntAct | 15 + 13 interactions | 数据充分 |

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
1. SMYD4 — Protein-lysine N-methyltransferase SMYD4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小804 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IYR2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000186532-SMYD4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SMYD4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IYR2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000186532-SMYD4/subcellular

![](https://images.proteinatlas.org/30059/295_C4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30059/295_C4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/30059/296_C4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30059/296_C4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/30059/297_C4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30059/297_C4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IYR2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
