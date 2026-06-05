---
type: protein-evaluation
gene: "CARD8"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CARD8 — REJECTED (研究热度过高 (PubMed strict=172，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CARD8 / DACAR, KIAA0955, NDPP1 |
| 蛋白名称 | Caspase recruitment domain-containing protein 8 |
| 蛋白大小 | 537 aa / 60.7 kDa |
| UniProt ID | Q9Y2G2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus; Inflammasome |
| 蛋白大小 | 10/10 | x1 | 10 | 537 aa / 60.7 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=172 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=71.0; PDB: 4IKM, 6K9F, 6XKJ, 7JKQ, 7JN7 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR001315, IPR011029, IPR025307, IPR051249; Pfam:  |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Cytoplasm; Nucleus; Inflammasome | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- CARD8 inflammasome complex (GO:0140634)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- NLRP3 inflammasome complex (GO:0072559)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 172 |
| PubMed broad count | 297 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DACAR, KIAA0955, NDPP1 |

**关键文献**:
1. ZAKα-driven ribotoxic stress response activates the human NLRP1 inflammasome.. *Science (New York, N.Y.)*. PMID: 35857590
2. Molecular mechanisms of emerging inflammasome complexes and their activation and signaling in inflammation and pyroptosis.. *Immunological reviews*. PMID: 39351983
3. The NLRP1 and CARD8 inflammasomes.. *Immunological reviews*. PMID: 32558991
4. CARD8 is an inflammasome sensor for HIV-1 protease activity.. *Science (New York, N.Y.)*. PMID: 33542150
5. Genetic and Epigenetic Regulation of the Innate Immune Response to Gout.. *Immunological investigations*. PMID: 36745138

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.0 |
| 高置信度残基 (pLDDT>90) 占比 | 41.7% |
| 置信残基 (pLDDT 70-90) 占比 | 23.3% |
| 中等置信 (pLDDT 50-70) 占比 | 3.7% |
| 低置信 (pLDDT<50) 占比 | 31.3% |
| 有序区域 (pLDDT>70) 占比 | 65.0% |
| 可用 PDB 条目 | 4IKM, 6K9F, 6XKJ, 7JKQ, 7JN7 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4IKM, 6K9F, 6XKJ, 7JKQ, 7JN7）+ AlphaFold极高置信度预测（pLDDT=71.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001315, IPR011029, IPR025307, IPR051249; Pfam: PF00619, PF13553, PF23679 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NLRP3 | 0.998 | 0.307 | — |
| CASP1 | 0.997 | 0.000 | — |
| PYCARD | 0.996 | 0.050 | — |
| CASP5 | 0.989 | 0.000 | — |
| AIM2 | 0.981 | 0.000 | — |
| CASP9 | 0.976 | 0.292 | — |
| DPP9 | 0.972 | 0.900 | — |
| NLRP1 | 0.956 | 0.000 | — |
| NLRC4 | 0.947 | 0.058 | — |
| NLRP6 | 0.944 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| tuf | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| lpd | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A1Q4M0N4 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CEP192 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HDAC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAP3K7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| E2F6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TADA2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TADA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FLNA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.0 + PDB: 4IKM, 6K9F, 6XKJ, 7JKQ, 7JN7 | pLDDT=71.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Inflammasome / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CARD8 -- Caspase recruitment domain-containing protein 8，研究基础较多，新颖性有限。
2. 蛋白大小537 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 172 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 172 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2G2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105483-CARD8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CARD8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2G2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000105483-CARD8/subcellular

![](https://images.proteinatlas.org/43513/752_G3_1_red_green.jpg)
![](https://images.proteinatlas.org/43513/752_G3_2_red_green.jpg)
![](https://images.proteinatlas.org/43513/847_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/43513/847_H6_3_red_green.jpg)
![](https://images.proteinatlas.org/43513/857_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/43513/857_H6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y2G2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
