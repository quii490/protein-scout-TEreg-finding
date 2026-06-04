---
type: protein-evaluation
gene: "FAM114A1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM114A1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM114A1 / NOXP20 |
| 蛋白名称 | Protein NOXP20 |
| 蛋白大小 | 563 aa / 60.7 kDa |
| UniProt ID | Q8IWE2 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM114A1/IF_images/BJ-Human-fibroblast_1.jpg|BJ [Human fibroblast]]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM114A1/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus, Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 563 aa / 60.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007998; Pfam: PF05334 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 4 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Cytosol; 额外: Nucleoplasm | Enhanced |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NOXP20 |

**关键文献**:
1. Family with sequence similarity 114 member A1 orchestrates immune evasion in triple-negative breast cancer.. *Signal transduction and targeted therapy*. PMID: 41249116
2. Ganoderma lucidum (Curtis) P. Karst. Immunomodulatory Protein Has the Potential to Improve the Prognosis of Breast Cancer Through the Regulation of Key Prognosis-Related Genes.. *Pharmaceuticals (Basel, Switzerland)*. PMID: 39770537
3. FAM114A1 influences cardiac pathological remodeling by regulating angiotensin II signaling.. *JCI insight*. PMID: 35671117
4. A Boolean approach for novel hypoxia-related gene discovery.. *PloS one*. PMID: 36006949
5. Inhibition of Fam114A1 protects melanocytes from apoptosis through higher RACK1 expression.. *Aging*. PMID: 34837888

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.6 |
| 高置信度残基 (pLDDT>90) 占比 | 31.4% |
| 置信残基 (pLDDT 70-90) 占比 | 12.3% |
| 中等置信 (pLDDT 50-70) 占比 | 10.7% |
| 低置信 (pLDDT<50) 占比 | 45.6% |
| 有序区域 (pLDDT>70) 占比 | 43.7% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM114A1/FAM114A1-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=63.6），有序残基占 43.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007998; Pfam: PF05334 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAB2A | 0.640 | 0.610 | — |
| RAB2B | 0.530 | 0.512 | — |
| UNC119B | 0.436 | 0.000 | — |
| POSTN | 0.425 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SNAPIN | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| SCHIP1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| SPG21 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| RAB2B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RAB2A | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TNFRSF10D | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GDAP1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CMTM5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TNS2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:25814554|imex:IM-22632 |
| AGTRAP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 4，IntAct interactions: 14
- 调控相关比例: 0 / 4 = 0%

**评价**: STRING 4 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.6 + PDB: 无 | pLDDT=63.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Golgi apparatus, Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 4 + 14 interactions | 数据充分 |

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
1. FAM114A1 — Protein NOXP20，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小563 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=63.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IWE2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197712-FAM114A1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM114A1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IWE2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM114A1/FAM114A1-PAE.png]]




