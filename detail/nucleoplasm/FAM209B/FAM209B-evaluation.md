---
type: protein-evaluation
gene: "FAM209B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM209B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM209B / C20orf107 |
| 蛋白名称 | Protein FAM209B |
| 蛋白大小 | 171 aa / 19.5 kDa |
| UniProt ID | Q5JX69 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus inner membrane; Cytoplasmic vesicle, secretory vesic |
| 蛋白大小 | 8/10 | ×1 | 8 | 171 aa / 19.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027943; Pfam: PF15206 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 6 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.5/180** | |
| **归一化总分** | | | **70.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus inner membrane; Cytoplasmic vesicle, secretory vesicle, acrosome | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- acrosomal vesicle (GO:0001669)
- nuclear inner membrane (GO:0005637)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf107 |

**关键文献**:
1. Altered mitochondrial function in spermatozoa from patients with repetitive fertilization failure after ICSI revealed by proteomics.. *Andrology*. PMID: 33615715
2. Identification of biomarkers associated with immune scores in diabetic retinopathy.. *Frontiers in endocrinology*. PMID: 37867507

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.3 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 30.4% |
| 中等置信 (pLDDT 50-70) 占比 | 34.5% |
| 低置信 (pLDDT<50) 占比 | 35.1% |
| 有序区域 (pLDDT>70) 占比 | 30.4% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM209B/FAM209B-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=58.3），有序残基占 30.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027943; Pfam: PF15206 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FMR1NB | 0.511 | 0.000 | — |
| FAM209A | 0.469 | 0.000 | — |
| BCAS4 | 0.450 | 0.000 | — |
| PDHA2 | 0.446 | 0.000 | — |
| PHACTR3 | 0.437 | 0.000 | — |
| RAB2B | 0.416 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 6，IntAct interactions: 0
- 调控相关比例: 0 / 6 = 0%

**评价**: STRING 6 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.3 + PDB: 无 | pLDDT=58.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus inner membrane; Cytoplasmic vesicle, secre / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 6 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FAM209B — Protein FAM209B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小171 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=58.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5JX69
- Protein Atlas: https://www.proteinatlas.org/ENSG00000213714-FAM209B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM209B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JX69
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM209B/FAM209B-PAE.png]]
