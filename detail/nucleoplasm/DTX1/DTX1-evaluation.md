---
type: protein-evaluation
gene: "DTX1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DTX1 — REJECTED (研究热度过高 (PubMed strict=110，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DTX1 |
| 蛋白名称 | E3 ubiquitin-protein ligase DTX1 |
| 蛋白大小 | 620 aa / 67.4 kDa |
| UniProt ID | Q86Y01 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Nuclear bodies; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 620 aa / 67.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=110 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=74.4; PDB: 6Y5N, 6Y5P, 8R5N, 8R6A, 8R6B |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039396, IPR039399, IPR039398, IPR018123, IPR004 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Nuclear bodies | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 110 |
| PubMed broad count | 373 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Simplified algorithm for genetic subtyping in diffuse large B-cell lymphoma.. *Signal transduction and targeted therapy*. PMID: 37032379
2. Phycotoxins.. *Journal of AOAC International*. PMID: 10367395
3. Ubiquitylation of nucleic acids by DELTEX ubiquitin E3 ligase DTX3L.. *EMBO reports*. PMID: 39242775
4. FOXP3 (in)stability and cancer immunotherapy.. *Cytokine*. PMID: 38547750
5. The DTX Protein Family: An Emerging Set of E3 Ubiquitin Ligases in Cancer.. *Cells*. PMID: 37443713

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.4 |
| 高置信度残基 (pLDDT>90) 占比 | 42.3% |
| 置信残基 (pLDDT 70-90) 占比 | 22.9% |
| 中等置信 (pLDDT 50-70) 占比 | 11.0% |
| 低置信 (pLDDT<50) 占比 | 23.9% |
| 有序区域 (pLDDT>70) 占比 | 65.2% |
| 可用 PDB 条目 | 6Y5N, 6Y5P, 8R5N, 8R6A, 8R6B |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6Y5N, 6Y5P, 8R5N, 8R6A, 8R6B）+ AlphaFold极高置信度预测（pLDDT=74.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039396, IPR039399, IPR039398, IPR018123, IPR004170; Pfam: PF18102, PF02825 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NOTCH1 | 0.984 | 0.727 | — |
| NOTCH2 | 0.918 | 0.133 | — |
| DNER | 0.869 | 0.071 | — |
| NOTCH3 | 0.863 | 0.133 | — |
| ITCH | 0.844 | 0.561 | — |
| NOTCH4 | 0.818 | 0.071 | — |
| RBPJ | 0.808 | 0.111 | — |
| DTX3L | 0.806 | 0.292 | — |
| NRARP | 0.773 | 0.053 | — |
| ANK2 | 0.765 | 0.050 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| G3BP1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| DEFA5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CRK | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| UBE2C | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2D1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2D2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2D3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2D4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2E1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2N | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.4 + PDB: 6Y5N, 6Y5P, 8R5N, 8R6A, 8R6B | pLDDT=74.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Cytosol; 额外: Nuclear bodies | 一致 |
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
1. DTX1 — E3 ubiquitin-protein ligase DTX1，研究基础较多，新颖性有限。
2. 蛋白大小620 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 110 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 110 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86Y01
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135144-DTX1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DTX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86Y01
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/DTX1/IF_images/DTX1_IF_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000135144-DTX1/subcellular

![](https://images.proteinatlas.org/51249/1213_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/51249/1213_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/51249/1269_F1_5_red_green.jpg)
![](https://images.proteinatlas.org/51249/1269_F1_7_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86Y01-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86Y01 |
| SMART | SM00184;SM00678; |
| UniProt Domain [FT] | DOMAIN 14..94; /note="WWE 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00248"; DOMAIN 95..171; /note="WWE 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00248" |
| InterPro | IPR039396;IPR039399;IPR039398;IPR018123;IPR004170;IPR037197;IPR001841;IPR013083; |
| Pfam | PF18102;PF02825; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000135144-DTX1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ITCH | Intact, Biogrid | true |
| EIF3F | Biogrid | false |
| EP300 | Biogrid | false |
| MAP3K1 | Biogrid | false |
| NOTCH1 | Biogrid | false |
| PRKAR1A | Intact | false |
| TAX1BP3 | Biogrid | false |
| UBE2D2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
