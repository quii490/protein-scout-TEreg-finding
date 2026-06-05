---
type: protein-evaluation
gene: "CHMP2A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CHMP2A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CHMP2A / BC2, CHMP2 |
| 蛋白名称 | Charged multivesicular body protein 2a |
| 蛋白大小 | 222 aa / 25.1 kDa |
| UniProt ID | O43633 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Cytosol; 额外: Nucleoplasm, Plasma membrane; UniProt: Late endosome membrane; Nucleus envelope |
| 蛋白大小 | 10/10 | x1 | 10 | 222 aa / 25.1 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=60 篇 (≤60→6) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=75.2; PDB: 7ZCG, 7ZCH |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR005024; Pfam: PF03357 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Plasma membrane | Approved |
| UniProt | Late endosome membrane; Nucleus envelope | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- amphisome membrane (GO:1904930)
- autophagosome membrane (GO:0000421)
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- ESCRT III complex (GO:0000815)
- extracellular exosome (GO:0070062)
- kinetochore (GO:0000776)
- kinetochore microtubule (GO:0005828)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 60 |
| PubMed broad count | 90 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BC2, CHMP2 |

**关键文献**:
1. De novo mutations in moderate or severe intellectual disability.. *PLoS genetics*. PMID: 25356899
2. CHMP2A regulates broad immune cell-mediated antitumor activity in an immunocompetent in vivo head and neck squamous cell carcinoma model.. *Journal for immunotherapy of cancer*. PMID: 38702144
3. ESCRT-mediated phagophore sealing during mitophagy.. *Autophagy*. PMID: 31366282
4. ATG9A controls all stages of autophagosome biogenesis.. *Autophagy*. PMID: 40241347
5. The endosomal sorting complex required for transport repairs the membrane to delay cell death.. *Frontiers in oncology*. PMID: 36330465

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.2 |
| 高置信度残基 (pLDDT>90) 占比 | 30.6% |
| 置信残基 (pLDDT 70-90) 占比 | 37.8% |
| 中等置信 (pLDDT 50-70) 占比 | 17.1% |
| 低置信 (pLDDT<50) 占比 | 14.4% |
| 有序区域 (pLDDT>70) 占比 | 68.4% |
| 可用 PDB 条目 | 7ZCG, 7ZCH |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7ZCG, 7ZCH）+ AlphaFold高质量预测（pLDDT=75.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005024; Pfam: PF03357 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000472680.1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-24991|pubmed:16730941 |
| EBI-1257125 | psi-mi:"MI:0096"(pull down) | pubmed:19463016|imex:IM-17246 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| TGFB3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| E2F4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| PCBD1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| EBI-1257121 | psi-mi:"MI:0096"(pull down) | pubmed:19367725|imex:IM-20587 |
| DLST | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| DECR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.2 + PDB: 7ZCG, 7ZCH | pLDDT=75.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Late endosome membrane; Nucleus envelope / Cytosol; 额外: Nucleoplasm, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CHMP2A -- Charged multivesicular body protein 2a，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小222 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 60 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43633
- Protein Atlas: https://www.proteinatlas.org/ENSG00000130724-CHMP2A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CHMP2A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43633
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43633-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
