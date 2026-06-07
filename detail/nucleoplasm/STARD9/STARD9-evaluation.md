---
type: protein-evaluation
gene: "STARD9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## STARD9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STARD9 / KIAA1300 |
| 蛋白名称 | StAR-related lipid transfer protein 9 |
| 蛋白大小 | 4700 aa / 516.3 kDa |
| UniProt ID | Q9P2P6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 0/10 | ×1 | 0 | 4700 aa / 516.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000253, IPR019821, IPR001752, IPR036961, IPR027 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriole; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centriole (GO:0005814)
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 26 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1300 |

**关键文献**:
1. A centrosomal protein STARD9 promotes microtubule stability and regulates spindle microtubule dynamics.. *Cell cycle (Georgetown, Tex.)*. PMID: 30160609
2. Clinical and genetic landscape of epilepsies with absence seizures and single-gene etiology.. *Epilepsia*. PMID: 41137852
3. Genome-wide common and rare variant analysis provides novel insights into clozapine-associated neutropenia.. *Molecular psychiatry*. PMID: 27400856
4. Identification and characterization of the human StARD9 gene in the LGMD2A-region on chromosome 15q15 by in silico methods.. *International journal of molecular medicine*. PMID: 16964419
5. Genome-wide association study for the primary feather color trait in a native Chinese duck.. *Frontiers in genetics*. PMID: 36936414

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.8 |
| 高置信度残基 (pLDDT>90) 占比 | 22.0% |
| 置信残基 (pLDDT 70-90) 占比 | 44.0% |
| 中等置信 (pLDDT 50-70) 占比 | 14.2% |
| 低置信 (pLDDT<50) 占比 | 19.8% |
| 有序区域 (pLDDT>70) 占比 | 66.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=72.8，有序区 66.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000253, IPR019821, IPR001752, IPR036961, IPR027417; Pfam: PF00498, PF00225, PF01852 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MCL1 | 0.561 | 0.557 | — |
| STARD10 | 0.556 | 0.000 | — |
| STARD8 | 0.546 | 0.000 | — |
| STARD6 | 0.543 | 0.000 | — |
| PCTP | 0.508 | 0.000 | — |
| DNHD1 | 0.501 | 0.071 | — |
| STARD5 | 0.493 | 0.000 | — |
| STARD7 | 0.490 | 0.000 | — |
| ACOT11 | 0.489 | 0.000 | — |
| LRRC57 | 0.479 | 0.099 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NDUFA7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CDK5RAP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HERPUD1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PPP1CC | psi-mi:"MI:0018"(two hybrid) | pubmed:21382349|imex:IM-17664 |
| HNRNPA2B1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HNRNPA1L2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HNRNPA3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| KIFBP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MCL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.8 + PDB: 无 | pLDDT=72.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. STARD9 — StAR-related lipid transfer protein 9，非常新颖，仅有少数基础研究。
2. 蛋白大小4700 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P2P6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000159433-STARD9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STARD9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P2P6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9P2P6 |
| SMART | SM00240;SM00129; |
| UniProt Domain [FT] | DOMAIN 3..384; /note="Kinesin motor"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00283"; DOMAIN 498..569; /note="FHA"; DOMAIN 4483..4700; /note="START"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00197" |
| InterPro | IPR000253;IPR019821;IPR001752;IPR036961;IPR027417;IPR008984;IPR023393;IPR002913; |
| Pfam | PF00498;PF00225;PF01852; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000159433-STARD9/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HNRNPA3 | Biogrid | false |
| PPP1CC | Biogrid | false |
| YWHAZ | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
