---
type: protein-evaluation
gene: "MSANTD3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MSANTD3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MSANTD3 / C9orf30 |
| 蛋白名称 | Myb/SANT-like DNA-binding domain-containing protein 3 |
| 蛋白大小 | 275 aa / 32.4 kDa |
| UniProt ID | Q96H12 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear bodies, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 275 aa / 32.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028002; Pfam: PF13873 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf30 |

**关键文献**:
1. PON3::LCN1 and HTN3::MSANTD3 Gene Fusions With NR4A3/NR4A2 Expression in Salivary Acinic Cell Carcinoma.. *The American journal of surgical pathology*. PMID: 38682454
2. The HTN3-MSANTD3 Fusion Gene Defines a Subset of Acinic Cell Carcinoma of the Salivary Gland.. *The American journal of surgical pathology*. PMID: 30520817
3. Decoding molecular markers and transcriptional circuitry of naive and primed states of human pluripotency.. *Stem cell research*. PMID: 33862536
4. Recurrent rearrangements of the Myb/SANT-like DNA-binding domain containing 3 gene (MSANTD3) in salivary gland acinic cell carcinoma.. *PloS one*. PMID: 28212443
5. Genetic Variants Associated with the Age of Onset Identified by Whole-Exome Sequencing in Fatal Familial Insomnia.. *Cells*. PMID: 37626863

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.0 |
| 高置信度残基 (pLDDT>90) 占比 | 50.2% |
| 置信残基 (pLDDT 70-90) 占比 | 6.2% |
| 中等置信 (pLDDT 50-70) 占比 | 17.1% |
| 低置信 (pLDDT<50) 占比 | 26.5% |
| 有序区域 (pLDDT>70) 占比 | 56.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=74.0，有序区 56.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028002; Pfam: PF13873 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TMEFF1 | 0.693 | 0.000 | — |
| HTN3 | 0.621 | 0.000 | — |
| NR4A3 | 0.497 | 0.000 | — |
| MSANTD2 | 0.481 | 0.000 | — |
| TP53BP1 | 0.447 | 0.439 | — |
| PRB3 | 0.445 | 0.000 | — |
| ANO1 | 0.415 | 0.000 | — |
| SUV39H1 | 0.414 | 0.000 | — |
| TBC1D21 | 0.400 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SMC3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ZDHHC17 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-21827|pubmed:24705354 |
| FGFR3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| GRIN2C | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| GSN | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| CHAT | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| ENSP00000480622.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| EBI-2532316 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-30341|pubmed:40739040 |
| EBI-2532212 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-30341|pubmed:40739040 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 9
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.0 + PDB: 无 | pLDDT=74.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Nuclear bodies, Cytosol | 待确认 |
| PPI | STRING + IntAct | 9 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MSANTD3 — Myb/SANT-like DNA-binding domain-containing protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小275 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96H12
- Protein Atlas: https://www.proteinatlas.org/ENSG00000066697-MSANTD3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MSANTD3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96H12
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
