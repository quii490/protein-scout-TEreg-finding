---
type: protein-evaluation
gene: "PRCC"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PRCC — REJECTED (研究热度过高 (PubMed strict=343，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRCC / TPRC |
| 蛋白名称 | Proline-rich protein PRCC |
| 蛋白大小 | 491 aa / 52.4 kDa |
| UniProt ID | Q92733 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nuclear speckles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 491 aa / 52.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=343 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR018800; Pfam: PF10253 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 343 |
| PubMed broad count | 1077 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TPRC |

**关键文献**:
1. The Cancer Genome Atlas of renal cell carcinoma: findings and clinical implications.. *Nature reviews. Urology*. PMID: 31278395
2. AKR1B10 Is a New Sensitive and Specific Marker for Fumarate Hydratase-Deficient Renal Cell Carcinoma.. *Modern pathology : an official journal of the United States and Canadian Academy of Pathology, Inc*. PMID: 37580017
3. TRIM59 suppresses mitochondrial-associated apoptosis to facilitate progression in papillary renal cell carcinoma via the ACAT1-cardiolipin pathway.. *Cell death & disease*. PMID: 40790033
4. TFE3 fusions drive oxidative metabolism and ferroptosis resistance in translocation renal cell carcinoma.. *EMBO molecular medicine*. PMID: 40148585
5. Epigenetic silencing and CRISPR-mediated reactivation of tight junction protein claudin10b (CLDN10B) in renal cancer.. *Clinical epigenetics*. PMID: 40524239

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.1 |
| 高置信度残基 (pLDDT>90) 占比 | 5.3% |
| 置信残基 (pLDDT 70-90) 占比 | 17.7% |
| 中等置信 (pLDDT 50-70) 占比 | 44.8% |
| 低置信 (pLDDT<50) 占比 | 32.2% |
| 有序区域 (pLDDT>70) 占比 | 23.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.1），有序残基占 23.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018800; Pfam: PF10253 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ASPSCR1 | 0.968 | 0.000 | — |
| TFE3 | 0.968 | 0.000 | — |
| CRNKL1 | 0.944 | 0.162 | — |
| ZNF830 | 0.941 | 0.000 | — |
| XAB2 | 0.891 | 0.000 | — |
| SNW1 | 0.883 | 0.000 | — |
| PPIL2 | 0.879 | 0.699 | — |
| RBM10 | 0.847 | 0.488 | — |
| MAD2L2 | 0.834 | 0.322 | — |
| CLTC | 0.820 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EGFR | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:20029029|imex:IM-17166 |
| CSNK2A1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22113938|imex:IM-16640 |
| DNAJC10 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| GORASP2 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| SARNP | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| DIS3 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| SEPTIN7 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| COPZ1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| SH3GLB1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| SEPTIN11 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.1 + PDB: 无 | pLDDT=59.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. PRCC — Proline-rich protein PRCC，研究基础较多，新颖性有限。
2. 蛋白大小491 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 343 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=59.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 343 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92733
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143294-PRCC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRCC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92733
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (enhanced)。来源: https://www.proteinatlas.org/ENSG00000143294-PRCC/subcellular

![](https://images.proteinatlas.org/17151/612_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/17151/612_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/17151/615_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/17151/615_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/17151/621_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/17151/621_C7_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92733-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q92733 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR018800; |
| Pfam | PF10253; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000143294-PRCC/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDC5L | Biogrid | false |
| EGFR | Intact | false |
| HOMER3 | Intact | false |
| LSM2 | Biogrid | false |
| MAD2L2 | Biogrid | false |
| PLOD3 | Bioplex | false |
| PRPF19 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
