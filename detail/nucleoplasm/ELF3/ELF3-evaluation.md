---
type: protein-evaluation
gene: "ELF3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ELF3 — REJECTED (研究热度过高 (PubMed strict=410，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ELF3 / ERT, ESX, JEN |
| 蛋白名称 | ETS-related transcription factor Elf-3 |
| 蛋白大小 | 371 aa / 41.5 kDa |
| UniProt ID | P78545 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 371 aa / 41.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=410 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.8; PDB: 2E8P |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR042693, IPR000418, IPR046328, IPR003118, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 410 |
| PubMed broad count | 672 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ERT, ESX, JEN |

**关键文献**:
1. A prion-like domain in ELF3 functions as a thermosensor in Arabidopsis.. *Nature*. PMID: 32848244
2. Genomic spectra of biliary tract cancer.. *Nature genetics*. PMID: 26258846
3. Plant Thermosensors.. *Annual review of genetics*. PMID: 38986032
4. Spatially Resolved Niche and Tumor Microenvironmental Alterations in Gastric Cancer Peritoneal Metastases.. *Gastroenterology*. PMID: 39147169
5. Identification and validation of glycolysis-related diagnostic signatures in diabetic nephropathy: a study based on integrative machine learning and single-cell sequence.. *Frontiers in immunology*. PMID: 39916957

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.8 |
| 高置信度残基 (pLDDT>90) 占比 | 18.1% |
| 置信残基 (pLDDT 70-90) 占比 | 28.3% |
| 中等置信 (pLDDT 50-70) 占比 | 14.0% |
| 低置信 (pLDDT<50) 占比 | 39.6% |
| 有序区域 (pLDDT>70) 占比 | 46.4% |
| 可用 PDB 条目 | 2E8P |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.8），有序残基占 46.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042693, IPR000418, IPR046328, IPR003118, IPR013761; Pfam: PF00178, PF02198 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ELF4 | 0.979 | 0.000 | — |
| MED23 | 0.923 | 0.735 | — |
| PRKCI | 0.846 | 0.316 | — |
| SPRR2A | 0.818 | 0.000 | — |
| SPRR2B | 0.817 | 0.000 | — |
| ESX1 | 0.771 | 0.000 | — |
| POU2F3 | 0.736 | 0.000 | — |
| EP300 | 0.729 | 0.292 | — |
| TBP | 0.719 | 0.292 | — |
| NOTCH3 | 0.679 | 0.296 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CRY2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15805487|imex:IM-19425 |
| PHYB | psi-mi:"MI:0055"(fluorescent resonance energy tran | pubmed:11089975 |
| COP1 | psi-mi:"MI:0018"(two hybrid) | pubmed:11509693|imex:IM-19075| |
| EEF1D | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| KCTD5 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CALR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ENSP00000356253.5 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TARS1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| H2BC10 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EWSR1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.8 + PDB: 2E8P | pLDDT=64.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm | 一致 |
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
1. ELF3 — ETS-related transcription factor Elf-3，研究基础较多，新颖性有限。
2. 蛋白大小371 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 410 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=64.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 410 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P78545
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163435-ELF3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ELF3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P78545
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P78545-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
