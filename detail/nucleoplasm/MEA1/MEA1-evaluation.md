---
type: protein-evaluation
gene: "MEA1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MEA1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MEA1 / MEA |
| 蛋白名称 | Male-enhanced antigen 1 |
| 蛋白大小 | 185 aa / 19.9 kDa |
| UniProt ID | Q16626 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 185 aa / 19.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009685; Pfam: PF06910 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 30 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MEA |

**关键文献**:
1. Peas-Mea1-Ppp2r5d overlapping gene complex: a transposon mediated-gene formation in mammals.. *DNA research : an international journal for rapid publication of reports on genes and genomes*. PMID: 12755172
2. EphA2 receptor activation by monomeric Ephrin-A1 on supported membranes.. *Biophysical journal*. PMID: 22261062
3. Male-enhanced antigen-1 gene flanked by two overlapping genes is expressed in late spermatogenesis.. *Biology of reproduction*. PMID: 12444059
4. Expression of the B56delta subunit of protein phosphatase 2A and Mea1 in mouse spermatogenesis. Identification of a new B56gamma subunit (B56gamma4) specifically expressed in testis.. *Cytogenetic and genome research*. PMID: 15051958
5. Regulation of AP1 adaptor assembly by the bi-handed chaperone MEA1.. *Nature communications*. PMID: 41559075

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.1 |
| 高置信度残基 (pLDDT>90) 占比 | 5.4% |
| 置信残基 (pLDDT 70-90) 占比 | 31.4% |
| 中等置信 (pLDDT 50-70) 占比 | 37.8% |
| 低置信 (pLDDT<50) 占比 | 25.4% |
| 有序区域 (pLDDT>70) 占比 | 36.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=64.1），有序残基占 36.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009685; Pfam: PF06910 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KLHDC3 | 0.944 | 0.000 | — |
| PPP2R5D | 0.934 | 0.000 | — |
| GOLGA3 | 0.887 | 0.000 | — |
| SPATA16 | 0.830 | 0.000 | — |
| BRK1 | 0.763 | 0.000 | — |
| KLHL1 | 0.761 | 0.000 | — |
| NDUFS7 | 0.759 | 0.000 | — |
| ZFY | 0.716 | 0.000 | — |
| AP2B1 | 0.677 | 0.674 | — |
| AP2M1 | 0.650 | 0.618 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| AP2B1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MDM2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| ECI2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| ECH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| AP1M1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| AP2M1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AP2A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| AP1B1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RAD23A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RAD23B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.1 + PDB: 无 | pLDDT=64.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MEA1 — Male-enhanced antigen 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小185 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q16626
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124733-MEA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MEA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q16626
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
