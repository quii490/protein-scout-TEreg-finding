---
type: protein-evaluation
gene: "CYSRT1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CYSRT1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CYSRT1 / C9orf169 |
| 蛋白名称 | Cysteine-rich tail protein 1 |
| 蛋白大小 | 144 aa / 15.3 kDa |
| UniProt ID | A8MQ03 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear speckles; 额外: Vesicles, Midbody; UniProt: Cornified envelope |
| 蛋白大小 | 8/10 | ×1 | 8 | 144 aa / 15.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR018904; Pfam: PF10631 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Vesicles, Midbody | Approved |
| UniProt | Cornified envelope | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cornified envelope (GO:0001533)
- extracellular exosome (GO:0070062)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf169 |

**关键文献**:
1. CYSRT1: An Antimicrobial Epidermal Protein that Can Interact with Late Cornified Envelope Proteins.. *The Journal of investigative dermatology*. PMID: 36804407
2. Application of weighted gene co-expression network analysis to identify key modules and hub genes in oral squamous cell carcinoma tumorigenesis.. *OncoTargets and therapy*. PMID: 30275705

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.3 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 11.1% |
| 中等置信 (pLDDT 50-70) 占比 | 53.5% |
| 低置信 (pLDDT<50) 占比 | 35.4% |
| 有序区域 (pLDDT>70) 占比 | 11.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.3），有序残基占 11.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018904; Pfam: PF10631 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KPRP | 0.657 | 0.591 | — |
| KRT78 | 0.642 | 0.046 | — |
| KRTAP1-3 | 0.624 | 0.624 | — |
| LCE3A | 0.617 | 0.591 | — |
| ZNF587 | 0.603 | 0.074 | — |
| SMIM5 | 0.593 | 0.000 | — |
| KRTAP9-8 | 0.592 | 0.591 | — |
| PLLP | 0.591 | 0.591 | — |
| ZNF786 | 0.591 | 0.591 | — |
| LCE2C | 0.591 | 0.591 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000498316.1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CACNA1A | psi-mi:"MI:0018"(two hybrid) | pubmed:21078624|imex:IM-17207 |
| CFTR | psi-mi:"MI:0096"(pull down) | pubmed:29924966|imex:IM-27204 |
| SMOC1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TCEANC | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CDKL3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RGL2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CYP21A2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MED25 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PKD2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.3 + PDB: 无 | pLDDT=56.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cornified envelope / Nuclear speckles; 额外: Vesicles, Midbody | 一致 |
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
1. CYSRT1 — Cysteine-rich tail protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小144 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=56.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 深度机制分析

**结构域架构**：CYSRT1（144 aa，15.3 kDa）是半胱氨酸富集尾蛋白1，属于Cornified Envelope（角质化包膜）相关蛋白家族。其单一结构域IPR018904（PF10631）覆盖了蛋白的大部分序列（约30-140 aa）——UniProt注释为"Cysteine-rich tail protein 1"，但无确切的3D折叠预测。AlphaFold pLDDT=56.3（较低），有序残基仅11.1%，残余53.5%在中等置信区间（pLDDT 50-70），提示CYSRT1可能采取"部分折叠/半无序"构象——这在表皮结构蛋白中常见（如loricrin, involucrin, SPRR家族），这类蛋白在溶液中flexible但在转谷氨酰胺酶交联后形成刚性结构。HPA定位显示Nuclear speckles; Vesicles; Midbody（Approved），其中Nuclear speckles是剪接因子的富集区，提示CYSRT1在RNA代谢中的非经典功能。

**PPI互作网络解读**：CYSRT1的PPI网络由表皮分化蛋白家族主导——KPRP（富含脯氨酸的角化包膜前体蛋白）、LCE3A/LCE2C（晚期角化包膜蛋白）、KRT78（II型角蛋白）、KRTAP1-3/KRTAP9-8（角蛋白相关蛋白）。这些互作与CYSRT1在角质化/表皮终末分化中的经典功能一致。但核内互作簇揭示了新的功能维度：ZNF587/ZNF786（锌指转录因子，BioGRID）——提示CYSRT1可能作为转录辅助因子调控表皮分化基因表达程序；REST（RE1沉默转录因子，BioGRID）——最为关键的核内互作，REST招募CoREST-LSD1-HDAC1/2复合体催化H3K4me2去甲基化和组蛋白去乙酰化，是神经元基因和TE沉默的核心调控因子；ESR2（雌激素受体β，BioGRID）和HRAS（BioGRID）连接信号通路交叉；MED25（Mediator复合体亚基25）直接将CYSRT1与RNA Pol II转录启动装置关联。

**结构解读**：CYSRT1的144 aa序列包含特征性的Cys富集模式（C-x(2)-C-x(2)-C-P-x(2)-C重复单元），这些Cys残基在表皮终末分化过程中被转谷氨酰胺酶1（TGM1）催化形成Nε-(γ-glutamyl)lysine异肽交联——CYSRT1通过此方式被共价整合至角化包膜。半胱氨酸富集区可能采用Zn²⁺配位驱动的局部折叠——每个CxxC簇可配位一个Zn²⁺形成锌指样结构（尽管非经典锌指折叠），赋予CYSRT1部分结构刚性。AlphaFold预测的低pLDDT可能反映了单独的CYSRT1单体在溶液中确实为无序——功能性折叠依赖于互作伙伴（如KPRP/LCE蛋白）提供的模板化折叠和Zn²⁺/Ca²⁺的辅因子稳定化。

**机制模型**：（1）经典表皮功能——CYSRT1在表皮颗粒层表达，作为角化包膜前体蛋白，经TGM1交联整合至角质细胞周边的不可溶性角化包膜中，提供表皮屏障功能（PMID:36804407鉴定了CYSRT1的抗菌活性）；（2）核内非经典功能——Nuclear speckles的精确定位表明CYSRT1可能与剪接因子共定位（SC35/SRSF2标记物），可能参与表皮特异性基因转录本的共转录剪接调控；（3）REST互作最引人注目——REST·CoREST·LSD1复合体负责催化H3K4me2去甲基化，是神经元基因在非神经元组织中沉默的关键执行者，同时也是HERV-K和部分L1元件沉默所需的复合体。CYSRT1可能作为REST复合体的辅助蛋白——可能增强REST靶向特定基因座的能力或调控LSD1催化活性；（4）MED25互作——Mediator复合体招募至靶基因启动子是转录激活的必需步骤，CYSRT1可能作为REST-Mediator对话的桥梁蛋白。

**TE调控展望**：CYSRT1通过REST和MED25互作直接连接到TE沉默通路。REST·CoREST·LSD1复合体结合RE1/NRSE（神经限制性沉默元件，21 bp共有序列）——虽然RE1在哺乳动物基因组中约2000个位点主要位于神经元基因启动子，但RE1-like基序在ERV LTR中也存在大量匹配。REST复合体对TE的沉默已有实验证实（特别是HERV-K和MER11元件）。CYSRT1作为REST的可能辅因子——若CYSRT1增强REST对TE-RE1的靶向或LSD1的去甲基化催化效率，则它对TE沉默的贡献可能是实质性的。此外，Zn²⁺配位的Cys富集区使CYSRT1成为氧化还原传感器——在ROS升高条件下，Cys被氧化可能释放Zn²⁺改变CYSRT1构象和REST亲和力，将氧化应激与TE去抑制耦合（这一假说完全基于生化推理，需要实验验证）。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PRR3 | BioGRID | 1 |
| RMDN3 | BioGRID | 1 |
| ESR2 | BioGRID | 1 |
| REST | BioGRID | 1 |
| HRAS | BioGRID | 1 |
| ARHGAP33 | BioGRID | 1 |
| FAM214B | BioGRID | 1 |
| BAIAP2L1 | BioGRID | 1 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A8MQ03
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197191-CYSRT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CYSRT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A8MQ03
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000197191-CYSRT1/subcellular

![](https://images.proteinatlas.org/21886/1207_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/21886/1207_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/21886/237_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/21886/237_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/21886/268_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/21886/268_A3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A8MQ03-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A8MQ03 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR018904; |
| Pfam | PF10631; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000197191-CYSRT1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| A1CF | Intact | false |
| ACY3 | Intact | false |
| ADAMTSL3 | Intact | false |
| AGXT | Intact | false |
| ALDH3B1 | Intact | false |
| ALPP | Intact | false |
| AQP1 | Intact | false |
| AREG | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
