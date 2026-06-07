---
type: protein-evaluation
gene: "LDB1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## LDB1 — REJECTED (研究热度过高 (PubMed strict=236，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LDB1 / CLIM2 |
| 蛋白名称 | LIM domain-binding protein 1 |
| 蛋白大小 | 411 aa / 46.5 kDa |
| UniProt ID | Q86U70 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 411 aa / 46.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=236 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=70.4; PDB: 2XJY, 2XJZ, 2YPA, 6TYD, 7OB5, 7OB8, 8HIB |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR041363, IPR029005; Pfam: PF17916, PF01803 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **102.0/180** | |
| **归一化总分** | | | **56.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- beta-catenin-TCF complex (GO:1990907)
- cell leading edge (GO:0031252)
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)
- transcription regulator complex (GO:0005667)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 236 |
| PubMed broad count | 315 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CLIM2 |

**关键文献**:
1. Nail-patella syndrome.. *Pflugers Archiv : European journal of physiology*. PMID: 28681095
2. LDB1 establishes multi-enhancer networks to regulate gene expression.. *Molecular cell*. PMID: 39721581
3. Solid phase transitions as a solution to the genome folding paradox.. *Nature*. PMID: 40369073
4. Gene Clusters Reveal Fundamental Principles of Genome Folding and Transcriptional Regulation.. *Annual review of cell and developmental biology*. PMID: 41034155
5. Single-stranded DNA-binding proteins are essential components of the architectural LDB1 protein complex.. *Molecular cell*. PMID: 40803327

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.4 |
| 高置信度残基 (pLDDT>90) 占比 | 42.1% |
| 置信残基 (pLDDT 70-90) 占比 | 11.4% |
| 中等置信 (pLDDT 50-70) 占比 | 7.8% |
| 低置信 (pLDDT<50) 占比 | 38.7% |
| 有序区域 (pLDDT>70) 占比 | 53.5% |
| 可用 PDB 条目 | 2XJY, 2XJZ, 2YPA, 6TYD, 7OB5, 7OB8, 8HIB, 8SSU, 9F5B |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2XJY, 2XJZ, 2YPA, 6TYD, 7OB5, 7OB8, 8HIB, 8SSU, 9F5B）+ AlphaFold极高置信度预测（pLDDT=70.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR041363, IPR029005; Pfam: PF17916, PF01803 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LHX3 | 0.999 | 0.648 | — |
| LMO2 | 0.999 | 0.980 | — |
| TAL1 | 0.999 | 0.922 | — |
| ISL1 | 0.998 | 0.732 | — |
| GATA1 | 0.998 | 0.127 | — |
| TCF3 | 0.997 | 0.294 | — |
| SSBP2 | 0.997 | 0.988 | — |
| LMO1 | 0.996 | 0.747 | — |
| GATA2 | 0.994 | 0.113 | — |
| CBFA2T3 | 0.991 | 0.516 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TOLLIP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SSBP4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| LMX1B | psi-mi:"MI:0018"(two hybrid) | pubmed:12792813 |
| SSBP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ATXN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| PSMA1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| IRAK3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| LMO2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| PSMD10 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| POLR1B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.4 + PDB: 2XJY, 2XJZ, 2YPA, 6TYD, 7OB5,  | pLDDT=70.4, v6 | 预测+实验 |
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
1. LDB1 — LIM domain-binding protein 1，研究基础较多，新颖性有限。
2. 蛋白大小411 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 236 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 236 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86U70
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198728-LDB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LDB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86U70
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000198728-LDB1/subcellular

![](https://images.proteinatlas.org/34488/434_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/34488/434_A4_2_red_green.jpg)
![](https://images.proteinatlas.org/34488/450_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/34488/450_A4_2_red_green.jpg)
![](https://images.proteinatlas.org/34488/453_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/34488/453_A4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86U70-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86U70 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 336..375; /note="LIM interaction domain (LID)"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01302" |
| InterPro | IPR041363;IPR029005; |
| Pfam | PF17916;PF01803; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000198728-LDB1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| LHX2 | Intact, Biogrid | true |
| LHX6 | Intact, Biogrid | true |
| LHX8 | Intact, Biogrid | true |
| LMO1 | Intact, Biogrid | true |
| LMO2 | Intact, Biogrid | true |
| LMO3 | Intact, Biogrid | true |
| LMO4 | Intact, Biogrid | true |
| LMX1B | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
