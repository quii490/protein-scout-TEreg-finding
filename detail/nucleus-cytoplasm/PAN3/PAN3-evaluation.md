---
type: protein-evaluation
gene: "PAN3"
date: 2026-06-02
tags: [protein-scout, nucleus-cytoplasm, evaluation]
status: scored
---

## PAN3 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PAN3 |
| 蛋白全名 | PAN2-PAN3 deadenylation complex subunit PAN3 |
| 蛋白大小 | 887 aa / 95.6 kDa |
| UniProt ID | Q58A45 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | Cytoplasm + P-body + Nucleus (ECO:0000269); GO nucleus IEA |
| 蛋白大小 | 8/10 | ×1 | 8.0 | 887 aa, 95.6 kDa, 尚可接受 |
| 研究新颖性 | 6/10 | ×5 | 30.0 | PubMed strict=60, symbol_only=84, broad=94 |
| 三维结构 | 6/10 | ×3 | 18.0 | 0 PDB; AF pLDDT=62.7, 44.3% <50 |
| 调控结构域 | 7/10 | ×2 | 14.0 | 7 domains (6 InterPro + 1 Pfam): ZnF_C3H1, kinase-like |
| PPI 网络 | 4/10 | ×3 | 12.0 | IntAct 15 + STRING 15 + UniProt 5; PAN complex, PABP, TNRC6 |
| **加权总分** | | | **98/180**** | |
| 互证加分 | | | +0.5 | 多库结构域一致(+0.5) |
| **归一化总分 (÷1.83)** | | | **53.6/100**** | |


### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Cytoplasm, P-body (ECO:0000255/ECO:0000269); Cytoplasm; Nucleus (ECO:0000269); Cytoplasm (ECO:0000269) | 实验证据 |
| GO-CC | cytosol TAS; nucleus IEA; P-body IBA; PAN complex IDA | 实验+预测 |
| Protein Atlas (IF) | HPA 有图像但 no_image_detected, IF 缩略图未获取 | 未确认 |

**HPA IF 状态**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。 — HPA 有 IHC 和 RNA 数据，IF 图像未可靠获取。核定位基于 UniProt 实验证据。

**结论**: 细胞质为主 (P-body enriched)，Nucleus 有 ECO:0000269 实验证据支持。

#### 3.2 结构与结构域

| 指标 | 数值 |
|---|---|
| AlphaFold | AF-Q58A45-F1 (v6) |
| 平均 pLDDT | 62.7 |
| pLDDT >90 / 70-90 / 50-70 / <50 | 30.6% / 17.7% / 7.4% / 44.3% |
| PDB | 0 |

| 来源 | 结构域 |
|---|---|
| InterPro | IPR011009 (Kinase-like_dom_sf), IPR030844 (PAN3), IPR041332 (Pan3_CK), IPR000719 (Prot_kinase_dom), IPR000571 (Znf_CCCH), IPR036855 (Znf_CCCH_sf) |
| Pfam | PF18101 (Pan3_CK) |

**评价**: AF pLDDT 62.7，整体结构预测置信度偏低。44.3% 残基 pLDDT <50，说明有大量无序区域。ZnF_C3H1 (CCCH-type zinc finger) 可能参与 RNA binding。Kinase-like domain 存在但可能无激酶活性。无实验结构(PBD=0)。

#### 3.3 研究现状

| 指标 | 数值 |
|---|---|
| PubMed strict | 60 |
| PubMed symbol_only | 84 |
| PubMed broad | 94 |

**关键文献**:
1. Passmore LA & Coller J (2022). "Roles of mRNA poly(A) tails in regulation of eukaryotic gene expression." *Nat Rev Mol Cell Biol*. PMID: 34594027
2. Wolf J & Passmore LA (2014). "mRNA deadenylation by Pan2-Pan3." *Biochem Soc Trans*. PMID: 24450649
3. Davis K et al. (2023). "Emerging molecular subtypes and therapies in acute lymphoblastic leukemia." *Semin Diagn Pathol*. PMID: 37120350
4. Kimura S et al. (2022). "Enhancer retargeting of CDX2 and UBTF::ATXN7L3 define a subtype of high-risk B-progenitor acute lymphoblastic leukemia." *Blood*. PMID: 35192684
5. Jiang T et al. (2021). "Development of small-molecule tropomyosin receptor kinase (TRK) inhibitors for NTRK fusion cancers." *Acta Pharm Sin B*. PMID: 33643817

**评价**: 文献以 mRNA deadenylation/PAN complex 为主，部分癌症相关文献中作为背景基因出现。60篇严格命中，研究热度中等。

#### 3.4 PPI 网络

**UniProt 实验互作**:

| Partner | Experiments | Relevance |
|---|---|---|
| PAN2 | 7 | PAN complex catalytic subunit |
| PABPC1 | 4 | Poly(A) binding, mRNA regulation |
| TNRC6A | 2 | miRNA pathway (GW182 family) |
| TNRC6B | 4 | miRNA pathway (GW182 family) |
| TNRC6C | 4 | miRNA pathway (GW182 family) |

**STRING 预测互作** (score >0.4):

| Partner | Score | Experimental | Relevance |
|---|---|---|---|
| PAN2 | 0.999 | 0.990 | PAN complex |
| PABPC1 | 0.960 | 0.899 | mRNA poly(A) |
| TNRC6C | 0.801 | 0.715 | miRNA |
| NIPBL | 0.710 | 0.071 | Cohesin loader, chromatin |

**已知复合体**: PAN complex (GO:0031251, IDA) with PAN2

**评价**: PPI 核心为 PAN2-PABPC1-TNRC6 家族，明确与 mRNA deadenylation 和 miRNA-mediated decay 相关。NIPBL (cohesin loader) 互作暗示与染色质调控的潜在联系。调控相关性中等。

#### 3.5 多库互证

| 维度 | 来源 | 结果 | 一致性 |
|---|---|---|---|
| 三维结构 | AlphaFold + PDB | 0 PDB, AF only | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 7 个 | 多库一致 |
| PPI 网络 | STRING + IntAct + UniProt | PAN2 多源确认 | 一致 |
| 核定位 | HPA/UniProt/GO | Nucleus + Cytoplasm | 部分一致 |

**互证加分明细**: 多库结构域一致(+0.5), 总计 +0.5

### 4. 总体评价

PAN3 是 PAN deadenylation complex 的调控亚基，负责招募 PAN2 催化亚基至 mRNA。含 CCCH-type zinc finger (RNA binding) 和 kinase-like domain。核定位有实验证据但以胞质 P-body 为主。AF结构预测置信度偏低(62.7)，存在大量无序区域。PPI 网络以 PAN2-PABPC1-TNRC6 为核心，NIPBL 互作提供有限染色质调控链接。研究热度中等，新颖性尚可。

**推荐**: 中等优先级。PAN2/PAN3 复合体功能明确但染色质调控关联有限。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprot/Q58A45
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q58A45
- PDB: None
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PAN3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000152520-PAN3 (HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。)

**HPA IF 状态**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。 — HPA 暂无 IF 原图数据。核定位基于 UniProt + GO-CC。



#### PPI 网络
| Partner | Source | Score/Evidence |
|---|---|---|
| PAN2 | STRING | 0.999 |
| PABPC1 | STRING | 0.96 |
| TNRC6C | STRING | 0.801 |
| NIPBL | STRING | 0.71 |
| PABPC4 | STRING | 0.67 |
| plu | IntAct | psi-mi:"MI:0018"(two hybrid) |
| CycJ | IntAct | psi-mi:"MI:0018"(two hybrid) |
| CycD | IntAct | psi-mi:"MI:0018"(two hybrid) |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q58A45-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q58A45 |
| SMART | SM00356; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011009;IPR030844;IPR041332;IPR000719;IPR000571;IPR036855; |
| Pfam | PF18101; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000152520-PAN3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PABPC1 | Intact, Biogrid | true |
| PAN2 | Intact, Biogrid | true |
| TNRC6A | Intact, Biogrid | true |
| TNRC6B | Intact, Biogrid | true |
| TNRC6C | Intact, Biogrid | true |
| ASF1A | Biogrid | false |
| DDX6 | Opencell | false |
| GSPT1 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
