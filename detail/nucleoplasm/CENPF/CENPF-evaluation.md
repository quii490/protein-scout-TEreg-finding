---
type: protein-evaluation
gene: "CENPF"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CENPF — REJECTED (研究热度过高 (PubMed strict=417，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CENPF |
| 蛋白名称 | Centromere protein F |
| 蛋白大小 | 3114 aa / 357.5 kDa |
| UniProt ID | P49454 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm, perinuclear region; Nucleus matrix; Chromosome, c |
| 蛋白大小 | 0/10 | ×1 | 0 | 3114 aa / 357.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=417 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043513, IPR018302, IPR019513, IPR018463; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **64.0/180** | |
| **归一化总分** | | | **35.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Cytoplasm, perinuclear region; Nucleus matrix; Chromosome, centromere, kinetochore; Cytoplasm, cytos... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axoneme (GO:0005930)
- centrosome (GO:0005813)
- chromatin (GO:0000785)
- chromosome, centromeric region (GO:0000775)
- ciliary basal body (GO:0036064)
- ciliary transition fiber (GO:0097539)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 417 |
| PubMed broad count | 512 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. CENP-F-dependent DRP1 function regulates APC/C activity during oocyte meiosis I.. *Nature communications*. PMID: 36513638
2. Strømme Syndrome.. **. PMID: 36375007
3. Predicting potential therapeutic targets and small molecule drugs for early-stage lung adenocarcinoma.. *Biomedicine & pharmacotherapy = Biomedecine & pharmacotherapie*. PMID: 38555814
4. N6-methyladenosine modification of CENPF mRNA facilitates gastric cancer metastasis via regulating FAK nuclear export.. *Cancer communications (London, England)*. PMID: 37256823
5. Identification of Key Prognostic Genes of Triple Negative Breast Cancer by LASSO-Based Machine Learning and Bioinformatics Analysis.. *Genes*. PMID: 35627287

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043513, IPR018302, IPR019513, IPR018463; Pfam: PF10490, PF10473, PF10481 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BUB1B | 0.999 | 0.000 | — |
| CENPE | 0.999 | 0.230 | — |
| CDC20 | 0.990 | 0.000 | — |
| FOXM1 | 0.989 | 0.000 | — |
| CCNB1 | 0.988 | 0.000 | — |
| BUB1 | 0.987 | 0.000 | — |
| NDC80 | 0.987 | 0.000 | — |
| ASPM | 0.987 | 0.000 | — |
| KIF2C | 0.985 | 0.000 | — |
| MKI67 | 0.979 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:14968112 |
| NDEL1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| TSC22D1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CENPE | psi-mi:"MI:0018"(two hybrid) | pubmed:9763420|imex:IM-18999 |
| ARRB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17620599 |
| PAFAH1B1 | psi-mi:"MI:0051"(fluorescence technology) | pubmed:17600710|imex:IM-18934 |
| NDE1 | psi-mi:"MI:0096"(pull down) | pubmed:17600710|imex:IM-18934 |
| Cep152 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:23075850|imex:IM-18674 |
| COPS6 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, perinuclear region; Nucleus matrix; Chr / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CENPF — Centromere protein F，研究基础较多，新颖性有限。
2. 蛋白大小3114 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 417 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 417 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P49454
- Protein Atlas: https://www.proteinatlas.org/ENSG00000117724-CENPF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CENPF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49454
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000117724-CENPF/subcellular

![](https://images.proteinatlas.org/52382/783_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/52382/783_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/52382/785_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/52382/785_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/52382/868_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/52382/868_E10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
