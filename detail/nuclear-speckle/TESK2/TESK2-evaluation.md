---
type: protein-evaluation
gene: "TESK2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TESK2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TESK2 |
| 蛋白名称 | Dual specificity testis-specific protein kinase 2 |
| 蛋白大小 | 571 aa / 63.6 kDa |
| UniProt ID | Q96S53 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 571 aa / 63.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050940, IPR011009, IPR000719, IPR017441, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Exosomal transcript cargo and functional correlation with HNSCC patients' survival.. *BMC cancer*. PMID: 39272022
2. Epimutations in both the TESK2 and MMACHC promoters in the Epi-cblC inherited disorder of intracellular metabolism of vitamin B(12).. *Clinical epigenetics*. PMID: 35440018
3. Identification and characterization of TESK2, a novel member of the LIMK/TESK family of protein kinases, predominantly expressed in testis.. *Genomics*. PMID: 10512679
4. Comparative analysis of an unusual gene arrangement in the human chromosome 1.. *Gene*. PMID: 18672041
5. Cofilin phosphorylation and actin reorganization activities of testicular protein kinase 2 and its predominant expression in testicular Sertoli cells.. *The Journal of biological chemistry*. PMID: 11418599

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.8 |
| 高置信度残基 (pLDDT>90) 占比 | 33.8% |
| 置信残基 (pLDDT 70-90) 占比 | 15.9% |
| 中等置信 (pLDDT 50-70) 占比 | 8.4% |
| 低置信 (pLDDT<50) 占比 | 41.9% |
| 有序区域 (pLDDT>70) 占比 | 49.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.8），有序残基占 49.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050940, IPR011009, IPR000719, IPR017441, IPR001245; Pfam: PF07714 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TEX36 | 0.572 | 0.000 | — |
| YWHAB | 0.526 | 0.521 | — |
| ADGRL1 | 0.514 | 0.514 | — |
| ADGRL2 | 0.514 | 0.514 | — |
| ADGRL3 | 0.514 | 0.514 | — |
| SSH3 | 0.491 | 0.094 | — |
| PDXP | 0.480 | 0.000 | — |
| TOE1 | 0.476 | 0.000 | — |
| SSH1 | 0.455 | 0.094 | — |
| YWHAQ | 0.448 | 0.443 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1380405 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| EBI-1380984 | psi-mi:"MI:0096"(pull down) | pubmed:17721511|imex:IM-19952 |
| HSP90AB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17906|pubmed:22939624| |
| YWHAQ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MBD2 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-26348|pubmed:27593931 |
| HSP90AA5P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SH3BP4 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| CGN | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 15
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.8 + PDB: 无 | pLDDT=65.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 13 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TESK2 — Dual specificity testis-specific protein kinase 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小571 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=65.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96S53
- Protein Atlas: https://www.proteinatlas.org/ENSG00000070759-TESK2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TESK2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96S53
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000070759-TESK2/subcellular

![](https://images.proteinatlas.org/27257/319_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/27257/319_B3_3_red_green.jpg)
![](https://images.proteinatlas.org/27257/320_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/27257/320_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/27257/340_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/27257/340_B3_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96S53-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
