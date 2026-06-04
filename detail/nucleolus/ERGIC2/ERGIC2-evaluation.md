---
type: protein-evaluation
gene: "ERGIC2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ERGIC2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ERGIC2 / ERV41, PTX1 |
| 蛋白名称 | Endoplasmic reticulum-Golgi intermediate compartment protein 2 |
| 蛋白大小 | 377 aa / 42.5 kDa |
| UniProt ID | Q96RQ1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus, Vesicles; 额外: Nucleoli rim; UniProt: Endoplasmic reticulum-Golgi intermediate compartment membran |
| 蛋白大小 | 10/10 | ×1 | 10 | 377 aa / 42.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045888, IPR012936, IPR039542; Pfam: PF07970, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.5/180** | |
| **归一化总分** | | | **75.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Vesicles; 额外: Nucleoli rim | Supported |
| UniProt | Endoplasmic reticulum-Golgi intermediate compartment membrane; Golgi apparatus, cis-Golgi network me... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- COPII-coated ER to Golgi transport vesicle (GO:0030134)
- cytoplasm (GO:0005737)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- endoplasmic reticulum-Golgi intermediate compartment membrane (GO:0033116)
- Golgi apparatus (GO:0005794)
- membrane (GO:0016020)
- nucleolus (GO:0005730)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ERV41, PTX1 |

**关键文献**:
1. ERGIC2 and ERGIC3 regulate the ER-to-Golgi transport of gap junction proteins in metazoans.. *Traffic (Copenhagen, Denmark)*. PMID: 34994051
2. Bioinformatics Analysis and Experimental Validation of Endoplasmic Reticulum Stress-Related Genes in Osteoporosis.. *International journal of general medicine*. PMID: 39582915
3. The E3 ubiquitin ligase MARCH2 regulates ERGIC3-dependent trafficking of secretory proteins.. *The Journal of biological chemistry*. PMID: 31142615
4. WLS retrograde transport to the endoplasmic reticulum during Wnt secretion.. *Developmental cell*. PMID: 24768165
5. Characterization of a variant of ERGIC2 transcript.. *DNA and cell biology*. PMID: 24303950

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.0 |
| 高置信度残基 (pLDDT>90) 占比 | 37.9% |
| 置信残基 (pLDDT 70-90) 占比 | 40.1% |
| 中等置信 (pLDDT 50-70) 占比 | 15.4% |
| 低置信 (pLDDT<50) 占比 | 6.6% |
| 有序区域 (pLDDT>70) 占比 | 78.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=81.0，有序区 78.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045888, IPR012936, IPR039542; Pfam: PF07970, PF13850 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ERGIC3 | 0.999 | 0.989 | — |
| GTPBP3 | 0.931 | 0.291 | — |
| DERL2 | 0.867 | 0.840 | — |
| DERL3 | 0.848 | 0.840 | — |
| UBN1 | 0.846 | 0.000 | — |
| SEL1L | 0.800 | 0.782 | — |
| SEL1L2 | 0.791 | 0.782 | — |
| SEL1L3 | 0.788 | 0.782 | — |
| COPB1 | 0.618 | 0.537 | — |
| TXNDC9 | 0.618 | 0.059 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| env | psi-mi:"MI:0096"(pull down) | imex:IM-17346|pubmed:22190034| |
| MAP3K6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ENPP7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSD17B2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TM2D2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZFPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SH2D3C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| LPAR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YIPF3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.0 + PDB: 无 | pLDDT=81.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum-Golgi intermediate compartme / Golgi apparatus, Vesicles; 额外: Nucleoli rim | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. ERGIC2 — Endoplasmic reticulum-Golgi intermediate compartment protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小377 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96RQ1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000087502-ERGIC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ERGIC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96RQ1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
