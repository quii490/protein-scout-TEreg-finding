---
type: protein-evaluation
gene: "LMNB1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## LMNB1 — REJECTED (研究热度过高 (PubMed strict=215，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LMNB1 / LMN2, LMNB |
| 蛋白名称 | Lamin-B1 |
| 蛋白大小 | 586 aa / 66.4 kDa |
| UniProt ID | P20700 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane; UniProt: Nucleus lamina |
| 蛋白大小 | 10/10 | ×1 | 10 | 586 aa / 66.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=215 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=82.4; PDB: 2KPW, 3JT0, 3TYY, 3UMN, 5BNW, 5VVX, 7DTG |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR018039, IPR039008, IPR001322, IPR036415; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane | Supported |
| UniProt | Nucleus lamina | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- lamin filament (GO:0005638)
- membrane (GO:0016020)
- nuclear envelope (GO:0005635)
- nuclear inner membrane (GO:0005637)
- nuclear lamina (GO:0005652)
- nuclear matrix (GO:0016363)
- nuclear membrane (GO:0031965)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 215 |
| PubMed broad count | 295 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LMN2, LMNB |

**关键文献**:
1. Organelle-specific autophagy in inflammatory diseases: a potential therapeutic target underlying the quality control of multiple organelles.. *Autophagy*. PMID: 32048886
2. Unmasking Transcriptional Heterogeneity in Senescent Cells.. *Current biology : CB*. PMID: 28844647
3. Mitochondrial depolarization after acute ethanol treatment drives mitophagy in living mice.. *Autophagy*. PMID: 35293288
4. Autophagic degradation of SQSTM1 enables fibroblast activation to accelerate wound healing.. *Autophagy*. PMID: 40400126
5. Structural Variants at the LMNB1 Locus: Deciphering Pathomechanisms in Autosomal Dominant Adult-Onset Demyelinating Leukodystrophy.. *Annals of neurology*. PMID: 39078102

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.4 |
| 高置信度残基 (pLDDT>90) 占比 | 66.4% |
| 置信残基 (pLDDT 70-90) 占比 | 11.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.8% |
| 低置信 (pLDDT<50) 占比 | 18.1% |
| 有序区域 (pLDDT>70) 占比 | 78.2% |
| 可用 PDB 条目 | 2KPW, 3JT0, 3TYY, 3UMN, 5BNW, 5VVX, 7DTG |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2KPW, 3JT0, 3TYY, 3UMN, 5BNW, 5VVX, 7DTG）+ AlphaFold极高置信度预测（pLDDT=82.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018039, IPR039008, IPR001322, IPR036415; Pfam: PF00038, PF00932 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LMNB2 | 0.999 | 0.829 | — |
| LBR | 0.999 | 0.335 | — |
| LMNA | 0.996 | 0.921 | — |
| EMD | 0.994 | 0.341 | — |
| SUN1 | 0.982 | 0.221 | — |
| TMPO | 0.981 | 0.635 | — |
| SYNE2 | 0.963 | 0.070 | — |
| SUN2 | 0.957 | 0.213 | — |
| SYNE1 | 0.956 | 0.070 | — |
| CASP6 | 0.944 | 0.102 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Plcb2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| - | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:14968112 |
| ATG12 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| BCAR3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| RTCA | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ATF4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| GIT2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| LMNA | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| MBIP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.4 + PDB: 2KPW, 3JT0, 3TYY, 3UMN, 5BNW,  | pLDDT=82.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus lamina / Nuclear membrane | 一致 |
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
1. LMNB1 — Lamin-B1，研究基础较多，新颖性有限。
2. 蛋白大小586 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 215 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 215 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P20700
- Protein Atlas: https://www.proteinatlas.org/ENSG00000113368-LMNB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LMNB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P20700
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000113368-LMNB1/subcellular

![](https://images.proteinatlas.org/50524/711_D6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/50524/711_D6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/50524/723_D6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/50524/723_D6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/50524/866_D6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/50524/866_D6_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P20700-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P20700 |
| SMART | SM01391; |
| UniProt Domain [FT] | DOMAIN 32..388; /note="IF rod"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01188"; DOMAIN 430..546; /note="LTD"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01187" |
| InterPro | IPR018039;IPR039008;IPR001322;IPR036415; |
| Pfam | PF00038;PF00932; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000113368-LMNB1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DDX21 | Biogrid, Opencell | true |
| DDX50 | Biogrid, Opencell | true |
| FAM169A | Intact, Biogrid | true |
| KPNA1 | Intact, Biogrid, Opencell | true |
| KPNA6 | Intact, Biogrid, Opencell | true |
| LBR | Biogrid, Opencell | true |
| LMNA | Intact, Biogrid, Opencell, Bioplex | true |
| LMNB2 | Intact, Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
