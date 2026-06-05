---
type: protein-evaluation
gene: "RMC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RMC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RMC1 / C18orf8, MIC1, WDR98 |
| 蛋白名称 | Regulator of MON1-CCZ1 complex |
| 蛋白大小 | 657 aa / 75.0 kDa |
| UniProt ID | Q96DM3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: Lysosome membrane; Late endosome membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 657 aa / 75.0 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=97 篇 (≤100→2) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.7; PDB: 9L0D |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR040371, IPR009755, IPR049040, IPR015943, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **87.0/180** | |
| **归一化总分** | | | **48.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Uncertain |
| UniProt | Lysosome membrane; Late endosome membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- late endosome membrane (GO:0031902)
- lysosomal membrane (GO:0005765)
- Mon1-Ccz1 complex (GO:0035658)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 97 |
| PubMed broad count | 153 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C18orf8, MIC1, WDR98 |

**关键文献**:
1. Genetics of vegetarianism: A genome-wide association study.. *PloS one*. PMID: 37792698
2. Usherin defects lead to early-onset retinal dysfunction in zebrafish.. *Experimental eye research*. PMID: 29777677
3. C5orf51 is a component of the MON1-CCZ1 complex and controls RAB7A localization and stability during mitophagy.. *Autophagy*. PMID: 34432599
4. Receptors for polytropic and xenotropic mouse leukaemia viruses encoded by a single gene at Rmc1.. *Nature genetics*. PMID: 9988277
5. Mechanistic adaptation of the metazoan RabGEFs Mon1-Ccz1 and Fuzzy-Inturned.. *Science advances*. PMID: 40864718

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.7 |
| 高置信度残基 (pLDDT>90) 占比 | 66.2% |
| 置信残基 (pLDDT 70-90) 占比 | 25.4% |
| 中等置信 (pLDDT 50-70) 占比 | 7.2% |
| 低置信 (pLDDT<50) 占比 | 1.2% |
| 有序区域 (pLDDT>70) 占比 | 91.6% |
| 可用 PDB 条目 | 9L0D |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.7，有序区 91.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040371, IPR009755, IPR049040, IPR015943, IPR036322; Pfam: PF07035, PF21029 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCZ1B | 0.999 | 0.994 | — |
| CCZ1 | 0.990 | 0.644 | — |
| MON1B | 0.939 | 0.202 | — |
| MON1A | 0.934 | 0.202 | — |
| SLC20A2 | 0.825 | 0.000 | — |
| LAMC1 | 0.749 | 0.000 | — |
| XPR1 | 0.720 | 0.000 | — |
| SP6 | 0.541 | 0.541 | — |
| RAB7A | 0.470 | 0.309 | — |
| WDR91 | 0.448 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| APC5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| CDC16 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| CDC23 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:9469814 |
| CDC27 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:9469814 |
| APC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:9469814 |
| CDC26 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:9469814 |
| APC11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:9469814 |
| APC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:9469814 |
| APC4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:9469814 |
| prfC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 15
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.7 + PDB: 9L0D | pLDDT=88.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Lysosome membrane; Late endosome membrane / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 14 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. RMC1 — Regulator of MON1-CCZ1 complex，研究基础较多，新颖性有限。
2. 蛋白大小657 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 97 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96DM3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000141452-RMC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RMC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96DM3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000141452-RMC1/subcellular

![](https://images.proteinatlas.org/43589/496_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/43589/496_G8_2_red_green.jpg)
![](https://images.proteinatlas.org/43589/547_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/43589/547_G8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96DM3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
