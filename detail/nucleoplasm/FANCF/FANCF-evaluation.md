---
type: protein-evaluation
gene: "FANCF"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FANCF — REJECTED (研究热度过高 (PubMed strict=115，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FANCF |
| 蛋白名称 | Fanconi anemia group F protein |
| 蛋白大小 | 374 aa / 42.3 kDa |
| UniProt ID | Q9NPI8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 374 aa / 42.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=115 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=78.6; PDB: 2IQC, 7KZP, 7KZQ, 7KZR, 7KZS, 7KZT, 7KZV |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR035428, IPR038505; Pfam: PF11107 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- Fanconi anaemia nuclear complex (GO:0043240)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 115 |
| PubMed broad count | 184 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Fanconi Anemia.. **. PMID: 20301575
2. The FANCC-FANCE-FANCF complex is evolutionarily conserved and regulates meiotic recombination.. *Nucleic acids research*. PMID: 36652992
3. CSRNP1 Promotes Apoptosis and Mitochondrial Dysfunction via ROS-Mediated JNK/p38 MAPK Pathway Activation in Hepatocellular Carcinoma.. *Oncology research*. PMID: 41502527
4. The Fanconi anemia gene product FANCF is a flexible adaptor protein.. *The Journal of biological chemistry*. PMID: 15262960
5. Promoter Hypermethylation of FANCF and Susceptibility and Prognosis of Epithelial Ovarian Cancer.. *Reproductive sciences (Thousand Oaks, Calif.)*. PMID: 26507869

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.6 |
| 高置信度残基 (pLDDT>90) 占比 | 36.6% |
| 置信残基 (pLDDT 70-90) 占比 | 38.2% |
| 中等置信 (pLDDT 50-70) 占比 | 13.9% |
| 低置信 (pLDDT<50) 占比 | 11.2% |
| 有序区域 (pLDDT>70) 占比 | 74.8% |
| 可用 PDB 条目 | 2IQC, 7KZP, 7KZQ, 7KZR, 7KZS, 7KZT, 7KZV |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2IQC, 7KZP, 7KZQ, 7KZR, 7KZS, 7KZT, 7KZV）+ AlphaFold极高置信度预测（pLDDT=78.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR035428, IPR038505; Pfam: PF11107 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FANCC | 0.999 | 0.998 | — |
| FANCM | 0.999 | 0.994 | — |
| FANCG | 0.999 | 0.998 | — |
| FANCB | 0.999 | 0.998 | — |
| FAAP100 | 0.999 | 0.998 | — |
| HES1 | 0.999 | 0.994 | — |
| FANCA | 0.999 | 0.998 | — |
| FANCD2 | 0.999 | 0.800 | — |
| FAAP20 | 0.999 | 0.994 | — |
| CENPX | 0.999 | 0.994 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FANCA | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:11063725 |
| FANCG | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:11063725 |
| MARK3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| OLFM2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| aguA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| FANCM | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17289582|imex:IM-25488 |
| TCP11 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| Hacd3 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| PPP5C | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| HTT | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.6 + PDB: 2IQC, 7KZP, 7KZQ, 7KZR, 7KZS,  | pLDDT=78.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
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
1. FANCF — Fanconi anemia group F protein，研究基础较多，新颖性有限。
2. 蛋白大小374 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 115 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 115 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NPI8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183161-FANCF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FANCF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NPI8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NPI8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NPI8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR035428;IPR038505; |
| Pfam | PF11107; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000183161-FANCF/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FANCA | Intact, Biogrid | true |
| FANCG | Intact, Biogrid | true |
| CENPS | Biogrid | false |
| CENPX | Biogrid | false |
| CTBP1 | Biogrid | false |
| FAAP100 | Biogrid | false |
| FAAP20 | Biogrid | false |
| FANCB | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
