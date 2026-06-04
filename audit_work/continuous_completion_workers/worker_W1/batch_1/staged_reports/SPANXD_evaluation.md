---
type: protein-evaluation
gene: "SPANXD"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPANXD 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPANXD / SPANXE |
| 蛋白名称 | Sperm protein associated with the nucleus on the X chromosome D |
| 蛋白大小 | 97 aa / 11.0 kDa |
| UniProt ID | Q9BXN6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 97 aa / 11.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR010007; Pfam: PF07458 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.0/180** | |
| **归一化总分** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（批量模式），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SPANXE |

**关键文献**:
1. Hypermethylation of genes in testicular embryonal carcinomas.. *British journal of cancer*. PMID: 26625006
2. Hominoid-specific SPANXA/D genes demonstrate differential expression in individuals and protein localization to a distinct nuclear envelope domain during spermatid morphogenesis.. *Molecular human reproduction*. PMID: 17012309
3. Multiomic Selection of Cancer-Testis Antigens as Precision Immuno-oncologic Targets in Head and Neck Cancer.. *JAMA otolaryngology-- head & neck surgery*. PMID: 41129177
4. Mutational analysis of SPANX genes in families with X-linked prostate cancer.. *The Prostate*. PMID: 17373721

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.9 |
| 高置信度残基 (pLDDT>90) 占比 | 6.2% |
| 置信残基 (pLDDT 70-90) 占比 | 39.2% |
| 中等置信 (pLDDT 50-70) 占比 | 44.3% |
| 低置信 (pLDDT<50) 占比 | 10.3% |
| 有序区域 (pLDDT>70) 占比 | 45.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=68.9），有序残基占 45.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010007; Pfam: PF07458 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SPANXN4 | 0.655 | 0.000 | — |
| SRY | 0.652 | 0.000 | — |
| GAGE2A | 0.603 | 0.000 | — |
| GAGE2E | 0.602 | 0.000 | — |
| SPANXN3 | 0.583 | 0.000 | — |
| XAGE2 | 0.570 | 0.000 | — |
| GAGE1 | 0.555 | 0.000 | — |
| LGALS4 | 0.551 | 0.046 | — |
| GAGE12G | 0.541 | 0.000 | — |
| SETBP1 | 0.525 | 0.521 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FLNA | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SETBP1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SPANXB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.9 + PDB: 无 | pLDDT=68.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

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
1. SPANXD — Sperm protein associated with the nucleus on the X chromosome D，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小97 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=68.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BXN6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196406-SPANXD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPANXD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BXN6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
