---
type: protein-evaluation
gene: "LMO1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## LMO1 — REJECTED (研究热度过高 (PubMed strict=111，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LMO1 / RBTN1, RHOM1, TTG1 |
| 蛋白名称 | Rhombotin-1 |
| 蛋白大小 | 156 aa / 17.8 kDa |
| UniProt ID | P25800 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 156 aa / 17.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=111 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR050945, IPR001781; Pfam: PF00412 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **90.5/180** | |
| **归一化总分** | | | **50.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 111 |
| PubMed broad count | 176 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RBTN1, RHOM1, TTG1 |

**关键文献**:
1. Transcription Factor TAL1 in Erythropoiesis.. *Advances in experimental medicine and biology*. PMID: 39017847
2. Associations between LMO1 gene polymorphisms and central nervous system tumor susceptibility.. *Pediatric investigation*. PMID: 34938970
3. Dissecting gene regulatory networks governing human cortical cell fate.. *Nature*. PMID: 41565813
4. Genetic predisposition to neuroblastoma mediated by a LMO1 super-enhancer polymorphism.. *Nature*. PMID: 26560027
5. Associations between LMO1 gene polymorphisms and Wilms' tumor susceptibility.. *Oncotarget*. PMID: 28881592

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.2 |
| 高置信度残基 (pLDDT>90) 占比 | 69.9% |
| 置信残基 (pLDDT 70-90) 占比 | 21.8% |
| 中等置信 (pLDDT 50-70) 占比 | 2.6% |
| 低置信 (pLDDT<50) 占比 | 5.8% |
| 有序区域 (pLDDT>70) 占比 | 91.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.2，有序区 91.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050945, IPR001781; Pfam: PF00412 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LDB1 | 0.996 | 0.747 | — |
| TAL1 | 0.964 | 0.477 | — |
| LDB2 | 0.955 | 0.456 | — |
| TAL2 | 0.894 | 0.250 | — |
| LYL1 | 0.886 | 0.235 | — |
| GATA3 | 0.859 | 0.536 | — |
| GATA1 | 0.854 | 0.139 | — |
| TCF3 | 0.850 | 0.061 | — |
| TLX1 | 0.830 | 0.104 | — |
| TLX3 | 0.824 | 0.104 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSP82 | psi-mi:"MI:0397"(two hybrid array) | pubmed:15766533 |
| VPS5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| NAF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| MET30 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SIS1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| ECM10 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| YDJ1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| TFIP11 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.2 + PDB: 无 | pLDDT=88.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. LMO1 — Rhombotin-1，研究基础较多，新颖性有限。
2. 蛋白大小156 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 111 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 111 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P25800
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166407-LMO1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LMO1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P25800
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P25800-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P25800 |
| SMART | SM00132; |
| UniProt Domain [FT] | DOMAIN 24..83; /note="LIM zinc-binding 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00125"; DOMAIN 88..147; /note="LIM zinc-binding 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00125" |
| InterPro | IPR050945;IPR001781; |
| Pfam | PF00412; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000166407-LMO1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| LDB1 | Intact, Biogrid | true |
| ZBTB43 | Intact, Biogrid | true |
| AKNA | Intact | false |
| ASB15 | Intact | false |
| BCAS2 | Intact | false |
| BIVM | Intact | false |
| BLZF1 | Intact | false |
| BNC2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
