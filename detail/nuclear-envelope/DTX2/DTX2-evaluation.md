---
type: protein-evaluation
gene: "DTX2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DTX2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DTX2 / KIAA1528, RNF58 |
| 蛋白名称 | Probable E3 ubiquitin-protein ligase DTX2 |
| 蛋白大小 | 622 aa / 67.2 kDa |
| UniProt ID | Q86UW9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear membrane; 额外: Vesicles, Plasma membrane; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 622 aa / 67.2 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=46 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=71.8; PDB: 6IR0, 6Y22, 6Y2X, 6Y3J |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039396, IPR039399, IPR039398, IPR018123, IPR004 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.5/180** | |
| **归一化总分** | | | **66.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear membrane; 额外: Vesicles, Plasma membrane, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nuclear membrane (GO:0031965)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 46 |
| PubMed broad count | 172 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1528, RNF58 |

**关键文献**:
1. DTX2 attenuates Lenvatinib-induced ferroptosis by suppressing docosahexaenoic acid biosynthesis through HSD17B4-dependent peroxisomal β-oxidation in hepatocellular carcinoma.. *Drug resistance updates : reviews and commentaries in antimicrobial and anticancer chemotherapy*. PMID: 40058099
2. Targeting DTX2/UFD1-mediated FTO degradation to regulate antitumor immunity.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 39661064
3. Ubiquitylation of nucleic acids by DELTEX ubiquitin E3 ligase DTX3L.. *EMBO reports*. PMID: 39242775
4. Targeting Deltex E3 Ubiquitin Ligase 2 Inhibits Tumor-associated Neutrophils and Sensitizes Hepatocellular Carcinoma Cells to Immunotherapy.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39733452
5. DTX2 promotes glioma development via regulation of HLTF.. *Biology direct*. PMID: 38163902

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.8 |
| 高置信度残基 (pLDDT>90) 占比 | 49.8% |
| 置信残基 (pLDDT 70-90) 占比 | 12.4% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 35.5% |
| 有序区域 (pLDDT>70) 占比 | 62.2% |
| 可用 PDB 条目 | 6IR0, 6Y22, 6Y2X, 6Y3J |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6IR0, 6Y22, 6Y2X, 6Y3J）+ AlphaFold高质量预测（pLDDT=71.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039396, IPR039399, IPR039398, IPR018123, IPR004170; Pfam: PF18102, PF02825 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RFX6 | 0.883 | 0.170 | — |
| NOTCH2 | 0.780 | 0.159 | — |
| NOTCH1 | 0.756 | 0.099 | — |
| SS18L1 | 0.746 | 0.000 | — |
| NOTCH3 | 0.745 | 0.159 | — |
| NOTCH4 | 0.734 | 0.071 | — |
| RFX3 | 0.733 | 0.049 | — |
| CCNK | 0.720 | 0.000 | — |
| ANK2 | 0.716 | 0.050 | — |
| ANK3 | 0.712 | 0.050 | — |

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
| 三维结构 | AlphaFold pLDDT=71.8 + PDB: 6IR0, 6Y22, 6Y2X, 6Y3J | pLDDT=71.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Nuclear membrane; 额外: Vesicles, Plasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DTX2 — Probable E3 ubiquitin-protein ligase DTX2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小622 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 46 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86UW9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000091073-DTX2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DTX2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86UW9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000091073-DTX2/subcellular

![](https://images.proteinatlas.org/42931/2268_H9_120_blue_red_green.jpg)
![](https://images.proteinatlas.org/42931/2268_H9_16_blue_red_green.jpg)
![](https://images.proteinatlas.org/42931/526_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/42931/526_H2_2_red_green.jpg)
![](https://images.proteinatlas.org/42931/528_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/42931/528_H2_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86UW9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86UW9 |
| SMART | SM00184;SM00678; |
| UniProt Domain [FT] | DOMAIN 8..97; /note="WWE 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00248"; DOMAIN 98..174; /note="WWE 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00248" |
| InterPro | IPR039396;IPR039399;IPR039398;IPR018123;IPR004170;IPR037197;IPR001841;IPR013083; |
| Pfam | PF18102;PF02825; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000091073-DTX2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARNT2 | Intact, Biogrid | true |
| HPCA | Intact, Biogrid, Bioplex | true |
| HPCAL1 | Intact, Biogrid | true |
| NCALD | Intact, Biogrid | true |
| RBPMS | Intact, Biogrid | true |
| RFX6 | Intact, Biogrid | true |
| SPG21 | Intact, Biogrid | true |
| UBE2D1 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
