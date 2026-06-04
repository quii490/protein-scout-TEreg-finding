---
type: protein-evaluation
gene: "AGTPBP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AGTPBP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AGTPBP1 / CCP1, KIAA1035, NNA1 |
| 蛋白名称 | Cytosolic carboxypeptidase 1 |
| 蛋白大小 | 1226 aa / 138.4 kDa |
| UniProt ID | Q9UPW5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Plasma membrane, Primary cilium, Centriolar; UniProt: Cytoplasm; Cytoplasm, cytosol; Nucleus; Mitochondrion |
| 蛋白大小 | 5/10 | ×1 | 5 | 1226 aa / 138.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=36 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011989, IPR016024, IPR033852, IPR050821, IPR040 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane, Primary cilium, Centriolar satellite, Basal body | Supported |
| UniProt | Cytoplasm; Cytoplasm, cytosol; Nucleus; Mitochondrion | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（批量模式），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axon cytoplasm (GO:1904115)
- centriolar satellite (GO:0034451)
- ciliary basal body (GO:0036064)
- cilium (GO:0005929)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- microtubule cytoskeleton (GO:0015630)
- mitochondrion (GO:0005739)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 36 |
| PubMed broad count | 83 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CCP1, KIAA1035, NNA1 |

**关键文献**:
1. The AGTPBP1 gene in neurobiology.. *Gene*. PMID: 34637898
2. Deleterious genetic changes in AGTPBP1 result in teratozoospermia with sperm head and flagella defects.. *Journal of cellular and molecular medicine*. PMID: 37937809
3. Lacosamide Is a Novel Drug That Improves AGTPBP1 Knockout-Mediated Impairment of Neuronal and Dopaminergic Function.. *Molecular neurobiology*. PMID: 40347376
4. The Childhood-Onset Neurodegeneration with Cerebellar Atrophy (CONDCA) Disease Caused by AGTPBP1 Gene Mutations: The Purkinje Cell Degeneration Mouse as an Animal Model for the Study of this Human Disease.. *Biomedicines*. PMID: 34572343
5. Circ-AGTPBP1 promotes white matter injury through miR-140-3p/Pcdh17 axis role of Circ-AGTPBP1 in white matter injury.. *Journal of bioenergetics and biomembranes*. PMID: 37994971

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.3 |
| 高置信度残基 (pLDDT>90) 占比 | 52.8% |
| 置信残基 (pLDDT 70-90) 占比 | 18.4% |
| 中等置信 (pLDDT 50-70) 占比 | 3.9% |
| 低置信 (pLDDT<50) 占比 | 24.9% |
| 有序区域 (pLDDT>70) 占比 | 71.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=75.3，有序区 71.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR033852, IPR050821, IPR040626; Pfam: PF18027, PF00246, PF25571 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TTLL4 | 0.781 | 0.595 | — |
| CPXM2 | 0.668 | 0.000 | — |
| TTL | 0.650 | 0.000 | — |
| TTLL1 | 0.612 | 0.000 | — |
| TTLL5 | 0.559 | 0.000 | — |
| SVBP | 0.481 | 0.000 | — |
| TTLL10 | 0.462 | 0.000 | — |
| NAA35 | 0.445 | 0.000 | — |
| TTLL7 | 0.442 | 0.000 | — |
| SPAST | 0.439 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CYCS | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| NYNRIN | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| CBY1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| PPFIA1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| PPFIA4 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| ENO1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| DISC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| PYGM | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| FOS | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| TTLL4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 15
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.3 + PDB: 无 | pLDDT=75.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytosol; Nucleus; Mitochondr / Nucleoplasm; 额外: Plasma membrane, Primary cilium,  | 一致 |
| PPI | STRING + IntAct | 13 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. AGTPBP1 — Cytosolic carboxypeptidase 1，非常新颖，仅有少数基础研究。
2. 蛋白大小1226 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 36 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UPW5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135049-AGTPBP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AGTPBP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UPW5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
