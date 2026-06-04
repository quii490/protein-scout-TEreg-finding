---
type: protein-evaluation
gene: ADPRHL1
date: 2026-06-03
tags:
  - protein-evaluation
  - ADPRHL1
  - nucleolus
  - ADP-ribosylhydrolase
status: rejected
---

# ADPRHL1 — 蛋白质评估报告

## 基本信息

| 属性 | 值 |
|------|-----|
| UniProt ID | Q8NDY3 |
| 蛋白质名称 | Inactive ADP-ribosyltransferase ARH2 |
| 别名 | ARH2 |
| 氨基酸长度 | 354 aa |
| 分子量 | 40.1 kDa |
| AlphaFold 平均 pLDDT | 93.8 |
| pLDDT > 90 比例 | 85.3% |
| PubMed (strict) | 10 |
| PubMed (broad) | 18 |

## 核定位证据

### HPA 免疫荧光

- **主要定位**：Plasma membrane
- **附加定位**：Nucleoli
- **可靠性**：Approved
- **IF 图像状态**：HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

HPA Approved级别IF显示ADPRHL1主要定位于质膜，同时在核仁（Nucleoli）检测到附加信号。核仁是rRNA转录和核糖体生物发生的场所，这一附加定位提示ADPRHL1可能参与核仁相关的调控过程。但核仁仅为附加定位（非主要定位），信号强度未知。

### UniProt 亚细胞定位

- **Cytoplasm, myofibril, sarcomere**（ECO:0000250，序列相似性推断）

UniProt将ADPRHL1定位于胞质的肌原纤维/肌节。证据代码为ECO:0000250（基于序列相似性推断），来自与其他物种ADPRHL1同源蛋白的比对。该注释与HPA的质膜/Nucleoli定位存在显著差异——UniProt认为该蛋白是肌肉结构蛋白，而HPA将其主要定位于质膜。这种跨数据库的不一致提示该蛋白的亚细胞定位可能存在组织/细胞类型特异性，或不同抗体检测到的是不同构象/修饰形式的蛋白。

### GO-CC 细胞组分

| GO ID | 术语 | 证据 |
|-------|------|------|
| GO:0030017 | sarcomere | ISS:UniProtKB（序列相似性推断） |

GO-CC仅收录一条sarcomere注释（肌节），证据为ISS（Inferred from Sequence or structural Similarity），与UniProt的注释来源一致。完全缺乏任何核定位相关的GO术语。

**核定位证据总结**：ADPRHL1的核定位证据存在显著的跨数据库矛盾。HPA在核仁检测到Approved级别的附加信号，但UniProt（基于序列相似性）和GO-CC（ISS）明确将其定位于肌节/胞质。这种矛盾可能源于：(1) 蛋白在不同组织/细胞类型中的定位差异（心脏/肌肉 vs 常用细胞系）；(2) 蛋白的双重功能/定位（结构角色在肌节中，酶功能在核仁中）；(3) ADP-ribosylhydrolase家族成员可能在特定条件下（如DNA损伤应激）转移到核内。当前核定位可信度因数据库矛盾而降低至中等偏弱水平，需要独立实验验证。

## PubMed 文献证据

PubMed strict检索：10篇
PubMed broad检索：18篇

ADPRHL1属于极低研究热度的蛋白（strict=10篇），处于PubMed ≤ 20的最高新颖性区间。文献主要集中在心脏发育功能。代表文献：

- **PMID: 27217161** — Smith SJ et al. (2016) "The cardiac-restricted protein ADP-ribosylhydrolase-like 1 is essential for heart chamber outgrowth and acts on muscle actin filament assembly." *Developmental Biology*. 确定ADPRHL1是心脏限制性表达蛋白，对心脏腔室发育和肌动蛋白丝组装必不可少。
- **PMID: 32726316** — Smith SJ et al. (2020) "Defective heart chamber growth and myofibrillogenesis after knockout of adprhl1 gene function by targeted disruption of the ancestral catalytic active site." *PLoS ONE*. 通过敲除ADPRHL1催化活性位点证实其在心肌原纤维形成和心脏腔室生长中的作用。
- **PMID: 34512719** — Li T et al. (2021) "A 104-bp Structural Variation of the ADPRHL1 Gene Is Associated With Growth Traits in Chickens." *Frontiers in Genetics*. 鉴定ADPRHL1基因结构变异与鸡生长性状的关联。
- **PMID: 35968320** — Guo J et al. (2022) "A novel 8-gene panel for prediction of early biochemical recurrence in patients with prostate cancer." *American Journal of Cancer Research*. ADPRHL1被纳入前列腺癌生化复发预测的8基因panel。
- **PMID: 34492228** — Finke D et al. (2022) "Histone deacetylase 4 deletion broadly affects cardiac epigenetic repression..." *JMCC*. 在HDAC4心脏条件性敲除的背景下提及ADPRHL1。

ADPRHL1的核心文献围绕心脏发育和肌原纤维形成，Smith SJ课题组的两篇论文是该基因功能研究的基石（PMID: 27217161和32726316）。前列腺癌预测panel和鸡生长性状的研究仅涉及该基因，未做功能探索。整体而言，该基因的功能研究深度非常有限，仅有2篇直接的功能性论文（均来自同一课题组），存在巨大的研究空白。目前没有任何已发表文献涉及ADPRHL1的核定位或核功能。

## AlphaFold 结构 / PAE / PDB

- **AlphaFold条目**：AF-Q8NDY3-F1（version 6）
- **平均pLDDT**：93.8（极高置信度）
- **pLDDT分布**：>90: 85.3%, 70-90: 10.7%, 50-70: 3.1%, <50: 0.8%
- **PAE数据**：可用
- **PDB结构**：无实验解析结构

AlphaFold预测质量在5个候选基因中最高（mean pLDDT 93.8）。85.3%的残基pLDDT > 90，仅0.8%的残基 < 50。极高的预测置信度意味着AlphaFold模型几乎等同于实验级别的结构精度，可为后续结构分析和理性设计提供可靠基础。PAE数据可用。无PDB实验结构是唯一的遗憾，但AlphaFold模型可在很大程度上弥补这一缺憾。

## InterPro / Pfam 结构域

| InterPro ID | Pfam ID | 描述 |
|-------------|---------|------|
| IPR012108 | - | ADP-ribosylhydrolase |
| IPR050792 | - | ADP-ribose glycohydrolase |
| IPR005502 | PF03747 | ADP-ribosylation/Crystallin J1 |
| IPR036705 | - | ADP-ribosylation factor-like superfamily |

ADPRHL1属于ADP-核糖基水解酶（ADP-ribosylhydrolase）家族，含有ADP-ribose glycohydrolase结构域（PF03747）。UniProt明确指出该蛋白"catalytically inactive"（催化失活），虽然含有ADP-ribosylhydrolase结构域但丧失了催化活性。其作为"非活性酶"的角色可能转向支架蛋白或调控功能——这一特征在某些信号通路中并不罕见（如伪激酶作为信号支架）。ADP-ribosylation因子样超家族与多种细胞过程（膜运输、信号转导、细胞骨架重组）相关，ADPRHL1的非活性酶身份可能在这些通路中发挥独特的调控作用，而非直接催化。

## STRING 蛋白互作网络

| 伙伴基因 | 综合得分 | 实验得分 | 数据库得分 | 文本挖掘 |
|----------|---------|---------|-----------|---------|
| GRTP1 | 0.737 | 0 | 0 | 0.541 |
| DCUN1D2 | 0.633 | 0 | 0 | 0.430 |
| TMCO3 | 0.546 | 0 | 0 | 0.531 |
| LSMEM2 | 0.502 | 0 | 0 | 0.484 |
| ABTB1 | 0.495 | 0.042 | 0 | 0.490 |
| ZNF541 | 0.441 | 0 | 0 | 0.437 |
| CUL1 | 0.402 | 0.311 | 0 | 0.160 |
| CUL3 | 0.402 | 0.311 | 0 | 0.160 |
| CACUL1 | 0.402 | 0.311 | 0 | 0.160 |

STRING检测到9个功能伙伴，PPI网络较稀疏。ABTB1（Ankyrin repeat and BTB domain containing 1）有微弱的实验互作信号（0.042）。CUL1、CUL3、CACUL1（Cullin家族蛋白）的实验得分为0.311，提示可能与泛素E3连接酶系统存在功能性关联。其余伙伴均为textmining来源。总体PPI证据薄弱，无高分互作。

## IntAct 分子互作

| 伙伴 | 检测方法 | PMID |
|------|---------|------|
| Cav3 | anti bait coimmunoprecipitation | 24952909 |

IntAct仅收录1条互作记录：Cav3（Caveolin-3，肌肉特异性caveolin蛋白）通过anti-bait co-IP在PMID: 24952909中检测到。Caveolin-3是肌细胞质膜微囊的主要结构蛋白，该互作与ADPRHL1在心肌/骨骼肌中的功能定位一致。但总体互作数据非常稀疏，仅1条记录。

## 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA Nucleoli additional only; main=Plasma membrane |
| 蛋白大小 | 7/10 | ×1 | 7 | 354 aa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 |
| 三维结构 | 7/10 | ×3 | 21 | pLDDT 93.8；无PDB |
| 调控结构域 | 3/10 | ×2 | 6 | 单结构域 |
| PPI网络 | 2/10 | ×3 | 6 | 有限data |
| **加权总分** | | | **102/180** | |
| **归一化总分 (÷1.83)** | | | **55.7/100** | |

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

## 最终决策

**Scored（中低优先级）**

ADPRHL1通过核评分阈值的初步筛选（nuclear_score=6 > 3），但深度评估揭示其核定位证据存在显著的跨数据库矛盾。HPA虽在核仁检测到Approved附加信号，但UniProt和GO-CC一致指向肌节/胞质定位。该矛盾是评估中的最大风险因素。

该基因的突出优势在于：(1) 极高的研究新颖性（PubMed=10，仅同一课题组2篇功能论文），存在广阔的研究空白；(2) AlphaFold结构质量极佳（mean pLDDT 93.8，5个基因中最高），几乎是实验级精度；(3) 蛋白尺寸紧凑（354 aa），适合结构/生化研究；(4) 作为"非活性酶"，可能存在尚未发现的scaffolding/regulatory功能，这在概念上具有吸引力。

核心短板为：(1) 核定位可信度低——跨数据库矛盾严重，核仁信号仅为HPA单方面附加定位；(2) PPI网络极弱——无任何高分实验互作，功能网络未建立；(3) 已知功能完全在胞质/肌节（心脏发育、肌动蛋白组装），缺乏任何核功能的文献或数据库支持。

综合得分17.49属于中低区间，建议作为第二轮候选（在核定位更明确的优先候选饱和后考虑），或等待核定位的独立实验验证（如western blot核质分离）后再重新评估。

## Manual Review Note

ADPRHL1是5个基因中最矛盾的候选者——其新颖性（PubMed=10）和结构质量（pLDDT 93.8）在本批评估中名列第一，但核定位证据的跨数据库冲突也是本批最严重的。值得深思的是，心脏限制性表达蛋白很少同时具有核仁定位，这要么是HPA的假阳性信号（来自抗体交叉反应或固定伪影），要么提示该蛋白在心肌细胞中确实存在尚未被认识的核仁功能。考虑到该蛋白催化失活的特殊性，作为伪酶的支架/调控功能的假说颇具吸引力——类似于伪激酶在信号通路中的作用模式。然而，在缺乏独立核定位验证的情况下（如核质分离western blot、免疫电镜、或核定位序列的突变分析），当前的核定位证据强度不足以支撑高置信度的评估。如果该基因能通过后续实验证实其核仁定位的真实性，应大幅提升其优先级。目前建议保留在中低优先级候选池中。
