---
type: protein-evaluation
gene: "C2CD2L"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## C2CD2L — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C2CD2L / KIAA0285, TMEM24 |
| 蛋白名称 | Phospholipid transfer protein C2CD2L |
| 蛋白大小 | 706 aa / 76.2 kDa |
| UniProt ID | O14523 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Plasma membrane; UniProt: Endoplasmic reticulum membrane; Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 706 aa / 76.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.9; PDB: 5TOD |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000008, IPR035892, IPR039934, IPR040885; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.5/180** | |
| **归一化总分** | | | **61.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane | Supported |
| UniProt | Endoplasmic reticulum membrane; Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cortical endoplasmic reticulum (GO:0032541)
- endoplasmic reticulum membrane (GO:0005789)
- endoplasmic reticulum-plasma membrane contact site (GO:0140268)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0285, TMEM24 |

**关键文献**:
1. Identification of novel therapeutic targets for chronic kidney disease and kidney function by integrating multi-omics proteome with transcriptome.. *Genome medicine*. PMID: 38898508
2. Experimental verification and identifying biomarkers related to insomnia.. *Frontiers in neurology*. PMID: 38090272
3. Astrocytes express aberrant immunoglobulins as putative gatekeeper of astrocytes to neuronal progenitor conversion.. *Cell death & disease*. PMID: 37015912
4. A novel lncRNA AC112721.1 promotes the progression of triple-negative breast cancer by directly binding to THBS1 and regulating miR-491-5p/C2CD2L axis.. *Scientific reports*. PMID: 39738500
5. The endoplasmic reticulum-plasma membrane tethering protein TMEM24 is a regulator of cellular Ca2+ homeostasis.. *Journal of cell science*. PMID: 34821358

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.9 |
| 高置信度残基 (pLDDT>90) 占比 | 15.9% |
| 置信残基 (pLDDT 70-90) 占比 | 28.5% |
| 中等置信 (pLDDT 50-70) 占比 | 18.1% |
| 低置信 (pLDDT<50) 占比 | 37.5% |
| 有序区域 (pLDDT>70) 占比 | 44.4% |
| 可用 PDB 条目 | 5TOD |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.9），有序残基占 44.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000008, IPR035892, IPR039934, IPR040885; Pfam: PF00168, PF18696 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ESYT1 | 0.622 | 0.000 | — |
| PITPNM1 | 0.591 | 0.000 | — |
| ESYT2 | 0.586 | 0.000 | — |
| OSBPL5 | 0.572 | 0.000 | — |
| OSBPL8 | 0.516 | 0.000 | — |
| VAPA | 0.500 | 0.192 | — |
| PITPNM2 | 0.477 | 0.000 | — |
| TMEM217 | 0.469 | 0.000 | — |
| TEX2 | 0.457 | 0.000 | — |
| OSBP | 0.452 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| H2BC21 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| PDGFRB | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| SLC10A6 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| GJB1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| CISD2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMPRSS2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SLC18A1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMEM86B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| REEP4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.9 + PDB: 5TOD | pLDDT=63.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Cell membrane / Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. C2CD2L — Phospholipid transfer protein C2CD2L，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小706 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=63.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14523
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172375-C2CD2L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C2CD2L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14523
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O14523-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
