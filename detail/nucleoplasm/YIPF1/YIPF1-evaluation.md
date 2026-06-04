---
type: protein-evaluation
gene: "YIPF1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## YIPF1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | YIPF1 |
| 蛋白名称 | Protein YIPF1 |
| 蛋白大小 | 306 aa / 34.3 kDa |
| UniProt ID | Q9Y548 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; 额外: Nucleoplasm, Plasma membrane; UniProt: Golgi apparatus, cis-Golgi network membrane; Golgi apparatus |
| 蛋白大小 | 10/10 | ×1 | 10 | 306 aa / 34.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR006977, IPR039765; Pfam: PF04893 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm, Plasma membrane | Supported |
| UniProt | Golgi apparatus, cis-Golgi network membrane; Golgi apparatus, trans-Golgi network membrane; Late end... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)
- Golgi medial cisterna (GO:0005797)
- Golgi trans cisterna (GO:0000138)
- late endosome membrane (GO:0031902)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)
- trans-Golgi network (GO:0005802)
- transport vesicle (GO:0030133)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of Crucial Candidate Genes and Pathways in Glioblastoma Multiform by Bioinformatics Analysis.. *Biomolecules*. PMID: 31137733
2. A two-stage hybrid gene selection algorithm combined with machine learning models to predict the rupture status in intracranial aneurysms.. *Frontiers in neuroscience*. PMID: 36340761
3. Functional characterisation of the YIPF protein family in mammalian cells.. *Histochemistry and cell biology*. PMID: 27999994
4. YIPF1, YIPF2, and YIPF6 are medial-/trans-Golgi and trans-Golgi network-localized Yip domain family proteins, which play a role in the Golgi reassembly and glycan synthesis.. *Experimental cell research*. PMID: 28286305

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.8 |
| 高置信度残基 (pLDDT>90) 占比 | 53.6% |
| 置信残基 (pLDDT 70-90) 占比 | 13.7% |
| 中等置信 (pLDDT 50-70) 占比 | 7.8% |
| 低置信 (pLDDT<50) 占比 | 24.8% |
| 有序区域 (pLDDT>70) 占比 | 67.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=76.8，有序区 67.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006977, IPR039765; Pfam: PF04893 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FBXO32 | 0.946 | 0.000 | — |
| YIPF6 | 0.900 | 0.777 | — |
| TRIM63 | 0.875 | 0.000 | — |
| YIPF3 | 0.835 | 0.000 | — |
| FBXO25 | 0.776 | 0.000 | — |
| YIPF4 | 0.711 | 0.245 | — |
| MSTN | 0.666 | 0.000 | — |
| MYH6 | 0.639 | 0.000 | — |
| YIPF2 | 0.632 | 0.000 | — |
| YIPF5 | 0.593 | 0.273 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KCNJ6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EBP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TLCD4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| VMA21 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMPPE | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ERGIC3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| AQP6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GPR152 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TMX2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SIGLEC12 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.8 + PDB: 无 | pLDDT=76.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus, cis-Golgi network membrane; Golgi / Golgi apparatus; 额外: Nucleoplasm, Plasma membrane | 一致 |
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
1. YIPF1 — Protein YIPF1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小306 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y548
- Protein Atlas: https://www.proteinatlas.org/ENSG00000058799-YIPF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=YIPF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y548
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
