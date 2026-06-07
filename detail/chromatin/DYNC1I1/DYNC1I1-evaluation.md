---
type: protein-evaluation
gene: "DYNC1I1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DYNC1I1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DYNC1I1 / DNCI1, DNCIC1 |
| 蛋白名称 | Cytoplasmic dynein 1 intermediate chain 1 |
| 蛋白大小 | 645 aa / 73.0 kDa |
| UniProt ID | O14576 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Chromosome, centromere, kinetochore; Cytoplasm, c |
| 蛋白大小 | 10/10 | ×1 | 10 | 645 aa / 73.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=38 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR025956, IPR050687, IPR015943, IPR036322, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Chromosome, centromere, kinetochore; Cytoplasm, cytoskeleton, spindle pole | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic dynein complex (GO:0005868)
- cytoplasmic ribonucleoprotein granule (GO:0036464)
- cytosol (GO:0005829)
- kinetochore (GO:0000776)
- microtubule (GO:0005874)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 38 |
| PubMed broad count | 53 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DNCI1, DNCIC1 |

**关键文献**:
1. CLASP1 regulates DYNC1I1 for PLK1-mediated spindle organization and cytokinesis in oocyte meiosis.. *Journal of cell science*. PMID: 40501366
2. Dynactin is involved in Lewy body pathology.. *Neuropathology : official journal of the Japanese Society of Neuropathology*. PMID: 30215870
3. DYNC1I1 acts as a promising prognostic biomarker and is correlated with immune infiltration in head and neck squamous cell carcinoma.. *Journal of stomatology, oral and maxillofacial surgery*. PMID: 38072235
4. TNPO2 operates downstream of DYNC1I1 and promotes gastric cancer cell proliferation and inhibits apoptosis.. *Cancer medicine*. PMID: 31605449
5. HTT (huntingtin) and RAB7 co-migrate retrogradely on a signaling LAMP1-containing late endosome during axonal injury.. *Autophagy*. PMID: 36048753

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.0 |
| 高置信度残基 (pLDDT>90) 占比 | 13.3% |
| 置信残基 (pLDDT 70-90) 占比 | 52.4% |
| 中等置信 (pLDDT 50-70) 占比 | 11.6% |
| 低置信 (pLDDT<50) 占比 | 22.6% |
| 有序区域 (pLDDT>70) 占比 | 65.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.0，有序区 65.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR025956, IPR050687, IPR015943, IPR036322, IPR001680; Pfam: PF11540, PF00400 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DYNC1LI1 | 0.999 | 0.994 | — |
| DYNC1H1 | 0.999 | 0.995 | — |
| DCTN2 | 0.998 | 0.994 | — |
| DCTN1 | 0.998 | 0.995 | — |
| DYNLL1 | 0.997 | 0.890 | — |
| BICD2 | 0.997 | 0.994 | — |
| DYNC1LI2 | 0.995 | 0.803 | — |
| DYNLRB1 | 0.990 | 0.906 | — |
| DYNLL2 | 0.989 | 0.737 | — |
| DYNC1I2 | 0.983 | 0.835 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DYNLRB1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DYNLL2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| STAU1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:15121898 |
| SMAD2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| H3-4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| BICD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27323|pubmed:23664119 |
| DYNC1LI2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPL23 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DYNC1I2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.0 + PDB: 无 | pLDDT=71.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Chromosome, centromere, kinetochore; Cy / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DYNC1I1 — Cytoplasmic dynein 1 intermediate chain 1，非常新颖，仅有少数基础研究。
2. 蛋白大小645 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 38 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14576
- Protein Atlas: https://www.proteinatlas.org/ENSG00000158560-DYNC1I1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DYNC1I1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14576
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O14576-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O14576 |
| SMART | SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR025956;IPR050687;IPR015943;IPR036322;IPR001680; |
| Pfam | PF11540;PF00400; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000158560-DYNC1I1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BICD2 | Intact, Biogrid | true |
| DYNLL2 | Intact, Biogrid | true |
| DYNLRB1 | Intact, Biogrid | true |
| FAM83D | Intact, Biogrid | true |
| DCTN1 | Biogrid | false |
| DCTN2 | Biogrid | false |
| DYNC1H1 | Biogrid | false |
| DYNC1I2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
