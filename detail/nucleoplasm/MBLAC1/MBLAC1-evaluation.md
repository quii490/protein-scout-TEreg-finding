---
type: protein-evaluation
gene: "MBLAC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MBLAC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MBLAC1 |
| 蛋白名称 | Metallo-beta-lactamase domain-containing protein 1 |
| 蛋白大小 | 266 aa / 27.2 kDa |
| UniProt ID | A4D2B0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytosol; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 266 aa / 27.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.1; PDB: 4V0H |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR039344, IPR001279, IPR036866; Pfam: PF00753 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, cytosol; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Glial swip-10 controls systemic mitochondrial function, oxidative stress, and neuronal viability via copper ion homeostasis.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 39288174
2. Biosynthesis of histone messenger RNA employs a specific 3' end endonuclease.. *eLife*. PMID: 30507380
3. Optical Imaging Reveals Liver Metabolic Perturbations in Mblac1 Knockout Mice.. *Annual International Conference of the IEEE Engineering in Medicine and Biology Society. IEEE Engineering in Medicine and Biology Society. Annual International Conference*. PMID: 38083729
4. Optical Imaging Demonstrates Tissue-Specific Metabolic Perturbations in Mblac1 Knockout Mice.. *IEEE journal of translational engineering in health and medicine*. PMID: 38410184
5. Dissecting the genetic relationship between cardiovascular risk factors and Alzheimer's disease.. *Acta neuropathologica*. PMID: 30413934

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.1 |
| 高置信度残基 (pLDDT>90) 占比 | 79.3% |
| 置信残基 (pLDDT 70-90) 占比 | 5.3% |
| 中等置信 (pLDDT 50-70) 占比 | 6.8% |
| 低置信 (pLDDT<50) 占比 | 8.6% |
| 有序区域 (pLDDT>70) 占比 | 84.6% |
| 可用 PDB 条目 | 4V0H |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.1，有序区 84.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039344, IPR001279, IPR036866; Pfam: PF00753 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MBLAC2 | 0.664 | 0.000 | — |
| LACTB2 | 0.642 | 0.000 | — |
| ELAC1 | 0.535 | 0.000 | — |
| HAGHL | 0.515 | 0.000 | — |
| DCLRE1A | 0.492 | 0.000 | — |
| FAM214A | 0.488 | 0.000 | — |
| ELAC2 | 0.486 | 0.000 | — |
| ZC3H6 | 0.479 | 0.000 | — |
| HAGH | 0.478 | 0.000 | — |
| INTS9 | 0.464 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| H1-7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CLP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Dmel\CG9117 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| CG12183 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9552|pubmed:19079254 |
| BCL7-like | psi-mi:"MI:0397"(two hybrid array) | pubmed:unassigned1513|imex:IM- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 5
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.1 + PDB: 4V0H | pLDDT=89.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 14 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MBLAC1 — Metallo-beta-lactamase domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小266 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A4D2B0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000214309-MBLAC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MBLAC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A4D2B0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
