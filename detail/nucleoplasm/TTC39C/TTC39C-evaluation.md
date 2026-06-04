---
type: protein-evaluation
gene: "TTC39C"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TTC39C 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TTC39C / C18orf17 |
| 蛋白名称 | Tetratricopeptide repeat protein 39C |
| 蛋白大小 | 583 aa / 65.9 kDa |
| UniProt ID | Q8N584 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 583 aa / 65.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR019412, IPR011990; Pfam: PF10300 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 6 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.0/180** | |
| **归一化总分** | | | **76.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
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
| PubMed strict count | 11 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C18orf17 |

**关键文献**:
1. Integrative causal inference illuminates gene-environment interactions linking endocrine disruptors to female infertility.. *Ecotoxicology and environmental safety*. PMID: 40663944
2. Unraveling the Etiology of Dilated Cardiomyopathy through Differential miRNA-mRNA Interactome.. *Biomolecules*. PMID: 38785931
3. Ttc39c is a potential target for the treatment of lung cancer.. *BMC pulmonary medicine*. PMID: 36303158
4. A genome-wide association study implicates that the TTC39C gene is associated with diabetic maculopathy with decreased visual acuity.. *Ophthalmic genetics*. PMID: 31264924
5. Overexpression and Selective Anticancer Efficacy of ENO3 in STK11 Mutant Lung Cancers.. *Molecules and cells*. PMID: 31697874

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.4 |
| 高置信度残基 (pLDDT>90) 占比 | 62.1% |
| 置信残基 (pLDDT 70-90) 占比 | 22.8% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 9.6% |
| 有序区域 (pLDDT>70) 占比 | 84.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.4，有序区 84.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019412, IPR011990; Pfam: PF10300 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TTC9C | 0.510 | 0.000 | — |
| HAUS4 | 0.502 | 0.000 | — |
| TTC5 | 0.482 | 0.000 | — |
| C18orf21 | 0.442 | 0.000 | — |
| TTC26 | 0.405 | 0.000 | — |
| TTC4 | 0.401 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSPB1 | psi-mi:"MI:0097"(reverse ras recruitment system) | imex:IM-20864|pubmed:25277244 |
| TMEM43 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| Xpo7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29748336|pubmed:unassig |
| RAN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29748336|pubmed:unassig |
| RYBP | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:34316702|imex:IM-29168 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 6，IntAct interactions: 6
- 调控相关比例: 0 / 6 = 0%

**评价**: STRING 6 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.4 + PDB: 无 | pLDDT=85.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 6 + 6 interactions | 数据充分 |

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
1. TTC39C — Tetratricopeptide repeat protein 39C，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小583 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N584
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168234-TTC39C/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TTC39C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N584
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
