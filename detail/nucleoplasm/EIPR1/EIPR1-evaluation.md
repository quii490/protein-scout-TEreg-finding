---
type: protein-evaluation
gene: "EIPR1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EIPR1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIPR1 / TSSC1 |
| 蛋白名称 | EARP and GARP complex-interacting protein 1 |
| 蛋白大小 | 387 aa / 43.6 kDa |
| UniProt ID | Q53HC9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Nucleoli; 额外: Intermediate filaments; UniProt: Golgi apparatus, trans-Golgi network |
| 蛋白大小 | 10/10 | ×1 | 10 | 387 aa / 43.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR059104, IPR040323, IPR015943, IPR019775, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli; 额外: Intermediate filaments | Supported |
| UniProt | Golgi apparatus, trans-Golgi network | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- trans-Golgi network (GO:0005802)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TSSC1 |

**关键文献**:
1. EIPR1 variants cause a neurodevelopmental disorder with endolysosomal and dense core vesicle defects.. *Brain : a journal of neurology*. PMID: 41058046
2. Pan-cancer analysis identifies EIPR1 as a potential prognostic and immunological biomarker for lung adenocarcinoma and its functional validation.. *Gene*. PMID: 40154585
3. EIPR1 controls dense-core vesicle cargo retention and EARP complex localization in insulin-secreting cells.. *Molecular biology of the cell*. PMID: 31721635
4. Genome-wide association study of pain sensitivity assessed by questionnaire and the cold pressor test.. *Pain*. PMID: 34924555
5. Genome-Wide Variants Associated With Longitudinal Survival Outcomes Among Individuals With Coronary Artery Disease.. *Frontiers in genetics*. PMID: 34140969

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.1 |
| 高置信度残基 (pLDDT>90) 占比 | 78.3% |
| 置信残基 (pLDDT 70-90) 占比 | 9.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.6% |
| 低置信 (pLDDT<50) 占比 | 8.3% |
| 有序区域 (pLDDT>70) 占比 | 88.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.1，有序区 88.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR059104, IPR040323, IPR015943, IPR019775, IPR001680; Pfam: PF23609, PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VPS50 | 0.943 | 0.842 | — |
| VPS51 | 0.938 | 0.839 | — |
| VPS54 | 0.929 | 0.836 | — |
| VPS53 | 0.923 | 0.822 | — |
| VPS52 | 0.863 | 0.717 | — |
| CCDC186 | 0.717 | 0.000 | — |
| TRAPPC12 | 0.646 | 0.000 | — |
| DTNBP1 | 0.627 | 0.321 | — |
| RNF144A | 0.582 | 0.000 | — |
| RAB2A | 0.518 | 0.237 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| QRICH2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TXN | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CDK2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| DEGS1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MOB1A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MAGEA6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CCAR2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SERBP1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| NSS | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |
| VPS50 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.1 + PDB: 无 | pLDDT=89.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus, trans-Golgi network / Nucleoplasm, Nucleoli; 额外: Intermediate filaments | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. EIPR1 — EARP and GARP complex-interacting protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小387 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q53HC9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000032389-EIPR1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIPR1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q53HC9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
