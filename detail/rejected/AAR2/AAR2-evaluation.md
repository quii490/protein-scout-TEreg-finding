---
type: protein-evaluation
gene: "AAR2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## AAR2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AAR2 / C20orf4 |
| 蛋白名称 | Protein AAR2 homolog |
| 蛋白大小 | 384 aa / 43.5 kDa |
| UniProt ID | Q9Y312 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 384 aa / 43.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.5; PDB: 7PJH |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR007946, IPR033648, IPR038514, IPR033647, IPR038 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.0/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- spliceosomal complex (GO:0005681)
- U5 snRNP (GO:0005682)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 28 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf4 |

**关键文献**:
1. Structural and Biochemical Investigation of Class I Ribonucleotide Reductase from the Hyperthermophile Aquifex aeolicus.. *Biochemistry*. PMID: 34941255
2. Integration of transcriptome-wide association study and gene-based association analysis identifies candidate genes for Hodgkin lymphoma.. *Journal of cancer research and clinical oncology*. PMID: 40392315
3. Crystallization and biochemical characterization of the human spliceosomal Aar2-Prp8(RNaseH) complex.. *Acta crystallographica. Section F, Structural biology communications*. PMID: 26527271
4. Structural and functional investigation of the human snRNP assembly factor AAR2 in complex with the RNase H-like domain of PRPF8.. *Acta crystallographica. Section D, Structural biology*. PMID: 36322420
5. AAR2, a gene for splicing pre-mRNA of the MATa1 cistron in cell type control of Saccharomyces cerevisiae.. *Molecular and cellular biology*. PMID: 1922071

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.5 |
| 高置信度残基 (pLDDT>90) 占比 | 71.6% |
| 置信残基 (pLDDT 70-90) 占比 | 21.4% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 1.6% |
| 有序区域 (pLDDT>70) 占比 | 93.0% |
| 可用 PDB 条目 | 7PJH |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.5，有序区 93.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007946, IPR033648, IPR038514, IPR033647, IPR038516; Pfam: PF05282, PF20981 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PRPF8 | 0.999 | 0.997 | — |
| SNRNP200 | 0.996 | 0.871 | — |
| EFTUD2 | 0.994 | 0.925 | — |
| DDX23 | 0.980 | 0.828 | — |
| SNRNP40 | 0.974 | 0.783 | — |
| CD2BP2 | 0.967 | 0.606 | — |
| ECD | 0.955 | 0.866 | — |
| PRPF6 | 0.955 | 0.604 | — |
| ZNHIT2 | 0.948 | 0.801 | — |
| TSSC4 | 0.933 | 0.850 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GJA5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EAPP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ARF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Csf1 | psi-mi:"MI:0096"(pull down) | pubmed:16267818|imex:IM-16654 |
| Cdk1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Prpf8 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Snw1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| H9A910 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:30177828|imex:IM-26452 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.5 + PDB: 7PJH | pLDDT=89.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. AAR2 — Protein AAR2 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小384 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y312
- Protein Atlas: https://www.proteinatlas.org/ENSG00000131043-AAR2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AAR2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y312
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000131043-AAR2/subcellular

![](https://images.proteinatlas.org/48645/1240_A9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/48645/1240_A9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/48645/721_G9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/48645/721_G9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/48645/727_G9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/48645/727_G9_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y312-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
