---
type: protein-evaluation
gene: "OSGIN2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## OSGIN2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OSGIN2 / C8orf1 |
| 蛋白名称 | Oxidative stress-induced growth inhibitor 2 |
| 蛋白大小 | 505 aa / 56.7 kDa |
| UniProt ID | Q9Y236 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; UniProt: Midbody |
| 蛋白大小 | 10/10 | ×1 | 10 | 505 aa / 56.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036188, IPR029731 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Approved |
| UniProt | Midbody | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- midbody (GO:0030496)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C8orf1 |

**关键文献**:
1. A Nrf2-OSGIN1&2-HSP70 axis mediates cigarette smoke-induced endothelial detachment: implications for plaque erosion.. *Cardiovascular research*. PMID: 36804807
2. miR-199a-5p regulates HIF-1α and OSGIN2 and its expression is correlated to soft-tissue sarcoma patients' outcome.. *Oncology letters*. PMID: 28101243
3. Selective footprints and genes relevant to cold adaptation and other phenotypic traits are unscrambled in the genomes of divergently selected chicken breeds.. *Journal of animal science and biotechnology*. PMID: 36829208
4. The Osgin Gene Family: Underexplored Yet Essential Mediators of Oxidative Stress.. *Biomolecules*. PMID: 40149945
5. Tim-3 deficiency aggravates cadmium nephrotoxicity via regulation of NF-κB signaling and mitochondrial damage.. *International immunopharmacology*. PMID: 38176346

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.7 |
| 高置信度残基 (pLDDT>90) 占比 | 69.9% |
| 置信残基 (pLDDT 70-90) 占比 | 17.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.6% |
| 低置信 (pLDDT<50) 占比 | 8.7% |
| 有序区域 (pLDDT>70) 占比 | 87.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.7，有序区 87.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036188, IPR029731 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DECR1 | 0.905 | 0.105 | — |
| CALB1 | 0.845 | 0.109 | — |
| CA7 | 0.767 | 0.000 | — |
| CALB2 | 0.663 | 0.109 | — |
| NBN | 0.535 | 0.000 | — |
| FRMPD3 | 0.455 | 0.000 | — |
| S100G | 0.431 | 0.098 | — |
| MSL1 | 0.407 | 0.132 | — |
| GPR146 | 0.401 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| H1-1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 1
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.7 + PDB: 无 | pLDDT=87.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Midbody / Nucleoli | 一致 |
| PPI | STRING + IntAct | 9 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. OSGIN2 — Oxidative stress-induced growth inhibitor 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小505 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y236
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164823-OSGIN2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OSGIN2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y236
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
