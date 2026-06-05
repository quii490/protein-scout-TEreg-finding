---
type: protein-evaluation
gene: "BRPF3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BRPF3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BRPF3 / KIAA1286 |
| 蛋白名称 | Bromodomain and PHD finger-containing protein 3 |
| 蛋白大小 | 1205 aa / 135.7 kDa |
| UniProt ID | Q9ULD4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Mitochondria; UniProt: Nucleus |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1205 aa / 135.7 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.1; PDB: 3PFS |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001487, IPR036427, IPR018359, IPR042005, IPR019 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.5/180** | |
| **归一化总分** | | | **69.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Mitochondria | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular region (GO:0005576)
- histone acetyltransferase complex (GO:0000123)
- MOZ/MORF histone acetyltransferase complex (GO:0070776)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1286 |

**关键文献**:
1. Identifying therapeutic target genes for migraine by systematic druggable genome-wide Mendelian randomization.. *The journal of headache and pain*. PMID: 38867170
2. BRPF3-HBO1 regulates replication origin activation and histone H3K14 acetylation.. *The EMBO journal*. PMID: 26620551
3. BRPF3-HUWE1-mediated regulation of MYST2 is required for differentiation and cell-cycle progression in embryonic stem cells.. *Cell death and differentiation*. PMID: 32555450
4. A novel feedback loop: CELF1/circ-CELF1/BRPF3/KAT7 in cardiac fibrosis.. *Acta pharmaceutica Sinica. B*. PMID: 41132846
5. Targeting BRPF3 moderately reverses olaparib resistance in high grade serous ovarian carcinoma.. *Molecular carcinogenesis*. PMID: 37493106

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.1 |
| 高置信度残基 (pLDDT>90) 占比 | 34.3% |
| 置信残基 (pLDDT 70-90) 占比 | 21.7% |
| 中等置信 (pLDDT 50-70) 占比 | 6.8% |
| 低置信 (pLDDT<50) 占比 | 37.3% |
| 有序区域 (pLDDT>70) 占比 | 56.0% |
| 可用 PDB 条目 | 3PFS |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.1），有序残基占 56.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001487, IPR036427, IPR018359, IPR042005, IPR019542; Pfam: PF00439, PF10513, PF13831 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KAT7 | 0.998 | 0.883 | — |
| MEAF6 | 0.997 | 0.897 | — |
| KAT6A | 0.992 | 0.705 | — |
| ING5 | 0.990 | 0.829 | — |
| BRD1 | 0.987 | 0.784 | — |
| KAT6B | 0.986 | 0.707 | — |
| BRPF1 | 0.964 | 0.594 | — |
| ING4 | 0.908 | 0.628 | — |
| KAT5 | 0.725 | 0.580 | — |
| TP53 | 0.713 | 0.421 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| pdpC2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| FYN | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| ABL1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| PIK3R1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| ENSP00000350267.6 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| PES1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H3-4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| TSG101 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.1 + PDB: 3PFS | pLDDT=67.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. BRPF3 — Bromodomain and PHD finger-containing protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1205 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9ULD4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000096070-BRPF3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BRPF3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9ULD4
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:16:29

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000096070-BRPF3/subcellular

![](https://images.proteinatlas.org/22787/195_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/22787/195_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/22787/196_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/22787/196_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/22787/197_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/22787/197_B8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9ULD4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
