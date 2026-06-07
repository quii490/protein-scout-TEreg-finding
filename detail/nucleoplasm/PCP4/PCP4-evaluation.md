---
type: protein-evaluation
gene: "PCP4"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PCP4 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PCP4 / PEP-19 |
| 蛋白全称 | Calmodulin regulator protein PCP4 |
| 蛋白大小 | 62 aa |
| UniProt ID | P48539 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 5/10 | ×1 | **5** | 62 aa, small/large |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed 70 篇，中等研究热度 |
| 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 1 domain(s), 新颖蛋白基线水平 |
| PPI 网络 | 4/10 | ×3 | **12** | STRING 15 个互作伙伴，调控相关性低 |
| 互证加分 | -- | -- | **+0.5** | PDB + AlphaFold 结构互证 (+0.5) |
|  | **原始总分** |  | **91.5/183** | **91.0/183** |  |  |  |
|  | **归一化总分** |  | **50.0/100** | **49.7/100** |  |  |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt |  | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PCP4/IF_images/MCF-7_HPA005792_1.jpg|MCF-7]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PCP4/IF_images/U2OS_HPA005792_2.jpg|U2OS]]

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 62 aa， small/large

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 70 |

**评价**: PubMed 70 篇，中等研究热度

**关键文献**:
1. Pan Y et al. (2025). "Prosapogenin CP4 exacerbates mitophagy to induce apoptosis via AMPK-mTOR and PINK1/Parkin pathways in A549 cells". *Phytomedicine*. PMID: 41067204
2. Jia W et al. (2025). "PCP4 inhibits the progression of prostate cancer through Ca(2+)/CAMKK2/AMPK/AR pathway". *Front Immunol*. PMID: 40746562
3. Hu D et al. (2023). "PCP4 Promotes Alzheimer's Disease Pathogenesis by Affecting Amyloid-β Protein Precursor Processing". *J Alzheimers Dis*. PMID: 37302034
4. Renelt M et al. (2014). "Distribution of PCP4 protein in the forebrain of adult mice". *Acta Histochem*. PMID: 24954028
5. Felizola SJ et al. (2014). "PCP4: a regulator of aldosterone synthesis in human adrenocortical tissues". *J Mol Endocrinol*. PMID: 24403568
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 62 aa |
| PDB 条数 | 1 |
| 已注释结构域 | 1 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PCP4/PCP4-PAE.png]]

**评价**: 1 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | Calmodulin_Regulator_PCP4-like |

**染色质调控潜力分析**: 1 domain(s), 新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|
| CALML6 | 0 |  | no |
| CALML5 | 0 |  | no |
| CALML4 | 0 |  | no |
| CALML3 | 0 |  | no |
| CALM3 | 0 |  | no |
| ETS2 | 0 |  | no |
| ABCG1 | 0 |  | no |
| RGS14 | 0 |  | no |
| CALB1 | 0 |  | no |
| PVALB | 0 |  | no |

**已知复合体成员** (GO-CC):

- C:protein-containing complex (GO:0032991, IDA:CAFA)

**评价**: STRING 15 个互作伙伴，调控相关性低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 1 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 1 个 | 多库一致 |
| PPI 网络 | STRING | 15 个 | 单一来源 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
PDB + AlphaFold 结构互证 (+0.5)
**总计**: +0.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 70 篇，中等研究热度
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 1 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PCP4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183036-PCP4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PCP4%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/P48539
- STRING: https://string-db.org/network/9606.ENSG00000183036
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P48539


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PCP4-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PCP4/PCP4-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000183036-PCP4/subcellular

![](https://images.proteinatlas.org/5792/1081_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/5792/1081_H10_2_red_green.jpg)
![](https://images.proteinatlas.org/5792/1888_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/5792/1888_B2_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P48539 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 39..62; /note="IQ"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00116" |
| InterPro | IPR052142; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000183036-PCP4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| A2ML1 | Bioplex | false |
| ACAA2 | Bioplex | false |
| ANXA8 | Bioplex | false |
| APOD | Bioplex | false |
| ARSF | Bioplex | false |
| CALML3 | Bioplex | false |
| CALML5 | Bioplex | false |
| CALML6 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
