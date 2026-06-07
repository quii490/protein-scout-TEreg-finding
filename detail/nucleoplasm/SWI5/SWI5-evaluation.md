---
type: protein-evaluation
gene: "SWI5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SWI5 — REJECTED (研究热度过高 (PubMed strict=130，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SWI5 / C9orf119, SAE3 |
| 蛋白名称 | DNA repair protein SWI5 homolog |
| 蛋白大小 | 235 aa / 26.7 kDa |
| UniProt ID | Q1ZZU3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 235 aa / 26.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=130 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR010760; Pfam: PF07061 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)
- Swi5-Sfr1 complex (GO:0032798)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 130 |
| PubMed broad count | 187 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf119, SAE3 |

**关键文献**:
1. Fission yeast Swi5 protein, a novel DNA recombination mediator.. *DNA repair*. PMID: 17716957
2. Expression, purification and crystallization of Swi5 and the Swi5-Sfr1 complex from fission yeast.. *Acta crystallographica. Section F, Structural biology and crystallization communications*. PMID: 20823543
3. Distinct regions of the Swi5 and Ace2 transcription factors are required for specific gene activation.. *The Journal of biological chemistry*. PMID: 10409653
4. Parallel pathways of gene regulation: homologous regulators SWI5 and ACE2 differentially control transcription of HO and chitinase.. *Genes & development*. PMID: 1730413
5. Role for the mammalian Swi5-Sfr1 complex in DNA strand break repair through homologous recombination.. *PLoS genetics*. PMID: 20976249

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.4 |
| 高置信度残基 (pLDDT>90) 占比 | 15.3% |
| 置信残基 (pLDDT 70-90) 占比 | 18.7% |
| 中等置信 (pLDDT 50-70) 占比 | 10.2% |
| 低置信 (pLDDT<50) 占比 | 55.7% |
| 有序区域 (pLDDT>70) 占比 | 34.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.4），有序残基占 34.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010760; Pfam: PF07061 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SFR1 | 0.999 | 0.609 | — |
| TMEM208 | 0.960 | 0.936 | — |
| XRCC3 | 0.952 | 0.294 | — |
| RAD51D | 0.951 | 0.294 | — |
| RAD51C | 0.948 | 0.299 | — |
| RAD51B | 0.942 | 0.294 | — |
| XRCC2 | 0.911 | 0.000 | — |
| RAD51 | 0.883 | 0.639 | — |
| SMARCA2 | 0.776 | 0.000 | — |
| MND1 | 0.751 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-926902 | psi-mi:"MI:0018"(two hybrid) | pubmed:14663140|imex:IM-30172 |
| swi2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14663140|imex:IM-30172 |
| sfr1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14663140|imex:IM-30172 |
| ssa2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-12104|pubmed:19750511 |
| sks2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-12104|pubmed:19750511 |
| ath1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-12104|pubmed:19750511 |
| tdh1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-12104|pubmed:19750511 |
| cip1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-12104|pubmed:19750511 |
| ssc1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-12104|pubmed:19750511 |
| tef101 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-12104|pubmed:19750511 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.4 + PDB: 无 | pLDDT=58.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Cytosol | 一致 |
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
1. SWI5 — DNA repair protein SWI5 homolog，研究基础较多，新颖性有限。
2. 蛋白大小235 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 130 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=58.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 130 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q1ZZU3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175854-SWI5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SWI5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q1ZZU3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/SWI5/IF_images/SWI5_IF_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000175854-SWI5/subcellular

![](https://images.proteinatlas.org/52032/783_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/52032/783_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/52032/785_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/52032/785_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/52032/868_G11_1_red_green.jpg)
![](https://images.proteinatlas.org/52032/868_G11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q1ZZU3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q1ZZU3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR010760; |
| Pfam | PF07061; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000175854-SWI5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| RAD51 | Biogrid | false |
| SFR1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
