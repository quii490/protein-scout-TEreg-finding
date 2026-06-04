---
type: protein-evaluation
gene: "ARIH1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ARIH1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ARIH1 / ARI, MOP6, UBCH7BP |
| 蛋白名称 | E3 ubiquitin-protein ligase ARIH1 |
| 蛋白大小 | 557 aa / 64.1 kDa |
| UniProt ID | Q9Y4X5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus; Nucleus, Cajal body |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 557 aa / 64.1 kDa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=42 篇 (≤60→6) |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=80.0; PDB: 1WD2, 2M9Y, 4KBL, 4KC9, 5TTE, 5UDH, 7B5L |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045840, IPR048962, IPR031127, IPR002867, IPR044 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分 (÷1.83)** | | | **67.2/100******** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Cytoplasm; Nucleus; Nucleus, Cajal body | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- Cajal body (GO:0015030)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- Lewy body (GO:0097413)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 42 |
| PubMed broad count | 80 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ARI, MOP6, UBCH7BP |

**关键文献**:
1. Sugar-mediated non-canonical ubiquitination impairs Nrf1/NFE2L1 activation.. *Molecular cell*. PMID: 39116872
2. Organelle-specific autophagy in inflammatory diseases: a potential therapeutic target underlying the quality control of multiple organelles.. *Autophagy*. PMID: 32048886
3. The E3 ubiquitin ligase ARIH1 promotes antiviral immunity and autoimmunity by inducing mono-ISGylation and oligomerization of cGAS.. *Nature communications*. PMID: 36217001
4. ARIH1 activates STING-mediated T-cell activation and sensitizes tumors to immune checkpoint blockade.. *Nature communications*. PMID: 37429863
5. Ubiquitin ligation to F-box protein targets by SCF-RBR E3-E3 super-assembly.. *Nature*. PMID: 33536622

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.0 |
| 高置信度残基 (pLDDT>90) 占比 | 57.6% |
| 置信残基 (pLDDT 70-90) 占比 | 19.6% |
| 中等置信 (pLDDT 50-70) 占比 | 3.8% |
| 低置信 (pLDDT<50) 占比 | 19.0% |
| 有序区域 (pLDDT>70) 占比 | 77.2% |
| 可用 PDB 条目 | 1WD2, 2M9Y, 4KBL, 4KC9, 5TTE, 5UDH, 7B5L, 7B5M, 7B5N, 7B5S |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: PDB实验结构（1WD2, 2M9Y, 4KBL, 4KC9, 5TTE, 5UDH, 7B5L, 7B5M, 7B5N, 7B5S）+ AlphaFold预测（pLDDT=80.0），实验结构可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045840, IPR048962, IPR031127, IPR002867, IPR044066; Pfam: PF19422, PF01485, PF22191 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UBE2L3 | 0.995 | 0.928 | — |
| RBX1 | 0.984 | 0.956 | — |
| NEDD8 | 0.981 | 0.963 | — |
| CUL1 | 0.977 | 0.960 | — |
| UBC | 0.972 | 0.962 | — |
| UBE2L6 | 0.967 | 0.491 | — |
| CDKN1B | 0.949 | 0.948 | — |
| RPS27A | 0.946 | 0.943 | — |
| UBE2L5 | 0.939 | 0.928 | — |
| CUL3 | 0.932 | 0.591 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FBXW11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| VAV2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-13772|pubmed:18654987 |
| NEDD8 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CUL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| HSPB1 | psi-mi:"MI:0097"(reverse ras recruitment system) | imex:IM-20864|pubmed:25277244 |
| ZNF35 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAGEE2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZNF501 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZNF263 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.0 + PDB: 1WD2, 2M9Y, 4KBL, 4KC9, 5TTE,  | pLDDT=80.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Nucleus, Cajal body / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. ARIH1 — E3 ubiquitin-protein ligase ARIH1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小557 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 42 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y4X5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166233-ARIH1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ARIH1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y4X5
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 02:30:01
