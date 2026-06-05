---
type: protein-evaluation
gene: "BUB1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BUB1 — REJECTED (研究热度过高 (PubMed strict=784，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BUB1 / BUB1L |
| 蛋白名称 | Mitotic checkpoint serine/threonine-protein kinase BUB1 |
| 蛋白大小 | 1085 aa / 122.4 kDa |
| UniProt ID | O43683 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Chromosome, centromere, kinetochore |
| 蛋白大小 | 8/10 | ×1 | 8 | 1085 aa / 122.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=784 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.6; PDB: 2LAH, 4A1G, 4QPM, 4R8Q, 5DMZ, 6F7B, 7B1F |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR015661, IPR011009, IPR013212, IPR000719, IPR017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.0/180** | |
| **归一化总分** | | | **43.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Chromosome, centromere, kinetochore | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- kinetochore (GO:0000776)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- outer kinetochore (GO:0000940)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 784 |
| PubMed broad count | 1502 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BUB1L |

**关键文献**:
1. Identification of Key Prognostic Genes of Triple Negative Breast Cancer by LASSO-Based Machine Learning and Bioinformatics Analysis.. *Genes*. PMID: 35627287
2. A noncanonical cytoplasmic role for BUB1 in restraining DNA damage-induced dsRNA accumulation and sensing within stress granules.. *Science immunology*. PMID: 40779648
3. Retraction.. *The New phytologist*. PMID: 27874987
4. BUB1 regulates non-homologous end joining pathway to mediate radioresistance in triple-negative breast cancer.. *Journal of experimental & clinical cancer research : CR*. PMID: 38863037
5. The BUB1 and BUBR1 paralogs scaffold the kinetochore fibrous corona.. *Science advances*. PMID: 40938979

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.6 |
| 高置信度残基 (pLDDT>90) 占比 | 29.5% |
| 置信残基 (pLDDT 70-90) 占比 | 18.8% |
| 中等置信 (pLDDT 50-70) 占比 | 6.8% |
| 低置信 (pLDDT<50) 占比 | 44.9% |
| 有序区域 (pLDDT>70) 占比 | 48.3% |
| 可用 PDB 条目 | 2LAH, 4A1G, 4QPM, 4R8Q, 5DMZ, 6F7B, 7B1F, 7B1H, 7B1J |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.6），有序残基占 48.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015661, IPR011009, IPR013212, IPR000719, IPR017441; Pfam: PF08311, PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BUB1B | 0.999 | 0.919 | — |
| TTK | 0.999 | 0.292 | — |
| CDC20 | 0.999 | 0.996 | — |
| KNL1 | 0.999 | 0.990 | — |
| BUB3 | 0.999 | 0.973 | — |
| MAD2L1 | 0.999 | 0.875 | — |
| NDC80 | 0.998 | 0.838 | — |
| MAD1L1 | 0.998 | 0.959 | — |
| CCNB2 | 0.998 | 0.279 | — |
| CDK1 | 0.998 | 0.354 | — |

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
| 三维结构 | AlphaFold pLDDT=62.6 + PDB: 2LAH, 4A1G, 4QPM, 4R8Q, 5DMZ,  | pLDDT=62.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, centromere, kinetochore / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BUB1 — Mitotic checkpoint serine/threonine-protein kinase BUB1，研究基础较多，新颖性有限。
2. 蛋白大小1085 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 784 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 784 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43683
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169679-BUB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BUB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43683
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000169679-BUB1/subcellular

![](https://images.proteinatlas.org/6123/79_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/6123/79_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/6123/80_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/6123/80_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/6123/967_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/6123/967_C5_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43683-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
