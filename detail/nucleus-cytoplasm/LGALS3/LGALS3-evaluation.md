---
type: protein-evaluation
gene: "LGALS3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## LGALS3 — REJECTED (研究热度过高 (PubMed strict=476，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LGALS3 / MAC2 |
| 蛋白名称 | Galectin-3 |
| 蛋白大小 | 250 aa / 26.2 kDa |
| UniProt ID | P17931 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Plasma membrane; UniProt: Cytoplasm; Nucleus; Secreted |
| 蛋白大小 | 10/10 | ×1 | 10 | 250 aa / 26.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=476 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=73.8; PDB: 1A3K, 1KJL, 1KJR, 2NMN, 2NMO, 2NN8, 2XG3 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013320, IPR044156, IPR001079; Pfam: PF00337 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Plasma membrane | Supported |
| UniProt | Cytoplasm; Nucleus; Secreted | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell surface (GO:0009986)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- extracellular matrix (GO:0031012)
- extracellular region (GO:0005576)
- extracellular space (GO:0005615)
- ficolin-1-rich granule membrane (GO:0101003)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 476 |
| PubMed broad count | 1655 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MAC2 |

**关键文献**:
1. Lgals3 Promotes Calcium Oxalate Crystal Formation and Kidney Injury Through Histone Lactylation-Mediated FGFR4 Activation.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39903812
2. Macrophages protect against sensory axon loss in peripheral neuropathy.. *Nature*. PMID: 39939762
3. LAMP3 inhibits autophagy and contributes to cell death by lysosomal membrane permeabilization.. *Autophagy*. PMID: 34802379
4. APOE4 impairs the microglial response in Alzheimer's disease by inducing TGFβ-mediated checkpoints.. *Nature immunology*. PMID: 37749326
5. Senescent endothelial cell-derived Galectin 3 promotes silicosis through endothelial-fibroblast and endothelial-macrophage crosstalk.. *Journal of hazardous materials*. PMID: 39955992

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.8 |
| 高置信度残基 (pLDDT>90) 占比 | 54.8% |
| 置信残基 (pLDDT 70-90) 占比 | 0.4% |
| 中等置信 (pLDDT 50-70) 占比 | 6.0% |
| 低置信 (pLDDT<50) 占比 | 38.8% |
| 有序区域 (pLDDT>70) 占比 | 55.2% |
| 可用 PDB 条目 | 1A3K, 1KJL, 1KJR, 2NMN, 2NMO, 2NN8, 2XG3, 3AYA, 3AYC, 3AYD |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1A3K, 1KJL, 1KJR, 2NMN, 2NMO, 2NN8, 2XG3, 3AYA, 3AYC, 3AYD）+ AlphaFold极高置信度预测（pLDDT=73.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013320, IPR044156, IPR001079; Pfam: PF00337 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LGALS3BP | 0.999 | 0.837 | — |
| MUC1 | 0.995 | 0.000 | — |
| CLEC7A | 0.994 | 0.294 | — |
| TRIM16 | 0.993 | 0.292 | — |
| FCGR2B | 0.992 | 0.292 | — |
| LAG3 | 0.990 | 0.000 | — |
| FN1 | 0.985 | 0.199 | — |
| ELN | 0.984 | 0.292 | — |
| PTPRC | 0.983 | 0.000 | — |
| GP6 | 0.974 | 0.048 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-3508325 | psi-mi:"MI:0018"(two hybrid) | pubmed:14611647|imex:IM-16925 |
| ENSP00000254301.9 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| CFTR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12000|pubmed:17110338 |
| EBI-1257125 | psi-mi:"MI:0096"(pull down) | pubmed:19463016|imex:IM-17246 |
| EBI-5327879 | psi-mi:"MI:0013"(biophysical) | pubmed:22106087|imex:IM-16985 |
| uvrB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| spoIVA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| metE | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A0J1HPY9 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| EBI-2809927 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.8 + PDB: 1A3K, 1KJL, 1KJR, 2NMN, 2NMO,  | pLDDT=73.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Secreted / Nucleoplasm, Cytosol; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. LGALS3 — Galectin-3，研究基础较多，新颖性有限。
2. 蛋白大小250 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 476 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 476 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P17931
- Protein Atlas: https://www.proteinatlas.org/ENSG00000131981-LGALS3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LGALS3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P17931
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000131981-LGALS3/subcellular

![](https://images.proteinatlas.org/5191/635_D6_5_red_green.jpg)
![](https://images.proteinatlas.org/5191/635_D6_6_red_green.jpg)
![](https://images.proteinatlas.org/5191/639_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/5191/639_D6_2_red_green.jpg)
![](https://images.proteinatlas.org/76528/1920_D10_30_cr5e39373c1daec_red_green.jpg)
![](https://images.proteinatlas.org/76528/1920_D10_3_cr5e39373c1d6a6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P17931-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
