---
type: protein-evaluation
gene: "OTUD4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## OTUD4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OTUD4 / HIN-1, KIAA1046 |
| 蛋白名称 | OTU domain-containing protein 4 |
| 蛋白大小 | 1114 aa / 124.0 kDa |
| UniProt ID | Q01804 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 1114 aa / 124.0 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=55 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=48.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003323, IPR038765, IPR050704; Pfam: PF02338 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.0/180** | |
| **归一化总分** | | | **60.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 55 |
| PubMed broad count | 76 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HIN-1, KIAA1046 |

**关键文献**:
1. AP3B1 facilitates PDIA3/ERP57 function to regulate rabies virus glycoprotein selective degradation and viral entry.. *Autophagy*. PMID: 39128851
2. OTUD4 inhibits ferroptosis by stabilizing GPX4 and suppressing autophagic degradation to promote tumor progression.. *Cell reports*. PMID: 40338740
3. Deubiquitinating enzyme OTUD4 stabilizes RBM47 to induce ATF3 transcription: a novel mechanism underlying the restrained malignant properties of ccRCC cells.. *Apoptosis : an international journal on programmed cell death*. PMID: 38553613
4. Elevated SPARC Disrupts the Intestinal Barrier Integrity in Crohn's Disease by Interacting with OTUD4 and Activating the MYD88/NF-κB Pathway.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39888301
5. Glutamine binds HSC70 to transduce signals inhibiting IFN-β-mediated immunogenic cell death.. *Developmental cell*. PMID: 40086433

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 48.9 |
| 高置信度残基 (pLDDT>90) 占比 | 14.6% |
| 置信残基 (pLDDT 70-90) 占比 | 7.0% |
| 中等置信 (pLDDT 50-70) 占比 | 9.0% |
| 低置信 (pLDDT<50) 占比 | 69.4% |
| 有序区域 (pLDDT>70) 占比 | 21.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=48.9），有序残基占 21.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003323, IPR038765, IPR050704; Pfam: PF02338 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| USP7 | 0.802 | 0.292 | — |
| USP9X | 0.757 | 0.292 | — |
| OTUD3 | 0.735 | 0.292 | — |
| UBC | 0.701 | 0.669 | — |
| RNF216 | 0.698 | 0.000 | — |
| PUM2 | 0.659 | 0.321 | — |
| SLC35F6 | 0.654 | 0.000 | — |
| RC3H1 | 0.647 | 0.612 | — |
| OTUD5 | 0.624 | 0.000 | — |
| OTUD6B | 0.621 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BRF2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TMBIM4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ILK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ATG12 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CDK5RAP3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| RUNX1T1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CLEC3B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| PRR5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17461779 |
| DNAJB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=48.9 + PDB: 无 | pLDDT=48.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. OTUD4 — OTU domain-containing protein 4，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1114 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 55 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=48.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q01804
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164164-OTUD4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OTUD4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q01804
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000164164-OTUD4/subcellular

![](https://images.proteinatlas.org/36623/412_B7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36623/412_B7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/36623/419_B7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36623/419_B7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/36623/471_B7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36623/471_B7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q01804-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
