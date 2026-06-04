---
type: protein-evaluation
gene: "FAM168B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM168B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM168B / KIAA0280L, MANI |
| 蛋白名称 | Myelin-associated neurite-outgrowth inhibitor |
| 蛋白大小 | 195 aa / 20.3 kDa |
| UniProt ID | A1KXE4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, perinuclear region; Cell membrane; Cell projectio |
| 蛋白大小 | 8/10 | ×1 | 8 | 195 aa / 20.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=50.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029247; Pfam: PF14944 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, perinuclear region; Cell membrane; Cell projection, axon | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axon (GO:0030424)
- extracellular exosome (GO:0070062)
- perinuclear region of cytoplasm (GO:0048471)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0280L, MANI |

**关键文献**:
1. Livebearing or egg-laying mammals: 27 decisive nucleotides of FAM168.. *Bioscience trends*. PMID: 28381702
2. Gene Co-Expression Network Analysis Reveals the Hub Genes and Key Pathways Associated with Resistance to Salmonella Enteritidis Colonization in Chicken.. *International journal of molecular sciences*. PMID: 36902251
3. Aberrant activation of FAM168B via chimeric PLEKHB2::FAM168B mRNA promotes breast invasive cancer progression.. *Biochemical and biophysical research communications*. PMID: 42105569
4. FAM168B identified as a novel candidate target for chimeric antigen receptor T cell-based cancer therapy.. *Discover oncology*. PMID: 41591662
5. Small rare recurrent deletions and reciprocal duplications in 2q21.1, including brain-specific ARHGEF4 and GPR148.. *Human molecular genetics*. PMID: 22543972

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 50.2 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 1.0% |
| 中等置信 (pLDDT 50-70) 占比 | 43.1% |
| 低置信 (pLDDT<50) 占比 | 55.9% |
| 有序区域 (pLDDT>70) 占比 | 1.0% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM168B/FAM168B-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=50.2），有序残基占 1.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029247; Pfam: PF14944 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RTN4R | 0.677 | 0.000 | — |
| GPR107 | 0.631 | 0.000 | — |
| CMTM4 | 0.476 | 0.000 | — |
| WSB2 | 0.473 | 0.000 | — |
| FUBP3 | 0.449 | 0.000 | — |
| GAGE12H | 0.445 | 0.000 | — |
| ALKBH5 | 0.434 | 0.000 | — |
| AMER3 | 0.430 | 0.000 | — |
| CD180 | 0.413 | 0.000 | — |
| GPR148 | 0.406 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NEDD9 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| FAM222B | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| AGXT | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ZC3H10 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PATZ1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CCNK | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SAMD7 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TCF7L2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FAM168A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ARID5A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 15
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=50.2 + PDB: 无 | pLDDT=50.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, perinuclear region; Cell membrane; Cell / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 11 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FAM168B — Myelin-associated neurite-outgrowth inhibitor，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小195 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=50.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A1KXE4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000152102-FAM168B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM168B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A1KXE4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM168B/FAM168B-PAE.png]]
