---
type: protein-evaluation
gene: "TOR1AIP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TOR1AIP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TOR1AIP2 / IFRG15, LULL1 |
| 蛋白名称 | Torsin-1A-interacting protein 2 |
| 蛋白大小 | 470 aa / 51.3 kDa |
| UniProt ID | Q8NFQ8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Endoplasmic reticulum; UniProt: Endoplasmic reticulum membrane; Nucleus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 470 aa / 51.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.2; PDB: 5J1S, 5J1T |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR038599, IPR008662, IPR046753, IPR046754; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.5/180** | |
| **归一化总分** | | | **72.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum | Enhanced |
| UniProt | Endoplasmic reticulum membrane; Nucleus membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- membrane (GO:0016020)
- nuclear membrane (GO:0031965)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 20 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IFRG15, LULL1 |

**关键文献**:
1. Case report: Identification of a novel TOR1AIP2::ETV6 transcript with FLT3-ITD mutation in acute myeloid leukemia progressed from myelodysplastic syndrome.. *Frontiers in oncology*. PMID: 39723366
2. Mediation Mendelian randomization study of plasma proteomics reveals the causal relationship and potential mechanisms between iron and colorectal adenocarcinoma.. *Discover oncology*. PMID: 41148479
3. Access of torsinA to the inner nuclear membrane is activity dependent and regulated in the endoplasmic reticulum.. *Journal of cell science*. PMID: 26092934
4. TOR1AIP2 as a candidate gene for dystonia-hemichorea/hemiballism.. *Parkinsonism & related disorders*. PMID: 40088780

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.2 |
| 高置信度残基 (pLDDT>90) 占比 | 44.0% |
| 置信残基 (pLDDT 70-90) 占比 | 5.7% |
| 中等置信 (pLDDT 50-70) 占比 | 7.9% |
| 低置信 (pLDDT<50) 占比 | 42.3% |
| 有序区域 (pLDDT>70) 占比 | 49.7% |
| 可用 PDB 条目 | 5J1S, 5J1T |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=69.2），有序残基占 49.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR038599, IPR008662, IPR046753, IPR046754; Pfam: PF05609, PF20443 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TOR1A | 0.999 | 0.983 | — |
| TOR1B | 0.905 | 0.292 | — |
| TOR3A | 0.687 | 0.000 | — |
| TOR2A | 0.657 | 0.000 | — |
| SUN2 | 0.643 | 0.000 | — |
| CUL4A | 0.594 | 0.588 | — |
| SUN1 | 0.525 | 0.000 | — |
| C6orf52 | 0.483 | 0.000 | — |
| TDRD5 | 0.482 | 0.000 | — |
| CEP350 | 0.482 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TOR1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15767459 |
| TSC22D1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| env | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| COPS5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| COPS6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| USP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| CUL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CUL4B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CUL4A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CANX | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.2 + PDB: 5J1S, 5J1T | pLDDT=69.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Nucleus membrane / Endoplasmic reticulum | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TOR1AIP2 — Torsin-1A-interacting protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小470 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NFQ8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169905-TOR1AIP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TOR1AIP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NFQ8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
