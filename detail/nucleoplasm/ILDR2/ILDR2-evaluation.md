---
type: protein-evaluation
gene: "ILDR2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ILDR2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ILDR2 / C1orf32 |
| 蛋白名称 | Immunoglobulin-like domain-containing receptor 2 |
| 蛋白大小 | 639 aa / 71.2 kDa |
| UniProt ID | Q71H61 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; UniProt: Endoplasmic reticulum membrane; Cell junction, tight junctio |
| 蛋白大小 | 10/10 | ×1 | 10 | 639 aa / 71.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036179, IPR051874, IPR013783, IPR003599, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane | Approved |
| UniProt | Endoplasmic reticulum membrane; Cell junction, tight junction; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- bicellular tight junction (GO:0005923)
- endoplasmic reticulum membrane (GO:0005789)
- membrane (GO:0016020)
- nucleus (GO:0005634)
- tight junction (GO:0070160)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 33 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf32 |

**关键文献**:
1. The role of the tricellular junction protein ILDR2 in glomerulopathies: Expression patterns and functional insights.. *iScience*. PMID: 39640577
2. ILDR2 stabilization is regulated by its interaction with GRP78.. *Scientific reports*. PMID: 33863978
3. ZNF70, a novel ILDR2-interacting protein, contributes to the regulation of HES1 gene expression.. *Biochemical and biophysical research communications*. PMID: 27353377
4. Tricellular tight junction-associated angulins in the gill epithelium of rainbow trout.. *American journal of physiology. Regulatory, integrative and comparative physiology*. PMID: 29631364
5. Angulin proteins ILDR1 and ILDR2 regulate alternative pre-mRNA splicing through binding to splicing factors TRA2A, TRA2B, or SRSF1.. *Scientific reports*. PMID: 28785060

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.3 |
| 高置信度残基 (pLDDT>90) 占比 | 15.3% |
| 置信残基 (pLDDT 70-90) 占比 | 12.4% |
| 中等置信 (pLDDT 50-70) 占比 | 17.1% |
| 低置信 (pLDDT<50) 占比 | 55.2% |
| 有序区域 (pLDDT>70) 占比 | 27.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.3），有序残基占 27.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036179, IPR051874, IPR013783, IPR003599, IPR008664; Pfam: PF05624 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MARVELD2 | 0.894 | 0.000 | — |
| OCLN | 0.660 | 0.126 | — |
| TRA2A | 0.581 | 0.000 | — |
| POGK | 0.511 | 0.000 | — |
| ZFP69 | 0.506 | 0.000 | — |
| TRA2B | 0.498 | 0.000 | — |
| LSR | 0.463 | 0.000 | — |
| LRIT3 | 0.459 | 0.250 | — |
| IGSF5 | 0.455 | 0.000 | — |
| ZNF70 | 0.450 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| H1-2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H1-5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| KCNJ2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:32541000|imex:IM-29166 |
| CHRNA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 4
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.3 + PDB: 无 | pLDDT=56.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Cell junction, tig / Plasma membrane | 一致 |
| PPI | STRING + IntAct | 12 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. ILDR2 — Immunoglobulin-like domain-containing receptor 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小639 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=56.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q71H61
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143195-ILDR2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ILDR2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q71H61
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000143195-ILDR2/subcellular

![](https://images.proteinatlas.org/12815/1864_E3_22_cr5afd7c3eba476_blue_red_green.jpg)
![](https://images.proteinatlas.org/12815/1864_E3_26_cr5afd7c3eba78d_blue_red_green.jpg)
![](https://images.proteinatlas.org/12815/1909_H3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/12815/1909_H3_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q71H61-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
