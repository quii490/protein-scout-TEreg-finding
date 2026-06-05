---
type: protein-evaluation
gene: "PHTF2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PHTF2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PHTF2 |
| 蛋白名称 | Protein PHTF2 |
| 蛋白大小 | 785 aa / 88.8 kDa |
| UniProt ID | Q8N3S3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 785 aa / 88.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039775, IPR021980; Pfam: PF12129 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. PHTF2 regulates lipids metabolism in gastric cancer.. *Aging*. PMID: 32335542
2. HOXA9 and HOXA13 along with their shared gene targets act as common immune biomarkers in recurrent implantation failure and pre-eclampsia.. *Human immunology*. PMID: 40020429
3. ChIP-seq assay revealed histone modification H3K9ac involved in heat shock response of the sea cucumber Apostichopus japonicus.. *The Science of the total environment*. PMID: 35051475
4. Molecular characterization of a novel gene family (PHTF) conserved from Drosophila to mammals.. *Genomics*. PMID: 10729229
5. [Analyses of differential expression of Homeobox genes between lingual squamaous cell carcinoma and normal mucosa].. *Hua xi kou qiang yi xue za zhi = Huaxi kouqiang yixue zazhi = West China journal of stomatology*. PMID: 18072571

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.8 |
| 高置信度残基 (pLDDT>90) 占比 | 7.0% |
| 置信残基 (pLDDT 70-90) 占比 | 36.2% |
| 中等置信 (pLDDT 50-70) 占比 | 13.8% |
| 低置信 (pLDDT<50) 占比 | 43.1% |
| 有序区域 (pLDDT>70) 占比 | 43.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.8），有序残基占 43.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039775, IPR021980; Pfam: PF12129 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PHTF1 | 0.628 | 0.610 | — |
| SLF1 | 0.497 | 0.289 | — |
| MSL3 | 0.480 | 0.414 | — |
| SHPRH | 0.457 | 0.107 | — |
| POLR3D | 0.453 | 0.000 | — |
| TMEM60 | 0.440 | 0.000 | — |
| ARID3B | 0.430 | 0.099 | — |
| LYPD3 | 0.423 | 0.420 | — |
| FUNDC2 | 0.413 | 0.045 | — |
| C9orf135 | 0.405 | 0.125 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000400958.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| uxuA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| DHRS2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| LYPD3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GPR156 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TTYH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| STXBP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| STXBP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| OSBPL6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| OSBPL3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 15
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.8 + PDB: 无 | pLDDT=59.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 12 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PHTF2 — Protein PHTF2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小785 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=59.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N3S3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000006576-PHTF2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PHTF2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N3S3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000006576-PHTF2/subcellular

![](https://images.proteinatlas.org/12312/112_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/12312/112_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/12312/113_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/12312/113_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/12312/161_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/12312/161_D4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N3S3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
