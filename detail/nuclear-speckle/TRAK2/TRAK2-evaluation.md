---
type: protein-evaluation
gene: "TRAK2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRAK2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRAK2 / ALS2CR3, KIAA0549 |
| 蛋白名称 | Trafficking kinesin-binding protein 2 |
| 蛋白大小 | 914 aa / 101.4 kDa |
| UniProt ID | O60296 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies; 额外: Vesicles; UniProt: Cytoplasm; Early endosome; Mitochondrion |
| 蛋白大小 | 8/10 | ×1 | 8 | 914 aa / 101.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=36 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR006933, IPR051946, IPR022154; Pfam: PF04849, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies; 额外: Vesicles | Approved |
| UniProt | Cytoplasm; Early endosome; Mitochondrion | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axonal growth cone (GO:0044295)
- cytoplasm (GO:0005737)
- cytoplasmic vesicle (GO:0031410)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- dendrite cytoplasm (GO:0032839)
- early endosome (GO:0005769)
- mitochondrion (GO:0005739)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 36 |
| PubMed broad count | 62 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ALS2CR3, KIAA0549 |

**关键文献**:
1. Mitochondrial adaptor TRAK2 activates and functionally links opposing kinesin and dynein motors.. *Nature communications*. PMID: 34321481
2. CircSLC22A3 inhibits the invasion and metastasis of ESCC via the miR-19b-3p/TRAK2 axis and by reducing the stability of m(6)A-modified ACSBG1 mRNA.. *BMC cancer*. PMID: 40448098
3. TRAK2, a novel regulator of ABCA1 expression, cholesterol efflux and HDL biogenesis.. *European heart journal*. PMID: 28655204
4. The amyloid precursor protein and its derived fragments concomitantly contribute to the alterations of mitochondrial transport machinery in Alzheimer's disease.. *Cell death & disease*. PMID: 38806484
5. A mammalian-specific Alex3/Gα(q) protein complex regulates mitochondrial trafficking, dendritic complexity, and neuronal survival.. *Science signaling*. PMID: 38320000

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.0 |
| 高置信度残基 (pLDDT>90) 占比 | 22.2% |
| 置信残基 (pLDDT 70-90) 占比 | 12.0% |
| 中等置信 (pLDDT 50-70) 占比 | 15.6% |
| 低置信 (pLDDT<50) 占比 | 50.1% |
| 有序区域 (pLDDT>70) 占比 | 34.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=60.0），有序残基占 34.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006933, IPR051946, IPR022154; Pfam: PF04849, PF12448 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RHOT1 | 0.998 | 0.492 | — |
| RHOT2 | 0.994 | 0.206 | — |
| GABRB2 | 0.968 | 0.295 | — |
| TRAK1 | 0.966 | 0.769 | — |
| GABRA1 | 0.954 | 0.000 | — |
| STRADB | 0.929 | 0.000 | — |
| KIF5C | 0.923 | 0.651 | — |
| GABRD | 0.917 | 0.045 | — |
| GABRA5 | 0.917 | 0.000 | — |
| GABRA3 | 0.913 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000328875.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TOMM22 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| GSK3B | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| OGT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PRKAB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KIF5C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KIF1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SNAPIN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KIF5B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.0 + PDB: 无 | pLDDT=60.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Early endosome; Mitochondrion / Nucleoplasm, Nuclear bodies; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. TRAK2 — Trafficking kinesin-binding protein 2，非常新颖，仅有少数基础研究。
2. 蛋白大小914 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 36 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=60.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60296
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115993-TRAK2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRAK2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60296
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
