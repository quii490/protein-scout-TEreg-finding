---
type: protein-evaluation
gene: "AKAP6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AKAP6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AKAP6 / AKAP100, KIAA0311 |
| 蛋白名称 | A-kinase anchor protein 6 |
| 蛋白大小 | 2319 aa / 256.7 kDa |
| UniProt ID | Q13023 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Sarcoplasmic reticulum; Nucleus membrane |
| 蛋白大小 | 2/10 | ×1 | 2 | 2319 aa / 256.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=42.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR018159, IPR002017; Pfam: PF00435 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **112.0/180** | |
| **归一化总分** | | | **62.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Sarcoplasmic reticulum; Nucleus membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- calcium channel complex (GO:0034704)
- caveola (GO:0005901)
- cytoplasm (GO:0005737)
- intercalated disc (GO:0014704)
- junctional sarcoplasmic reticulum membrane (GO:0014701)
- nuclear envelope (GO:0005635)
- nuclear membrane (GO:0031965)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 79 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AKAP100, KIAA0311 |

**关键文献**:
1. Exploring AKAPs in visual signaling.. *Frontiers in molecular neuroscience*. PMID: 38813437
2. AKAP6 and phospholamban colocalize and interact in HEK-293T cells and primary murine cardiomyocytes.. *Physiological reports*. PMID: 31325238
3. AKAP6 inhibition impairs myoblast differentiation and muscle regeneration: Positive loop between AKAP6 and myogenin.. *Scientific reports*. PMID: 26563778
4. Impact of AKAP6 polymorphisms on Glioma susceptibility and prognosis.. *BMC neurology*. PMID: 31759389
5. Wnt/β-catenin pathway induces cardiac dysfunction via AKAP6-mediated RyR2 phosphorylation and sarcoplasmic reticulum calcium leakage.. *Journal of molecular cell biology*. PMID: 40097291

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 42.1 |
| 高置信度残基 (pLDDT>90) 占比 | 1.9% |
| 置信残基 (pLDDT 70-90) 占比 | 17.1% |
| 中等置信 (pLDDT 50-70) 占比 | 7.4% |
| 低置信 (pLDDT<50) 占比 | 73.6% |
| 有序区域 (pLDDT>70) 占比 | 19.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=42.1），有序残基占 19.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018159, IPR002017; Pfam: PF00435 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RYR2 | 0.992 | 0.496 | — |
| RAPGEF3 | 0.967 | 0.095 | — |
| MAPK7 | 0.958 | 0.000 | — |
| PRKACB | 0.953 | 0.091 | — |
| PRKACA | 0.953 | 0.091 | — |
| PRKACG | 0.953 | 0.091 | — |
| PDE4D | 0.944 | 0.292 | — |
| PDE4A | 0.941 | 0.292 | — |
| AKAP1 | 0.931 | 0.000 | — |
| FKBP1B | 0.929 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DTNBP1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| 4757996 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| OPTN | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| SRC | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| FYN | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| ABL1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| CRK | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| PIK3R1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=42.1 + PDB: 无 | pLDDT=42.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Sarcoplasmic reticulum; Nucleus membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. AKAP6 — A-kinase anchor protein 6，非常新颖，仅有少数基础研究。
2. 蛋白大小2319 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=42.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13023
- Protein Atlas: https://www.proteinatlas.org/ENSG00000151320-AKAP6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AKAP6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13023
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
