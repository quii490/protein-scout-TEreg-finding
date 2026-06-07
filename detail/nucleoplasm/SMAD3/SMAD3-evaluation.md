---
type: protein-evaluation
gene: "SMAD3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SMAD3 — REJECTED (研究热度过高 (PubMed strict=5576，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SMAD3 / MADH3 |
| 蛋白名称 | SMAD family member 3 |
| 蛋白大小 | 425 aa / 48.1 kDa |
| UniProt ID | P84022 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles, Primary cilium transition zone, B; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 425 aa / 48.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=5576 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=83.6; PDB: 1MHD, 1MJS, 1MK2, 1OZJ, 1U7F, 2LAJ, 2LB2 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR013790, IPR003619, IPR013019, IPR017855, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Primary cilium transition zone, Basal body | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- ciliary basal body (GO:0036064)
- ciliary transition zone (GO:0035869)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- heteromeric SMAD protein complex (GO:0071144)
- nuclear inner membrane (GO:0005637)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5576 |
| PubMed broad count | 10765 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MADH3 |

**关键文献**:
1. Btg2 Promotes Focal Segmental Glomerulosclerosis via Smad3-Dependent Podocyte-Mesenchymal Transition.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 37749872
2. Smad3 Mediates Renal Fibrosis via GPX4-Dependent Ferroptosis.. *International journal of biological sciences*. PMID: 41079940
3. C-reactive protein promotes diabetic kidney disease via Smad3-mediated NLRP3 inflammasome activation.. *Molecular therapy : the journal of the American Society of Gene Therapy*. PMID: 39539016
4. Fibroblast-specific PRMT5 deficiency suppresses cardiac fibrosis and left ventricular dysfunction in male mice.. *Nature communications*. PMID: 38503742
5. Biochanin A suppresses Klf6-mediated Smad3 transcription to attenuate renal fibrosis in UUO mice.. *Phytomedicine : international journal of phytotherapy and phytopharmacology*. PMID: 39326137

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.6 |
| 高置信度残基 (pLDDT>90) 占比 | 65.9% |
| 置信残基 (pLDDT 70-90) 占比 | 13.9% |
| 中等置信 (pLDDT 50-70) 占比 | 3.1% |
| 低置信 (pLDDT<50) 占比 | 17.2% |
| 有序区域 (pLDDT>70) 占比 | 79.8% |
| 可用 PDB 条目 | 1MHD, 1MJS, 1MK2, 1OZJ, 1U7F, 2LAJ, 2LB2, 5OD6, 5ODG, 5XOC |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1MHD, 1MJS, 1MK2, 1OZJ, 1U7F, 2LAJ, 2LB2, 5OD6, 5ODG, 5XOC）+ AlphaFold极高置信度预测（pLDDT=83.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013790, IPR003619, IPR013019, IPR017855, IPR001132; Pfam: PF03165, PF03166 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NEDD4L | 0.999 | 0.978 | — |
| EP300 | 0.999 | 0.926 | — |
| SMAD4 | 0.999 | 0.999 | — |
| ZFYVE9 | 0.999 | 0.984 | — |
| SMAD2 | 0.999 | 0.911 | — |
| E2F4 | 0.999 | 0.292 | — |
| TGFBR1 | 0.999 | 0.658 | — |
| CTNNB1 | 0.999 | 0.768 | — |
| SKIL | 0.998 | 0.898 | — |
| FOXH1 | 0.998 | 0.639 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SMAD2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.6 + PDB: 1MHD, 1MJS, 1MK2, 1OZJ, 1U7F,  | pLDDT=83.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Vesicles, Primary cilium transiti | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

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
1. SMAD3 — SMAD family member 3，研究基础较多，新颖性有限。
2. 蛋白大小425 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5576 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 5576 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P84022
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166949-SMAD3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SMAD3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P84022
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000166949-SMAD3/subcellular

![](https://images.proteinatlas.org/46386/2266_G7_111_blue_red_green.jpg)
![](https://images.proteinatlas.org/46386/2266_G7_15_blue_red_green.jpg)
![](https://images.proteinatlas.org/46386/2133_F6_16_red_green.jpg)
![](https://images.proteinatlas.org/46386/2133_F6_58_red_green.jpg)
![](https://images.proteinatlas.org/46386/2160_F11_31_red_green.jpg)
![](https://images.proteinatlas.org/46386/2160_F11_42_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P84022-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P84022 |
| SMART | SM00523;SM00524; |
| UniProt Domain [FT] | DOMAIN 10..136; /note="MH1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00438"; DOMAIN 232..425; /note="MH2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00439" |
| InterPro | IPR013790;IPR003619;IPR013019;IPR017855;IPR001132;IPR008984;IPR036578; |
| Pfam | PF03165;PF03166; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000166949-SMAD3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| APP | Intact, Biogrid | true |
| CHRD | Intact, Biogrid | true |
| DAB2 | Intact, Biogrid | true |
| DOCK9 | Intact, Biogrid | true |
| EPAS1 | Intact, Biogrid | true |
| FOXH1 | Intact, Biogrid | true |
| FOXO3 | Intact, Biogrid | true |
| HIF1A | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
