---
type: protein-evaluation
gene: "APEX1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## APEX1 — REJECTED (研究热度过高 (PubMed strict=249，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | APEX1 / APE, APE1, APEX, APX, HAP1 |
| 蛋白名称 | DNA repair nuclease/redox regulator APEX1 |
| 蛋白大小 | 318 aa / 35.6 kDa |
| UniProt ID | P27695 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Centrosome; UniProt: Nucleus; Nucleus, nucleolus; Nucleus speckle; Endoplasmic re |
| 蛋白大小 | 10/10 | ×1 | 10 | 318 aa / 35.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=249 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=90.5; PDB: 1BIX, 1CQG, 1CQH, 1DE8, 1DE9, 1DEW, 1E9N |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR004808, IPR020847, IPR020848, IPR036691, IPR005 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **95.5/180** | |
| **归一化总分** | | | **53.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Centrosome | Supported |
| UniProt | Nucleus; Nucleus, nucleolus; Nucleus speckle; Endoplasmic reticulum; Cytoplasm; Mitochondrion | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- chromosome, telomeric region (GO:0000781)
- cytoplasm (GO:0005737)
- endoplasmic reticulum (GO:0005783)
- mitochondrion (GO:0005739)
- nuclear speck (GO:0016607)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 249 |
| PubMed broad count | 1709 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: APE, APE1, APEX, APX, HAP1, REF1 |

**关键文献**:
1. Nicotinamide mononucleotide supplementation improves oocyte developmental competence in different ovarian damage conditions.. *American journal of obstetrics and gynecology*. PMID: 39923879
2. APEX1 in intestinal epithelium triggers neutrophil infiltration and intestinal barrier damage in ulcerative colitis.. *Free radical biology & medicine*. PMID: 39389211
3. APEX1 gene amplification and its protein overexpression in osteosarcoma: correlation with recurrence, metastasis, and survival.. *Technology in cancer research & treatment*. PMID: 20218738
4. Air pollution-related immune gene prognostic signature for hepatocellular carcinoma: network toxicology, machine learning and multi-omics analysis.. *Frontiers in immunology*. PMID: 41019083
5. Association between the OGG1 Ser326Cys and APEX1 Asp148Glu polymorphisms and lung cancer risk: a meta-analysis.. *Molecular biology reports*. PMID: 23065211

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.5 |
| 高置信度残基 (pLDDT>90) 占比 | 84.0% |
| 置信残基 (pLDDT 70-90) 占比 | 3.1% |
| 中等置信 (pLDDT 50-70) 占比 | 1.6% |
| 低置信 (pLDDT<50) 占比 | 11.3% |
| 有序区域 (pLDDT>70) 占比 | 87.1% |
| 可用 PDB 条目 | 1BIX, 1CQG, 1CQH, 1DE8, 1DE9, 1DEW, 1E9N, 1HD7, 2ISI, 2O3H |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1BIX, 1CQG, 1CQH, 1DE8, 1DE9, 1DEW, 1E9N, 1HD7, 2ISI, 2O3H）+ AlphaFold极高置信度预测（pLDDT=90.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004808, IPR020847, IPR020848, IPR036691, IPR005135; Pfam: PF03372 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| XRCC1 | 0.999 | 0.480 | — |
| POLB | 0.998 | 0.510 | — |
| FEN1 | 0.998 | 0.310 | — |
| LIG1 | 0.996 | 0.143 | — |
| ANP32A | 0.996 | 0.292 | — |
| NTHL1 | 0.994 | 0.314 | — |
| OGG1 | 0.986 | 0.134 | — |
| TXN | 0.983 | 0.940 | — |
| NME1 | 0.982 | 0.000 | — |
| MUTYH | 0.975 | 0.647 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.5 + PDB: 1BIX, 1CQG, 1CQH, 1DE8, 1DE9,  | pLDDT=90.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus; Nucleus speckle; Endo / Nucleoplasm; 额外: Centrosome | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. APEX1 — DNA repair nuclease/redox regulator APEX1，研究基础较多，新颖性有限。
2. 蛋白大小318 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 249 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 249 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P27695
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100823-APEX1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=APEX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P27695
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000100823-APEX1/subcellular

![](https://images.proteinatlas.org/2564/17_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/2564/17_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/2564/18_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/2564/18_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/2564/19_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/2564/19_G2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P27695-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P27695 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR004808;IPR020847;IPR020848;IPR036691;IPR005135; |
| Pfam | PF03372; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000100823-APEX1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EP300 | Intact, Biogrid | true |
| SIRT1 | Intact, Biogrid | true |
| ACTN1 | Biogrid | false |
| APP | Biogrid | false |
| BAZ1A | Biogrid | false |
| BRCA1 | Biogrid | false |
| BRD3 | Biogrid | false |
| BTRC | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
