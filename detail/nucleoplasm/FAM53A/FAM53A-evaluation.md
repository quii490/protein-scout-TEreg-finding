---
type: protein-evaluation
gene: "FAM53A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM53A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM53A |
| 蛋白名称 | Protein FAM53A |
| 蛋白大小 | 398 aa / 42.6 kDa |
| UniProt ID | Q6NSI3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Plasma membrane; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 398 aa / 42.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=52.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029356; Pfam: PF15242 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. FAM53A Affects Breast Cancer Cell Proliferation, Migration, and Invasion in a p53-Dependent Manner.. *Frontiers in oncology*. PMID: 31799197
2. Discovering a trans-omics biomarker signature that predisposes high risk diabetic patients to diabetic kidney disease.. *NPJ digital medicine*. PMID: 36323795
3. Transcriptome-wide association study identifies genes associated with bladder cancer risk.. *Scientific reports*. PMID: 39789109
4. Leveraging osteoclast genetic regulatory data to identify genes with a role in osteoarthritis.. *Genetics*. PMID: 37579195
5. TP53-based interaction analysis identifies cis-eQTL variants for TP53BP2, FBXO28, and FAM53A that associate with survival and treatment outcome in breast cancer.. *Oncotarget*. PMID: 28179588

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 52.5 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 5.8% |
| 中等置信 (pLDDT 50-70) 占比 | 41.7% |
| 低置信 (pLDDT<50) 占比 | 52.5% |
| 有序区域 (pLDDT>70) 占比 | 5.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=52.5），有序残基占 5.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029356; Pfam: PF15242 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TMEM129 | 0.665 | 0.000 | — |
| SLBP | 0.516 | 0.000 | — |
| TACC3 | 0.506 | 0.000 | — |
| CRIPAK | 0.474 | 0.000 | — |
| TMEM241 | 0.460 | 0.000 | — |
| CLLU1OS | 0.431 | 0.000 | — |
| IGFL1 | 0.411 | 0.000 | — |
| GTF3C3 | 0.410 | 0.000 | — |
| FCAMR | 0.406 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 1
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=52.5 + PDB: 无 | pLDDT=52.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 9 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FAM53A — Protein FAM53A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小398 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=52.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6NSI3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174137-FAM53A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM53A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6NSI3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000174137-FAM53A/subcellular

![](https://images.proteinatlas.org/36452/2130_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/36452/2130_F1_3_red_green.jpg)
![](https://images.proteinatlas.org/36452/433_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/36452/433_F9_2_red_green.jpg)
![](https://images.proteinatlas.org/36452/440_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/36452/440_F9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6NSI3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6NSI3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029356; |
| Pfam | PF15242; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000174137-FAM53A/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
