---
type: protein-evaluation
gene: "GET3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GET3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GET3 / ARSA, ASNA1, TRC40 |
| 蛋白名称 | ATPase GET3 |
| 蛋白大小 | 348 aa / 38.8 kDa |
| UniProt ID | O43681 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Nucleoplasm; UniProt: Cytoplasm; Endoplasmic reticulum; Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 348 aa / 38.8 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=87 篇 (≤100→2) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=79.2; PDB: 6SO5, 8CQZ, 8CR1, 8CR2 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR025723, IPR016300, IPR027542, IPR027417; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.0/180** | |
| **归一化总分** | | | **56.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm | Enhanced |
| UniProt | Cytoplasm; Endoplasmic reticulum; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- endoplasmic reticulum membrane (GO:0005789)
- extracellular exosome (GO:0070062)
- GET complex (GO:0043529)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 87 |
| PubMed broad count | 128 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ARSA, ASNA1, TRC40 |

**关键文献**:
1. The natural history of Get3-like chaperones.. *Traffic (Copenhagen, Denmark)*. PMID: 30972921
2. Protein targeting. Structure of the Get3 targeting factor in complex with its membrane protein cargo.. *Science (New York, N.Y.)*. PMID: 25745174
3. Structural insights into metazoan pretargeting GET complexes.. *Nature structural & molecular biology*. PMID: 34887561
4. Structures of Get3, Get4, and Get5 provide new models for TA membrane protein targeting.. *Structure (London, England : 1993)*. PMID: 20696390
5. A protean clamp guides membrane targeting of tail-anchored proteins.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 28973888

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.2 |
| 高置信度残基 (pLDDT>90) 占比 | 48.6% |
| 置信残基 (pLDDT 70-90) 占比 | 16.4% |
| 中等置信 (pLDDT 50-70) 占比 | 25.6% |
| 低置信 (pLDDT<50) 占比 | 9.5% |
| 有序区域 (pLDDT>70) 占比 | 65.0% |
| 可用 PDB 条目 | 6SO5, 8CQZ, 8CR1, 8CR2 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（6SO5, 8CQZ, 8CR1, 8CR2）+ AlphaFold高质量预测（pLDDT=79.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR025723, IPR016300, IPR027542, IPR027417; Pfam: PF02374 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GET1 | 0.999 | 0.995 | — |
| GET4 | 0.999 | 0.991 | — |
| UBL4A | 0.999 | 0.772 | — |
| CAMLG | 0.999 | 0.976 | — |
| BAG6 | 0.978 | 0.787 | — |
| SGTA | 0.976 | 0.479 | — |
| STX5 | 0.960 | 0.606 | — |
| ACP1 | 0.897 | 0.000 | — |
| RNF126 | 0.857 | 0.632 | — |
| VAMP2 | 0.847 | 0.344 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| D6VRQ0 | psi-mi:"MI:0018"(two hybrid) | imex:IM-14544|pubmed:16260785 |
| GET2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| CMD1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| DED1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| ILS1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| PAB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RPS0B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RVB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.2 + PDB: 6SO5, 8CQZ, 8CR1, 8CR2 | pLDDT=79.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Endoplasmic reticulum; Nucleus, nucleol / Nucleoli; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GET3 — ATPase GET3，研究基础较多，新颖性有限。
2. 蛋白大小348 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 87 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43681
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198356-GET3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GET3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43681
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
