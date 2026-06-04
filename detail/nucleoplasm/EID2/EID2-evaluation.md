---
type: protein-evaluation
gene: "EID2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EID2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EID2 / CRI2 |
| 蛋白名称 | EP300-interacting inhibitor of differentiation 2 |
| 蛋白大小 | 236 aa / 25.2 kDa |
| UniProt ID | Q8N6I1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Centrosome; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 236 aa / 25.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033258 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.0/180** | |
| **归一化总分** | | | **76.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Centrosome | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CRI2 |

**关键文献**:
1. Analysis of the Nse3/MAGE-binding domain of the Nse4/EID family proteins.. *PloS one*. PMID: 22536443
2. The plasma peptides of breast versus ovarian cancer.. *Clinical proteomics*. PMID: 31889940
3. Microarray analysis of cartilage: comparison between damaged and non-weight-bearing healthy cartilage.. *Connective tissue research*. PMID: 31142155
4. EID3 is a novel EID family member and an inhibitor of CBP-dependent co-activation.. *Nucleic acids research*. PMID: 15987788
5. Identification of stable reference genes in differentiating human pluripotent stem cells.. *Physiological genomics*. PMID: 25852171

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.4 |
| 高置信度残基 (pLDDT>90) 占比 | 9.3% |
| 置信残基 (pLDDT 70-90) 占比 | 22.9% |
| 中等置信 (pLDDT 50-70) 占比 | 17.4% |
| 低置信 (pLDDT<50) 占比 | 50.4% |
| 有序区域 (pLDDT>70) 占比 | 32.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=56.4），有序残基占 32.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033258 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EID3 | 0.921 | 0.292 | — |
| SMC5 | 0.707 | 0.000 | — |
| ZNF324B | 0.637 | 0.000 | — |
| RABEP2 | 0.574 | 0.000 | — |
| SMAD4 | 0.540 | 0.292 | — |
| SMAD3 | 0.528 | 0.292 | — |
| HDAC2 | 0.503 | 0.292 | — |
| SMAD2 | 0.497 | 0.292 | — |
| MAGEF1 | 0.495 | 0.292 | — |
| RAD17 | 0.469 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KERA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAGEE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| BCL2L10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SPG11 | psi-mi:"MI:0018"(two hybrid) | pubmed:37871017|imex:IM-29701 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.4 + PDB: 无 | pLDDT=56.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Centrosome | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. EID2 — EP300-interacting inhibitor of differentiation 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小236 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=56.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N6I1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176396-EID2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EID2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N6I1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
