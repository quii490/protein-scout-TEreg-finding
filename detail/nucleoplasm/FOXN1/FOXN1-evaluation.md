---
type: protein-evaluation
gene: "FOXN1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FOXN1 — REJECTED (研究热度过高 (PubMed strict=270，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOXN1 / RONU, WHN |
| 蛋白名称 | Forkhead box protein N1 |
| 蛋白大小 | 648 aa / 68.9 kDa |
| UniProt ID | O15353 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 648 aa / 68.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=270 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.7; PDB: 5OCN, 6EL8 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR047401, IPR001766, IPR049624, IPR030456, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.5/180** | |
| **归一化总分** | | | **46.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 270 |
| PubMed broad count | 606 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RONU, WHN |

**关键文献**:
1. Developmental trajectory and evolutionary origin of thymic mimetic cells.. *Nature*. PMID: 40500437
2. Evolution of thymopoietic microenvironments.. *Open biology*. PMID: 33622100
3. FOXN1 deficient nude severe combined immunodeficiency.. *Orphanet journal of rare diseases*. PMID: 28077132
4. Foxn1 in Skin Development, Homeostasis and Wound Healing.. *International journal of molecular sciences*. PMID: 29973508
5. Human FOX gene family (Review).. *International journal of oncology*. PMID: 15492844

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.7 |
| 高置信度残基 (pLDDT>90) 占比 | 16.0% |
| 置信残基 (pLDDT 70-90) 占比 | 1.5% |
| 中等置信 (pLDDT 50-70) 占比 | 20.4% |
| 低置信 (pLDDT<50) 占比 | 62.0% |
| 有序区域 (pLDDT>70) 占比 | 17.5% |
| 可用 PDB 条目 | 5OCN, 6EL8 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=53.7），有序残基占 17.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR047401, IPR001766, IPR049624, IPR030456, IPR036388; Pfam: PF00250 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WNT5B | 0.813 | 0.046 | — |
| HOXC13 | 0.794 | 0.184 | — |
| AIRE | 0.756 | 0.073 | — |
| SUPT6H | 0.755 | 0.000 | — |
| WNT10B | 0.723 | 0.045 | — |
| GCM2 | 0.720 | 0.067 | — |
| WNT3 | 0.694 | 0.046 | — |
| WNT4 | 0.687 | 0.046 | — |
| PSMB11 | 0.675 | 0.000 | — |
| FZD7 | 0.669 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DMRT3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CDC23 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MAPKBP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TSSK1B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HOXA1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TLE5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TRAPPC6A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CDA | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SPATC1L | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PIN1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 12
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.7 + PDB: 5OCN, 6EL8 | pLDDT=53.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 12 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FOXN1 — Forkhead box protein N1，研究基础较多，新颖性有限。
2. 蛋白大小648 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 270 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=53.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 270 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15353
- Protein Atlas: https://www.proteinatlas.org/ENSG00000109101-FOXN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FOXN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15353
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O15353-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O15353 |
| SMART | SM00339; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR047401;IPR001766;IPR049624;IPR030456;IPR036388;IPR036390; |
| Pfam | PF00250; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000109101-FOXN1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDA | Intact | false |
| CDC23 | Intact | false |
| DMRT3 | Intact | false |
| LHX8 | Intact | false |
| MAPKBP1 | Intact | false |
| PIN1 | Intact | false |
| TRAF2 | Intact | false |
| TSSK1B | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
