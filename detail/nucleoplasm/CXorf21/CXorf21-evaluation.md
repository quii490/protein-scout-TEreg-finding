---
type: protein-evaluation
gene: "CXorf21"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CXorf21 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CXorf21 / TASL |
| 蛋白名称 | TLR adapter interacting with SLC15A4 on the lysosome |
| 蛋白大小 | 301 aa / 33.9 kDa |
| UniProt ID | Q9HAI6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm; 额外: Vesicles, Cytosol; UniProt: Lysosome membrane; Endosome membrane; Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | x1 | 10 | 301 aa / 33.9 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=58.3; PDB: 无 |
| 调控结构域 | 5/10 | x2 | 10 | 无注释结构域 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **122.5/180** | |
| **归一化总分** | | | **68.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Cytosol | Supported |
| UniProt | Lysosome membrane; Endosome membrane; Nucleus; Cytoplasm | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 15 |
| 别名(未计入scoring) |  |

**关键文献**:
1. The adaptor protein TASL is required for age-related B cell emergence and lupus-like disease development in mice.. *PLoS Biol*. PMID: 41785302
2. The molecular underpinnings of female predominance in lupus.. *Trends Mol Med*. PMID: 39627079
3. Genes that escape from X-chromosome inactivation and sexual dimorphism of systemic lupus erythematosus.. *Yi Chuan*. PMID: 38230454
4. A Novel Look at Dosage-Sensitive Sex Locus Xp21.2 in a Case of 46,XY Partial Gonadal Dysgenesis without NR0B1 Duplication.. *Int J Mol Sci*. PMID: 36613932
5. [Clinical and genetic analysis of a child with disorder of sex development].. *Zhonghua Yi Xue Yi Chuan Xue Za Zhi*. PMID: 35929938

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.3 |
| 高置信度残基 (pLDDT>90) 占比 | 11.0% |
| 置信残基 (pLDDT 70-90) 占比 | 16.6% |
| 中等置信 (pLDDT 50-70) 占比 | 30.6% |
| 低置信 (pLDDT<50) 占比 | 41.9% |
| 有序区域 (pLDDT>70) 占比 | 27.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.3），有序残基占 27.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q8N697 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:P54652 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P60709 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P68032 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9H0C2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9NQC7 | psi-mi:"MI:0081"(peptide array) | pubmed:- |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 8
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.3 + PDB: 无 | pLDDT=58.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Lysosome membrane; Endosome membrane; Nucleus; Cyt / Nucleoplasm; 额外: Vesicles, Cytosol | 一致 |
| PPI | STRING + IntAct | 0 + 8 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CXorf21 -- TLR adapter interacting with SLC15A4 on the lysosome，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小301 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=58.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HAI6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120280-CXorf21/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CXorf21
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HAI6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HAI6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
