---
type: protein-evaluation
gene: "ERBIN"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ERBIN — REJECTED (研究热度过高 (PubMed strict=118，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ERBIN / ERBB2IP, KIAA1225, LAP2 |
| 蛋白名称 | Erbin |
| 蛋白大小 | 1412 aa / 158.3 kDa |
| UniProt ID | Q96RT1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Cell Junctions; UniProt: Cell junction, hemidesmosome; Nucleus membrane; Basolateral  |
| 蛋白大小 | 5/10 | ×1 | 5 | 1412 aa / 158.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=118 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.7; PDB: 1MFG, 1MFL, 1N7T, 2H3L, 2QBW, 3CH8, 6Q0M |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001611, IPR003591, IPR032675, IPR055414, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.5/180** | |
| **归一化总分** | | | **42.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cell Junctions | Supported |
| UniProt | Cell junction, hemidesmosome; Nucleus membrane; Basolateral cell membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- basal plasma membrane (GO:0009925)
- basement membrane (GO:0005604)
- basolateral plasma membrane (GO:0016323)
- cell junction (GO:0030054)
- cytoplasm (GO:0005737)
- glutamatergic synapse (GO:0098978)
- hemidesmosome (GO:0030056)
- neuromuscular junction (GO:0031594)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 118 |
| PubMed broad count | 313 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ERBB2IP, KIAA1225, LAP2 |

**关键文献**:
1. Targeting Erbin-mitochondria axis in platelets/megakaryocytes promotes B cell-mediated antitumor immunity.. *Cell metabolism*. PMID: 38232736
2. New insights into the interplay between autophagy, gut microbiota and inflammatory responses in IBD.. *Autophagy*. PMID: 31286804
3. Erbin protects against sepsis-associated encephalopathy by attenuating microglia pyroptosis via IRE1α/Xbp1s-Ca(2+) axis.. *Journal of neuroinflammation*. PMID: 36171629
4. CRISPR-Cas9 library screening combined with an exosome-targeted delivery system addresses tumorigenesis/TMZ resistance in the mesenchymal subtype of glioblastoma.. *Theranostics*. PMID: 38773970
5. Erbin alleviates sepsis-induced cardiomyopathy by inhibiting RIPK1-dependent necroptosis through activating PKA/CREB pathway.. *Cellular signalling*. PMID: 39216682

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.7 |
| 高置信度残基 (pLDDT>90) 占比 | 30.5% |
| 置信残基 (pLDDT 70-90) 占比 | 5.5% |
| 中等置信 (pLDDT 50-70) 占比 | 4.2% |
| 低置信 (pLDDT<50) 占比 | 59.8% |
| 有序区域 (pLDDT>70) 占比 | 36.0% |
| 可用 PDB 条目 | 1MFG, 1MFL, 1N7T, 2H3L, 2QBW, 3CH8, 6Q0M, 6Q0N, 6Q0U, 6UBH |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.7），有序残基占 36.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001611, IPR003591, IPR032675, IPR055414, IPR001478; Pfam: PF23598, PF13855, PF00595 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ERBB2 | 0.999 | 0.842 | — |
| NOD2 | 0.993 | 0.404 | — |
| PKP4 | 0.935 | 0.757 | — |
| SMAD2 | 0.888 | 0.685 | — |
| SHOC2 | 0.888 | 0.292 | — |
| DSG1 | 0.877 | 0.000 | — |
| EGFR | 0.875 | 0.175 | — |
| ITGB4 | 0.850 | 0.303 | — |
| DST | 0.847 | 0.304 | — |
| SMAD3 | 0.841 | 0.685 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000284037.4 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| SHOC2 | psi-mi:"MI:0096"(pull down) | imex:IM-14435|pubmed:16301319 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| STAT3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| tuf | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SMAD2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:18729074|imex:IM-19222 |
| APC | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| leuO | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SMAD3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:18729074|imex:IM-19222 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.7 + PDB: 1MFG, 1MFL, 1N7T, 2H3L, 2QBW,  | pLDDT=55.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell junction, hemidesmosome; Nucleus membrane; Ba / Plasma membrane, Cell Junctions | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ERBIN — Erbin，研究基础较多，新颖性有限。
2. 蛋白大小1412 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 118 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=55.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 118 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96RT1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112851-ERBIN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ERBIN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96RT1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96RT1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96RT1 |
| SMART | SM00364;SM00365;SM00369;SM00228; |
| UniProt Domain [FT] | DOMAIN 1321..1410; /note="PDZ"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00143" |
| InterPro | IPR001611;IPR003591;IPR032675;IPR055414;IPR001478;IPR036034;IPR050614; |
| Pfam | PF23598;PF13855;PF00595; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000112851-ERBIN/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PKP4 | Intact, Biogrid | true |
| YWHAE | Biogrid, Opencell | true |
| YWHAZ | Biogrid, Opencell | true |
| ALK | Biogrid | false |
| APC | Biogrid | false |
| ARVCF | Biogrid | false |
| AXL | Biogrid | false |
| BCR | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
