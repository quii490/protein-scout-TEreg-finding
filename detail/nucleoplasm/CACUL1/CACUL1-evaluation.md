---
type: protein-evaluation
gene: "CACUL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CACUL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CACUL1 / C10orf46, CAC1 |
| 蛋白名称 | CDK2-associated and cullin domain-containing protein 1 |
| 蛋白大小 | 369 aa / 41.1 kDa |
| UniProt ID | Q86Y37 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 5/10 | ×4 | 20 | HPA: Nucleoplasm; UniProt: 无注释 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 369 aa / 41.1 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.6; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR042652, IPR001373, IPR016159; Pfam: PF00888 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 14 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.0/180** | |
| **归一化总分** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Uncertain |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据存在但较为混杂，部分数据源指向非核区室。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C10orf46, CAC1 |

**关键文献**:
1. CACUL1 reciprocally regulates SIRT1 and LSD1 to repress PPARγ and inhibit adipogenesis.. *Cell death & disease*. PMID: 29233982
2. CACUL1/CAC1 attenuates p53 activity through PML post-translational modification.. *Biochemical and biophysical research communications*. PMID: 27889610
3. Unravelling the Genetic Architecture of Serum Biochemical Indicators in Sheep.. *Genes*. PMID: 39202351
4. Helicobacter pylori promotes invasion and metastasis of gastric cancer cells through activation of AP-1 and up-regulation of CACUL1.. *The international journal of biochemistry & cell biology*. PMID: 24004834
5. [Effect of cell cycle-related novel gene CACUL1 on the apoptosis of colorectal cancer cells in vitro].. *Xi bao yu fen zi mian yi xue za zhi = Chinese journal of cellular and molecular immunology*. PMID: 23643261

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.6 |
| 高置信度残基 (pLDDT>90) 占比 | 51.5% |
| 置信残基 (pLDDT 70-90) 占比 | 7.6% |
| 中等置信 (pLDDT 50-70) 占比 | 4.3% |
| 低置信 (pLDDT<50) 占比 | 36.6% |
| 有序区域 (pLDDT>70) 占比 | 59.1% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.6，有序区 59.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042652, IPR001373, IPR016159; Pfam: PF00888 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RBX1 | 0.690 | 0.573 | — |
| SKP1 | 0.675 | 0.563 | — |
| RNF7 | 0.667 | 0.573 | — |
| E5RI56_HUMAN | 0.660 | 0.563 | — |
| CAND1 | 0.631 | 0.434 | — |
| KBTBD4 | 0.616 | 0.589 | — |
| SPOP | 0.606 | 0.489 | — |
| SPOPL | 0.597 | 0.470 | — |
| CAND2 | 0.563 | 0.434 | — |
| DCUN1D1 | 0.544 | 0.311 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KBTBD4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| H2BC17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RAP1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HBB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MICAL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CSNK1G3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KLHL34 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| VSIG8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| AMY1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DSG3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 14
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.6 + PDB: 无 | pLDDT=72.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 15 + 14 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CACUL1 — CDK2-associated and cullin domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小369 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86Y37
- Protein Atlas: https://www.proteinatlas.org/ENSG00000151893-CACUL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CACUL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86Y37
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:29:25

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000151893-CACUL1/subcellular

![](https://images.proteinatlas.org/50611/1162_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/50611/1162_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/50611/761_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/50611/761_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/50611/769_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/50611/769_C10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86Y37-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
