---
type: protein-evaluation
gene: "SRI"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SRI — REJECTED (研究热度过高 (PubMed strict=1302，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SRI |
| 蛋白名称 | Sorcin |
| 蛋白大小 | 198 aa / 21.7 kDa |
| UniProt ID | P30626 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Sarcoplasmic reticulum membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 198 aa / 21.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1302 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=84.9; PDB: 1JUO, 2JC2, 4U8D, 4UPG, 4USL, 5MRA |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011992, IPR018247, IPR002048; Pfam: PF13499, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.5/180** | |
| **归一化总分** | | | **51.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm; Sarcoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum membrane (GO:0005789)
- extracellular exosome (GO:0070062)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- sarcoplasmic reticulum (GO:0016529)
- sarcoplasmic reticulum membrane (GO:0033017)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1302 |
| PubMed broad count | 51044 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A small molecule that induces translational readthrough of CFTR nonsense mutations by eRF1 depletion.. *Nature communications*. PMID: 34272367
2. Predictive biomarkers for low-dose IL-2 therapy efficacy in systemic lupus erythematosus: a clinical analysis.. *Arthritis research & therapy*. PMID: 39438922
3. Landscape of Genomic Mechanisms of Resistance to Selective RET Inhibitors in RET-Altered Solid Tumors: Analysis of the RETgistry Global Consortium.. *Clinical cancer research : an official journal of the American Association for Cancer Research*. PMID: 41537704
4. Morphological and odorant-binding protein 1 gene intron 1 sequence variations in Anopheles stephensi from Jaffna city in northern Sri Lanka.. *Medical and veterinary entomology*. PMID: 35838413
5. Phylogenetic and phylogeographic insights into Sri Lankan killifishes (Teleostei: Aplocheilidae).. *Journal of fish biology*. PMID: 38769734

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.9 |
| 高置信度残基 (pLDDT>90) 占比 | 70.7% |
| 置信残基 (pLDDT 70-90) 占比 | 13.6% |
| 中等置信 (pLDDT 50-70) 占比 | 2.5% |
| 低置信 (pLDDT<50) 占比 | 13.1% |
| 有序区域 (pLDDT>70) 占比 | 84.3% |
| 可用 PDB 条目 | 1JUO, 2JC2, 4U8D, 4UPG, 4USL, 5MRA |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1JUO, 2JC2, 4U8D, 4UPG, 4USL, 5MRA）+ AlphaFold极高置信度预测（pLDDT=84.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011992, IPR018247, IPR002048; Pfam: PF13499, PF13833 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RYR2 | 0.973 | 0.516 | — |
| PSEN2 | 0.939 | 0.301 | — |
| ANXA7 | 0.936 | 0.622 | — |
| TRDN | 0.915 | 0.044 | — |
| CALM3 | 0.865 | 0.000 | — |
| CALML3 | 0.845 | 0.000 | — |
| CALML5 | 0.845 | 0.000 | — |
| CALML6 | 0.843 | 0.000 | — |
| CALML4 | 0.843 | 0.000 | — |
| NEK8 | 0.727 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.9 + PDB: 1JUO, 2JC2, 4U8D, 4UPG, 4USL,  | pLDDT=84.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Sarcoplasmic reticulum membrane / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. SRI — Sorcin，研究基础较多，新颖性有限。
2. 蛋白大小198 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 1302 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1302 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P30626
- Protein Atlas: https://www.proteinatlas.org/ENSG00000075142-SRI/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SRI
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P30626
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
