---
type: protein-evaluation
gene: "SGO1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SGO1 — REJECTED (研究热度过高 (PubMed strict=118，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SGO1 / SGOL1 |
| 蛋白名称 | Shugoshin 1 |
| 蛋白大小 | 561 aa / 64.2 kDa |
| UniProt ID | Q5FBB7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Kinetochore, Cytosol; UniProt: Nucleus; Chromosome, centromere; Chromosome, centromere, kin |
| 蛋白大小 | 10/10 | ×1 | 10 | 561 aa / 64.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=118 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.1; PDB: 3FGA, 3Q6S, 4A0I, 7ZJS |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR038889, IPR011515, IPR011516; Pfam: PF07557, PF |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.0/180** | |
| **归一化总分** | | | **43.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Kinetochore, Cytosol | Approved |
| UniProt | Nucleus; Chromosome, centromere; Chromosome, centromere, kinetochore; Cytoplasm, cytoskeleton, spind... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- chromosome, centromeric region (GO:0000775)
- condensed chromosome, centromeric region (GO:0000779)
- cytosol (GO:0005829)
- kinetochore (GO:0000776)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- spindle pole (GO:0000922)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 118 |
| PubMed broad count | 281 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SGOL1 |

**关键文献**:
1. The expanding phenotypes of cohesinopathies: one ring to rule them all!. *Cell cycle (Georgetown, Tex.)*. PMID: 31516082
2. Assessment of SGO1 and SGO1-AS1 contribution in breast cancer.. *Human antibodies*. PMID: 31156154
3. The zebrafish cohesin protein Sgo1 is required for cardiac function and eye development.. *Developmental dynamics : an official publication of the American Association of Anatomists*. PMID: 35275424
4. Pan-cancer analysis reveals SGO1 as a potential cancer prognostic and immunological biomarker.. *Journal of Cancer*. PMID: 40861810
5. Molecular mechanism targeting condensin for chromosome condensation.. *The EMBO journal*. PMID: 39690240

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.1 |
| 高置信度残基 (pLDDT>90) 占比 | 10.7% |
| 置信残基 (pLDDT 70-90) 占比 | 11.9% |
| 中等置信 (pLDDT 50-70) 占比 | 19.8% |
| 低置信 (pLDDT<50) 占比 | 57.6% |
| 有序区域 (pLDDT>70) 占比 | 22.6% |
| 可用 PDB 条目 | 3FGA, 3Q6S, 4A0I, 7ZJS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.1），有序残基占 22.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR038889, IPR011515, IPR011516; Pfam: PF07557, PF07558 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q588H1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| PPP2CA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-9155|pubmed:19156129 |
| PPP2CB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-9155|pubmed:19156129 |
| PPP2R1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-9155|pubmed:19156129 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| HSP42 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| RPS15 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| MLLT6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Wdr5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.1 + PDB: 3FGA, 3Q6S, 4A0I, 7ZJS | pLDDT=55.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, centromere; Chromosome, centr / Nucleoplasm; 额外: Kinetochore, Cytosol | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SGO1 — Shugoshin 1，研究基础较多，新颖性有限。
2. 蛋白大小561 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 118 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=55.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 118 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5FBB7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000129810-SGO1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SGO1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5FBB7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000129810-SGO1/subcellular

![](https://images.proteinatlas.org/35501/1773_D2_3_red_green.jpg)
![](https://images.proteinatlas.org/35501/1773_D2_7_red_green.jpg)
![](https://images.proteinatlas.org/35501/1899_C8_31_red_green.jpg)
![](https://images.proteinatlas.org/35501/1899_C8_32_red_green.jpg)
![](https://images.proteinatlas.org/35501/813_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/35501/813_C3_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5FBB7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5FBB7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR038889;IPR011515;IPR011516; |
| Pfam | PF07557;PF07558; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000129810-SGO1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CBX5 | Intact, Biogrid | true |
| PPP2CA | Intact, Biogrid, Opencell | true |
| PPP2R5A | Intact, Biogrid | true |
| SMC1A | Intact, Biogrid | true |
| CBX1 | Intact | false |
| CDCA5 | Intact | false |
| CDCA8 | Intact | false |
| NSL1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
