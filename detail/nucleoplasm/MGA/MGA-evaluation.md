---
type: protein-evaluation
gene: "MGA"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MGA — REJECTED (研究热度过高 (PubMed strict=437，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MGA / KIAA0518, MAD5 |
| 蛋白名称 | MAX gene-associated protein |
| 蛋白大小 | 3065 aa / 336.2 kDa |
| UniProt ID | Q8IWI9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 0/10 | ×1 | 0 | 3065 aa / 336.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=437 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR036638, IPR037935, IPR032060, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **72.0/180** | |
| **归一化总分** | | | **40.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- MLL1 complex (GO:0071339)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 437 |
| PubMed broad count | 1968 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0518, MAD5 |

**关键文献**:
1. Comprehensive molecular profiling of lung adenocarcinoma.. *Nature*. PMID: 25079552
2. MGA loss-of-function variants cause premature ovarian insufficiency.. *The Journal of clinical investigation*. PMID: 39545409
3. Teplizumab.. **. PMID: 36701504
4. Retifanlimab.. **. PMID: 37247364
5. New perspective in diagnostics of mitochondrial disorders: two years' experience with whole-exome sequencing at a national paediatric centre.. *Journal of translational medicine*. PMID: 27290639

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
| InterPro/Pfam | InterPro: IPR011598, IPR036638, IPR037935, IPR032060, IPR008967; Pfam: PF00010, PF16059, PF00907 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAX | 0.995 | 0.782 | — |
| E2F6 | 0.989 | 0.837 | — |
| WDR5 | 0.979 | 0.774 | — |
| L3MBTL2 | 0.966 | 0.804 | — |
| RNF2 | 0.966 | 0.629 | — |
| PCGF6 | 0.948 | 0.836 | — |
| TAF1 | 0.928 | 0.000 | — |
| KMT2A | 0.912 | 0.044 | — |
| KANSL1 | 0.910 | 0.000 | — |
| CHD8 | 0.909 | 0.071 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LSM8 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| TULP3 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| MAX | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| clpB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Q81RC9 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| MGAM | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Tfcp2l1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| Rnf2 | psi-mi:"MI:0096"(pull down) | pubmed:17296600 |
| Dpy-30L2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG6985 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. MGA — MAX gene-associated protein，研究基础较多，新颖性有限。
2. 蛋白大小3065 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 437 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 437 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IWI9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174197-MGA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MGA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IWI9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000174197-MGA/subcellular

![](https://images.proteinatlas.org/36876/1891_N14_5_cr5bbdd611b31e0_red_green.jpg)
![](https://images.proteinatlas.org/36876/1891_N14_7_cr5bbdd611b31e6_red_green.jpg)
![](https://images.proteinatlas.org/36876/1951_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/36876/1951_B8_3_red_green.jpg)
![](https://images.proteinatlas.org/36876/2198_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/36876/2198_C3_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IWI9 |
| SMART | SM00353;SM00425; |
| UniProt Domain [FT] | DOMAIN 2423..2474; /note="bHLH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00981" |
| InterPro | IPR011598;IPR036638;IPR037935;IPR032060;IPR008967;IPR046360;IPR036960;IPR001699;IPR018186; |
| Pfam | PF00010;PF16059;PF00907; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000174197-MGA/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CBX3 | Intact, Biogrid | true |
| MAX | Intact, Biogrid | true |
| CBX1 | Biogrid | false |
| CSNK2A1 | Opencell | false |
| CSNK2A2 | Opencell | false |
| E2F6 | Biogrid | false |
| H3C1 | Biogrid | false |
| HDAC1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
