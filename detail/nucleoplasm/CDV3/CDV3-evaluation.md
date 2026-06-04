---
type: protein-evaluation
gene: "CDV3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CDV3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CDV3 / H41 |
| 蛋白名称 | Protein CDV3 homolog |
| 蛋白大小 | 258 aa / 27.3 kDa |
| UniProt ID | Q9UKY7 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CDV3/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/CDV3/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoli, Plasma membrane; UniProt: Cytoplasm |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 258 aa / 27.3 kDa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.7; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026806; Pfam: PF15359 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.0/180** | |
| **归一化总分** | | | **60.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoli, Plasma membrane | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 26 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: H41 |

**关键文献**:
1. Quantitative proteomics combined independent PRM analysis reveals the mitochondrial and synaptic mechanism underlying norisoboldine's antidepressant effects.. *Translational psychiatry*. PMID: 39358323
2. ZipN, an FtsA-like orchestrator of divisome assembly in the model cyanobacterium Synechocystis PCC6803.. *Molecular microbiology*. PMID: 19737354
3. The potential value of CDV3 in the prognosis evaluation in Hepatocellular carcinoma.. *Genes & diseases*. PMID: 30258946
4. Identification of cyanobacterial cell division genes by comparative and mutational analyses.. *Molecular microbiology*. PMID: 15773984
5. Targeted Proteomics for Multiplexed Verification of Markers of Colorectal Tumorigenesis.. *Molecular & cellular proteomics : MCP*. PMID: 28062797

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.7 |
| 高置信度残基 (pLDDT>90) 占比 | 0.8% |
| 置信残基 (pLDDT 70-90) 占比 | 27.1% |
| 中等置信 (pLDDT 50-70) 占比 | 44.6% |
| 低置信 (pLDDT<50) 占比 | 27.5% |
| 有序区域 (pLDDT>70) 占比 | 27.9% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=59.7），有序残基占 27.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026806; Pfam: PF15359 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AKAP5 | 0.601 | 0.000 | — |
| H2AC18 | 0.593 | 0.000 | — |
| H2AC20 | 0.590 | 0.000 | — |
| H2BC21 | 0.569 | 0.000 | — |
| PA2G4 | 0.535 | 0.000 | — |
| CASC4 | 0.506 | 0.000 | — |
| H1-6 | 0.506 | 0.000 | — |
| TXLNG | 0.497 | 0.480 | — |
| QKI | 0.462 | 0.438 | — |
| ZFAND6 | 0.461 | 0.462 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| PTPN1 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| SHC1 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| - | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| ERBIN | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| LRP4 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| VAV1 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| FES | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| IGF1R | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| DUSP3 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 15
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.7 + PDB: 无 | pLDDT=59.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol; 额外: Nucleoli, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 14 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CDV3 — Protein CDV3 homolog，非常新颖，仅有少数基础研究。
2. 蛋白大小258 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=59.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UKY7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000091527-CDV3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CDV3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UKY7
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:45:50
