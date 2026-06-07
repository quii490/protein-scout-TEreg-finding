---
type: protein-evaluation
gene: "TFPT"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TFPT 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TFPT / INO80F |
| 蛋白名称 | TCF3 fusion partner |
| 蛋白大小 | 253 aa / 28.3 kDa |
| UniProt ID | P0C1Z6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 253 aa / 28.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR056513, IPR033555; Pfam: PF24245 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- Ino80 complex (GO:0031011)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 70 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: INO80F |

**关键文献**:
1. Expression of PRPF31 and TFPT: regulation in health and retinal disease.. *Human molecular genetics*. PMID: 22723017
2. Promoter analysis of TFPT (FB1), a molecular partner of TCF3 (E2A) in childhood acute lymphoblastic leukemia.. *Biochemical and biophysical research communications*. PMID: 11700047
3. Apoptosis promoted by up-regulation of TFPT (TCF3 fusion partner) appears p53 independent, cell type restricted and cell density influenced.. *Apoptosis : an international journal on programmed cell death*. PMID: 17041757
4. A Study into the Evolutionary Divergence of the Core Promoter Elements of PRPF31 and TFPT.. *Journal of molecular and genetic medicine : an international journal of biomedical research*. PMID: 25729402
5. Genes on bovine chromosome 18 associated with bilateral convergent strabismus with exophthalmos in German Brown cattle.. *Molecular vision*. PMID: 18836565

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.0 |
| 高置信度残基 (pLDDT>90) 占比 | 26.1% |
| 置信残基 (pLDDT 70-90) 占比 | 6.7% |
| 中等置信 (pLDDT 50-70) 占比 | 41.9% |
| 低置信 (pLDDT<50) 占比 | 25.3% |
| 有序区域 (pLDDT>70) 占比 | 32.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.0），有序残基占 32.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR056513, IPR033555; Pfam: PF24245 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| INO80E | 0.996 | 0.833 | — |
| UCHL5 | 0.986 | 0.818 | — |
| ACTR8 | 0.985 | 0.753 | — |
| NFRKB | 0.984 | 0.619 | — |
| ACTR5 | 0.981 | 0.652 | — |
| INO80 | 0.979 | 0.760 | — |
| RUVBL2 | 0.977 | 0.686 | — |
| INO80C | 0.976 | 0.631 | — |
| MCRS1 | 0.974 | 0.645 | — |
| YY1 | 0.972 | 0.684 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000484338.1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| hflC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| INO80B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16230350 |
| ACTR8 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16230350 |
| ACTL6A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16230350 |
| MCRS1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16230350 |
| INO80E | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16230350 |
| INO80D | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16230350 |
| EAF2 | psi-mi:"MI:0018"(two hybrid) | pubmed:17395368 |
| EAF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17395368 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.0 + PDB: 无 | pLDDT=66.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
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
1. TFPT — TCF3 fusion partner，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小253 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=66.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P0C1Z6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105619-TFPT/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TFPT
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P0C1Z6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000105619-TFPT/subcellular

![](https://images.proteinatlas.org/58534/975_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/58534/975_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/58534/976_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/58534/976_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/58534/980_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/58534/980_D4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P0C1Z6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P0C1Z6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR056513;IPR033555; |
| Pfam | PF24245; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000105619-TFPT/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACTR5 | Biogrid, Bioplex | true |
| ACTR8 | Biogrid, Bioplex | true |
| CCNDBP1 | Intact, Biogrid | true |
| GRIPAP1 | Intact, Biogrid, Bioplex | true |
| INO80 | Biogrid, Bioplex | true |
| INO80B | Biogrid, Bioplex | true |
| INO80C | Biogrid, Bioplex | true |
| INO80E | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
