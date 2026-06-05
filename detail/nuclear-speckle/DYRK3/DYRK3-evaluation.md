---
type: protein-evaluation
gene: "DYRK3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DYRK3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DYRK3 |
| 蛋白名称 | Dual specificity tyrosine-phosphorylation-regulated kinase 3 |
| 蛋白大小 | 588 aa / 65.7 kDa |
| UniProt ID | O43781 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm; Nucleus speckle; Cytoplasmic granule; Cy |
| 蛋白大小 | 10/10 | ×1 | 10 | 588 aa / 65.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=46 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=75.0; PDB: 5Y86 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR042521, IPR011009, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 7 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.0/180** | |
| **归一化总分** | | | **65.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Nucleus speckle; Cytoplasmic granule; Cytoplasm, cytoskeleton, microtubule organ... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic stress granule (GO:0010494)
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- pericentriolar material (GO:0000242)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 46 |
| PubMed broad count | 70 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. [Molecular cloning and characterization of novel protein kinase gene DYRK3].. *Zhonghua yi xue yi chuan xue za zhi = Zhonghua yixue yichuanxue zazhi = Chinese journal of medical genetics*. PMID: 9845759
2. DYRK gene structure and erythroid-restricted features of DYRK3 gene expression.. *Genomics*. PMID: 15607427
3. DYRK1A and DYRK3 promote cell survival through phosphorylation and activation of SIRT1.. *The Journal of biological chemistry*. PMID: 20167603
4. DYRK3 enables secretory trafficking by maintaining the liquid-like state of ER exit sites.. *Developmental cell*. PMID: 37643612
5. DYRK3 phosphorylates SNAPIN to regulate axonal retrograde transport and neurotransmitter release.. *Cell death discovery*. PMID: 36585413

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.0 |
| 高置信度残基 (pLDDT>90) 占比 | 62.6% |
| 置信残基 (pLDDT 70-90) 占比 | 3.6% |
| 中等置信 (pLDDT 50-70) 占比 | 0.9% |
| 低置信 (pLDDT<50) 占比 | 33.0% |
| 有序区域 (pLDDT>70) 占比 | 66.2% |
| 可用 PDB 条目 | 5Y86 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=75.0，有序区 66.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042521, IPR011009, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DCAF7 | 0.681 | 0.457 | — |
| GATA1 | 0.559 | 0.091 | — |
| H2BC21 | 0.516 | 0.000 | — |
| SIRT1 | 0.496 | 0.314 | — |
| PLK4 | 0.410 | 0.309 | — |
| G3BP1 | 0.405 | 0.000 | — |
| MKRN2OS | 0.400 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PRNP | psi-mi:"MI:0089"(protein array) | pubmed:18482256|imex:IM-19010 |
| SORL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| PKM | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-22313|pubmed:24606918 |
| EBI-9351778 | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-22313|pubmed:24606918 |
| GORASP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EIF3F | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |
| HSPB1 | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |
| EIF2S1 | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |
| TPM3 | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |
| TPM2 | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 7，IntAct interactions: 15
- 调控相关比例: 0 / 7 = 0%

**评价**: STRING 7 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.0 + PDB: 5Y86 | pLDDT=75.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Nucleus speckle; Cytoplasmic g / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 7 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DYRK3 — Dual specificity tyrosine-phosphorylation-regulated kinase 3，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小588 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 46 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43781
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143479-DYRK3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DYRK3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43781
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000143479-DYRK3/subcellular

![](https://images.proteinatlas.org/75041/1486_C4_1_red_green.jpg)
![](https://images.proteinatlas.org/75041/1486_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/75041/1534_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/75041/1534_A3_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43781-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
