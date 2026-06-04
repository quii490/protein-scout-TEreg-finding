---
type: protein-evaluation
gene: "TMX4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TMX4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TMX4 / KIAA1162, TXNDC13 |
| 蛋白名称 | Thioredoxin-related transmembrane protein 4 |
| 蛋白大小 | 349 aa / 39.0 kDa |
| UniProt ID | Q9H1E5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane; UniProt: Nucleus inner membrane; Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 349 aa / 39.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036249, IPR017937, IPR013766, IPR052454; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane | Approved |
| UniProt | Nucleus inner membrane; Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endomembrane system (GO:0012505)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- nuclear inner membrane (GO:0005637)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 26 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1162, TXNDC13 |

**关键文献**:
1. Thioredoxin-Related Transmembrane Proteins: TMX1 and Little Brothers TMX2, TMX3, TMX4 and TMX5.. *Cells*. PMID: 32878123
2. Estrogen receptor beta promotes lung cancer invasion via increasing CXCR4 expression.. *Cell death & disease*. PMID: 35064116
3. TMX4-driven LINC complex disassembly and asymmetric autophagy of the nuclear envelope upon acute ER stress.. *Nature communications*. PMID: 37311770
4. Novel thioredoxin-related transmembrane protein TMX4 has reductase activity.. *The Journal of biological chemistry*. PMID: 20056998
5. TMX5/TXNDC15, a natural trapping mutant of the PDI family is a client of the proteostatic factor ERp44.. *Life science alliance*. PMID: 39348940

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.4 |
| 高置信度残基 (pLDDT>90) 占比 | 37.5% |
| 置信残基 (pLDDT 70-90) 占比 | 19.5% |
| 中等置信 (pLDDT 50-70) 占比 | 18.6% |
| 低置信 (pLDDT<50) 占比 | 24.4% |
| 有序区域 (pLDDT>70) 占比 | 57.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=72.4，有序区 57.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036249, IPR017937, IPR013766, IPR052454; Pfam: PF00085 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TXNDC12 | 0.725 | 0.055 | — |
| TMX3 | 0.675 | 0.000 | — |
| TMX2 | 0.665 | 0.130 | — |
| CANX | 0.577 | 0.359 | — |
| EREG | 0.535 | 0.535 | — |
| PRDX3 | 0.510 | 0.174 | — |
| PDIA2 | 0.505 | 0.000 | — |
| ERP44 | 0.504 | 0.000 | — |
| MSRA | 0.494 | 0.398 | — |
| CSGALNACT1 | 0.487 | 0.478 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NR2F6 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| IL9R | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CSGALNACT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CLEC2D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IL27RA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TMEM30A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ADGRG5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BTN2A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VASN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TEX29 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.4 + PDB: 无 | pLDDT=72.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus inner membrane; Endoplasmic reticulum memb / Nuclear membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TMX4 — Thioredoxin-related transmembrane protein 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小349 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H1E5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125827-TMX4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TMX4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H1E5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
