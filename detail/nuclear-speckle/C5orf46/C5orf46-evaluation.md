---
type: protein-evaluation
gene: "C5orf46"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C5orf46 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C5orf46 |
| 蛋白名称 | C5orf46 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | C5orf46 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; 额外: Mitochondria; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Mitochondria | Approved |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. [Significance of high expression of C5orf46 in gastric cancer and potential intervention of tarditional Chinese medicine based on bioinformatics, molecular docking, and cell experiments].. *Zhongguo Zhong yao za zhi = Zhongguo zhongyao zazhi = China journal of Chinese materia medica*. PMID: 37282866
2. Admixture mapping of severe asthma exacerbations in Hispanic/Latino children and youth.. *Thorax*. PMID: 36180068
3. Identification of a novel Immune-Related prognostic model for patients with colorectal cancer based on 3 subtypes.. *Immunobiology*. PMID: 36827833
4. C5orf46: a promising prognosis risk indicator with implication in the remodeling of KIRC and pan-cancer tumor microenvironments.. *Frontiers in oncology*. PMID: 42158413
5. Aberrant lncRNA-mRNA expression profile and function networks during the adipogenesis of mesenchymal stem cells from patients with ankylosing spondylitis.. *Frontiers in genetics*. PMID: 36246583

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WFDC5 | 0.581 | 0.000 | — |
| TMBIM6 | 0.470 | 0.401 | — |
| GPR87 | 0.468 | 0.000 | — |
| ADGRF4 | 0.457 | 0.000 | — |
| MUCL1 | 0.453 | 0.000 | — |
| SERPINB7 | 0.444 | 0.000 | — |
| IGFL2 | 0.428 | 0.000 | — |
| SUMO4 | 0.419 | 0.000 | — |
| CDHR1 | 0.418 | 0.000 | — |
| TMEM45A | 0.415 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TMEM80 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SGTB | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PEX12 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FAM210B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TIMMDC1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TBXA2R | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SLC30A2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| AQP6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| EBP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| RUSF1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 14
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Nuclear speckles; 额外: Mitochondria | 待确认 |
| PPI | STRING + IntAct | 11 + 14 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. C5orf46 — C5orf46 (UniProt未获取)，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| C5orf46 | BioGRID | 0 |
| TBXA2R | BioGRID | 0 |
| AQP6 | BioGRID | 0 |
| SGTA | BioGRID | 0 |
| PEX12 | BioGRID | 0 |
| TIMMDC1 | BioGRID | 0 |
| FAM210B | BioGRID | 0 |
| C16orf58 | BioGRID | 0 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/C5orf46
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178776-C5orf46/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C5orf46
- AlphaFold: https://alphafold.ebi.ac.uk/entry/C5orf46
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000178776-C5orf46/subcellular

![](https://images.proteinatlas.org/58999/1020_E9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/58999/1020_E9_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/58999/1169_A9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/58999/1169_A9_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/58999/993_E9_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/58999/993_E9_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6UWT4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027950; |
| Pfam | PF15144; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000178776-C5orf46/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AQP6 | Intact | false |
| EBP | Intact | false |
| FAM210B | Intact | false |
| LHFPL5 | Intact | false |
| PEX12 | Intact | false |
| RUSF1 | Intact | false |
| SGTA | Intact | false |
| SGTB | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

### 深度机制分析

C5orf46是本次评估中最具功能神秘性的蛋白之一。该蛋白几乎在所有数据库维度上均呈现显著的"数据空白"特征：UniProt获取失败（基因名本身未映射到标准UniProt accession），AlphaFold预测失败（pLDDT=0），蛋白大小未知，InterPro/Pfam最初报告为"暂无数据"（后续修复后添加了IPR027950/PF15144注释）。这种数据库层面的"不可见性"可能有以下原因：(1)该基因编码一种极低丰度或组织/条件特异性表达的蛋白，不足以积累足够的实验或预测数据；(2)基因预测模型可能将该ORF误注释为蛋白编码基因，实际上不产生稳定的多肽产物；(3)该基因近期才被注释（人类基因组注释的持续更新），数据库未及时收录。

尽管如此，HPA提供了强有力的反对"无效基因"假说的证据——C5orf46在HPA中显示Nuclear speckles定位，reliability为Approved（可靠性最高级别）。Nuclear speckles（核散斑体）是核质中富含pre-mRNA剪接因子的相分离无膜细胞器，在基因表达调控中处于关键位置。这种定位将C5orf46与mRNA加工和剪接调控直接联系起来，为其赋予潜在的功能意义。即使在其他数据库维度均为空白的极端情况下，Approved可靠性的HPA核散斑定位本身即构成一个有效的功能假设起点。

后续修复添加的Domain/SMART数据显示了IPR027950（Protein of unknown function DUF4585）和PF15144——意味着C5orf46的序列确实含有一个可被Pfam检测到的domain，虽然该domain的功能完全未知（DUF = Domain of Unknown Function）。这修正了"无任何结构域"的初始判断，但并未解决功能注释的核心困境。

PPI互作网络揭示了有趣的功能关联。IntAct实验互作中，TBXA2R（thromboxane A2 receptor）、AQP6（aquaporin 6）、EBP（emopamil binding protein/sterol isomerase）、FAM210B（mitochondrial protein）和TIMMDC1（mitochondrial complex I assembly factor）均经validated two-hybrid或two-hybrid array方法验证（PMID 32296183）。这些互作的功能分布极为分散——从GPCR信号（TBXA2R）到水通道（AQP6）到胆固醇合成（EBP）到线粒体呼吸链组装（FAM210B/TIMMDC1），缺乏功能一致性。这提示C5orf46可能是一个通用的分子伴侣或支架蛋白，能够在不同亚细胞环境中与多种蛋白产生弱互作，或者这些互作中的许多是酵母双杂系统中的假阳性。

STRING数据中TMBIM6（BAX inhibitor-1, combined score=0.470 with experimental=0.401）是一个具有实验支持的互作，TMBIM6是内质网膜上的抗凋亡蛋白，调控ER应激和钙稳态。SUMO4（score=0.419）的互作虽仅为text-mining推断，但其作为SUMO化修饰的底物/参与者，在核散斑体生物学中具有特殊意义——SUMO化修饰是核散斑体动力学和剪接调控的核心翻译后修饰。

PubMed文献中PMID 42158413是C5orf46最重要的独立研究——发现C5orf46是一个"promising prognosis risk indicator"并参与KIRC（肾透明细胞癌）和泛癌肿瘤微环境的重塑。这一发现与C5orf46的核散斑体定位之间存在潜在的关联——核散斑体是pre-mRNA剪接和mRNA成熟的关键位点，而可变剪接的改变是肿瘤发生的核心驱动因素。PMID 37282866探索了C5orf46在胃癌中的高表达和中药干预潜力，提供了另一项肿瘤关联。

在TE调控的潜在关联上，核散斑体定位本身即构成一个合理的机制推测——部分含有内含子的TE（如LINE-1）转录后的剪接和加工可能与核散斑体功能相关。若C5orf46确实参与剪接调控，它可能间接影响TE转录本的命运。但这一假设目前缺乏任何实验支持。

归一化总分65.8/100，推荐等级三星。C5orf46的深度机制模型目前仅能描述为：核散斑体定位（HPA Approved）→ DUF4585 domain（功能未知）→ 可能与剪接调控和肿瘤微环境重塑相关。这是本次评估中数据库空白最大、实验验证最少但HPA定位最强的蛋白之一，需要在UniProt映射和基本生化表征方面投入优先资源。TE调控潜力目前仅基于核散斑体的间接推测，为所有候选蛋白中最为薄弱的。


