---
type: protein-evaluation
gene: "GABPB2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GABPB2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GABPB2 / E4TF1B, GABPB, GABPB2 |
| 蛋白名称 | GA-binding protein subunit beta-1 |
| 蛋白大小 | 395 aa / 42.5 kDa |
| UniProt ID | Q06547 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 395 aa / 42.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050663, IPR002110, IPR036770; Pfam: PF00023, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasmic ribonucleoprotein granule (GO:0036464)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: E4TF1B, GABPB, GABPB2 |

**关键文献**:
1. Genome-wide analysis of alternative splicing differences in hepatic ischemia reperfusion injury.. *Scientific reports*. PMID: 39732885
2. Cancer-specific loss of TERT activation sensitizes glioblastoma to DNA damage.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 33758097
3. TERT and its binding protein: overexpression of GABPA/B in high grade gliomas.. *Oncotarget*. PMID: 34194624
4. Epigenetic profiling of human brain differential DNA methylation networks in schizophrenia.. *BMC medical genomics*. PMID: 28117656
5. Integrated analysis of ceRNA-miRNA changes in paraquat-induced pulmonary epithelial-mesenchymal transition via high-throughput sequencing.. *Journal of biochemical and molecular toxicology*. PMID: 38444083

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.1 |
| 高置信度残基 (pLDDT>90) 占比 | 45.6% |
| 置信残基 (pLDDT 70-90) 占比 | 7.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.3% |
| 低置信 (pLDDT<50) 占比 | 42.3% |
| 有序区域 (pLDDT>70) 占比 | 53.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.1），有序残基占 53.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050663, IPR002110, IPR036770; Pfam: PF00023, PF12796 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GABPA | 0.882 | 0.751 | — |
| ZNF383 | 0.554 | 0.091 | — |
| GK5 | 0.507 | 0.095 | — |
| POTEM | 0.507 | 0.092 | — |
| ZBTB25 | 0.505 | 0.091 | — |
| SMIM7 | 0.499 | 0.000 | — |
| M0QYU9_HUMAN | 0.476 | 0.000 | — |
| ANKRD30BL | 0.473 | 0.000 | — |
| CDKN2C | 0.448 | 0.000 | — |
| ANKRD30B | 0.435 | 0.092 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GABPB1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| FANCG | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| HCFC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:10675337 |
| CIC | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| IL16 | psi-mi:"MI:0397"(two hybrid array) | pubmed:19060904|imex:IM-20259 |
| PB1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-13585|pubmed:20064372 |
| GABPA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| SNRPB2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TSEN2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 15
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.1 + PDB: 无 | pLDDT=68.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 11 + 15 interactions | 数据充分 |

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
1. GABPB2 — GA-binding protein subunit beta-1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小395 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=68.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q06547
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143458-GABPB2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GABPB2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q06547
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GABPB2/IF_images/U-251MG_1.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GABPB2/IF_images/MCF-7_1.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000143458-GABPB2/subcellular

![](https://images.proteinatlas.org/28471/254_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/28471/254_H4_2_red_green.jpg)
![](https://images.proteinatlas.org/28471/291_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/28471/291_H4_2_red_green.jpg)
![](https://images.proteinatlas.org/28471/546_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/28471/546_H4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q06547-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
