---
type: protein-evaluation
gene: "RBPJ"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RBPJ — REJECTED (研究热度过高 (PubMed strict=541，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RBPJ / IGKJRB, IGKJRB1, RBPJK, RBPSUH |
| 蛋白名称 | Recombining binding protein suppressor of hairless |
| 蛋白大小 | 500 aa / 55.6 kDa |
| UniProt ID | Q06330 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 500 aa / 55.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=541 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=85.0; PDB: 2F8X, 3NBN, 3V79, 6PY8 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR015350, IPR036358, IPR040159, IPR013783, IPR014 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.0/180** | |
| **归一化总分** | | | **51.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- MAML1-RBP-Jkappa- ICN1 complex (GO:0002193)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription repressor complex (GO:0017053)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 541 |
| PubMed broad count | 1124 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IGKJRB, IGKJRB1, RBPJK, RBPSUH |

**关键文献**:
1. Notch signaling regulates macrophage-mediated inflammation in metabolic dysfunction-associated steatotic liver disease.. *Immunity*. PMID: 39317200
2. Single-cell CRISPR screens in vivo map T cell fate regulomes in cancer.. *Nature*. PMID: 37968405
3. Genome-wide CRISPR screen in human T cells reveals regulators of FOXP3.. *Nature*. PMID: 40140585
4. In vivo CRISPR screening reveals nutrient signaling processes underpinning CD8(+) T cell fate decisions.. *Cell*. PMID: 33636132
5. Glucose dissociates DDX21 dimers to regulate mRNA splicing and tissue differentiation.. *Cell*. PMID: 36608661

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.0 |
| 高置信度残基 (pLDDT>90) 占比 | 71.2% |
| 置信残基 (pLDDT 70-90) 占比 | 10.2% |
| 中等置信 (pLDDT 50-70) 占比 | 5.6% |
| 低置信 (pLDDT<50) 占比 | 13.0% |
| 有序区域 (pLDDT>70) 占比 | 81.4% |
| 可用 PDB 条目 | 2F8X, 3NBN, 3V79, 6PY8 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2F8X, 3NBN, 3V79, 6PY8）+ AlphaFold高质量预测（pLDDT=85.0），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015350, IPR036358, IPR040159, IPR013783, IPR014756; Pfam: PF09270, PF09271, PF20144 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAML3 | 0.999 | 0.292 | — |
| MAML1 | 0.999 | 0.990 | — |
| MAML2 | 0.999 | 0.292 | — |
| NOTCH1 | 0.999 | 0.993 | — |
| NCOR2 | 0.998 | 0.705 | — |
| NOTCH2 | 0.998 | 0.758 | — |
| NOTCH3 | 0.998 | 0.855 | — |
| KAT2B | 0.992 | 0.328 | — |
| CIR1 | 0.989 | 0.261 | — |
| NOTCH4 | 0.988 | 0.133 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CIR1 | psi-mi:"MI:0018"(two hybrid) | pubmed:9874765|mint:MINT-65484 |
| EBNA2 | psi-mi:"MI:0018"(two hybrid) | pubmed:9874765|mint:MINT-65484 |
| SNW1 | psi-mi:"MI:0018"(two hybrid) | pubmed:10713164 |
| Bx42 | psi-mi:"MI:0018"(two hybrid) | pubmed:10713164 |
| EBI-322121 | psi-mi:"MI:0018"(two hybrid) | pubmed:10713164 |
| NCOR2 | psi-mi:"MI:0018"(two hybrid) | pubmed:10713164 |
| NOTCH1 | psi-mi:"MI:0018"(two hybrid) | pubmed:10713164 |
| MAML1 | psi-mi:"MI:0114"(x-ray crystallography) | imex:IM-11966|pubmed:16530044 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| MED27 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.0 + PDB: 2F8X, 3NBN, 3V79, 6PY8 | pLDDT=85.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm | 一致 |
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
1. RBPJ — Recombining binding protein suppressor of hairless，研究基础较多，新颖性有限。
2. 蛋白大小500 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 541 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 541 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q06330
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168214-RBPJ/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RBPJ
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q06330
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000168214-RBPJ/subcellular

![](https://images.proteinatlas.org/60647/1227_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/60647/1227_G4_3_red_green.jpg)
![](https://images.proteinatlas.org/60647/1252_B11_2_red_green.jpg)
![](https://images.proteinatlas.org/60647/1252_B11_3_red_green.jpg)
![](https://images.proteinatlas.org/60647/1271_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/60647/1271_G4_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q06330-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q06330 |
| SMART | SM01268;SM01267; |
| UniProt Domain [FT] | DOMAIN 355..445; /note="IPT/TIG" |
| InterPro | IPR015350;IPR036358;IPR040159;IPR013783;IPR014756;IPR008967;IPR015351;IPR037095;IPR038007; |
| Pfam | PF09270;PF09271;PF20144; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000168214-RBPJ/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FBXO42 | Intact, Biogrid | true |
| KDM1A | Intact, Biogrid | true |
| NCOR2 | Intact, Biogrid | true |
| NOTCH1 | Intact, Biogrid | true |
| RITA1 | Intact, Biogrid | true |
| SMARCA4 | Intact, Biogrid | true |
| SNW1 | Intact, Biogrid | true |
| SPEN | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
