---
type: protein-evaluation
gene: "MEF2B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MEF2B — REJECTED (研究热度过高 (PubMed strict=118，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MEF2B / XMEF2 |
| 蛋白名称 | Myocyte-specific enhancer factor 2B |
| 蛋白大小 | 365 aa / 38.6 kDa |
| UniProt ID | Q02080 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Cell Junctions; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 365 aa / 38.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=118 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.8; PDB: 1N6J, 1TQE, 6BYY, 6BZ1, 6C9L, 6WC2, 6WC5 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033896, IPR002100, IPR036879; Pfam: PF00319 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Cell Junctions | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell junction (GO:0030054)
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 118 |
| PubMed broad count | 177 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: XMEF2 |

**关键文献**:
1. Follicular lymphoma t(14;18)-negative is genetically a heterogeneous disease.. *Blood advances*. PMID: 33211828
2. MEF2B C-terminal mutations enhance transcriptional activity and stability to drive B cell lymphomagenesis.. *Nature communications*. PMID: 39179580
3. Integration of gene mutations in risk prognostication for patients receiving first-line immunochemotherapy for follicular lymphoma: a retrospective analysis of a prospective clinical trial and validation in a population-based registry.. *The Lancet. Oncology*. PMID: 26256760
4. The Molecular and Biological Function of MEF2D in Leukemia.. *Advances in experimental medicine and biology*. PMID: 39017853
5. Mouse Mef2b gene: unique member of MEF2 gene family.. *Journal of biochemistry*. PMID: 9443808

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.8 |
| 高置信度残基 (pLDDT>90) 占比 | 24.1% |
| 置信残基 (pLDDT 70-90) 占比 | 1.1% |
| 中等置信 (pLDDT 50-70) 占比 | 26.8% |
| 低置信 (pLDDT<50) 占比 | 47.9% |
| 有序区域 (pLDDT>70) 占比 | 25.2% |
| 可用 PDB 条目 | 1N6J, 1TQE, 6BYY, 6BZ1, 6C9L, 6WC2, 6WC5 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.8），有序残基占 25.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033896, IPR002100, IPR036879; Pfam: PF00319 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CABIN1 | 0.996 | 0.973 | — |
| MEF2A | 0.987 | 0.760 | — |
| HDAC9 | 0.980 | 0.949 | — |
| MEF2D | 0.979 | 0.661 | — |
| NKX2-5 | 0.948 | 0.907 | — |
| NFATC1 | 0.920 | 0.000 | — |
| NFATC3 | 0.918 | 0.000 | — |
| NFATC4 | 0.916 | 0.000 | — |
| NFATC2 | 0.915 | 0.000 | — |
| MYOG | 0.864 | 0.049 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BORCS8 | psi-mi:"MI:0096"(pull down) | pubmed:16189514|imex:IM-16520| |
| CDC37 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| MEF2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MEF2C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MEF2D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UBN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CABIN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RAB9A | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TEKT4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CTAG1A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.8 + PDB: 1N6J, 1TQE, 6BYY, 6BZ1, 6C9L,  | pLDDT=60.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Cytosol; 额外: Cell Junctions | 一致 |
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
1. MEF2B — Myocyte-specific enhancer factor 2B，研究基础较多，新颖性有限。
2. 蛋白大小365 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 118 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 118 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q02080
- Protein Atlas: https://www.proteinatlas.org/ENSG00000213999-MEF2B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MEF2B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q02080
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000213999-MEF2B/subcellular

![](https://images.proteinatlas.org/4734/112_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/4734/112_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/4734/113_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/4734/113_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/4734/967_A5_5_red_green.jpg)
![](https://images.proteinatlas.org/4734/967_A5_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q02080-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
