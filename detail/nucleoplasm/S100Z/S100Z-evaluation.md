---
type: protein-evaluation
gene: "S100Z"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## S100Z 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | S100Z |
| 蛋白名称 | Protein S100-Z |
| 蛋白大小 | 99 aa / 11.6 kDa |
| UniProt ID | Q8WXG8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Centrosome, Cytosol; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 99 aa / 11.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=84.7; PDB: 5HYD |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011992, IPR018247, IPR002048, IPR001751, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome, Cytosol; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of Novel Genes Involved in Hyperglycemia in Mice.. *International journal of molecular sciences*. PMID: 35328627
2. S100 proteins in oral squamous cell carcinoma.. *Clinica chimica acta; international journal of clinical chemistry*. PMID: 29453969
3. Molecular characterization and tissue distribution of a novel member of the S100 family of EF-hand proteins.. *Biochemistry*. PMID: 11747429
4. S100Z is expressed in a lateral subpopulation of olfactory receptor neurons in the main olfactory system of Xenopus laevis.. *Developmental neurobiology*. PMID: 38439531
5. Significance of Immune-Related Genes in the Diagnosis and Classification of Intervertebral Disc Degeneration.. *Journal of immunology research*. PMID: 36081453

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.7 |
| 高置信度残基 (pLDDT>90) 占比 | 36.4% |
| 置信残基 (pLDDT 70-90) 占比 | 51.5% |
| 中等置信 (pLDDT 50-70) 占比 | 11.1% |
| 低置信 (pLDDT<50) 占比 | 1.0% |
| 有序区域 (pLDDT>70) 占比 | 87.9% |
| 可用 PDB 条目 | 5HYD |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=84.7，有序区 87.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011992, IPR018247, IPR002048, IPR001751, IPR013787; Pfam: PF01023 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HRNR | 0.697 | 0.000 | — |
| S100A13 | 0.675 | 0.000 | — |
| S100A3 | 0.645 | 0.547 | — |
| S100A1 | 0.603 | 0.548 | — |
| S100A7L2 | 0.583 | 0.000 | — |
| S100P | 0.581 | 0.578 | — |
| S100A14 | 0.573 | 0.000 | — |
| S100A7A | 0.573 | 0.000 | — |
| S100A7 | 0.571 | 0.000 | — |
| RPTN | 0.571 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.7 + PDB: 5HYD | pLDDT=84.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Centrosome, Cytosol; 额外: Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. S100Z — Protein S100-Z，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小99 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WXG8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171643-S100Z/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=S100Z
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WXG8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
