---
type: protein-evaluation
gene: "SBF1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SBF1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SBF1 / MTMR5 |
| 蛋白名称 | Myotubularin-related protein 5 |
| 蛋白大小 | 1868 aa / 208.4 kDa |
| UniProt ID | O95248 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; UniProt: Cytoplasm; Cytoplasm, perinuclear region; Cell projection, n |
| 蛋白大小 | 5/10 | ×1 | 5 | 1868 aa / 208.4 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=59 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001194, IPR005112, IPR043153, IPR004182, IPR030 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Supported |
| UniProt | Cytoplasm; Cytoplasm, perinuclear region; Cell projection, neuron projection | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（批量模式），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum membrane (GO:0005789)
- membrane (GO:0016020)
- neuron projection (GO:0043005)
- nuclear body (GO:0016604)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 59 |
| PubMed broad count | 92 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MTMR5 |

**关键文献**:
1. Selective mitophagy activation and protein aggregate accumulation in MTMR5/SBF1-deficient fibroblasts.. *Life sciences*. PMID: 40998285
2. A novel SBF1 missense mutation causes autosomal dominant Charcot-Marie-Tooth disease type 4B3.. *Frontiers in neurology*. PMID: 39664754
3. Establishment and characterization of three human pluripotent stem cell lines from Charcot-Marie-Tooth disease Type 4B3 patients bearing mutations in MTMR5/Sbf1 gene.. *Stem cell research*. PMID: 39461113
4. Recent advances in Charcot-Marie-Tooth disease.. *Current opinion in neurology*. PMID: 25110935
5. WANTED - Dead or alive: Myotubularins, a large disease-associated protein family.. *Advances in biological regulation*. PMID: 27666502

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.8 |
| 高置信度残基 (pLDDT>90) 占比 | 31.1% |
| 置信残基 (pLDDT 70-90) 占比 | 37.6% |
| 中等置信 (pLDDT 50-70) 占比 | 10.7% |
| 低置信 (pLDDT<50) 占比 | 20.6% |
| 有序区域 (pLDDT>70) 占比 | 68.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=73.8，有序区 68.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001194, IPR005112, IPR043153, IPR004182, IPR030564; Pfam: PF02141, PF02893, PF06602 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MTMR2 | 0.993 | 0.756 | — |
| MTMR1 | 0.860 | 0.704 | — |
| FZR1 | 0.841 | 0.000 | — |
| KMT2A | 0.755 | 0.368 | — |
| RAB21 | 0.720 | 0.136 | — |
| MTMR6 | 0.614 | 0.000 | — |
| FIG4 | 0.611 | 0.000 | — |
| SH3TC2 | 0.610 | 0.000 | — |
| SUV39H1 | 0.597 | 0.331 | — |
| FGD4 | 0.585 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| trx | psi-mi:"MI:0045"(experimental interaction detectio | pubmed:unassigned4 |
| Spn | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| dlp | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Fas2 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| ABF1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| CALM1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:16512683|imex:IM-19867 |
| GLC7 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14660704 |
| SIRT3 | psi-mi:"MI:0096"(pull down) | imex:IM-12078|pubmed:19343720 |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SIS1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.8 + PDB: 无 | pLDDT=73.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, perinuclear region; Cell pro / Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. SBF1 — Myotubularin-related protein 5，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1868 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 59 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95248
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100241-SBF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SBF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95248
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
