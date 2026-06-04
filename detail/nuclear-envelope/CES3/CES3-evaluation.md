---
type: protein-evaluation
gene: "CES3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, E-batch]
status: scored
---

## CES3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CES3 / — |
| 蛋白名称 | Carboxylesterase 3 |
| 蛋白大小 | 571 aa / 62.3 kDa |
| UniProt ID | Q6UWW8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 6/10 | ×4 | 24 | HPA: Nuclear membrane, Endoplasmic reticulum; UniProt: Endoplasmic reticulum lumen |
| 蛋白大小 | 10/10 | ×1 | 10 | 571 aa / 62.3 kDa |
| 研究新颖性 | 9/10 | ×5 | 45 | PubMed strict=40 篇 |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=91.6; PDB: 暂无 |
| 调控结构域 | 9/10 | ×2 | 18 | InterPro: IPR029058, IPR002018, IPR019826, IPR050309; Pfam: PF00135 |
| PPI 网络 | 10/10 | ×3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.2 | AlphaFold 结构预测: +0.25 |
| **原始总分** | | | **158.2/180** | |
| **归一化总分 (÷1.83)** | | | **86.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane, Endoplasmic reticulum | Approved |
| UniProt | Endoplasmic reticulum lumen | ECO:0000250

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- cytosol (GO:0005829) [TAS:Reactome]
- endoplasmic reticulum lumen (GO:0005788) [IEA:UniProtKB-SubCell]
- extracellular exosome (GO:0070062) [HDA:UniProtKB]

**结论**: HPA: Nuclear membrane, Endoplasmic reticulum; UniProt: Endoplasmic reticulum lumen

#### 3.2 蛋白大小评估

**评价**: 571 aa / 62.3 kDa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 40 |
| PubMed 搜索链接 | [CES3 PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CES3) |

**关键文献**:
暂无文献记录。

**评价**: 较新颖，研究关注度低。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.6 |
| 高置信度残基 (pLDDT>90) 占比 | 82.3% |
| 置信残基 (pLDDT 70-90) 占比 | 10.9% |
| 中等置信 (pLDDT 50-70) 占比 | 1.9% |
| 低置信 (pLDDT<50) 占比 | 4.9% |
| 有序区域 (pLDDT>70) 占比 | 93.2% |
| 可用 PDB 条目 | 暂无 |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold 预测质量高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029058, IPR002018, IPR019826, IPR050309; Pfam: PF00135 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ESD | 0.862 | 0.062 | — |
| LIPE | 0.786 | 0.000 | — |
| TNFRSF13C | 0.743 | 0.000 | — |
| HAGH | 0.678 | 0.000 | — |
| ADH5 | 0.587 | 0.000 | — |
| PPARA | 0.562 | 0.000 | — |
| SECISBP2 | 0.526 | 0.074 | — |
| KLK1 | 0.463 | 0.052 | — |
| LTF | 0.461 | 0.000 | — |
| RPS7 | 0.447 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BMPR2 | psi-mi:"MI:0096"(pull down) | pubmed:15188402 |
| Q81SN0 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TMTC4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| SUOX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| PTPRK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| TMEM25 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| DEFB106A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| SPX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| MCU | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278|doi:10.1016/j.cell.2021.04.011 |
| APP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |

**PPI 互证分析**:
STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0/15。

**评价**: STRING + IntAct 双源 PPI 数据充分。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold | pLDDT=91.6, v6 | 预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum lumen / Nuclear membrane, Endoplasmic reticulum | 部分一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- AlphaFold 结构预测: +0.25
- 单库核定位证据: +0.25
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5

**总分**: +1.2 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐

**归一化总分**: 86.5/100

**核心优势**:
1. CES3 — Carboxylesterase 3，极度新颖，几乎未被系统研究（PubMed 40 篇）。
2. 蛋白大小571 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
3. AlphaFold pLDDT=91.6，结构预测质量高。

**风险/不确定性**:
1. 功能研究较少，具体调控机制待阐明

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6UWW8
- Protein Atlas: https://www.proteinatlas.org/search/CES3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CES3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6UWW8
- STRING: https://string-db.org/network/9606.CES3
- Packet data timestamp: 2026-06-03 04:52:37
