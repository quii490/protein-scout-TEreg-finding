---
type: protein-evaluation
gene: "TTC36"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TTC36 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TTC36 / HBP21 |
| 蛋白名称 | Tetratricopeptide repeat protein 36 |
| 蛋白大小 | 189 aa / 20.9 kDa |
| UniProt ID | A6NLP5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 5/10 | ×4 | 20 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 189 aa / 20.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011990, IPR019734, IPR038906; Pfam: PF13424 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Uncertain |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据存在但较为混杂，部分数据源指向非核区室。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 27 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HBP21 |

**关键文献**:
1. TTC36 promotes proliferation and drug resistance in hepatocellular carcinoma cells by inhibiting c-Myc degradation.. *Cell death & disease*. PMID: 40274799
2. Tetratricopeptide repeat domain 36 deficiency mitigates renal tubular injury by inhibiting TGF-β1-induced epithelial-mesenchymal transition in a mouse model of chronic kidney disease.. *Genes & diseases*. PMID: 36157495
3. HPD degradation regulated by the TTC36-STK33-PELI1 signaling axis induces tyrosinemia and neurological damage.. *Nature communications*. PMID: 31537781
4. TTC36 inactivation induce malignant properties via Wnt-β-catenin pathway in gastric carcinoma.. *Journal of Cancer*. PMID: 33854620
5. Single-cell reconstruction and mutation enrichment analysis identifies dysregulated cardiomyocyte and endothelial cells in congenital heart disease.. *Physiological genomics*. PMID: 37811720

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.8 |
| 高置信度残基 (pLDDT>90) 占比 | 58.7% |
| 置信残基 (pLDDT 70-90) 占比 | 23.8% |
| 中等置信 (pLDDT 50-70) 占比 | 16.4% |
| 低置信 (pLDDT<50) 占比 | 1.1% |
| 有序区域 (pLDDT>70) 占比 | 82.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.8，有序区 82.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011990, IPR019734, IPR038906; Pfam: PF13424 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HPD | 0.686 | 0.327 | — |
| HGD | 0.640 | 0.000 | — |
| FAH | 0.577 | 0.000 | — |
| HSPA4 | 0.508 | 0.000 | — |
| STK33 | 0.473 | 0.000 | — |
| RNF138 | 0.454 | 0.000 | — |
| TMEM74B | 0.432 | 0.000 | — |
| SRCIN1 | 0.422 | 0.000 | — |
| GCC2 | 0.418 | 0.000 | — |
| TTC38 | 0.416 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENST00000302783 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 1
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.8 + PDB: 无 | pLDDT=85.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 10 + 1 interactions | 数据充分 |

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
1. TTC36 — Tetratricopeptide repeat protein 36，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小189 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NLP5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172425-TTC36/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TTC36
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NLP5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
