---
type: protein-evaluation
gene: "DDX50"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DDX50 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DDX50 |
| 蛋白名称 | ATP-dependent RNA helicase DDX50 |
| 蛋白大小 | 737 aa / 82.6 kDa |
| UniProt ID | Q9BQ39 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoli; UniProt: Nucleus, nucleolus; Cytoplasm |
| 蛋白大小 | 10/10 | x1 | 10 | 737 aa / 82.6 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=72.9; PDB: 2E29 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR059027, IPR011545, IPR050079, IPR012562, IPR014 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.5/180** | |
| **归一化总分** | | | **75.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Enhanced |
| UniProt | Nucleus, nucleolus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- membrane (GO:0016020)
- nucleolus (GO:0005730)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 15 |
| 别名(未计入scoring) |  |

**关键文献**:
1. A chemical probe to modulate human GID4 Pro/N-degron interactions.. *Nature chemical biology*. PMID: 38773330
2. DDX50 cooperates with STAU1 to effect stabilization of pro-differentiation RNAs.. *Cell reports*. PMID: 39764852
3. DDX50 Is a Viral Restriction Factor That Enhances IRF3 Activation.. *Viruses*. PMID: 35215908
4. The association of immunosurveillance and distant metastases in colorectal cancer.. *Journal of cancer research and clinical oncology*. PMID: 34476575
5. Study on biomarkers of homocysteine-induced transformation of vascular smooth muscle cells into foam cells.. *Scientific reports*. PMID: 41644998

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.9 |
| 高置信度残基 (pLDDT>90) 占比 | 28.2% |
| 置信残基 (pLDDT 70-90) 占比 | 40.3% |
| 中等置信 (pLDDT 50-70) 占比 | 4.7% |
| 低置信 (pLDDT<50) 占比 | 26.7% |
| 有序区域 (pLDDT>70) 占比 | 68.5% |
| 可用 PDB 条目 | 2E29 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=72.9，有序区 68.5%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR059027, IPR011545, IPR050079, IPR012562, IPR014001; Pfam: PF26142, PF00270, PF08152 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARMC8 | 0.768 | 0.329 | — |
| DDX54 | 0.720 | 0.420 | — |
| PES1 | 0.718 | 0.269 | — |
| DDX18 | 0.710 | 0.000 | — |
| DDX56 | 0.709 | 0.070 | — |
| PRKRA | 0.701 | 0.596 | — |
| NIFK | 0.693 | 0.501 | — |
| NOP56 | 0.691 | 0.509 | — |
| SRSF2 | 0.686 | 0.000 | — |
| DDX24 | 0.671 | 0.101 | — |

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
| 三维结构 | AlphaFold pLDDT=72.9 + PDB: 2E29 | pLDDT=72.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus; Cytoplasm / Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DDX50 -- ATP-dependent RNA helicase DDX50，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小737 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BQ39
- Protein Atlas: https://www.proteinatlas.org/ENSG00000107625-DDX50/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DDX50
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BQ39
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (enhanced)。来源: https://www.proteinatlas.org/ENSG00000107625-DDX50/subcellular

![](https://images.proteinatlas.org/37388/403_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/37388/403_C5_2_red_green.jpg)
![](https://images.proteinatlas.org/37388/406_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/37388/406_C5_2_red_green.jpg)
![](https://images.proteinatlas.org/37388/408_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/37388/408_C5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BQ39-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BQ39 |
| SMART | SM00487;SM00490; |
| UniProt Domain [FT] | DOMAIN 168..347; /note="Helicase ATP-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00541"; DOMAIN 380..524; /note="Helicase C-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00542" |
| InterPro | IPR059027;IPR011545;IPR050079;IPR012562;IPR014001;IPR001650;IPR027417;IPR035979; |
| Pfam | PF26142;PF00270;PF08152;PF00271; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000107625-DDX50/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| C1QBP | Biogrid, Bioplex | true |
| DDX21 | Biogrid, Opencell | true |
| LIN28A | Biogrid, Bioplex | true |
| LMNB1 | Biogrid, Opencell | true |
| NIFK | Biogrid, Bioplex | true |
| PRKRA | Biogrid, Bioplex | true |
| RPL10 | Biogrid, Bioplex | true |
| RPL31 | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
