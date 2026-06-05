---
type: protein-evaluation
gene: "TEDC2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TEDC2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TEDC2 / C16orf59 |
| 蛋白名称 | Tubulin epsilon and delta complex protein 2 |
| 蛋白大小 | 433 aa / 46.4 kDa |
| UniProt ID | Q7L2K0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cell Junctions; UniProt: Cell projection, cilium; Cytoplasm, cytoskeleton, microtubul |
| 蛋白大小 | 10/10 | ×1 | 10 | 433 aa / 46.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031518; Pfam: PF15764 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cell Junctions | Approved |
| UniProt | Cell projection, cilium; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centrio... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centriole (GO:0005814)
- cilium (GO:0005929)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C16orf59 |

**关键文献**:
1. TEDC2 correlated with prognosis and immune microenvironment in lung adenocarcinoma.. *Scientific reports*. PMID: 36973475
2. Identification of Novel Prognostic Markers Associated With Laryngeal Squamous Cell Carcinoma Using Comprehensive Analysis.. *Frontiers in oncology*. PMID: 35087752
3. TEDC2 plays an oncogenic role and serves as a therapeutic target of hepatocellular carcinoma.. *Digestive and liver disease : official journal of the Italian Society of Gastroenterology and the Italian Association for the Study of the Liver*. PMID: 37867019
4. Biallelic TEDC1 variants cause a new syndrome with severe growth impairment and endocrine complications.. *European journal of human genetics : EJHG*. PMID: 39979680
5. Identification of potential prognostic markers for lung adenocarcinoma using comprehensive analysis.. *Molecular medicine reports*. PMID: 37350390

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.1 |
| 高置信度残基 (pLDDT>90) 占比 | 12.9% |
| 置信残基 (pLDDT 70-90) 占比 | 41.1% |
| 中等置信 (pLDDT 50-70) 占比 | 13.2% |
| 低置信 (pLDDT<50) 占比 | 32.8% |
| 有序区域 (pLDDT>70) 占比 | 54.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.1），有序残基占 54.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031518; Pfam: PF15764 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TUBE1 | 0.862 | 0.788 | — |
| TEDC1 | 0.860 | 0.600 | — |
| TUBD1 | 0.665 | 0.095 | — |
| CDC45 | 0.603 | 0.000 | — |
| FGL1 | 0.546 | 0.525 | — |
| C16orf70 | 0.541 | 0.000 | — |
| RAD54L | 0.537 | 0.065 | — |
| ZNF311 | 0.509 | 0.046 | — |
| CDT1 | 0.500 | 0.000 | — |
| CDCA5 | 0.494 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TUBE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TEDC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MIS18A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FGL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KRT27 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MDFI | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| KRTAP10-7 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| KRTAP10-9 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| NOTCH2NLA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.1 + PDB: 无 | pLDDT=67.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, cilium; Cytoplasm, cytoskeleton,  / Nucleoplasm, Cell Junctions | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. TEDC2 — Tubulin epsilon and delta complex protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小433 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7L2K0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162062-TEDC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TEDC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7L2K0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000162062-TEDC2/subcellular

![](https://images.proteinatlas.org/51394/1028_E8_5_red_green.jpg)
![](https://images.proteinatlas.org/51394/1028_E8_6_red_green.jpg)
![](https://images.proteinatlas.org/51394/865_C11_1_red_green.jpg)
![](https://images.proteinatlas.org/51394/865_C11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7L2K0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
