---
type: protein-evaluation
gene: "FOXL2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FOXL2 — REJECTED (研究热度过高 (PubMed strict=841，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOXL2 |
| 蛋白名称 | Forkhead box protein L2 |
| 蛋白大小 | 376 aa / 38.8 kDa |
| UniProt ID | P58012 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 376 aa / 38.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=841 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.1; PDB: 7VOU, 7VOV |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR047515, IPR001766, IPR050211, IPR018122, IPR030 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- Flemming body (GO:0090543)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 841 |
| PubMed broad count | 1311 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. FOXL2 interaction with different binding partners regulates the dynamics of ovarian development.. *Science advances*. PMID: 38517962
2. Human FOX gene family (Review).. *International journal of oncology*. PMID: 15492844
3. Long-Range Regulation of Key Sex Determination Genes.. *Sexual development : genetics, molecular biology, evolution, endocrinology, embryology, and pathology of sex determination and differentiation*. PMID: 34753143
4. FOXL2 drives the differentiation of supporting gonadal cells in early ovarian development.. *Reproductive biology and endocrinology : RB&E*. PMID: 40102860
5. Sex determination and maintenance: the role of DMRT1 and FOXL2.. *Asian journal of andrology*. PMID: 28091399

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.1 |
| 高置信度残基 (pLDDT>90) 占比 | 17.3% |
| 置信残基 (pLDDT 70-90) 占比 | 9.6% |
| 中等置信 (pLDDT 50-70) 占比 | 31.9% |
| 低置信 (pLDDT<50) 占比 | 41.2% |
| 有序区域 (pLDDT>70) 占比 | 26.9% |
| 可用 PDB 条目 | 7VOU, 7VOV |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.1），有序残基占 26.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR047515, IPR001766, IPR050211, IPR018122, IPR030456; Pfam: PF00250 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMAD3 | 0.941 | 0.314 | — |
| NR5A1 | 0.926 | 0.000 | — |
| NOBOX | 0.899 | 0.070 | — |
| FIGLA | 0.891 | 0.053 | — |
| BMP15 | 0.890 | 0.000 | — |
| SOX9 | 0.883 | 0.071 | — |
| DDX20 | 0.861 | 0.095 | — |
| DMRT1 | 0.837 | 0.045 | — |
| MRPS22 | 0.817 | 0.000 | — |
| OSR2 | 0.813 | 0.096 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-944480 | psi-mi:"MI:0018"(two hybrid) | pubmed:16153597|imex:IM-20082 |
| Ddx20 | psi-mi:"MI:0018"(two hybrid) | pubmed:16153597|imex:IM-20082 |
| ENSMUSP00000053297.3 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-12116|pubmed:20005806 |
| Esr1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12116|pubmed:20005806 |
| Esr2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12116|pubmed:20005806 |
| Sp100 | psi-mi:"MI:0018"(two hybrid) | pubmed:22022399|imex:IM-26668 |
| Pias2 | psi-mi:"MI:0018"(two hybrid) | pubmed:22022399|imex:IM-26668 |
| Ube2i | psi-mi:"MI:0018"(two hybrid) | pubmed:22022399|imex:IM-26668 |
| SMAD4 | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |
| SMARCA4 | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.1 + PDB: 7VOU, 7VOV | pLDDT=60.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FOXL2 — Forkhead box protein L2，研究基础较多，新颖性有限。
2. 蛋白大小376 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 841 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 841 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P58012
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183770-FOXL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FOXL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P58012
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000183770-FOXL2/subcellular

![](https://images.proteinatlas.org/69613/1339_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/69613/1339_C5_3_red_green.jpg)
![](https://images.proteinatlas.org/69613/1365_E7_2_red_green.jpg)
![](https://images.proteinatlas.org/69613/1365_E7_4_red_green.jpg)
![](https://images.proteinatlas.org/69613/2054_C2_3_red_green.jpg)
![](https://images.proteinatlas.org/69613/2054_C2_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P58012-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P58012 |
| SMART | SM00339; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR047515;IPR001766;IPR050211;IPR018122;IPR030456;IPR036388;IPR036390; |
| Pfam | PF00250; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000183770-FOXL2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| LATS1 | Biogrid | false |
| UBE2I | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
