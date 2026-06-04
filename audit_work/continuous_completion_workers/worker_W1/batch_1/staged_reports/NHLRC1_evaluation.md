---
type: protein-evaluation
gene: "NHLRC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NHLRC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NHLRC1 / EPM2B |
| 蛋白名称 | E3 ubiquitin-protein ligase NHLRC1 |
| 蛋白大小 | 395 aa / 42.3 kDa |
| UniProt ID | Q6VVB1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Endoplasmic reticulum; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 395 aa / 42.3 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=80 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011042, IPR001258, IPR050952, IPR001841, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Endoplasmic reticulum; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（批量模式），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 80 |
| PubMed broad count | 191 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EPM2B |

**关键文献**:
1. Lafora Disease.. **. PMID: 29489177
2. Polyglucosan storage myopathies.. *Molecular aspects of medicine*. PMID: 26278982
3. Progressive Myoclonus Epilepsy, Lafora Type.. **. PMID: 20301563
4. Lafora progressive myoclonus epilepsy: a meta-analysis of reported mutations in the first decade following the discovery of the EPM2A and NHLRC1 genes.. *Human mutation*. PMID: 19267391
5. Lafora disease: severe phenotype associated with homozygous deletion of the NHLRC1 gene.. *Journal of the neurological sciences*. PMID: 23317923

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.4 |
| 高置信度残基 (pLDDT>90) 占比 | 53.9% |
| 置信残基 (pLDDT 70-90) 占比 | 32.9% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 6.6% |
| 有序区域 (pLDDT>70) 占比 | 86.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.4，有序区 86.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011042, IPR001258, IPR050952, IPR001841, IPR013083; Pfam: PF14634 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EPM2A | 0.999 | 0.879 | — |
| GYS1 | 0.960 | 0.510 | — |
| PPP1R3C | 0.946 | 0.476 | — |
| AGL | 0.905 | 0.292 | — |
| CSTB | 0.825 | 0.000 | — |
| PRDM8 | 0.800 | 0.292 | — |
| STUB1 | 0.758 | 0.510 | — |
| KCTD7 | 0.725 | 0.000 | — |
| GYG1 | 0.720 | 0.089 | — |
| EPM2AIP1 | 0.700 | 0.065 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| NUDC | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| NUDCD3 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| ENSP00000345464.3 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| TK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HNRNPCL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| EPM2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PCK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TRIM47 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.4 + PDB: 无 | pLDDT=85.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. NHLRC1 — E3 ubiquitin-protein ligase NHLRC1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小395 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 80 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6VVB1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187566-NHLRC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NHLRC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6VVB1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
