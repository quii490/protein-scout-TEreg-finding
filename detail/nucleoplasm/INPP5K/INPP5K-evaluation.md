---
type: protein-evaluation
gene: "INPP5K"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## INPP5K 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | INPP5K / PPS, SKIP |
| 蛋白名称 | Inositol polyphosphate 5-phosphatase K |
| 蛋白大小 | 448 aa / 51.1 kDa |
| UniProt ID | Q9BT40 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 448 aa / 51.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036691, IPR046985, IPR000300, IPR041611; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Endoplasmic reticulum; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- membrane (GO:0016020)
- neuron projection (GO:0043005)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 38 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PPS, SKIP |

**关键文献**:
1. The phosphoinositide 5-phosphatase INPP5K: From gene structure to in vivo functions.. *Advances in biological regulation*. PMID: 33060052
2. Duplicated zebrafish (Danio rerio) inositol phosphatases inpp5ka and inpp5kb diverged in expression pattern and function.. *Development genes and evolution*. PMID: 37184573
3. Knockdown of INPP5K compromises the differentiation of N2A cells.. *Frontiers in molecular neuroscience*. PMID: 38559586
4. Analysis of an independent tumor suppressor locus telomeric to Tp53 suggested Inpp5k and Myo1c as novel tumor suppressor gene candidates in this region.. *BMC genetics*. PMID: 26170120
5. The inositol Inpp5k 5-phosphatase affects osmoregulation through the vasopressin-aquaporin 2 pathway in the collecting system.. *Pflugers Archiv : European journal of physiology*. PMID: 21938401

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.4 |
| 高置信度残基 (pLDDT>90) 占比 | 72.3% |
| 置信残基 (pLDDT 70-90) 占比 | 16.1% |
| 中等置信 (pLDDT 50-70) 占比 | 6.9% |
| 低置信 (pLDDT<50) 占比 | 4.7% |
| 有序区域 (pLDDT>70) 占比 | 88.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.4，有序区 88.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036691, IPR046985, IPR000300, IPR041611; Pfam: PF22669, PF17751 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| INPP5A | 0.957 | 0.000 | — |
| ITPKC | 0.925 | 0.000 | — |
| ITPKB | 0.925 | 0.000 | — |
| MINPP1 | 0.923 | 0.000 | — |
| ITPKA | 0.923 | 0.000 | — |
| IPMK | 0.921 | 0.000 | — |
| ITPK1 | 0.920 | 0.000 | — |
| INPP1 | 0.915 | 0.000 | — |
| INPP5J | 0.907 | 0.000 | — |
| PLCE1 | 0.755 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ARL6IP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| LNX1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16002321|imex:IM-18900 |
| EPPK1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PYGM | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PDXDC1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| DCD | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| BDNF | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| TANK | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CPTP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Ripk3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.4 + PDB: 无 | pLDDT=88.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum; Cytoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. INPP5K — Inositol polyphosphate 5-phosphatase K，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小448 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BT40
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132376-INPP5K/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=INPP5K
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BT40
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BT40-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
