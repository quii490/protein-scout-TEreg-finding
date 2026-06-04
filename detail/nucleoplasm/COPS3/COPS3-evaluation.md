---
type: protein-evaluation
gene: "COPS3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## COPS3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COPS3 / CSN3 |
| 蛋白名称 | COP9 signalosome complex subunit 3 |
| 蛋白大小 | 423 aa / 47.9 kDa |
| UniProt ID | Q9UNS2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 423 aa / 47.9 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=84.2; PDB: 4D10, 4D18, 4WSN, 6R6H, 6R7F, 6R7H, 6R7I |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR055089, IPR050756, IPR048621, IPR000717, IPR036 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **145.5/180** | |
| **归一化总分** | | | **80.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA检测到可靠IF图像信号。

**GO Cellular Component**:
- COP9 signalosome (GO:0008180)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) |  |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.2 |
| 高置信度残基 (pLDDT>90) 占比 | 49.6% |
| 置信残基 (pLDDT 70-90) 占比 | 36.6% |
| 中等置信 (pLDDT 50-70) 占比 | 10.2% |
| 低置信 (pLDDT<50) 占比 | 3.5% |
| 有序区域 (pLDDT>70) 占比 | 86.2% |
| 可用 PDB 条目 | 4D10, 4D18, 4WSN, 6R6H, 6R7F, 6R7H, 6R7I, 6R7N, 8H38, 8H3A |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构 + AlphaFold极高置信度（pLDDT=84.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR055089, IPR050756, IPR048621, IPR000717, IPR036390; Pfam: PF22788, PF21215, PF01399 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GPS1 | 0.999 | 0.997 | — |
| COPS6 | 0.999 | 0.995 | — |
| COPS7A | 0.999 | 0.996 | — |
| COPS2 | 0.999 | 0.998 | — |
| COPS4 | 0.999 | 0.997 | — |
| COPS8 | 0.999 | 0.996 | — |
| COPS7B | 0.999 | 0.994 | — |
| COPS5 | 0.999 | 0.995 | — |
| COPS9 | 0.982 | 0.796 | — |
| CUL2 | 0.965 | 0.958 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.2 + PDB: 4D10, 4D18, 4WSN, 6R6H, 6R7F,  | pLDDT=84.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. COPS3 -- COP9 signalosome complex subunit 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小423 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UNS2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000141030-COPS3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COPS3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UNS2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
