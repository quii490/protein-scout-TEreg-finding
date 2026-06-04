---
type: protein-evaluation
gene: "DPPA3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DPPA3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DPPA3 / STELLAR |
| 蛋白名称 | Developmental pluripotency-associated protein 3 |
| 蛋白大小 | 159 aa / 17.9 kDa |
| UniProt ID | Q6W0C5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 159 aa / 17.9 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=94 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.3; PDB: 8WMS, 8XV7, 8XV8 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029096; Pfam: PF15549 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- female pronucleus (GO:0001939)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 94 |
| PubMed broad count | 196 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: STELLAR |

**关键文献**:
1. Rolling back human pluripotent stem cells to an eight-cell embryo-like stage.. *Nature*. PMID: 35314832
2. Dppa3 in pluripotency maintenance of ES cells and early embryogenesis.. *Journal of cellular biochemistry*. PMID: 30417435
3. Dppa3 facilitates self-renewal of embryonic stem cells by stabilization of pluripotent factors.. *Stem cell research & therapy*. PMID: 35477484
4. Embryonic defects induced by maternal obesity in mice derive from Stella insufficiency in oocytes.. *Nature genetics*. PMID: 29459681
5. Cytoplasmic cleavage of DPPA3 is required for intracellular trafficking and cleavage-stage development in mice.. *Nature communications*. PMID: 29158485

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.3 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 29.6% |
| 中等置信 (pLDDT 50-70) 占比 | 48.4% |
| 低置信 (pLDDT<50) 占比 | 22.0% |
| 有序区域 (pLDDT>70) 占比 | 29.6% |
| 可用 PDB 条目 | 8WMS, 8XV7, 8XV8 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=63.3），有序残基占 29.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029096; Pfam: PF15549 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DPPA5 | 0.823 | 0.000 | — |
| NANOG | 0.813 | 0.000 | — |
| POU5F1 | 0.807 | 0.092 | — |
| PRDM1 | 0.802 | 0.000 | — |
| LIN28A | 0.766 | 0.074 | — |
| LIN28B | 0.753 | 0.074 | — |
| ZFP57 | 0.746 | 0.000 | — |
| KLF4 | 0.740 | 0.000 | — |
| SOX2 | 0.738 | 0.000 | — |
| UTF1 | 0.736 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRIB3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NUP62 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| DYNLL1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| HAUS7 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SERTAD3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| DEPDC5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ZNF618 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DYNLL2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TFIP11 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.3 + PDB: 8WMS, 8XV7, 8XV8 | pLDDT=63.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. DPPA3 — Developmental pluripotency-associated protein 3，研究基础较多，新颖性有限。
2. 蛋白大小159 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 94 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=63.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6W0C5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187569-DPPA3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DPPA3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6W0C5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
