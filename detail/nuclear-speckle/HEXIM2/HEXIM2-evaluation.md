---
type: protein-evaluation
gene: "HEXIM2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HEXIM2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HEXIM2 |
| 蛋白名称 | Protein HEXIM2 |
| 蛋白大小 | 286 aa / 32.4 kDa |
| UniProt ID | Q96MH2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear speckles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 286 aa / 32.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024872; Pfam: PF15313 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear speckles | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Machine learning-based multimodal radiomics and transcriptomics models for predicting radiotherapy sensitivity and prognosis in esophageal cancer.. *The Journal of biological chemistry*. PMID: 40381695
2. Specificity of Hexim1 and Hexim2 complex formation with cyclin T1/T2, importin alpha and 7SK snRNA.. *Journal of molecular biology*. PMID: 19883659
3. HEXIM2, a HEXIM1-related protein, regulates positive transcription elongation factor b through association with 7SK.. *The Journal of biological chemistry*. PMID: 15713662
4. Compensatory contributions of HEXIM1 and HEXIM2 in maintaining the balance of active and inactive positive transcription elongation factor b complexes for control of transcription.. *The Journal of biological chemistry*. PMID: 15713661
5. Analysis of the large inactive P-TEFb complex indicates that it contains one 7SK molecule, a dimer of HEXIM1 or HEXIM2, and two P-TEFb molecules containing Cdk9 phosphorylated at threonine 186.. *The Journal of biological chemistry*. PMID: 15965233

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.3 |
| 高置信度残基 (pLDDT>90) 占比 | 32.2% |
| 置信残基 (pLDDT 70-90) 占比 | 17.8% |
| 中等置信 (pLDDT 50-70) 占比 | 21.0% |
| 低置信 (pLDDT<50) 占比 | 29.0% |
| 有序区域 (pLDDT>70) 占比 | 50.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.3，有序区 50.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024872; Pfam: PF15313 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MEPCE | 0.998 | 0.615 | — |
| LARP7 | 0.998 | 0.627 | — |
| HEXIM1 | 0.995 | 0.848 | — |
| CDK9 | 0.979 | 0.876 | — |
| CCNT1 | 0.942 | 0.640 | — |
| CCNT2 | 0.882 | 0.691 | — |
| FERD3L | 0.755 | 0.680 | — |
| BRD4 | 0.707 | 0.000 | — |
| AFF1 | 0.635 | 0.000 | — |
| METTL8 | 0.615 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000468773.2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| Cdk9 | psi-mi:"MI:0096"(pull down) | pubmed:20593818|imex:IM-17619 |
| AHCYL1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LNX1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HSF2BP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DBF4B | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| AP2M1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PSMA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CFP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.3 + PDB: 无 | pLDDT=70.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nuclear speckles | 一致 |
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
1. HEXIM2 — Protein HEXIM2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小286 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96MH2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168517-HEXIM2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HEXIM2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96MH2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000168517-HEXIM2/subcellular

![](https://images.proteinatlas.org/28455/255_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/28455/255_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/28455/256_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/28455/256_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/28455/257_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/28455/257_A6_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96MH2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96MH2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR024872; |
| Pfam | PF15313; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000168517-HEXIM2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AHCYL1 | Intact, Biogrid | true |
| CCNT1 | Biogrid, Bioplex | true |
| CDK9 | Biogrid, Opencell | true |
| CSNK2B | Biogrid, Opencell, Bioplex | true |
| HEXIM1 | Intact, Biogrid, Bioplex | true |
| MEPCE | Biogrid, Bioplex | true |
| TCF12 | Intact, Biogrid | true |
| AP2M1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
