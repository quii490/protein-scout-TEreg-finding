---
type: protein-evaluation
gene: "WAPL"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## WAPL — REJECTED (研究热度过高 (PubMed strict=143，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WAPL / FOE, KIAA0261, WAPAL |
| 蛋白名称 | Wings apart-like protein homolog |
| 蛋白大小 | 1190 aa / 132.9 kDa |
| UniProt ID | Q7Z5K2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Nucleus; Chromosome; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 1190 aa / 132.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=143 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.0; PDB: 4K6J, 5HDT |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011989, IPR016024, IPR039874, IPR022771, IPR012 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.5/180** | |
| **归一化总分** | | | **43.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Nucleus; Chromosome; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromosome (GO:0005694)
- chromosome, centromeric region (GO:0000775)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- intercellular bridge (GO:0045171)
- mitotic spindle (GO:0072686)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 143 |
| PubMed broad count | 242 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FOE, KIAA0261, WAPAL |

**关键文献**:
1. The expanding phenotypes of cohesinopathies: one ring to rule them all!. *Cell cycle (Georgetown, Tex.)*. PMID: 31516082
2. Topologically associating domains and chromatin loops depend on cohesin and are regulated by CTCF, WAPL, and PDS5 proteins.. *The EMBO journal*. PMID: 29217591
3. Sister chromatid cohesion.. *Cold Spring Harbor perspectives in biology*. PMID: 23043155
4. Transcriptional function of E2A, Ebf1, Pax5, Ikaros and Aiolos analyzed by in vivo acute protein degradation in early B cell development.. *Nature immunology*. PMID: 39179932
5. BRD4 orchestrates genome folding to promote neural crest differentiation.. *Nature genetics*. PMID: 34611363

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.0 |
| 高置信度残基 (pLDDT>90) 占比 | 25.0% |
| 置信残基 (pLDDT 70-90) 占比 | 14.4% |
| 中等置信 (pLDDT 50-70) 占比 | 7.7% |
| 低置信 (pLDDT<50) 占比 | 52.9% |
| 有序区域 (pLDDT>70) 占比 | 39.4% |
| 可用 PDB 条目 | 4K6J, 5HDT |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.0），有序残基占 39.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR039874, IPR022771, IPR012502; Pfam: PF07814 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PDS5A | 0.999 | 0.877 | — |
| RAD21 | 0.999 | 0.893 | — |
| SMC3 | 0.999 | 0.876 | — |
| STAG1 | 0.999 | 0.869 | — |
| PDS5B | 0.999 | 0.984 | — |
| NIPBL | 0.998 | 0.126 | — |
| CDCA5 | 0.998 | 0.421 | — |
| STAG2 | 0.997 | 0.893 | — |
| SMC1A | 0.993 | 0.875 | — |
| ESCO1 | 0.982 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000298767.4 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| XRN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| STAG2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| STAG1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| SMC3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| RAD21 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| PDS5B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| PDS5A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| SMC1A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| rbsD | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.0 + PDB: 4K6J, 5HDT | pLDDT=59.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus; Chromosome; Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. WAPL — Wings apart-like protein homolog，研究基础较多，新颖性有限。
2. 蛋白大小1190 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 143 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=59.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 143 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z5K2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000062650-WAPL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WAPL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z5K2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000062650-WAPL/subcellular

![](https://images.proteinatlas.org/66141/1211_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/66141/1211_A6_3_red_green.jpg)
![](https://images.proteinatlas.org/66141/1769_B2_18_cr5950e2cbd9ed7_red_green.jpg)
![](https://images.proteinatlas.org/66141/1769_B2_9_cr5950e2cbd8be8_red_green.jpg)
![](https://images.proteinatlas.org/66141/1975_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/66141/1975_D10_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z5K2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7Z5K2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 626..1169; /note="WAPL"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00603" |
| InterPro | IPR011989;IPR016024;IPR039874;IPR022771;IPR012502; |
| Pfam | PF07814; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000062650-WAPL/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PDS5A | Intact, Biogrid | true |
| PDS5B | Intact, Biogrid | true |
| RAD21 | Intact, Biogrid, Opencell | true |
| SMC1A | Intact, Biogrid, Opencell | true |
| SMC3 | Intact, Biogrid | true |
| STAG1 | Intact, Biogrid | true |
| STAG2 | Intact, Biogrid, Opencell | true |
| AURKA | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
