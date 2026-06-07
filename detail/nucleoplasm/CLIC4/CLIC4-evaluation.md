---
type: protein-evaluation
gene: "CLIC4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLIC4 — REJECTED (研究热度过高 (PubMed strict=135，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLIC4 |
| 蛋白名称 | Chloride intracellular channel protein 4 |
| 蛋白大小 | 253 aa / 28.8 kDa |
| UniProt ID | Q9Y696 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Centrosome; 额外: Calyx, Connecting piece, Pr; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 10/10 | ×1 | 10 | 253 aa / 28.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=135 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=91.7; PDB: 2AHE, 2D2Z, 3OQS |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002946, IPR053823, IPR010987, IPR036282, IPR040 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.0/180** | |
| **归一化总分** | | | **51.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Centrosome; 额外: Calyx, Connecting piece, Principal piece | Supported |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasmic vesicle membrane; Nu... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- apical part of cell (GO:0045177)
- cell surface (GO:0009986)
- cell-cell junction (GO:0005911)
- centrosome (GO:0005813)
- chloride channel complex (GO:0034707)
- cytoplasm (GO:0005737)
- cytoplasmic vesicle membrane (GO:0030659)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 135 |
| PubMed broad count | 213 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. CLIC4/Arf6 Pathway.. *Circulation research*. PMID: 30582444
2. CLIC4 and Schnurri-2: a dynamic duo in TGF-beta signaling with broader implications in cellular homeostasis and disease.. *Nucleus (Austin, Tex.)*. PMID: 20617112
3. Retraction.. *Journal of cellular biochemistry*. PMID: 34191361
4. Oxidative modification of G-quadruplex triggers CLIC4-associated mitochondrial dysfunction to promote glioblastoma progression.. *Redox biology*. PMID: 41265251
5. CLIC4, skin homeostasis and cutaneous cancer: surprising connections.. *Molecular carcinogenesis*. PMID: 17443730

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.7 |
| 高置信度残基 (pLDDT>90) 占比 | 79.4% |
| 置信残基 (pLDDT 70-90) 占比 | 14.6% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 4.0% |
| 有序区域 (pLDDT>70) 占比 | 94.0% |
| 可用 PDB 条目 | 2AHE, 2D2Z, 3OQS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2AHE, 2D2Z, 3OQS）+ AlphaFold高质量预测（pLDDT=91.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002946, IPR053823, IPR010987, IPR036282, IPR040079; Pfam: PF22441 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HIVEP2 | 0.897 | 0.047 | — |
| TPRN | 0.871 | 0.841 | — |
| CLIC5 | 0.857 | 0.837 | — |
| CLIC2 | 0.853 | 0.838 | — |
| CLIC6 | 0.801 | 0.768 | — |
| HRH3 | 0.770 | 0.000 | — |
| PPM1A | 0.751 | 0.000 | — |
| EZR | 0.739 | 0.185 | — |
| SMAD3 | 0.711 | 0.000 | — |
| CLCN4 | 0.683 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Pip5k1b | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HSP90AB1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| REL | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| EBI-6390790 | psi-mi:"MI:1219"(enzyme-mediated activation of rad | pubmed:22936677|imex:IM-18006 |
| GATD3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| TPRN | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CLIC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ICAM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CLIC6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.7 + PDB: 2AHE, 2D2Z, 3OQS | pLDDT=91.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Plasma membrane, Centrosome; 额外: Calyx, Connecting | 一致 |
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
1. CLIC4 — Chloride intracellular channel protein 4，研究基础较多，新颖性有限。
2. 蛋白大小253 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 135 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 135 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y696
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169504-CLIC4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLIC4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y696
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000169504-CLIC4/subcellular

![](https://images.proteinatlas.org/60804/1979_F12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/60804/1979_F12_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/60804/2057_C11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/60804/2057_C11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/60804/2063_E10_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/60804/2063_E10_7_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y696-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y696 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 81..244; /note="GST C-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00685" |
| InterPro | IPR002946;IPR053823;IPR010987;IPR036282;IPR040079;IPR036249; |
| Pfam | PF22441; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000169504-CLIC4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CLIC6 | Intact, Biogrid | true |
| CSK | Biogrid | false |
| MYC | Biogrid | false |
| SAR1B | Opencell | false |
| TPRN | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
