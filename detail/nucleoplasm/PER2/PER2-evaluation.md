---
type: protein-evaluation
gene: "PER2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PER2 — REJECTED (研究热度过高 (PubMed strict=2023，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PER2 / KIAA0347 |
| 蛋白名称 | Period circadian protein homolog 2 |
| 蛋白大小 | 1255 aa / 136.6 kDa |
| UniProt ID | O15055 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm; Cytoplasm, perinuclear region; Nucleus,  |
| 蛋白大小 | 5/10 | ×1 | 5 | 1255 aa / 136.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2023 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=52.8; PDB: 6OF7, 8D7M, 8D7N, 8D7O |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000014, IPR035965, IPR013655, IPR057310, IPR048 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.5/180** | |
| **归一化总分** | | | **42.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Cytoplasm, perinuclear region; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Cry-Per complex (GO:1990512)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2023 |
| PubMed broad count | 3149 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0347 |

**关键文献**:
1. Unsaturated fat alters clock phosphorylation to align rhythms to the season in mice.. *Science (New York, N.Y.)*. PMID: 41129636
2. PER2 interaction with HSP70 promotes cuproptosis in oral squamous carcinoma cells by decreasing AKT stability.. *Cell death & disease*. PMID: 40113747
3. PER2 binding to HSP90 enhances immune response against oral squamous cell carcinoma by inhibiting IKK/NF-κB pathway and PD-L1 expression.. *Journal for immunotherapy of cancer*. PMID: 37914384
4. PER2 integrates circadian disruption and pituitary tumorigenesis.. *Theranostics*. PMID: 37215573
5. A Peripheral Mechanism of Depression: Disturbed Intestinal Epithelial Per2 Gene Expression Causes Depressive Behaviors in Mice with Circadian Rhythm Disruption via Gut Barrier Damage and Microbiota Dysbiosis.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40847793

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 52.8 |
| 高置信度残基 (pLDDT>90) 占比 | 14.9% |
| 置信残基 (pLDDT 70-90) 占比 | 16.0% |
| 中等置信 (pLDDT 50-70) 占比 | 7.5% |
| 低置信 (pLDDT<50) 占比 | 61.6% |
| 有序区域 (pLDDT>70) 占比 | 30.9% |
| 可用 PDB 条目 | 6OF7, 8D7M, 8D7N, 8D7O |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=52.8），有序残基占 30.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000014, IPR035965, IPR013655, IPR057310, IPR048814; Pfam: PF23170, PF08447, PF21353 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BHLHE41 | 0.999 | 0.968 | — |
| CSNK1E | 0.999 | 0.890 | — |
| CRY1 | 0.999 | 0.992 | — |
| CRY2 | 0.999 | 0.991 | — |
| PER3 | 0.998 | 0.963 | — |
| NR1D1 | 0.998 | 0.154 | — |
| PER1 | 0.997 | 0.968 | — |
| ARNTL | 0.997 | 0.963 | — |
| CSNK1D | 0.996 | 0.826 | — |
| BTRC | 0.993 | 0.720 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| O54954 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| TNFRSF14 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Sirt1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11902|pubmed:18662546 |
| Clock | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11902|pubmed:18662546 |
| Btrc | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11930|pubmed:17462724 |
| CSNK1E | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-11852|pubmed:17218255 |
| Bmal1 | psi-mi:"MI:0728"(gal4 vp16 complementation) | pubmed:18430226|imex:IM-18930 |
| Cry1 | psi-mi:"MI:0018"(two hybrid) | pubmed:23555304|imex:IM-20564 |
| Cry2 | psi-mi:"MI:0018"(two hybrid) | pubmed:23555304|imex:IM-20564 |
| CSNK2B | psi-mi:"MI:0018"(two hybrid) | pubmed:23555304|imex:IM-20564 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=52.8 + PDB: 6OF7, 8D7M, 8D7N, 8D7O | pLDDT=52.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, perinuclear region; / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. PER2 — Period circadian protein homolog 2，研究基础较多，新颖性有限。
2. 蛋白大小1255 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 2023 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=52.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2023 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15055
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132326-PER2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PER2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15055
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
