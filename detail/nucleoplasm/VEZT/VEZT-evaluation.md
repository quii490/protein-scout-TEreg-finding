---
type: protein-evaluation
gene: "VEZT"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## VEZT 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | VEZT |
| 蛋白名称 | Vezatin |
| 蛋白大小 | 779 aa / 88.7 kDa |
| UniProt ID | Q9HBM0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cell membrane; Cell projection, stereocilium membrane; Cell  |
| 蛋白大小 | 10/10 | ×1 | 10 | 779 aa / 88.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026859, IPR026858; Pfam: PF12632 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cell membrane; Cell projection, stereocilium membrane; Cell junction, adherens junction; Nucleus; Cy... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- acrosomal vesicle (GO:0001669)
- adherens junction (GO:0005912)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)
- stereocilia ankle link complex (GO:0002142)
- stereocilium membrane (GO:0060171)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 32 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Targeted next generation sequencing for molecular diagnosis of Usher syndrome.. *Orphanet journal of rare diseases*. PMID: 25404053
2. Multitrait GWAS and functional validation reveal genetic loci for gastric cancer.. *Nature communications*. PMID: 41833930
3. The role of gene polymorphisms in endometriosis.. *Molecular medicine reports*. PMID: 28901453
4. Down-regulation of VEZT gene expression in human gastric cancer involves promoter methylation and miR-43c.. *Biochemical and biophysical research communications*. PMID: 21156161
5. A Conserved Role for Vezatin Proteins in Cargo-Specific Regulation of Retrograde Axonal Transport.. *Genetics*. PMID: 32788307

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.4 |
| 高置信度残基 (pLDDT>90) 占比 | 18.1% |
| 置信残基 (pLDDT 70-90) 占比 | 34.3% |
| 中等置信 (pLDDT 50-70) 占比 | 16.6% |
| 低置信 (pLDDT<50) 占比 | 31.1% |
| 有序区域 (pLDDT>70) 占比 | 52.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.4），有序残基占 52.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026859, IPR026858; Pfam: PF12632 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MYO7A | 0.935 | 0.292 | — |
| WHRN | 0.907 | 0.000 | — |
| USH2A | 0.905 | 0.095 | — |
| ADGRV1 | 0.899 | 0.000 | — |
| PDZD7 | 0.889 | 0.000 | — |
| RPL5 | 0.876 | 0.544 | — |
| RPL23 | 0.875 | 0.516 | — |
| RPL35 | 0.871 | 0.508 | — |
| RPL23A | 0.855 | 0.570 | — |
| USH1C | 0.829 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LAMP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| PLGRKT | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| CANX | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| HSCB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28380382|imex:IM-25655 |
| DLK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IPPK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| C3AR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GPR21 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.4 + PDB: 无 | pLDDT=65.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Cell projection, stereocilium membr / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. VEZT — Vezatin，非常新颖，仅有少数基础研究。
2. 蛋白大小779 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=65.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HBM0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000028203-VEZT/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=VEZT
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HBM0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000028203-VEZT/subcellular

![](https://images.proteinatlas.org/4811/77_C11_1_red_green.jpg)
![](https://images.proteinatlas.org/4811/77_C11_2_red_green.jpg)
![](https://images.proteinatlas.org/4811/78_C11_1_red_green.jpg)
![](https://images.proteinatlas.org/4811/78_C11_2_red_green.jpg)
![](https://images.proteinatlas.org/4811/92_C11_1_red_green.jpg)
![](https://images.proteinatlas.org/4811/92_C11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HBM0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
