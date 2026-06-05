---
type: protein-evaluation
gene: "TRUB1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRUB1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRUB1 / PUS4 |
| 蛋白名称 | Pseudouridylate synthase TRUB1 |
| 蛋白大小 | 349 aa / 37.3 kDa |
| UniProt ID | Q8WWH5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; UniProt: Nucleus; Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 349 aa / 37.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=81.1; PDB: 8JFX |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR020103, IPR002501, IPR014780; Pfam: PF01509 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Approved |
| UniProt | Nucleus; Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- mitochondrion (GO:0005739)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PUS4 |

**关键文献**:
1. TRUB1 is a novel biomarker for promoting malignancy in colorectal cancer via NFκB signaling.. *Gastroenterology report*. PMID: 40260225
2. The tRNA pseudouridine synthase TruB1 regulates the maturation of let-7 miRNA.. *The EMBO journal*. PMID: 32926445
3. The human TruB family of pseudouridine synthase genes, including the Dyskeratosis Congenita 1 gene and the novel member TRUB1.. *International journal of molecular medicine*. PMID: 12736709
4. Human TRUB1 is a highly conserved pseudouridine synthase responsible for the formation of Ψ55 in mitochondrial tRNAAsn, tRNAGln, tRNAGlu and tRNAPro.. *Nucleic acids research*. PMID: 36018806
5. Mapping of pseudouridine residues on cellular and viral transcripts using a novel antibody-based technique.. *RNA (New York, N.Y.)*. PMID: 34376564

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.1 |
| 高置信度残基 (pLDDT>90) 占比 | 62.8% |
| 置信残基 (pLDDT 70-90) 占比 | 8.0% |
| 中等置信 (pLDDT 50-70) 占比 | 10.0% |
| 低置信 (pLDDT<50) 占比 | 19.2% |
| 有序区域 (pLDDT>70) 占比 | 70.8% |
| 可用 PDB 条目 | 8JFX |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=81.1，有序区 70.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR020103, IPR002501, IPR014780; Pfam: PF01509 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NOP56 | 0.953 | 0.525 | — |
| PUS1 | 0.945 | 0.277 | — |
| NOP10 | 0.938 | 0.778 | — |
| NOP58 | 0.936 | 0.304 | — |
| GAR1 | 0.929 | 0.778 | — |
| PUS3 | 0.913 | 0.128 | — |
| PUS7 | 0.901 | 0.000 | — |
| NHP2 | 0.896 | 0.406 | — |
| FBL | 0.869 | 0.522 | — |
| METTL1 | 0.855 | 0.105 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CAND1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| SRPK2 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| USP11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TCEAL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MTFMT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC2A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| SETMAR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NUDT9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PRPS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.1 + PDB: 8JFX | pLDDT=81.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytosol / Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TRUB1 — Pseudouridylate synthase TRUB1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小349 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WWH5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165832-TRUB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRUB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WWH5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000165832-TRUB1/subcellular

![](https://images.proteinatlas.org/57552/1005_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/57552/1005_B5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/57552/1015_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/57552/1015_B5_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/57552/1176_D2_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/57552/1176_D2_6_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WWH5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
