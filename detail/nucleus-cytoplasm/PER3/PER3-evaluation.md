---
type: protein-evaluation
gene: "PER3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PER3 — REJECTED (研究热度过高 (PubMed strict=593，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PER3 |
| 蛋白名称 | Period circadian protein homolog 3 |
| 蛋白大小 | 1201 aa / 131.9 kDa |
| UniProt ID | P56645 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1201 aa / 131.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=593 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000014, IPR035965, IPR013655, IPR057310, IPR048 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **75.0/180** | |
| **归一化总分** | | | **41.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 593 |
| PubMed broad count | 855 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A length polymorphism in the circadian clock gene Per3 is linked to delayed sleep phase syndrome and extreme diurnal preference.. *Sleep*. PMID: 12841365
2. Nucleosome destabilization by polyamines.. *Archives of biochemistry and biophysics*. PMID: 35395253
3. Circadian gene variants and breast cancer.. *Cancer letters*. PMID: 28109907
4. Actigraphic characterization of sleep and circadian phenotypes of PER3 gene VNTR genotypes.. *Chronobiology international*. PMID: 37691400
5. Alterations in CRY2 and PER3 gene expression associated with thalamic-limbic community structural abnormalities in patients with bipolar depression or unipolar depression.. *Journal of affective disorders*. PMID: 34732337

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.6 |
| 高置信度残基 (pLDDT>90) 占比 | 15.6% |
| 置信残基 (pLDDT 70-90) 占比 | 16.2% |
| 中等置信 (pLDDT 50-70) 占比 | 8.9% |
| 低置信 (pLDDT<50) 占比 | 59.3% |
| 有序区域 (pLDDT>70) 占比 | 31.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=53.6），有序残基占 31.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000014, IPR035965, IPR013655, IPR057310, IPR048814; Pfam: PF23170, PF08447, PF21353 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CRY2 | 0.999 | 0.958 | — |
| CRY1 | 0.999 | 0.954 | — |
| PER2 | 0.998 | 0.963 | — |
| PER1 | 0.997 | 0.968 | — |
| CSNK1E | 0.994 | 0.551 | — |
| CSNK1D | 0.988 | 0.392 | — |
| ARNTL | 0.980 | 0.954 | — |
| NR1D1 | 0.978 | 0.125 | — |
| NR1D2 | 0.969 | 0.125 | — |
| BHLHE41 | 0.960 | 0.457 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| yycF | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| BRL2 | psi-mi:"MI:0084"(phage display) | pubmed:19000166|imex:IM-20277 |
| Csnk1e | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| yscH | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| DHRS2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CRY2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| ANKRD36B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| MIB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CCDC88A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| AVL9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.6 + PDB: 无 | pLDDT=53.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol | 一致 |
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
1. PER3 — Period circadian protein homolog 3，研究基础较多，新颖性有限。
2. 蛋白大小1201 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 593 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=53.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 593 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P56645
- Protein Atlas: https://www.proteinatlas.org/ENSG00000049246-PER3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PER3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P56645
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000049246-PER3/subcellular

![](https://images.proteinatlas.org/19530/177_G2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19530/177_G2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19530/178_G2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19530/178_G2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19530/247_G2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19530/247_G2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P56645-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
