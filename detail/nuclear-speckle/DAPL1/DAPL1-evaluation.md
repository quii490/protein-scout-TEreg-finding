---
type: protein-evaluation
gene: "DAPL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DAPL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DAPL1 / EEDA |
| 蛋白名称 | Death-associated protein-like 1 |
| 蛋白大小 | 107 aa / 11.9 kDa |
| UniProt ID | A0PJW8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies, Microtubules; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 107 aa / 11.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=26 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024130; Pfam: PF15228 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.5/180** | |
| **归一化总分** | | | **63.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies, Microtubules | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 26 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EEDA |

**关键文献**:
1. A molecular network of conserved factors keeps ribosomes dormant in the egg.. *Nature*. PMID: 36653451
2. DAPL1 prevents epithelial-mesenchymal transition in the retinal pigment epithelium and experimental proliferative vitreoretinopathy.. *Cell death & disease*. PMID: 36841807
3. A Dapl1(+) subpopulation of naïve CD8 T cells is enriched for memory-lineage precursors.. *Science advances*. PMID: 40845112
4. DAPL1 inhibits epithelial-mesenchymal transition of retinal pigment epithelial cells by regulating the TGF-β/MITF pathway.. *Experimental eye research*. PMID: 40466854
5. DAPL1 deficiency in mice impairs antioxidant defenses in the RPE and leads to retinal degeneration with AMD-like features.. *Redox biology*. PMID: 36933392

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.2 |
| 高置信度残基 (pLDDT>90) 占比 | 2.8% |
| 置信残基 (pLDDT 70-90) 占比 | 44.9% |
| 中等置信 (pLDDT 50-70) 占比 | 31.8% |
| 低置信 (pLDDT<50) 占比 | 20.6% |
| 有序区域 (pLDDT>70) 占比 | 47.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.2），有序残基占 47.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024130; Pfam: PF15228 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FHL2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FNDC3B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TSR2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZIC1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| LSM1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TRIM63 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:31391242|imex:IM-25805| |
| TRIM55 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:31391242|imex:IM-25805| |
| ENSP00000309538.4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| Ppp1r13l | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:37284462|imex:IM-29688 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 9
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.2 + PDB: 无 | pLDDT=68.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Nuclear bodies, Microtubules | 一致 |
| PPI | STRING + IntAct | 0 + 9 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DAPL1 — Death-associated protein-like 1，非常新颖，仅有少数基础研究。
2. 蛋白大小107 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 26 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=68.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A0PJW8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163331-DAPL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DAPL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0PJW8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000163331-DAPL1/subcellular

![](https://images.proteinatlas.org/58635/1550_A2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/58635/1550_A2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/58635/1556_F7_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/58635/1556_F7_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/58635/1582_F7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/58635/1582_F7_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A0PJW8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
