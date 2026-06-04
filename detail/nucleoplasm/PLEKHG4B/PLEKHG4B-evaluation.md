---
type: protein-evaluation
gene: "PLEKHG4B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLEKHG4B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLEKHG4B / KIAA1909 |
| 蛋白名称 | Pleckstrin homology domain-containing family G member 4B |
| 蛋白大小 | 1627 aa / 178.4 kDa |
| UniProt ID | Q96PX9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Basal cell membrane; Cell junction; Nucleus; Cytoplasm |
| 蛋白大小 | 5/10 | ×1 | 5 | 1627 aa / 178.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR035899, IPR000219, IPR011993, IPR001849, IPR052 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.0/180** | |
| **归一化总分** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Basal cell membrane; Cell junction; Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- basal plasma membrane (GO:0009925)
- cell-cell junction (GO:0005911)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extrinsic component of membrane (GO:0019898)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1909 |

**关键文献**:
1. Construction and evaluation of a bladder cancer prognosis model based on super-enhancer-associated genes.. *Discover oncology*. PMID: 41870815
2. Bioinformatic Analysis of Gene Variants from Gastroschisis Recurrence Identifies Multiple Novel Pathogenetic Pathways: Implication for the Closure of the Ventral Body Wall.. *International journal of molecular sciences*. PMID: 31075877
3. Epigenetics of Skeletal Muscle-Associated Genes in the ASB, LRRC, TMEM, and OSBPL Gene Families.. *Epigenomes*. PMID: 34968235

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.3 |
| 高置信度残基 (pLDDT>90) 占比 | 18.1% |
| 置信残基 (pLDDT 70-90) 占比 | 25.3% |
| 中等置信 (pLDDT 50-70) 占比 | 7.8% |
| 低置信 (pLDDT<50) 占比 | 48.7% |
| 有序区域 (pLDDT>70) 占比 | 43.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=58.3），有序残基占 43.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR035899, IPR000219, IPR011993, IPR001849, IPR052231; Pfam: PF00621, PF22697 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC42 | 0.611 | 0.365 | — |
| ARHGEF19 | 0.530 | 0.000 | — |
| ARHGEF11 | 0.495 | 0.129 | — |
| LRRC14B | 0.480 | 0.000 | — |
| LRRC20 | 0.477 | 0.000 | — |
| FHL3 | 0.437 | 0.205 | — |
| ARHGEF33 | 0.429 | 0.000 | — |
| OR13F1 | 0.418 | 0.000 | — |
| IQCA1L | 0.418 | 0.000 | — |
| RASGRF2 | 0.404 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ARHGAP18 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| ARHGEF11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| ARHGEF12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| CSTA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| DUS3L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| GINS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| LYAR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| MAP3K7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| SRRM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| ARHGEF40 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 15
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.3 + PDB: 无 | pLDDT=58.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Basal cell membrane; Cell junction; Nucleus; Cytop / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 11 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PLEKHG4B — Pleckstrin homology domain-containing family G member 4B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1627 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=58.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96PX9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000153404-PLEKHG4B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLEKHG4B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96PX9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
