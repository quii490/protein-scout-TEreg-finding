---
type: protein-evaluation
gene: "GALNT12"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GALNT12 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GALNT12 |
| 蛋白名称 | Polypeptide N-acetylgalactosaminyltransferase 12 |
| 蛋白大小 | 581 aa / 66.9 kDa |
| UniProt ID | Q8IXK2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane; 额外: Nucleoplasm, Cell Junctions; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 581 aa / 66.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=27 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=93.5; PDB: 6PXU |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045885, IPR001173, IPR029044, IPR035992, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.0/180** | |
| **归一化总分** | | | **65.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm, Cell Junctions | Approved |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 27 |
| PubMed broad count | 41 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Interaction between GALNT12 and C1GALT1 Associates with Galactose-Deficient IgA1 and IgA Nephropathy.. *Journal of the American Society of Nephrology : JASN*. PMID: 33593824
2. Identification of <italic>GALNT12</italic> as a Novel Potential Diagnostic and Prognostic Marker for Esophageal Squamous Cell Carcinoma by Integrated Bioinformatics Analysis.. *Digestion*. PMID: 40334654
3. GALNT12 promotes fibrosarcoma growth by accelerating YAP1 nuclear localization.. *Oncology letters*. PMID: 38020290
4. Inactivating germ-line and somatic mutations in polypeptide N-acetylgalactosaminyltransferase 12 in human colon cancers.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 19617566
5. GALNT12 is associated with the malignancy of glioma and promotes glioblastoma multiforme in vitro by activating Akt signaling.. *Biochemical and biophysical research communications*. PMID: 35461073

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.5 |
| 高置信度残基 (pLDDT>90) 占比 | 88.5% |
| 置信残基 (pLDDT 70-90) 占比 | 3.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.1% |
| 低置信 (pLDDT<50) 占比 | 4.6% |
| 有序区域 (pLDDT>70) 占比 | 92.3% |
| 可用 PDB 条目 | 6PXU |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.5，有序区 92.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045885, IPR001173, IPR029044, IPR035992, IPR000772; Pfam: PF00535, PF00652 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GCNT1 | 0.964 | 0.000 | — |
| ST6GALNAC1 | 0.931 | 0.000 | — |
| B3GNT6 | 0.923 | 0.000 | — |
| C1GALT1C1 | 0.837 | 0.000 | — |
| C1GALT1 | 0.815 | 0.000 | — |
| MUC5AC | 0.785 | 0.292 | — |
| C1GALT1C1L | 0.769 | 0.000 | — |
| MUC1 | 0.767 | 0.293 | — |
| POLD1 | 0.756 | 0.000 | — |
| MUC7 | 0.743 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HPX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MGAT4C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| B3GNT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PIANP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ODAPH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LAMP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HLA-E | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RXYLT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TMPRSS11B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TCTN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.5 + PDB: 6PXU | pLDDT=93.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Plasma membrane; 额外: Nucleoplasm, Cell Junctions | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GALNT12 — Polypeptide N-acetylgalactosaminyltransferase 12，非常新颖，仅有少数基础研究。
2. 蛋白大小581 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 27 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IXK2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119514-GALNT12/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GALNT12
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IXK2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
