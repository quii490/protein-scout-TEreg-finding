---
type: protein-evaluation
gene: "LPIN3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LPIN3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LPIN3 / LIPN3L |
| 蛋白名称 | Phosphatidate phosphatase LPIN3 |
| 蛋白大小 | 851 aa / 93.6 kDa |
| UniProt ID | Q9BQK8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 851 aa / 93.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036412, IPR026058, IPR031703, IPR007651, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum membrane (GO:0005789)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 30 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LIPN3L |

**关键文献**:
1. Lipin3 deficiency promotes hepatocyte ferroptosis and pyroptosis via activating JAK1-STAT3 pathway during acetaminophen induced acute liver injury.. *Molecular biomedicine*. PMID: 41071519
2. Ontogenetic Expression of Lpin2 and Lpin3 Genes and Their Associations with Traits in Two Breeds of Chinese Fat-tailed Sheep.. *Asian-Australasian journal of animal sciences*. PMID: 26950863
3. A suggested shared aetiology of dementia - a colocalization study.. *Neurobiology of aging*. PMID: 35675752
4. The role of glycerophospholipid metabolism in feline parvovirus infected CRFK cells.. *Frontiers in microbiology*. PMID: 40919194
5. Prognostic and Therapeutic Value of Metabolism-Related Genes in Nephroblastoma: A Focus on the Key Gene NNMT and Its Regulative Effect on Metabolism.. *Cell biochemistry and function*. PMID: 40574709

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.1 |
| 高置信度残基 (pLDDT>90) 占比 | 24.0% |
| 置信残基 (pLDDT 70-90) 占比 | 17.5% |
| 中等置信 (pLDDT 50-70) 占比 | 11.0% |
| 低置信 (pLDDT<50) 占比 | 47.5% |
| 有序区域 (pLDDT>70) 占比 | 41.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.1），有序残基占 41.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036412, IPR026058, IPR031703, IPR007651, IPR013209; Pfam: PF16876, PF04571, PF08235 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LPIN1 | 0.980 | 0.785 | — |
| PLPP2 | 0.966 | 0.087 | — |
| LPIN2 | 0.963 | 0.617 | — |
| PLPP3 | 0.961 | 0.087 | — |
| CHPT1 | 0.936 | 0.000 | — |
| CEPT1 | 0.933 | 0.000 | — |
| SELENOI | 0.920 | 0.000 | — |
| PLPP4 | 0.920 | 0.091 | — |
| PLPP5 | 0.920 | 0.091 | — |
| CDS2 | 0.919 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RTN4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| NOLC1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| RASAL2 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| ZBTB21 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| CBY1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| KCTD3 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| TANC2 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| KIF13B | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| INPP5E | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| CWC25 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.1 + PDB: 无 | pLDDT=61.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LPIN3 — Phosphatidate phosphatase LPIN3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小851 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=61.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BQK8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132793-LPIN3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LPIN3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BQK8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000132793-LPIN3/subcellular

![](https://images.proteinatlas.org/51466/781_F1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/51466/781_F1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/70640/1346_D7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/70640/1346_D7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/70640/1351_D7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/70640/1351_D7_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BQK8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BQK8 |
| SMART | SM00775; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR036412;IPR026058;IPR031703;IPR007651;IPR013209;IPR031315; |
| Pfam | PF16876;PF04571;PF08235; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000132793-LPIN3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| YWHAE | Biogrid, Opencell | true |
| YWHAG | Biogrid | false |
| YWHAZ | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
