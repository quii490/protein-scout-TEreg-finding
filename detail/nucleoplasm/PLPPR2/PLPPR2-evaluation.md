---
type: protein-evaluation
gene: "PLPPR2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLPPR2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLPPR2 / LPPR2, PRG4 |
| 蛋白名称 | Phospholipid phosphatase-related protein type 2 |
| 蛋白大小 | 343 aa / 36.9 kDa |
| UniProt ID | Q96GM1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 343 aa / 36.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043216, IPR000326, IPR036938; Pfam: PF01569 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Uncertain |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LPPR2, PRG4 |

**关键文献**:
1. Identification of lipid metabolism-related genes in myocardial infarction: implications for diagnosis and therapy.. *Journal of cardiothoracic surgery*. PMID: 40635026
2. Cell type-specific and subcellular expression of phospholipid phosphatase-related proteins to modulate lyso-phosphatidic acid synaptic signaling in the developing and adult CNS.. *Journal of neurochemistry*. PMID: 38994820
3. A novel paracetamol derivative alleviates lipopolysaccharide-induced neuroinflammation.. *European journal of pharmacology*. PMID: 39986592
4. Screening the hub genes and analyzing the mechanisms in discharged COVID-19 patients retesting positive through bioinformatics analysis.. *Journal of clinical laboratory analysis*. PMID: 35657140

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.0 |
| 高置信度残基 (pLDDT>90) 占比 | 50.1% |
| 置信残基 (pLDDT 70-90) 占比 | 19.8% |
| 中等置信 (pLDDT 50-70) 占比 | 10.5% |
| 低置信 (pLDDT<50) 占比 | 19.5% |
| 有序区域 (pLDDT>70) 占比 | 69.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=79.0，有序区 69.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043216, IPR000326, IPR036938; Pfam: PF01569 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCDC159 | 0.634 | 0.000 | — |
| NADK | 0.486 | 0.000 | — |
| FRAT2 | 0.484 | 0.000 | — |
| TMEM125 | 0.469 | 0.000 | — |
| COL9A2 | 0.468 | 0.065 | — |
| CLDN19 | 0.465 | 0.000 | — |
| IER2 | 0.461 | 0.000 | — |
| SWSAP1 | 0.454 | 0.000 | — |
| RNF214 | 0.451 | 0.451 | — |
| DOLPP1 | 0.447 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CLDN5 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SSMEM1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CD79A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| UBE2J1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMED9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GYPC | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CREB3L1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SMAGP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TMEM237 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.0 + PDB: 无 | pLDDT=79.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PLPPR2 — Phospholipid phosphatase-related protein type 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小343 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96GM1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105520-PLPPR2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLPPR2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96GM1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000105520-PLPPR2/subcellular

![](https://images.proteinatlas.org/48973/821_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/48973/821_E9_2_red_green.jpg)
![](https://images.proteinatlas.org/48973/831_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/48973/831_E3_3_red_green.jpg)
![](https://images.proteinatlas.org/48973/882_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/48973/882_E3_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96GM1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
