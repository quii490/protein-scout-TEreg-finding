---
type: protein-evaluation
gene: "SSX1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SSX1 — REJECTED (研究热度过高 (PubMed strict=242，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SSX1 |
| 蛋白名称 | Protein SSX1 |
| 蛋白大小 | 188 aa / 21.9 kDa |
| UniProt ID | Q16384 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; UniProt: Cytoplasm, cytoskeleton, flagellum axoneme |
| 蛋白大小 | 8/10 | ×1 | 8 | 188 aa / 21.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=242 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.6; PDB: 8HR1 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003655, IPR001909, IPR036051, IPR019041; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.0/180** | |
| **归一化总分** | | | **43.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Approved |
| UniProt | Cytoplasm, cytoskeleton, flagellum axoneme | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)
- sperm flagellum (GO:0036126)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 242 |
| PubMed broad count | 372 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of novel SSX1 fusions in synovial sarcoma.. *Modern pathology : an official journal of the United States and Canadian Academy of Pathology, Inc*. PMID: 34504309
2. Cooperation between SS18-SSX1 and miR-214 in Synovial Sarcoma Development and Progression.. *Cancers*. PMID: 32019274
3. Ossifying synovial sarcoma.. *Pathology, research and practice*. PMID: 19041192
4. Dual colour fluorescence in situ hybridization to paraffin-embedded samples to deduce the presence of the der(X)t(X;18)(p11.2;q11.2) and involvement of either the SSX1 or SSX2 gene: a diagnostic and prognostic aid for synovial sarcoma.. *The Journal of pathology*. PMID: 10398111
5. Higher Expression Levels of SSX1 and SSX2 in Patients with Colon Cancer: Regulated In Vitro by the Inhibition of Methylation and Histone Deacetylation.. *Medicina (Kaunas, Lithuania)*. PMID: 37241221

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.6 |
| 高置信度残基 (pLDDT>90) 占比 | 26.6% |
| 置信残基 (pLDDT 70-90) 占比 | 15.4% |
| 中等置信 (pLDDT 50-70) 占比 | 42.0% |
| 低置信 (pLDDT<50) 占比 | 16.0% |
| 有序区域 (pLDDT>70) 占比 | 42.0% |
| 可用 PDB 条目 | 8HR1 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.6），有序残基占 42.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003655, IPR001909, IPR036051, IPR019041; Pfam: PF09514 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SS18 | 0.969 | 0.000 | — |
| SSX2 | 0.966 | 0.000 | — |
| SS18L1 | 0.878 | 0.000 | — |
| TLE1 | 0.778 | 0.000 | — |
| SSX2IP | 0.761 | 0.000 | — |
| ZNF83 | 0.760 | 0.000 | — |
| ZNF117 | 0.760 | 0.000 | — |
| SSX3 | 0.755 | 0.000 | — |
| MAGEC2 | 0.743 | 0.358 | — |
| MAGEA1 | 0.726 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.6 + PDB: 8HR1 | pLDDT=68.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, flagellum axoneme / Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SSX1 — Protein SSX1，研究基础较多，新颖性有限。
2. 蛋白大小188 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 242 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=68.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 242 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q16384
- Protein Atlas: https://www.proteinatlas.org/ENSG00000126752-SSX1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SSX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q16384
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000126752-SSX1/subcellular

![](https://images.proteinatlas.org/45683/1397_A4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45683/1397_A4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/45683/1402_A4_10_blue_red_green.jpg)
![](https://images.proteinatlas.org/45683/1402_A4_11_blue_red_green.jpg)
![](https://images.proteinatlas.org/45683/1440_H11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/45683/1440_H11_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q16384-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q16384 |
| SMART | SM00349; |
| UniProt Domain [FT] | DOMAIN 20..83; /note="KRAB-related"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00120" |
| InterPro | IPR003655;IPR001909;IPR036051;IPR019041; |
| Pfam | PF09514; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000126752-SSX1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDCA7L | Intact | false |
| MAGEC2 | Intact | false |
| MTURN | Intact | false |
| NCALD | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
