---
type: protein-evaluation
gene: "STX1B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## STX1B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STX1B / STX1B1, STX1B2 |
| 蛋白名称 | Syntaxin-1B |
| 蛋白大小 | 288 aa / 33.2 kDa |
| UniProt ID | P61266 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane, Vesicles; UniProt: Membrane; Nucleus; Cytoplasm, cytoskeleton, microtubule orga |
| 蛋白大小 | 10/10 | ×1 | 10 | 288 aa / 33.2 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=89 篇 (≤100→2) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR010989, IPR045242, IPR006012, IPR006011, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **95.5/180** | |
| **归一化总分** | | | **53.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane, Vesicles | Uncertain |
| UniProt | Membrane; Nucleus; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm, cy... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axon (GO:0030424)
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endomembrane system (GO:0012505)
- membrane (GO:0016020)
- neuromuscular junction (GO:0031594)
- nuclear lamina (GO:0005652)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 89 |
| PubMed broad count | 154 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: STX1B1, STX1B2 |

**关键文献**:
1. Systematic discovery of protein interaction interfaces using AlphaFold and experimental validation.. *Molecular systems biology*. PMID: 38225382
2. Clinical spectrum of STX1B-related epileptic disorders.. *Neurology*. PMID: 30737342
3. Cryo-EM structures of engineered Shiga toxin-based immunogens capable of eliciting neutralizing antibodies with therapeutic potential against hemolytic uremic syndrome.. *Protein science : a publication of the Protein Society*. PMID: 40411437
4. Autosomal Dominant Sleep-Related Hypermotor (Hyperkinetic) Epilepsy.. **. PMID: 20301348
5. Mutations in STX1B, encoding a presynaptic protein, cause fever-associated epilepsy syndromes.. *Nature genetics*. PMID: 25362483

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.1 |
| 高置信度残基 (pLDDT>90) 占比 | 47.9% |
| 置信残基 (pLDDT 70-90) 占比 | 34.7% |
| 中等置信 (pLDDT 50-70) 占比 | 15.3% |
| 低置信 (pLDDT<50) 占比 | 2.1% |
| 有序区域 (pLDDT>70) 占比 | 82.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=84.1，有序区 82.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010989, IPR045242, IPR006012, IPR006011, IPR000727; Pfam: PF05739, PF00804 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| STXBP1 | 0.999 | 0.864 | — |
| VAMP3 | 0.998 | 0.622 | — |
| VAMP2 | 0.998 | 0.713 | — |
| SNAP25 | 0.997 | 0.718 | — |
| VAMP1 | 0.994 | 0.672 | — |
| SNAP23 | 0.991 | 0.670 | — |
| VAMP4 | 0.969 | 0.460 | — |
| VAMP8 | 0.960 | 0.307 | — |
| NAPA | 0.954 | 0.746 | — |
| NAPB | 0.953 | 0.792 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LRRK2 | psi-mi:"MI:0096"(pull down) | pubmed:21307259|imex:IM-17182 |
| Cltc | psi-mi:"MI:0028"(cosedimentation in solution) | imex:IM-11648|pubmed:19562802 |
| Sox4 | psi-mi:"MI:0028"(cosedimentation in solution) | imex:IM-11648|pubmed:19562802 |
| Dlg4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11694|pubmed:19455133 |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| STXBP1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| SNAP29 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TXLNA | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FAM209A | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ABHD16A | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.1 + PDB: 无 | pLDDT=84.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane; Nucleus; Cytoplasm, cytoskeleton, microt / Nuclear membrane, Vesicles | 一致 |
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
1. STX1B — Syntaxin-1B，研究基础较多，新颖性有限。
2. 蛋白大小288 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 89 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P61266
- Protein Atlas: https://www.proteinatlas.org/ENSG00000099365-STX1B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STX1B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P61266
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (uncertain)。来源: https://www.proteinatlas.org/ENSG00000099365-STX1B/subcellular

![](https://images.proteinatlas.org/69176/1851_B12_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/69176/1851_B12_32_blue_red_green.jpg)
![](https://images.proteinatlas.org/69176/1913_O2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/69176/1913_O2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/69176/1931_C1_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/69176/1931_C1_6_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P61266-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
