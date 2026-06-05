---
type: protein-evaluation
gene: "POU2AF3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## POU2AF3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | POU2AF3 / C11orf93, CASC13, COLCA2 |
| 蛋白名称 | POU class 2 homeobox associating factor 3 |
| 蛋白大小 | 251 aa / 27.4 kDa |
| UniProt ID | A8K830 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 251 aa / 27.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR047571, IPR043265 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 20 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C11orf93, CASC13, COLCA2 |

**关键文献**:
1. OCA-T1 and OCA-T2 are coactivators of POU2F3 in the tuft cell lineage.. *Nature*. PMID: 35576971
2. EWSR1::POU2AF3(COLCA2) Sarcoma: An Aggressive, Polyphenotypic Sarcoma With a Head and Neck Predilection.. *Modern pathology : an official journal of the United States and Canadian Academy of Pathology, Inc*. PMID: 37742928
3. POU2AF3-rearranged sarcomas: A novel tumor defined by fusions of EWSR1 or FUS to a gene formerly designated COLCA2.. *Genes, chromosomes & cancer*. PMID: 36862145
4. Genetic variation at 11q23.1 confers colorectal cancer risk by dysregulation of colonic tuft cell transcriptional activator POU2AF2.. *Gut*. PMID: 39609081
5. Optical Genome Mapping for Comprehensive Cytogenetic Analysis of Soft-Tissue and Bone Tumors for Diagnostic Purposes.. *The Journal of molecular diagnostics : JMD*. PMID: 38395407

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.5 |
| 高置信度残基 (pLDDT>90) 占比 | 8.8% |
| 置信残基 (pLDDT 70-90) 占比 | 6.0% |
| 中等置信 (pLDDT 50-70) 占比 | 37.8% |
| 低置信 (pLDDT<50) 占比 | 47.4% |
| 有序区域 (pLDDT>70) 占比 | 14.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.5），有序残基占 14.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR047571, IPR043265 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 无PPI数据
- STRING partners: 0，IntAct interactions: 0
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.5 + PDB: 无 | pLDDT=55.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 0 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. POU2AF3 — POU class 2 homeobox associating factor 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小251 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=55.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A8K830
- Protein Atlas: https://www.proteinatlas.org/ENSG00000214290-POU2AF3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=POU2AF3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A8K830
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000214290-POU2AF3/subcellular

![](https://images.proteinatlas.org/40625/1404_G12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40625/1404_G12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/40625/502_H5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40625/502_H5_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A8K830-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
