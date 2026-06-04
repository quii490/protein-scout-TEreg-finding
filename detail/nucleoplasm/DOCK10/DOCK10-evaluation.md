---
type: protein-evaluation
gene: "DOCK10"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DOCK10 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DOCK10 / KIAA0694, ZIZ3 |
| 蛋白名称 | Dedicator of cytokinesis protein 10 |
| 蛋白大小 | 2186 aa / 249.5 kDa |
| UniProt ID | Q96BY6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Nucleus; Cytoplasm; Cell projection, dendritic spine |
| 蛋白大小 | 2/10 | ×1 | 2 | 2186 aa / 249.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=75.5; PDB: 6TKY, 6TKZ, 6TM1, 7Q43 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037809, IPR027007, IPR035892, IPR026791, IPR021 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Cell projection, dendritic spine | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendritic spine (GO:0043197)
- extracellular exosome (GO:0070062)
- glutamatergic synapse (GO:0098978)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 47 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0694, ZIZ3 |

**关键文献**:
1. Roles of the DOCK-D family proteins in a mouse model of neuroinflammation.. *The Journal of biological chemistry*. PMID: 32241915
2. Dock10 Regulates Cardiac Function under Neurohormonal Stress.. *International journal of molecular sciences*. PMID: 36077014
3. DOCK10 Regulates Insulin Hypersecretion in Insulinoma and Serves as a Diagnostic and Therapeutic Target.. *Cellular and molecular gastroenterology and hepatology*. PMID: 41389876
4. The RhoGEF DOCK10 is essential for dendritic spine morphogenesis.. *Molecular biology of the cell*. PMID: 25851601
5. Dock10, a novel CZH protein selectively induced by interleukin-4 in human B lymphocytes.. *Molecular immunology*. PMID: 18499258

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.5 |
| 高置信度残基 (pLDDT>90) 占比 | 28.1% |
| 置信残基 (pLDDT 70-90) 占比 | 46.3% |
| 中等置信 (pLDDT 50-70) 占比 | 7.5% |
| 低置信 (pLDDT<50) 占比 | 18.2% |
| 有序区域 (pLDDT>70) 占比 | 74.4% |
| 可用 PDB 条目 | 6TKY, 6TKZ, 6TM1, 7Q43 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（6TKY, 6TKZ, 6TM1, 7Q43）+ AlphaFold高质量预测（pLDDT=75.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037809, IPR027007, IPR035892, IPR026791, IPR021816; Pfam: PF06920, PF20422, PF20421 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC42 | 0.983 | 0.922 | — |
| RAC3 | 0.953 | 0.914 | — |
| HERC2 | 0.901 | 0.900 | — |
| DHX37 | 0.892 | 0.000 | — |
| DHX8 | 0.866 | 0.000 | — |
| RAC2 | 0.654 | 0.184 | — |
| RAC1 | 0.648 | 0.184 | — |
| RHOF | 0.637 | 0.127 | — |
| RHOJ | 0.630 | 0.177 | — |
| DOCK9 | 0.623 | 0.447 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LURAP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| hdlbp.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |
| Lat | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-25620|pubmed:24584089 |
| VIM | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| MKI67 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26949251|imex:IM-26415 |
| CSTF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| TRIO | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| CCDC102B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HAL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DOCK9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 13
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.5 + PDB: 6TKY, 6TKZ, 6TM1, 7Q43 | pLDDT=75.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cell projection, dendritic spi / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 13 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DOCK10 — Dedicator of cytokinesis protein 10，非常新颖，仅有少数基础研究。
2. 蛋白大小2186 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96BY6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135905-DOCK10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DOCK10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96BY6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DOCK10/IF_images/DOCK10_BJ_31.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DOCK10/IF_images/DOCK10_BJ_32.jpg]]
