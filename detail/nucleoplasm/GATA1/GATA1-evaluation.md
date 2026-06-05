---
type: protein-evaluation
gene: "GATA1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GATA1 — REJECTED (研究热度过高 (PubMed strict=2161，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GATA1 / ERYF1, GF1 |
| 蛋白名称 | Erythroid transcription factor |
| 蛋白大小 | 413 aa / 42.8 kDa |
| UniProt ID | P15976 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 413 aa / 42.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2161 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.4; PDB: 6G0Q |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039355, IPR000679, IPR013088; Pfam: PF00320 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-DNA complex (GO:0032993)
- transcription regulator complex (GO:0005667)
- transcription repressor complex (GO:0017053)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2161 |
| PubMed broad count | 3265 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ERYF1, GF1 |

**关键文献**:
1. GATA-related hematologic disorders.. *Experimental hematology*. PMID: 27235756
2. GATA1-related leukaemias.. *Nature reviews. Cancer*. PMID: 18354416
3. HIC2 controls developmental hemoglobin switching by repressing BCL11A transcription.. *Nature genetics*. PMID: 35941187
4. Unfriendly protein of GATA1 and mechanisms of bone marrow failure.. *Haematologica*. PMID: 38618686
5. Mapping the cellular origin and early evolution of leukemia in Down syndrome.. *Science (New York, N.Y.)*. PMID: 34244384

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.4 |
| 高置信度残基 (pLDDT>90) 占比 | 17.7% |
| 置信残基 (pLDDT 70-90) 占比 | 6.8% |
| 中等置信 (pLDDT 50-70) 占比 | 24.5% |
| 低置信 (pLDDT<50) 占比 | 51.1% |
| 有序区域 (pLDDT>70) 占比 | 24.5% |
| 可用 PDB 条目 | 6G0Q |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.4），有序残基占 24.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039355, IPR000679, IPR013088; Pfam: PF00320 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZFPM1 | 0.999 | 0.482 | — |
| TAL1 | 0.999 | 0.520 | — |
| LMO2 | 0.999 | 0.929 | — |
| LDB1 | 0.998 | 0.127 | — |
| KLF1 | 0.997 | 0.091 | — |
| SPI1 | 0.996 | 0.512 | — |
| TCF3 | 0.995 | 0.000 | — |
| LDB2 | 0.995 | 0.127 | — |
| RUNX1 | 0.989 | 0.132 | — |
| BRD3 | 0.986 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Zfpm1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15234987|imex:IM-17033 |
| PRKAA1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Lmo2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:7568177|imex:IM-16983 |
| TAL1 | psi-mi:"MI:0018"(two hybrid) | pubmed:7568177|imex:IM-16983 |
| TCF3 | psi-mi:"MI:0018"(two hybrid) | pubmed:7568177|imex:IM-16983 |
| TRIP6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCL5 | psi-mi:"MI:0412"(electrophoretic mobility supershi | imex:IM-27584|pubmed:10640782 |
| ush | psi-mi:"MI:0077"(nuclear magnetic resonance) | pubmed:15644435|imex:IM-27656 |
| Hba-a1 | psi-mi:"MI:0096"(pull down) | pubmed:15644435|imex:IM-27656 |
| Alas2 | psi-mi:"MI:0096"(pull down) | pubmed:15644435|imex:IM-27656 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.4 + PDB: 6G0Q | pLDDT=58.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
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
1. GATA1 — Erythroid transcription factor，研究基础较多，新颖性有限。
2. 蛋白大小413 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2161 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=58.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2161 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P15976
- Protein Atlas: https://www.proteinatlas.org/ENSG00000102145-GATA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GATA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P15976
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000102145-GATA1/subcellular

![](https://images.proteinatlas.org/233/13_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/233/13_H2_2_red_green.jpg)
![](https://images.proteinatlas.org/233/1877_D6_32_red_green.jpg)
![](https://images.proteinatlas.org/233/1877_D6_33_red_green.jpg)
![](https://images.proteinatlas.org/233/1892_H5_1_red_green.jpg)
![](https://images.proteinatlas.org/233/1892_H5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P15976-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
