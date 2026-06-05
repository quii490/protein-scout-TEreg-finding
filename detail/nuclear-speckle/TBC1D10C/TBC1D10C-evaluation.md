---
type: protein-evaluation
gene: "TBC1D10C"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TBC1D10C 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TBC1D10C |
| 蛋白名称 | Carabin |
| 蛋白大小 | 446 aa / 49.7 kDa |
| UniProt ID | Q8IV04 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear bodies; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 446 aa / 49.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000195, IPR035969, IPR050302; Pfam: PF00566 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- ficolin-1-rich granule membrane (GO:0101003)
- filopodium membrane (GO:0031527)
- membrane (GO:0016020)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 34 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Embryonic expression patterns of TBC1D10 subfamily genes in zebrafish.. *Gene expression patterns : GEP*. PMID: 34843939
2. TBC1D10C is a cytoskeletal functional linker that modulates cell spreading and phagocytosis in macrophages.. *Scientific reports*. PMID: 34686741
3. Enhanced cardiac TBC1D10C expression lowers heart rate and enhances exercise capacity and survival.. *Scientific reports*. PMID: 27667030
4. Integrative ATAC-seq and RNA-seq analysis associated with diabetic nephropathy and identification of novel targets for treatment by dapagliflozin.. *Cell biochemistry and function*. PMID: 38379015
5. All members of the EPI64 subfamily of TBC/RabGAPs also have GAP activities towards Ras.. *Journal of biochemistry*. PMID: 23248241

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.6 |
| 高置信度残基 (pLDDT>90) 占比 | 67.9% |
| 置信残基 (pLDDT 70-90) 占比 | 6.1% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 18.4% |
| 有序区域 (pLDDT>70) 占比 | 74.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=81.6，有序区 74.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000195, IPR035969, IPR050302; Pfam: PF00566 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RASAL3 | 0.809 | 0.000 | — |
| ARHGAP9 | 0.794 | 0.000 | — |
| RAB35 | 0.779 | 0.075 | — |
| TRAF3IP3 | 0.750 | 0.000 | — |
| PTPRCAP | 0.676 | 0.000 | — |
| RASA1 | 0.667 | 0.000 | — |
| ACAP1 | 0.631 | 0.000 | — |
| TBC1D13 | 0.620 | 0.000 | — |
| TBC1D22B | 0.593 | 0.000 | — |
| TBC1D21 | 0.593 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SHANK1 | psi-mi:"MI:0900"(p8 filamentous phage display) | imex:IM-26482|pubmed:30126976 |
| HOXA1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KLHL12 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRTAP5-9 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| NOTCH2NLA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| - | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.6 + PDB: 无 | pLDDT=81.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TBC1D10C — Carabin，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小446 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IV04
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175463-TBC1D10C/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TBC1D10C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IV04
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (approved)。来源: https://www.proteinatlas.org/ENSG00000175463-TBC1D10C/subcellular

![](https://images.proteinatlas.org/69743/1325_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/69743/1325_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/69743/1414_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/69743/1414_A7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IV04-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
