---
type: protein-evaluation
gene: "FAM181A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM181A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM181A / C14orf152 |
| 蛋白名称 | Protein FAM181A |
| 蛋白大小 | 354 aa / 38.7 kDa |
| UniProt ID | Q8N9Y4 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM181A/IF_images/U2OS_1.jpg|U2OS]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM181A/IF_images/AF22_1.jpg|AF22]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 354 aa / 38.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.3; PDB: 6L9F, 6SEN |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029359, IPR053819; Pfam: PF15238 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C14orf152 |

**关键文献**:
1. Knockout of the family with sequence similarity 181, member A (Fam181a) gene does not impair spermatogenesis or male fertility in the mouse.. *Reproduction, fertility, and development*. PMID: 34253288
2. Decreased Expression of a Novel lncRNA FAM181A-AS1 is Associated with Poor Prognosis and Immune Infiltration in Lung Adenocarcinoma.. *Pharmacogenomics and personalized medicine*. PMID: 36482943
3. Epigenome variation in severe asthma.. *Biological research for nursing*. PMID: 25288825
4. Analysis of the Fam181 gene family during mouse development reveals distinct strain-specific expression patterns, suggesting a role in nervous system development and function.. *Gene*. PMID: 26407640
5. Identification of Three Prognosis-Related Differentially Expressed lncRNAs Driven by Copy Number Variation in Thyroid Cancer.. *Journal of immunology research*. PMID: 35642209

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.3 |
| 高置信度残基 (pLDDT>90) 占比 | 9.3% |
| 置信残基 (pLDDT 70-90) 占比 | 11.6% |
| 中等置信 (pLDDT 50-70) 占比 | 47.2% |
| 低置信 (pLDDT<50) 占比 | 31.9% |
| 有序区域 (pLDDT>70) 占比 | 20.9% |
| 可用 PDB 条目 | 6L9F, 6SEN |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM181A/FAM181A-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=59.3），有序残基占 20.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029359, IPR053819; Pfam: PF15238 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TEAD4 | 0.907 | 0.907 | — |
| LRRC43 | 0.609 | 0.000 | — |
| TEX43 | 0.567 | 0.000 | — |
| MRI1 | 0.540 | 0.000 | — |
| OR13J1 | 0.522 | 0.000 | — |
| KRTAP19-7 | 0.507 | 0.000 | — |
| OR6X1 | 0.507 | 0.000 | — |
| CFAP47 | 0.497 | 0.000 | — |
| C1orf189 | 0.480 | 0.000 | — |
| ZNF718 | 0.479 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CLYBL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PSMG3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DIS3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.3 + PDB: 6L9F, 6SEN | pLDDT=59.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FAM181A — Protein FAM181A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小354 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=59.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N9Y4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140067-FAM181A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM181A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N9Y4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM181A/FAM181A-PAE.png]]




