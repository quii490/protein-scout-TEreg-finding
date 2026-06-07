---
type: protein-evaluation
gene: "XRCC5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## XRCC5 — REJECTED (研究热度过高 (PubMed strict=217，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | XRCC5 / G22P2 |
| 蛋白名称 | DNA repair protein Ku80 |
| 蛋白大小 | 732 aa / 82.7 kDa |
| UniProt ID | P13010 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Nucleus, nucleolus; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 732 aa / 82.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=217 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=83.1; PDB: 1JEQ, 1JEY, 1Q2Z, 1RW2, 3RZ9, 5Y3R, 6ERF |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR006164, IPR024193, IPR005160, IPR036494, IPR005 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Nucleus, nucleolus; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- cytosol (GO:0005829)
- DNA-dependent protein kinase complex (GO:0070418)
- DNA-dependent protein kinase-DNA ligase 4 complex (GO:0005958)
- extracellular region (GO:0005576)
- Ku70:Ku80 complex (GO:0043564)
- membrane (GO:0016020)
- nonhomologous end joining complex (GO:0070419)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 217 |
| PubMed broad count | 1072 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: G22P2 |

**关键文献**:
1. TOP2B's contributions to transcription.. *Biochemical Society transactions*. PMID: 34747992
2. Lactylation Enhances the Activity of Lactate Dehydrogenase A and Promotes the Chemoresistance to Cisplatin Through Facilitating DNA Nonhomologous End Junction in Lung Adenocarcinoma.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 41190808
3. XRCC5 downregulated by TRIM25 is susceptible for lens epithelial cell apoptosis.. *Cellular signalling*. PMID: 35331835
4. Association between XRCC5, 6 and 7 gene polymorphisms and the risk of breast cancer: a HuGE review and meta-analysis.. *Asian Pacific journal of cancer prevention : APJCP*. PMID: 23098447
5. Xrcc5/KU80 is not required for the survival or activation of prophase-arrested oocytes in primordial follicles.. *Frontiers in endocrinology*. PMID: 37900135

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.1 |
| 高置信度残基 (pLDDT>90) 占比 | 57.0% |
| 置信残基 (pLDDT 70-90) 占比 | 26.8% |
| 中等置信 (pLDDT 50-70) 占比 | 6.1% |
| 低置信 (pLDDT<50) 占比 | 10.1% |
| 有序区域 (pLDDT>70) 占比 | 83.8% |
| 可用 PDB 条目 | 1JEQ, 1JEY, 1Q2Z, 1RW2, 3RZ9, 5Y3R, 6ERF, 6ERG, 6ERH, 6ZH6 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1JEQ, 1JEY, 1Q2Z, 1RW2, 3RZ9, 5Y3R, 6ERF, 6ERG, 6ERH, 6ZH6）+ AlphaFold极高置信度预测（pLDDT=83.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006164, IPR024193, IPR005160, IPR036494, IPR005161; Pfam: PF02735, PF03730, PF03731 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LIG4 | 0.999 | 0.974 | — |
| XRCC4 | 0.999 | 0.897 | — |
| PRKDC | 0.999 | 0.991 | — |
| NHEJ1 | 0.999 | 0.979 | — |
| APLF | 0.999 | 0.982 | — |
| XRCC6 | 0.999 | 0.999 | — |
| ATM | 0.998 | 0.587 | — |
| DCLRE1C | 0.998 | 0.942 | — |
| PAXX | 0.997 | 0.510 | — |
| PARP1 | 0.996 | 0.879 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| WRN | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:11328876 |
| NFKB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| PARP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14734561 |
| TERF2IP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15383534 |
| CDH1 | psi-mi:"MI:0107"(surface plasmon resonance) | pubmed:16212417 |
| CDC16 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| HDGF | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21907836|imex:IM-17230 |
| Q81VA8 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| GABARAPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.1 + PDB: 1JEQ, 1JEY, 1Q2Z, 1RW2, 3RZ9,  | pLDDT=83.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus; Chromosome / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. XRCC5 — DNA repair protein Ku80，研究基础较多，新颖性有限。
2. 蛋白大小732 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 217 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 217 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P13010
- Protein Atlas: https://www.proteinatlas.org/ENSG00000079246-XRCC5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=XRCC5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P13010
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000079246-XRCC5/subcellular

![](https://images.proteinatlas.org/25813/258_F3_1_red_green.jpg)
![](https://images.proteinatlas.org/25813/258_F3_2_red_green.jpg)
![](https://images.proteinatlas.org/25813/259_F3_1_red_green.jpg)
![](https://images.proteinatlas.org/25813/259_F3_2_red_green.jpg)
![](https://images.proteinatlas.org/25813/260_F3_1_red_green.jpg)
![](https://images.proteinatlas.org/25813/260_F3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P13010-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P13010 |
| SMART | SM00559;SM00327; |
| UniProt Domain [FT] | DOMAIN 9..231; /note="VWFA"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00219"; DOMAIN 253..452; /note="Ku"; /evidence="ECO:0000255" |
| InterPro | IPR006164;IPR024193;IPR005160;IPR036494;IPR005161;IPR014893;IPR016194;IPR002035;IPR036465; |
| Pfam | PF02735;PF03730;PF03731;PF08785; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000079246-XRCC5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| APLF | Intact, Biogrid | true |
| COIL | Intact, Biogrid | true |
| HOXB7 | Intact, Biogrid | true |
| HSPB1 | Intact, Biogrid | true |
| NHEJ1 | Intact, Biogrid | true |
| PARP1 | Intact, Biogrid, Opencell | true |
| PPM1G | Intact, Biogrid, Opencell | true |
| PRKDC | Intact, Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
