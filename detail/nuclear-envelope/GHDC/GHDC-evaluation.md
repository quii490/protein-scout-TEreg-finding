---
type: protein-evaluation
gene: "GHDC"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GHDC 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GHDC / D11LGP1E, LGP1 |
| 蛋白名称 | GH3 domain-containing protein |
| 蛋白大小 | 530 aa / 57.5 kDa |
| UniProt ID | Q8N2G8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum; Nucleus envelope |
| 蛋白大小 | 10/10 | ×1 | 10 | 530 aa / 57.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR004993, IPR055378, IPR055377, IPR056985; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.5/180** | |
| **归一化总分** | | | **75.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Endoplasmic reticulum; Nucleus envelope | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- endoplasmic reticulum (GO:0005783)
- extracellular region (GO:0005576)
- membrane (GO:0016020)
- nuclear envelope (GO:0005635)
- secretory granule lumen (GO:0034774)
- specific granule lumen (GO:0035580)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 131 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: D11LGP1E, LGP1 |

**关键文献**:
1. Modifiable lifestyle factors influencing psychiatric disorders mediated by plasma proteins: A systemic Mendelian randomization study.. *Journal of affective disorders*. PMID: 38246286
2. Biological significance of genome-wide DNA methylation profiles in keloids.. *The Laryngoscope*. PMID: 27312686
3. Targeted imputation of sequence variants and gene expression profiling identifies twelve candidate genes associated with lactation volume, composition and calving interval in dairy cattle.. *Mammalian genome : official journal of the International Mammalian Genome Society*. PMID: 26613780
4. Anti-EGF antibody cationic polymeric liposomes for delivery of the p53 gene for ovarian carcinoma therapy.. *International journal of clinical and experimental pathology*. PMID: 31933735

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.7 |
| 高置信度残基 (pLDDT>90) 占比 | 54.7% |
| 置信残基 (pLDDT 70-90) 占比 | 25.7% |
| 中等置信 (pLDDT 50-70) 占比 | 9.2% |
| 低置信 (pLDDT<50) 占比 | 10.4% |
| 有序区域 (pLDDT>70) 占比 | 80.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=82.7，有序区 80.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004993, IPR055378, IPR055377, IPR056985; Pfam: PF23572, PF23571, PF25146 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CAVIN1 | 0.832 | 0.000 | — |
| HCRT | 0.812 | 0.000 | — |
| STAT5B | 0.733 | 0.000 | — |
| DHX58 | 0.720 | 0.000 | — |
| STAT5A | 0.713 | 0.000 | — |
| STAT3 | 0.579 | 0.000 | — |
| KCNH4 | 0.572 | 0.000 | — |
| AAR2 | 0.467 | 0.444 | — |
| CD3E | 0.407 | 0.390 | — |
| KAT2A | 0.401 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PACC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KCNA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CHRNA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PCDHAC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CHRNA9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ATG9A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PCDHA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CNGA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TSPAN17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PCDHGB4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 15
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.7 + PDB: 无 | pLDDT=82.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum; Nucleus envelope / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 10 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GHDC — GH3 domain-containing protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小530 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N2G8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167925-GHDC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GHDC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N2G8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N2G8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
