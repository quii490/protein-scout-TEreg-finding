---
type: protein-evaluation
gene: "NEK6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NEK6 — REJECTED (研究热度过高 (PubMed strict=119，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NEK6 |
| 蛋白名称 | Serine/threonine-protein kinase Nek6 |
| 蛋白大小 | 313 aa / 35.7 kDa |
| UniProt ID | Q9HC98 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Centriolar satellite; UniProt: Cytoplasm; Nucleus; Nucleus speckle; Cytoplasm, cytoskeleton |
| 蛋白大小 | 10/10 | ×1 | 10 | 313 aa / 35.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=119 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011009, IPR000719, IPR017441, IPR001245, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **85.5/180** | |
| **归一化总分** | | | **47.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Centriolar satellite | Supported |
| UniProt | Cytoplasm; Nucleus; Nucleus speckle; Cytoplasm, cytoskeleton, microtubule organizing center, centros... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centriolar satellite (GO:0034451)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- microtubule (GO:0005874)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 119 |
| PubMed broad count | 176 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Phosphorylation of FOXN3 by NEK6 promotes pulmonary fibrosis through Smad signaling.. *Nature communications*. PMID: 39984467
2. NEK6 Regulates Redox Balance and DNA Damage Response in DU-145 Prostate Cancer Cells.. *Cells*. PMID: 36672191
3. Identification of NEK6 as a potential biomarker for prognosis in glioma and its functional implications.. *Journal of neuro-oncology*. PMID: 41369743
4. NIMA-related kinase-6 (NEK6) as an executable target in cancer.. *Clinical & translational oncology : official publication of the Federation of Spanish Oncology Societies and of the National Cancer Institute of Mexico*. PMID: 36074296
5. Predictive Role of NEK6 in Prognosis and Immune Infiltration in Head and Neck Squamous Cell Carcinoma.. *Frontiers in endocrinology*. PMID: 35898455

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.2 |
| 高置信度残基 (pLDDT>90) 占比 | 58.5% |
| 置信残基 (pLDDT 70-90) 占比 | 22.0% |
| 中等置信 (pLDDT 50-70) 占比 | 4.8% |
| 低置信 (pLDDT<50) 占比 | 14.7% |
| 有序区域 (pLDDT>70) 占比 | 80.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=83.2，有序区 80.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR000719, IPR017441, IPR001245, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NEK9 | 0.975 | 0.842 | — |
| NEK7 | 0.946 | 0.836 | — |
| RCC1L | 0.843 | 0.091 | — |
| BICD2 | 0.777 | 0.000 | — |
| ANKS3 | 0.746 | 0.473 | — |
| DENND1A | 0.733 | 0.000 | — |
| ANKS6 | 0.731 | 0.461 | — |
| CRB2 | 0.668 | 0.041 | — |
| EML4 | 0.655 | 0.337 | — |
| LHX2 | 0.654 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CCDC85B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PIN1 | psi-mi:"MI:0096"(pull down) | pubmed:16476580|imex:IM-19382 |
| NEK9 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MB2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CCAR2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| WEE1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SMC2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ENSP00000442636.1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| XPO5 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| NUP93 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.2 + PDB: 无 | pLDDT=83.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Nucleus speckle; Cytoplasm, cy / Nucleoplasm, Cytosol; 额外: Centriolar satellite | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NEK6 — Serine/threonine-protein kinase Nek6，研究基础较多，新颖性有限。
2. 蛋白大小313 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 119 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 119 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HC98
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119408-NEK6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NEK6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HC98
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/NEK6/NEK6-PAE.png]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/NEK6/NEK6-PAE.png]]
