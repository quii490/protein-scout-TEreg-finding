---
type: protein-evaluation
gene: "PRAG1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRAG1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRAG1 / SGK223 |
| 蛋白名称 | Inactive tyrosine-protein kinase PRAG1 |
| 蛋白大小 | 1406 aa / 149.6 kDa |
| UniProt ID | Q86YV5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Focal adhesion sites; UniProt: Cytoplasm; Cell junction, focal adhesion; Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1406 aa / 149.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=50.2; PDB: 5VE6, 8DGN |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR051511, IPR000719, IPR001245, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.5/180** | |
| **归一化总分** | | | **69.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Focal adhesion sites | Uncertain |
| UniProt | Cytoplasm; Cell junction, focal adhesion; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- focal adhesion (GO:0005925)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SGK223 |

**关键文献**:
1. MicroRNA mechanisms instructing Purkinje cell specification.. *Neuron*. PMID: 40179877
2. PRAG1 promotes cholangiocyte epithelial-mesenchymal transition and liver fibrosis in biliary atresia.. *Biochimica et biophysica acta. Molecular basis of disease*. PMID: 40743806
3. Role of genetics in the development of cardiac allograft vasculopathy.. *Bratislavske lekarske listy*. PMID: 36598310
4. Candidate Genes for IgA Nephropathy in Pediatric Patients: Exome-Wide Association Study.. *International journal of molecular sciences*. PMID: 37958966
5. Investigating the Protective Effects of a Citrus Flavonoid on the Retardation Morphogenesis of the Oligodendroglia-like Cell Line by Rnd2 Knockdown.. *Neurology international*. PMID: 38251051

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 50.2 |
| 高置信度残基 (pLDDT>90) 占比 | 17.1% |
| 置信残基 (pLDDT 70-90) 占比 | 8.2% |
| 中等置信 (pLDDT 50-70) 占比 | 5.0% |
| 低置信 (pLDDT<50) 占比 | 69.7% |
| 有序区域 (pLDDT>70) 占比 | 25.3% |
| 可用 PDB 条目 | 5VE6, 8DGN |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=50.2），有序残基占 25.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR051511, IPR000719, IPR001245, IPR008266; Pfam: PF07714 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CSK | 0.854 | 0.603 | — |
| RND2 | 0.810 | 0.000 | — |
| PEAK3 | 0.531 | 0.292 | — |
| MAML1 | 0.496 | 0.000 | — |
| RHOA | 0.476 | 0.000 | — |
| SHROOM3 | 0.433 | 0.000 | — |
| MTMR9 | 0.426 | 0.000 | — |
| EPHA10 | 0.418 | 0.000 | — |
| S100A8 | 0.414 | 0.000 | — |
| ERBIN | 0.412 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CHGB | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PSAP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| Crk | psi-mi:"MI:0096"(pull down) | imex:IM-8314|pubmed:20697350|m |
| Actn1 | psi-mi:"MI:0096"(pull down) | imex:IM-8314|pubmed:20697350|m |
| Csk | psi-mi:"MI:0096"(pull down) | imex:IM-8314|pubmed:20697350|m |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GRB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| CRKL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 15
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=50.2 + PDB: 5VE6, 8DGN | pLDDT=50.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cell junction, focal adhesion; Nucleus / Nucleoli; 额外: Focal adhesion sites | 一致 |
| PPI | STRING + IntAct | 13 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PRAG1 — Inactive tyrosine-protein kinase PRAG1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1406 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=50.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86YV5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000275342-PRAG1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRAG1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86YV5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
