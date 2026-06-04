---
type: protein-evaluation
gene: "EIF1AD"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EIF1AD 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF1AD |
| 蛋白名称 | Probable RNA-binding protein EIF1AD |
| 蛋白大小 | 165 aa / 19.1 kDa |
| UniProt ID | Q8N9N8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Vesicles; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 165 aa / 19.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.7; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles; 额外: Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 12 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Hypoxia-associated genes as predictors of outcomes in gastric cancer: a genomic approach.. *Front Immunol*. PMID: 40129974
2. Epigenetic aging studies of pair bonding in prairie voles.. *Sci Rep*. PMID: 39075111
3. CRISPRi screening reveals regulators of tau pathology shared between exosomal and vesicle-free tau.. *Life Sci Alliance*. PMID: 36316035
4. Plasma Proteins as Occupational Hazard Risk Monitors for Populations Working in Harsh Environments: A Mendelian Randomization Study.. *Front Public Health*. PMID: 35602164
5. Structural basis for the final steps of human 40S ribosome maturation.. *Nature*. PMID: 33208940

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.7 |
| 高置信度残基 (pLDDT>90) 占比 | 23.6% |
| 置信残基 (pLDDT 70-90) 占比 | 44.8% |
| 中等置信 (pLDDT 50-70) 占比 | 21.8% |
| 低置信 (pLDDT<50) 占比 | 9.7% |
| 有序区域 (pLDDT>70) 占比 | 68.4% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 中等质量（pLDDT=75.7，有序区 68.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RIOK1 | 0.000 | 0.000 | — |
| LRRC47 | 0.000 | 0.000 | — |
| FAU | 0.000 | 0.000 | — |
| RPS15 | 0.000 | 0.000 | — |
| RPS18 | 0.000 | 0.000 | — |
| NOB1 | 0.000 | 0.000 | — |
| RPS23 | 0.000 | 0.000 | — |
| RPS21 | 0.000 | 0.000 | — |
| RPS9 | 0.000 | 0.000 | — |
| RPS2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q8N9N8 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q53EZ4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q92609 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q96BR9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9H190 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P26367 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9NRD5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q96NG5 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |
| uniprotkb:Q9UJV3-2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q8N7W2-2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.7 + PDB: 无 | pLDDT=75.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Vesicles; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. EIF1AD — Probable RNA-binding protein EIF1AD，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小165 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N9N8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175376-EIF1AD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF1AD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N9N8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
