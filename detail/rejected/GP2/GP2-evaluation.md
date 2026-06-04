---
type: protein-evaluation
gene: "GP2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GP2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GP2 |
| 蛋白名称 | Pancreatic secretory granule membrane major glycoprotein GP2 |
| 蛋白大小 | 537 aa / 59.5 kDa |
| UniProt ID | P55259 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Zymogen granule membrane; Secreted; Cell membrane; Apical ce |
| 蛋白大小 | 10/10 | ×1 | 10 | 537 aa / 59.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=78.6; PDB: 7P6R, 7P6S, 7P6T, 8XC5 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR057774, IPR055355, IPR042235, IPR055356, IPR048 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Zymogen granule membrane; Secreted; Cell membrane; Apical cell membrane; Membrane raft; Endosome | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- apical plasma membrane (GO:0016324)
- cell surface (GO:0009986)
- endosome (GO:0005768)
- external side of plasma membrane (GO:0009897)
- extracellular exosome (GO:0070062)
- extracellular region (GO:0005576)
- extracellular space (GO:0005615)
- membrane raft (GO:0045121)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.6 |
| 高置信度残基 (pLDDT>90) 占比 | 44.1% |
| 置信残基 (pLDDT 70-90) 占比 | 30.9% |
| 中等置信 (pLDDT 50-70) 占比 | 9.9% |
| 低置信 (pLDDT<50) 占比 | 15.1% |
| 有序区域 (pLDDT>70) 占比 | 75.0% |
| 可用 PDB 条目 | 7P6R, 7P6S, 7P6T, 8XC5 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（7P6R, 7P6S, 7P6T, 8XC5）+ AlphaFold高质量预测（pLDDT=78.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR057774, IPR055355, IPR042235, IPR055356, IPR048290; Pfam: PF23283, PF00100, PF23344 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GTPBP1 | 0.999 | 0.000 | — |
| CD36 | 0.994 | 0.000 | — |
| CD163 | 0.976 | 0.107 | — |
| NPC1 | 0.948 | 0.000 | — |
| GP5 | 0.944 | 0.099 | — |
| SV2C | 0.923 | 0.091 | — |
| SV2B | 0.905 | 0.091 | — |
| SV2A | 0.905 | 0.091 | — |
| GP6 | 0.835 | 0.113 | — |
| PPY | 0.734 | 0.125 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SOX30 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| TSSK3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| JAGN1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.6 + PDB: 7P6R, 7P6S, 7P6T, 8XC5 | pLDDT=78.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Zymogen granule membrane; Secreted; Cell membrane; / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GP2 — Pancreatic secretory granule membrane major glycoprotein GP2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小537 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P55259
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169347-GP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P55259
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
