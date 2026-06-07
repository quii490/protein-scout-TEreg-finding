---
type: protein-evaluation
gene: "Alyref"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## Alyref — REJECTED (研究热度过高 (PubMed strict=159，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Alyref / ALY, BEF, THOC4 |
| 蛋白名称 | THO complex subunit 4 |
| 蛋白大小 | 257 aa / 26.9 kDa |
| UniProt ID | Q86V81 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear speckles; UniProt: Nucleus; Nucleus speckle; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 257 aa / 26.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=159 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.1; PDB: 3ULH, 7ZNJ, 7ZNK, 8R7L |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051229, IPR025715, IPR012677, IPR035979, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear speckles | Approved |
| UniProt | Nucleus; Nucleus speckle; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- catalytic step 2 spliceosome (GO:0071013)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- membrane (GO:0016020)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 159 |
| PubMed broad count | 276 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ALY, BEF, THOC4 |

**关键文献**:
1. MicroRNA sequence codes for small extracellular vesicle release and cellular retention.. *Nature*. PMID: 34937935
2. NSUN6-mediated 5-methylcytosine modification of NDRG1 mRNA promotes radioresistance in cervical cancer.. *Molecular cancer*. PMID: 38970106
3. HnRNPA2B1 ISGylation Regulates m6A-Tagged mRNA Selective Export via ALYREF/NXF1 Complex to Foster Breast Cancer Development.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 38626369
4. Rare and de novo variants in 827 congenital diaphragmatic hernia probands implicate LONP1 as candidate risk gene.. *American journal of human genetics*. PMID: 34547244
5. Aberrant CircTMEM45A Facilitates Inflammatory Progression of Esophageal Squamous Cell Carcinoma through m5C-Mediated NLRP3 Activation.. *Cancer research*. PMID: 40215175

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.1 |
| 高置信度残基 (pLDDT>90) 占比 | 23.3% |
| 置信残基 (pLDDT 70-90) 占比 | 17.9% |
| 中等置信 (pLDDT 50-70) 占比 | 19.5% |
| 低置信 (pLDDT<50) 占比 | 39.3% |
| 有序区域 (pLDDT>70) 占比 | 41.2% |
| 可用 PDB 条目 | 3ULH, 7ZNJ, 7ZNK, 8R7L |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.1），有序残基占 41.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051229, IPR025715, IPR012677, IPR035979, IPR000504; Pfam: PF13865, PF00076 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| THOC1 | 0.999 | 0.831 | — |
| DDX39B | 0.999 | 0.979 | — |
| EIF4A3 | 0.999 | 0.995 | — |
| THOC3 | 0.999 | 0.781 | — |
| THOC2 | 0.999 | 0.932 | — |
| SARNP | 0.999 | 0.332 | — |
| NXF1 | 0.999 | 0.996 | — |
| UPF3A | 0.998 | 0.994 | — |
| NCBP1 | 0.998 | 0.829 | — |
| UPF1 | 0.998 | 0.994 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Ref1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:37061542|imex:IM-28761 |
| Or45a | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ALY2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| Eip63E | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| NetB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| kuz | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| BNIP3 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Dmel\CG6583 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| CG10984-RB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| Usp10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.1 + PDB: 3ULH, 7ZNJ, 7ZNK, 8R7L | pLDDT=64.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus speckle; Cytoplasm / Nucleoplasm, Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. Alyref — THO complex subunit 4，研究基础较多，新颖性有限。
2. 蛋白大小257 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 159 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=64.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 159 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86V81
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183684-ALYREF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Alyref
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86V81
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000183684-ALYREF/subcellular

![](https://images.proteinatlas.org/19799/183_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/19799/183_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/19799/185_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/19799/185_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/19799/242_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/19799/242_H9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86V81-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86V81 |
| SMART | SM01218;SM00360; |
| UniProt Domain [FT] | DOMAIN 106..182; /note="RRM"; /evidence="ECO:0000269\|PubMed:37020021" |
| InterPro | IPR051229;IPR025715;IPR012677;IPR035979;IPR000504; |
| Pfam | PF13865;PF00076; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000183684-ALYREF/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DDX39B | Biogrid, Opencell | true |
| RBM39 | Biogrid, Opencell | true |
| RBM8A | Biogrid, Opencell | true |
| UPF1 | Biogrid, Opencell | true |
| AKT1 | Biogrid | false |
| ATG13 | Opencell | false |
| BAG1 | Biogrid | false |
| BAP1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
