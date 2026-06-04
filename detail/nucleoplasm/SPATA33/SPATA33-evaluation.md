---
type: protein-evaluation
gene: "SPATA33"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPATA33 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPATA33 / C16orf55 |
| 蛋白名称 | Spermatogenesis-associated protein 33 |
| 蛋白大小 | 139 aa / 15.5 kDa |
| UniProt ID | Q96N06 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Cytoplasm, cytosol; Nucleus; Cytoplasm; Mitochondrion |
| 蛋白大小 | 8/10 | ×1 | 8 | 139 aa / 15.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027930; Pfam: PF15382 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Approved |
| UniProt | Cytoplasm, cytosol; Nucleus; Cytoplasm; Mitochondrion | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- mitochondrion (GO:0005739)
- nucleus (GO:0005634)
- sperm midpiece (GO:0097225)
- sperm mitochondrial sheath (GO:0097226)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C16orf55 |

**关键文献**:
1. Tethering ATG16L1 or LC3 induces targeted autophagic degradation of protein aggregates and mitochondria.. *Autophagy*. PMID: 37424101
2. Gene alterations and expression spectrum of SPATA33 in nonobstructive azoospermic Iranian men.. *Molecular reproduction and development*. PMID: 30098056
3. A novel testis-enriched gene Spata33 is expressed during spermatogenesis.. *PloS one*. PMID: 23844118
4. SPATA33 localizes calcineurin to the mitochondria and regulates sperm motility in mice.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 34446558
5. Further Insights on RNA Expression and Sperm Motility.. *Genes*. PMID: 35886074

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.8 |
| 高置信度残基 (pLDDT>90) 占比 | 7.2% |
| 置信残基 (pLDDT 70-90) 占比 | 24.5% |
| 中等置信 (pLDDT 50-70) 占比 | 57.6% |
| 低置信 (pLDDT<50) 占比 | 10.8% |
| 有序区域 (pLDDT>70) 占比 | 31.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=65.8），有序残基占 31.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027930; Pfam: PF15382 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DEF8 | 0.602 | 0.000 | — |
| TEX43 | 0.560 | 0.000 | — |
| DBNDD1 | 0.560 | 0.000 | — |
| CDK10 | 0.539 | 0.000 | — |
| PPP3CC | 0.531 | 0.421 | — |
| SPIRE2 | 0.487 | 0.000 | — |
| VDAC2 | 0.479 | 0.292 | — |
| CENPBD1 | 0.465 | 0.000 | — |
| AP1G1 | 0.451 | 0.451 | — |
| KBTBD2 | 0.447 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ACOT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPP3CC | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| LBX2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| AP1G1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PPP3CB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| AP1S2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| AP1S1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PPP3R1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PPP3CA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| AP1B1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.8 + PDB: 无 | pLDDT=65.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Nucleus; Cytoplasm; Mitochondr / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. SPATA33 — Spermatogenesis-associated protein 33，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小139 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=65.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96N06
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167523-SPATA33/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPATA33
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96N06
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
