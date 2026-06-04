---
type: protein-evaluation
gene: "NUTM2A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NUTM2A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NUTM2A / FAM22A, KIAA2020 |
| 蛋白名称 | NUT family member 2A |
| 蛋白大小 | 878 aa / 93.9 kDa |
| UniProt ID | Q8IVF1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 878 aa / 93.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=27 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=46.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024310, IPR024309; Pfam: PF12881 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.5/180** | |
| **归一化总分** | | | **65.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 27 |
| PubMed broad count | 59 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM22A, KIAA2020 |

**关键文献**:
1. MAD::NUT Fusion Sarcoma: A Sarcoma Class With NUTM1, NUTM2A, and NUTM2G Fusions and Possibly Distinctive Subtypes.. *Modern pathology : an official journal of the United States and Canadian Academy of Pathology, Inc*. PMID: 39921028
2. Long Non-Coding RNA NUTM2A-AS1/miR-376a-3p/PRMT5 Axis Promotes Prostate Cancer Progression.. *Archivos espanoles de urologia*. PMID: 38583010
3. NUTM2A-AS1 as a potential key regulator in cancer: unraveling its ceRNA networks and impact on tumor biology.. *European journal of medical research*. PMID: 40903777
4. NR1D1-transactivated lncRNA NUTM2A-AS1 promotes chemoresistance and immune evasion in neuroblastoma via inhibiting B7-H3 degradation.. *Journal of cellular and molecular medicine*. PMID: 38785199
5. NFATC2::NUTM2A/B Fusions Characterize a Novel Indolent Myoepithelial-Like Neoplasm of the Lungs and Salivary Glands.. *Genes, chromosomes & cancer*. PMID: 40944358

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 46.3 |
| 高置信度残基 (pLDDT>90) 占比 | 6.5% |
| 置信残基 (pLDDT 70-90) 占比 | 10.7% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 75.2% |
| 有序区域 (pLDDT>70) 占比 | 17.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=46.3），有序残基占 17.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024310, IPR024309; Pfam: PF12881 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| YWHAE | 0.784 | 0.093 | — |
| NUTM2B | 0.768 | 0.000 | — |
| JAZF1 | 0.704 | 0.046 | — |
| ZC3H7B | 0.698 | 0.092 | — |
| EZHIP | 0.564 | 0.074 | — |
| PHF1 | 0.545 | 0.000 | — |
| MEAF6 | 0.527 | 0.000 | — |
| MBTD1 | 0.524 | 0.069 | — |
| ZC3H7A | 0.515 | 0.092 | — |
| SUZ12 | 0.483 | 0.049 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| actP | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 1
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=46.3 + PDB: 无 | pLDDT=46.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear bodies | 待确认 |
| PPI | STRING + IntAct | 13 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. NUTM2A — NUT family member 2A，非常新颖，仅有少数基础研究。
2. 蛋白大小878 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 27 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=46.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IVF1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184923-NUTM2A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NUTM2A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IVF1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
