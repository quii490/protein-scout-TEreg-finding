---
type: protein-evaluation
gene: "DISP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DISP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DISP2 / C15orf36, DISPB, KIAA1742, LINC00594 |
| 蛋白名称 | Protein dispatched homolog 2 |
| 蛋白大小 | 1401 aa / 152.0 kDa |
| UniProt ID | A7MBM2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles; UniProt: Membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 1401 aa / 152.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052081, IPR000731 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- membrane (GO:0016020)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C15orf36, DISPB, KIAA1742, LINC00594 |

**关键文献**:
1. The ataxia-telangiectasia disease protein ATM controls vesicular protein secretion via CHGA and microtubule dynamics via CRMP5.. *Neurobiology of disease*. PMID: 39615799
2. Genetic Determinants of Colonic Diverticulosis-A Systematic Review.. *Genes*. PMID: 40428403
3. Pancreatic islet and progenitor cell surface markers with cell sorting potential.. *Diabetologia*. PMID: 21947380
4. A Hypermutable Region in the DISP2 Gene Links to Natural Selection and Late-Onset Neurocognitive Disorders in Humans.. *Molecular neurobiology*. PMID: 38565786
5. Hedgehog signaling pathway and gastric cancer.. *Cancer biology & therapy*. PMID: 16258256

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.5 |
| 高置信度残基 (pLDDT>90) 占比 | 26.7% |
| 置信残基 (pLDDT 70-90) 占比 | 32.9% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 34.5% |
| 有序区域 (pLDDT>70) 占比 | 59.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=67.5），有序残基占 59.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052081, IPR000731 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SHH | 0.916 | 0.563 | — |
| DHH | 0.858 | 0.563 | — |
| IHH | 0.850 | 0.563 | — |
| PTCH1 | 0.592 | 0.000 | — |
| SCUBE2 | 0.569 | 0.000 | — |
| FAM185A | 0.506 | 0.000 | — |
| MAP6D1 | 0.493 | 0.000 | — |
| COMTD1 | 0.482 | 0.000 | — |
| PAXBP1 | 0.479 | 0.000 | — |
| DUS2 | 0.466 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CACNA1C | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:37207277|imex:IM-29810 |
| HCN1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:37207277|imex:IM-29810 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.5 + PDB: 无 | pLDDT=67.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

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
1. DISP2 — Protein dispatched homolog 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1401 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A7MBM2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140323-DISP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DISP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A7MBM2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
