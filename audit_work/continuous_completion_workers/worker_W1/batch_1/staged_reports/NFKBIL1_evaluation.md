---
type: protein-evaluation
gene: "NFKBIL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NFKBIL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NFKBIL1 / IKBL |
| 蛋白名称 | NF-kappa-B inhibitor-like protein 1 |
| 蛋白大小 | 381 aa / 43.3 kDa |
| UniProt ID | Q9UBC1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 381 aa / 43.3 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=42 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036770, IPR038753 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（批量模式），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 42 |
| PubMed broad count | 82 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IKBL |

**关键文献**:
1. Associations between autistic-like traits and polymorphisms in NFKBIL1.. *Acta neuropsychiatrica*. PMID: 31162003
2. CASP1 Gene Polymorphisms and BAT1-NFKBIL-LTA-CASP1 Gene-Gene Interactions Are Associated with Restenosis after Coronary Stenting.. *Biomolecules*. PMID: 35740890
3. Unbiased multitissue transcriptomic analysis reveals complex neuroendocrine regulatory networks mediated by spinal cord injury-induced immunodeficiency.. *Journal of neuroinflammation*. PMID: 37775760
4. Association study between the -62A/T NFKBIL1 polymorphism and obsessive-compulsive disorder.. *Revista brasileira de psiquiatria (Sao Paulo, Brazil : 1999)*. PMID: 19578685
5. A novel link of HLA locus to the regulation of immunity and infection: NFKBIL1 regulates alternative splicing of human immune-related genes and influenza virus M gene.. *Journal of autoimmunity*. PMID: 23953137

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.2 |
| 高置信度残基 (pLDDT>90) 占比 | 19.7% |
| 置信残基 (pLDDT 70-90) 占比 | 56.2% |
| 中等置信 (pLDDT 50-70) 占比 | 8.7% |
| 低置信 (pLDDT<50) 占比 | 15.5% |
| 有序区域 (pLDDT>70) 占比 | 75.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=77.2，有序区 75.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036770, IPR038753 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MRPS22 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| STEEP1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| RFXANK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ENSP00000414206.2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| RNPS1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GEMIN4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MRPS34 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| LUC7L | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MRPS18B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MRPL44 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.2 + PDB: 无 | pLDDT=77.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. NFKBIL1 — NF-kappa-B inhibitor-like protein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小381 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 42 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UBC1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204498-NFKBIL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NFKBIL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UBC1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
