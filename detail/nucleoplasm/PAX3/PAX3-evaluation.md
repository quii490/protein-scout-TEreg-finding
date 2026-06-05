---
type: protein-evaluation
gene: "PAX3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PAX3 — REJECTED (研究热度过高 (PubMed strict=1442，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PAX3 / HUP2 |
| 蛋白名称 | Paired box protein Pax-3 |
| 蛋白大小 | 479 aa / 53.0 kDa |
| UniProt ID | P23760 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 479 aa / 53.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1442 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.9; PDB: 3CMY |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR017970, IPR009057, IPR043182, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1442 |
| PubMed broad count | 2357 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HUP2 |

**关键文献**:
1. PAX genes.. *Current opinion in genetics & development*. PMID: 7919921
2. Therapeutic targeting of ATR in alveolar rhabdomyosarcoma.. *Nature communications*. PMID: 35879366
3. PAX3-FOXO1 Drives Targetable Cell State-Dependent Metabolic Vulnerabilities in Rhabdomyosarcoma.. *Cancer research*. PMID: 40911784
4. The expression and function of PAX3 in development and disease.. *Gene*. PMID: 29730428
5. PAX3 Regulatory Signatures and Gene Targets in Melanoma Cells.. *Genes*. PMID: 40428399

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.9 |
| 高置信度残基 (pLDDT>90) 占比 | 29.0% |
| 置信残基 (pLDDT 70-90) 占比 | 8.4% |
| 中等置信 (pLDDT 50-70) 占比 | 19.2% |
| 低置信 (pLDDT<50) 占比 | 43.4% |
| 有序区域 (pLDDT>70) 占比 | 37.4% |
| 可用 PDB 条目 | 3CMY |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.9），有序残基占 37.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR017970, IPR009057, IPR043182, IPR001523; Pfam: PF00046, PF00292, PF12360 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SOX10 | 0.997 | 0.629 | — |
| MYF5 | 0.959 | 0.000 | — |
| MYOD1 | 0.950 | 0.000 | — |
| MYOG | 0.945 | 0.000 | — |
| FOXO1 | 0.938 | 0.249 | — |
| NCOA1 | 0.936 | 0.000 | — |
| SIX1 | 0.925 | 0.000 | — |
| PAX7 | 0.907 | 0.000 | — |
| MYF6 | 0.900 | 0.000 | — |
| MITF | 0.881 | 0.088 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SOX10 | psi-mi:"MI:0018"(two hybrid) | pubmed:11029584|imex:IM-19682 |
| POU3F2 | psi-mi:"MI:0018"(two hybrid) | pubmed:11029584|imex:IM-19682 |
| SRC | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| FYN | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| UBB | psi-mi:"MI:0071"(molecular sieving) | imex:IM-12055|pubmed:17662948 |
| PSMD4 | psi-mi:"MI:0096"(pull down) | imex:IM-12055|pubmed:17662948 |
| RAD23B | psi-mi:"MI:0096"(pull down) | imex:IM-12055|pubmed:17662948 |
| ABL1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.9 + PDB: 3CMY | pLDDT=63.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. PAX3 — Paired box protein Pax-3，研究基础较多，新颖性有限。
2. 蛋白大小479 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1442 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=63.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1442 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P23760
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135903-PAX3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PAX3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P23760
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000135903-PAX3/subcellular

![](https://images.proteinatlas.org/63659/1152_F3_1_red_green.jpg)
![](https://images.proteinatlas.org/63659/1152_F3_3_red_green.jpg)
![](https://images.proteinatlas.org/63659/1156_F3_1_red_green.jpg)
![](https://images.proteinatlas.org/63659/1156_F3_2_red_green.jpg)
![](https://images.proteinatlas.org/63659/1269_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/63659/1269_E12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P23760-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
