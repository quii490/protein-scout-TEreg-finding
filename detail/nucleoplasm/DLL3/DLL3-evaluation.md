---
type: protein-evaluation
gene: "DLL3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DLL3 — REJECTED (研究热度过高 (PubMed strict=272，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DLL3 |
| 蛋白名称 | Delta-like protein 3 |
| 蛋白大小 | 618 aa / 64.6 kDa |
| UniProt ID | Q9NYJ7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Golgi apparatus, Plasma membrane; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 618 aa / 64.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=272 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000742, IPR001881, IPR013032, IPR009030, IPR051 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **68.0/180** | |
| **归一化总分** | | | **37.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Golgi apparatus, Plasma membrane | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 272 |
| PubMed broad count | 593 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. DLL3 as an Emerging Target for the Treatment of Neuroendocrine Neoplasms.. *The oncologist*. PMID: 35983951
2. IL-18-secreting CAR T cells targeting DLL3 are highly effective in small cell lung cancer models.. *The Journal of clinical investigation*. PMID: 36951942
3. A DLL3-targeted antibody-drug conjugate eradicates high-grade pulmonary neuroendocrine tumor-initiating cells in vivo.. *Science translational medicine*. PMID: 26311731
4. SCLC Subtypes Defined by ASCL1, NEUROD1, POU2F3, and YAP1: A Comprehensive Immunohistochemical and Histopathologic Characterization.. *Journal of thoracic oncology : official publication of the International Association for the Study of Lung Cancer*. PMID: 33011388
5. Unravelling the biology of SCLC: implications for therapy.. *Nature reviews. Clinical oncology*. PMID: 28534531

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.2 |
| 高置信度残基 (pLDDT>90) 占比 | 5.7% |
| 置信残基 (pLDDT 70-90) 占比 | 48.4% |
| 中等置信 (pLDDT 50-70) 占比 | 18.4% |
| 低置信 (pLDDT<50) 占比 | 27.5% |
| 有序区域 (pLDDT>70) 占比 | 54.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.2），有序残基占 54.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000742, IPR001881, IPR013032, IPR009030, IPR051022; Pfam: PF00008, PF12661, PF07657 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NOTCH1 | 0.998 | 0.000 | — |
| NOTCH3 | 0.998 | 0.000 | — |
| NOTCH2 | 0.998 | 0.000 | — |
| NOTCH4 | 0.998 | 0.000 | — |
| DLL1 | 0.940 | 0.000 | — |
| DLL4 | 0.919 | 0.000 | — |
| SRRT | 0.867 | 0.000 | — |
| MESP2 | 0.857 | 0.045 | — |
| LFNG | 0.848 | 0.073 | — |
| EGF | 0.756 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| hspa1a_hspa1b_human-1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TUBB8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MYADM | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CGRRF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| XYLT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PDP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SPOP | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |
| SMAD4 | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |
| AKT1 | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |
| FBXW7 | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:35512704|imex:IM-29493| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.2 + PDB: 无 | pLDDT=65.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm; 额外: Golgi apparatus, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DLL3 — Delta-like protein 3，研究基础较多，新颖性有限。
2. 蛋白大小618 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 272 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=65.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 272 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NYJ7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000090932-DLL3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DLL3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NYJ7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000090932-DLL3/subcellular

![](https://images.proteinatlas.org/24559/1931_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/24559/1931_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/24559/1979_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/24559/1979_A7_3_red_green.jpg)
![](https://images.proteinatlas.org/24559/2020_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/24559/2020_B10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NYJ7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NYJ7 |
| SMART | SM00181;SM00179; |
| UniProt Domain [FT] | DOMAIN 176..215; /note="DSL"; DOMAIN 216..249; /note="EGF-like 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 274..310; /note="EGF-like 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 312..351; /note="EGF-like 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 353..389; /note="EGF-like 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 391..427; /note="EGF-like 5"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 429..465; /note="EGF-like 6"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076" |
| InterPro | IPR000742;IPR001881;IPR013032;IPR009030;IPR051022;IPR011651; |
| Pfam | PF00008;PF12661;PF07657; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000090932-DLL3/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
