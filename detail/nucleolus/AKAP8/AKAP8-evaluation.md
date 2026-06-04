---
type: protein-evaluation
gene: "AKAP8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AKAP8 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AKAP8 / AKAP95 |
| 蛋白名称 | A-kinase anchor protein 8 |
| 蛋白大小 | 692 aa / 76.1 kDa |
| UniProt ID | O43823 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Nucleus matrix; Nucleus, nucleolus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 692 aa / 76.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=52.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007071, IPR034736; Pfam: PF04988 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Nucleus matrix; Nucleus, nucleolus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- condensed chromosome (GO:0000793)
- cytoplasm (GO:0005737)
- female pronucleus (GO:0001939)
- membrane (GO:0016020)
- nuclear matrix (GO:0016363)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 68 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AKAP95 |

**关键文献**:
1. Unbiased multitissue transcriptomic analysis reveals complex neuroendocrine regulatory networks mediated by spinal cord injury-induced immunodeficiency.. *Journal of neuroinflammation*. PMID: 37775760
2. The RNA-binding protein AKAP8 suppresses tumor metastasis by antagonizing EMT-associated alternative splicing.. *Nature communications*. PMID: 31980632
3. AKAP8 promotes ovarian cancer progression and antagonizes PARP inhibitor sensitivity through regulating hnRNPUL1 transcription.. *iScience*. PMID: 38711442
4. ZNF384-Related Fusion Genes in Acute Lymphoblastic Leukemia.. *Cancer control : journal of the Moffitt Cancer Center*. PMID: 37306722
5. PKA-binding domain of AKAP8 is essential for direct interaction with DPY30 protein.. *The FEBS journal*. PMID: 29288530

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 52.6 |
| 高置信度残基 (pLDDT>90) 占比 | 2.5% |
| 置信残基 (pLDDT 70-90) 占比 | 20.8% |
| 中等置信 (pLDDT 50-70) 占比 | 13.4% |
| 低置信 (pLDDT<50) 占比 | 63.3% |
| 有序区域 (pLDDT>70) 占比 | 23.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=52.6），有序残基占 23.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007071, IPR034736; Pfam: PF04988 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AKAP1 | 0.903 | 0.000 | — |
| AKAP5 | 0.842 | 0.000 | — |
| PRKACA | 0.834 | 0.190 | — |
| DPY30 | 0.829 | 0.292 | — |
| PRKACB | 0.814 | 0.095 | — |
| PRKACG | 0.803 | 0.000 | — |
| AKAP10 | 0.715 | 0.000 | — |
| AKAP9 | 0.702 | 0.045 | — |
| AKAP11 | 0.697 | 0.000 | — |
| AKAP8L | 0.689 | 0.287 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Iqcb1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| Rpgrip1l | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| CSNK2A1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22113938|imex:IM-16640 |
| Tfcp2l1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| Aurkb | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Mis12 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| ESR1 | psi-mi:"MI:0029"(cosedimentation through density g | imex:IM-13780|pubmed:21182205 |
| ESR2 | psi-mi:"MI:0029"(cosedimentation through density g | imex:IM-13781|pubmed:21182203 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=52.6 + PDB: 无 | pLDDT=52.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Nucleus matrix; Nucleus, nucleolus; Cytop / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. AKAP8 — A-kinase anchor protein 8，非常新颖，仅有少数基础研究。
2. 蛋白大小692 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=52.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43823
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105127-AKAP8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AKAP8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43823
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/AKAP8/IF_images/AKAP8_IF_69_E2_1_red_green.jpg]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/AKAP8/AKAP8-PAE.png]]
