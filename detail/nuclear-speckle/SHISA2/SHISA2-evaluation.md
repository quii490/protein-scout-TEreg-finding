---
type: protein-evaluation
gene: "SHISA2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SHISA2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SHISA2 / C13orf13, TMEM46 |
| 蛋白名称 | Protein shisa-2 homolog |
| 蛋白大小 | 295 aa / 31.4 kDa |
| UniProt ID | Q6UWI4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Nuclear bodies, Vesicles; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 295 aa / 31.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026910, IPR053891; Pfam: PF13908 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 5 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies, Vesicles | Approved |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 26 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C13orf13, TMEM46 |

**关键文献**:
1. CRL2(KLHDC3) and CRL1(Fbxw7) cooperatively mediate c-Myc degradation.. *Oncogene*. PMID: 38698266
2. The role of ferroptosis-related genes in airway epithelial cells of asthmatic patients based on bioinformatics.. *Medicine*. PMID: 36862916
3. Simulating neuronal development: exploring potential mechanisms for central nervous system metastasis in acute lymphoblastic leukemia.. *Frontiers in oncology*. PMID: 38239636
4. Impaired myogenesis in limb girdle muscular dystrophy type 2B.. *Scientific reports*. PMID: 41028869
5. Shisa2 regulates the fusion of muscle progenitors.. *Stem cell research*. PMID: 30007221

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.4 |
| 高置信度残基 (pLDDT>90) 占比 | 25.8% |
| 置信残基 (pLDDT 70-90) 占比 | 10.2% |
| 中等置信 (pLDDT 50-70) 占比 | 22.4% |
| 低置信 (pLDDT<50) 占比 | 41.7% |
| 有序区域 (pLDDT>70) 占比 | 36.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.4），有序残基占 36.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026910, IPR053891; Pfam: PF13908 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZNF646 | 0.504 | 0.000 | — |
| RPL36A-HNRNPH2 | 0.471 | 0.000 | — |
| PTGES2 | 0.465 | 0.466 | — |
| CDC42EP5 | 0.452 | 0.000 | — |
| ZADH2 | 0.412 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| CEP170P1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PTGES2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ATXN1L | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TMEM17 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| EPHX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RAP1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MYADM | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000319420 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 5，IntAct interactions: 9
- 调控相关比例: 0 / 5 = 0%

**评价**: STRING 5 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.4 + PDB: 无 | pLDDT=63.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / Nucleoplasm; 额外: Nuclear bodies, Vesicles | 一致 |
| PPI | STRING + IntAct | 5 + 9 interactions | 数据充分 |

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
1. SHISA2 — Protein shisa-2 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小295 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=63.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6UWI4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000180730-SHISA2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SHISA2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6UWI4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000180730-SHISA2/subcellular

![](https://images.proteinatlas.org/49752/1020_A5_2_red_green.jpg)
![](https://images.proteinatlas.org/49752/1020_A5_4_red_green.jpg)
![](https://images.proteinatlas.org/49752/1177_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/49752/1177_H8_3_red_green.jpg)
![](https://images.proteinatlas.org/49752/993_A5_5_red_green.jpg)
![](https://images.proteinatlas.org/49752/993_A5_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6UWI4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
