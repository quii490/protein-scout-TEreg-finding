---
type: protein-evaluation
gene: "COMMD5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## COMMD5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COMMD5 |
| 蛋白名称 | COMM domain-containing protein 5 |
| 蛋白大小 | 224 aa / 24.7 kDa |
| UniProt ID | Q9GZQ3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 224 aa / 24.7 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=84.0; PDB: 8ESD, 8F2R, 8F2U, 8P0W |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR017920, IPR037357; Pfam: PF07258, PF21672 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **143.0/180** | |
| **归一化总分** | | | **79.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 21 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Hypertension-related, calcium-regulated gene (HCaRG/COMMD5) and kidney diseases: HCaRG accelerates tubular repair.. *Journal of nephrology*. PMID: 24515317
2. COMMD5 counteracts cisplatin-induced nephrotoxicity by maintaining tubular epithelial integrity and autophagy flux.. *American journal of physiology. Renal physiology*. PMID: 39298552
3. COMMD5/HCaRG Hooks Endosomes on Cytoskeleton and Coordinates EGFR Trafficking.. *Cell reports*. PMID: 30021164
4. COMMD5 is involved in the mechanisms of hypotension after parathyroidectomy in patients receiving hemodialysis.. *European journal of pharmacology*. PMID: 36804542
5. Contrasting Role of COMMD5 in Renal Cell Carcinoma: Tumor Suppression and Metastatic Enhancement.. *Anticancer research*. PMID: 40155026

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.0 |
| 高置信度残基 (pLDDT>90) 占比 | 59.8% |
| 置信残基 (pLDDT 70-90) 占比 | 23.7% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 8.9% |
| 有序区域 (pLDDT>70) 占比 | 83.5% |
| 可用 PDB 条目 | 8ESD, 8F2R, 8F2U, 8P0W |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8ESD, 8F2R, 8F2U, 8P0W）+ AlphaFold高质量预测（pLDDT=84.0），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017920, IPR037357; Pfam: PF07258, PF21672 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COMMD2 | 0.980 | 0.891 | — |
| COMMD10 | 0.979 | 0.866 | — |
| COMMD1 | 0.974 | 0.873 | — |
| COMMD4 | 0.969 | 0.866 | — |
| FAU | 0.967 | 0.967 | — |
| COMMD8 | 0.962 | 0.832 | — |
| CCDC22 | 0.956 | 0.848 | — |
| COMMD6 | 0.954 | 0.782 | — |
| COMMD9 | 0.950 | 0.623 | — |
| COMMD3 | 0.949 | 0.826 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| COMMD1 | psi-mi:"MI:0096"(pull down) | pubmed:15799966 |
| RELB | psi-mi:"MI:0096"(pull down) | pubmed:15799966 |
| RELA | psi-mi:"MI:0096"(pull down) | pubmed:15799966 |
| NFKB1 | psi-mi:"MI:0096"(pull down) | pubmed:15799966 |
| EBI-1257121 | psi-mi:"MI:0096"(pull down) | pubmed:19367725|imex:IM-20587 |
| COMMD10 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| DENND10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| COMMD8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| COMMD6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.0 + PDB: 8ESD, 8F2R, 8F2U, 8P0W | pLDDT=84.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. COMMD5 -- COMM domain-containing protein 5，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小224 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9GZQ3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170619-COMMD5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COMMD5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9GZQ3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000170619-COMMD5/subcellular

![](https://images.proteinatlas.org/46905/1034_A11_2_red_green.jpg)
![](https://images.proteinatlas.org/46905/1034_A11_3_red_green.jpg)
![](https://images.proteinatlas.org/46905/1137_G3_1_red_green.jpg)
![](https://images.proteinatlas.org/46905/1137_G3_2_red_green.jpg)
![](https://images.proteinatlas.org/46905/573_H1_3_red_green.jpg)
![](https://images.proteinatlas.org/46905/573_H1_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9GZQ3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
