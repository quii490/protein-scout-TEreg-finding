---
type: protein-evaluation
gene: "FOXO1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FOXO1 — REJECTED (研究热度过高 (PubMed strict=4764，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOXO1 / FKHR, FOXO1A |
| 蛋白名称 | Forkhead box protein O1 |
| 蛋白大小 | 655 aa / 69.7 kDa |
| UniProt ID | Q12778 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 655 aa / 69.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=4764 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=51.0; PDB: 3CO6, 3CO7, 3COA, 4LG0, 5DUI, 6LBI, 6QVW |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR047408, IPR001766, IPR032067, IPR032068, IPR030 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4764 |
| PubMed broad count | 8322 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FKHR, FOXO1A |

**关键文献**:
1. FOXO1 reshapes neutrophils to aggravate acute brain damage and promote late depression after traumatic brain injury.. *Military Medical Research*. PMID: 38556884
2. FOXO regulation of TXNIP induces ferroptosis in satellite cells by inhibiting glutathione metabolism, promoting Sarcopenia.. *Cellular and molecular life sciences : CMLS*. PMID: 39982519
3. Inhibitory Regulation of FOXO1 in PPARδ Expression Drives Mitochondrial Dysfunction and Insulin Resistance.. *Diabetes*. PMID: 38656552
4. SIRT1-FOXO1 Signaling in Cancer.. *Journal of biochemical and molecular toxicology*. PMID: 41082310
5. Fusion transcription factor dosage controls cell state in rhabdomyosarcoma.. *bioRxiv : the preprint server for biology*. PMID: 40475567

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 51.0 |
| 高置信度残基 (pLDDT>90) 占比 | 9.8% |
| 置信残基 (pLDDT 70-90) 占比 | 4.1% |
| 中等置信 (pLDDT 50-70) 占比 | 18.2% |
| 低置信 (pLDDT<50) 占比 | 67.9% |
| 有序区域 (pLDDT>70) 占比 | 13.9% |
| 可用 PDB 条目 | 3CO6, 3CO7, 3COA, 4LG0, 5DUI, 6LBI, 6QVW, 6QZR, 6QZS, 8A62 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=51.0），有序残基占 13.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR047408, IPR001766, IPR032067, IPR032068, IPR030456; Pfam: PF00250, PF16676, PF16675 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SIRT1 | 0.999 | 0.816 | — |
| PPARGC1A | 0.999 | 0.067 | — |
| AKT1 | 0.999 | 0.881 | — |
| ATG7 | 0.998 | 0.739 | — |
| CREBBP | 0.993 | 0.810 | — |
| SMAD3 | 0.990 | 0.317 | — |
| AKT2 | 0.986 | 0.312 | — |
| CTNNB1 | 0.985 | 0.113 | — |
| SFN | 0.984 | 0.938 | — |
| EP300 | 0.984 | 0.809 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Fcor | psi-mi:"MI:0018"(two hybrid) | pubmed:22510882|imex:IM-17324 |
| ENSMUSP00000055308.6 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:23467085|imex:IM-24357 |
| ESR1 | psi-mi:"MI:0018"(two hybrid) | pubmed:11353774|imex:IM-19370 |
| CDK1 | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-14935|pubmed:18408765 |
| CCNB1 | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-14935|pubmed:18408765 |
| EBI-1767788 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-14935|pubmed:18408765 |
| AR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17202144|imex:IM-19808 |
| Hdac4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21565616|imex:IM-15737 |
| Foxo3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22510882|imex:IM-17324 |
| EP300 | psi-mi:"MI:0889"(acetylase assay) | pubmed:22510882|imex:IM-17324 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=51.0 + PDB: 3CO6, 3CO7, 3COA, 4LG0, 5DUI,  | pLDDT=51.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. FOXO1 — Forkhead box protein O1，研究基础较多，新颖性有限。
2. 蛋白大小655 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4764 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=51.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 4764 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q12778
- Protein Atlas: https://www.proteinatlas.org/ENSG00000150907-FOXO1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FOXO1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q12778
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000150907-FOXO1/subcellular

![](https://images.proteinatlas.org/22326/667_G1_4_red_green.jpg)
![](https://images.proteinatlas.org/22326/667_G1_6_red_green.jpg)
![](https://images.proteinatlas.org/22326/673_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/22326/673_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/22326/710_G1_3_red_green.jpg)
![](https://images.proteinatlas.org/22326/710_G1_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q12778-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q12778 |
| SMART | SM00339; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR047408;IPR001766;IPR032067;IPR032068;IPR030456;IPR036388;IPR036390; |
| Pfam | PF00250;PF16676;PF16675; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000150907-FOXO1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AKT1 | Intact, Biogrid | true |
| CDK1 | Intact, Biogrid | true |
| CREBBP | Intact, Biogrid | true |
| ESR1 | Intact, Biogrid | true |
| FHL2 | Intact, Biogrid | true |
| SIRT1 | Intact, Biogrid | true |
| YWHAB | Biogrid, Opencell | true |
| YWHAE | Intact, Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
