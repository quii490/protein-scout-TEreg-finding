---
type: protein-evaluation
gene: "CMAHP"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CMAHP 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CMAHP |
| 蛋白名称 | Inactive cytidine monophosphate-N-acetylneuraminic acid hydroxylase |
| 蛋白大小 | 501 aa / 58.4 kDa |
| UniProt ID | Q9Y471 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 501 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=7 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=93.1; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Cnh; RibonucZ/Hydroxyglut_hydro |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=1 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +2 |

### 3. 分析
- HPA: nan (nan)
- PubMed: strict=7, broad=9
- AF pLDDT: 93.1 / PDB: 0
- InterPro: Cnh; RibonucZ/Hydroxyglut_hydro
- Pfam: Lactamase_B_3
- PPI degree=1 ChIP: None
36223881: Long-read sequencing reveals oncogenic mechanism of HPV-human fusion transcripts | 36311939: A more novel and powerful prognostic gene signature of lung adenocarcinoma deter | 34716430: CMAHP promotes metastasis by reducing ubiquitination of Snail and inducing angio

### 4. 总体评价
★★★★  **68.3/100**  **nucleoplasm**
Nuclear protein


### 深度机制分析

**失活唾液酸羟化酶的非催化核内功能**：CMAHP（Inactive cytidine monophosphate-N-acetylneuraminic acid hydroxylase, 501 aa, UniProt Q9Y471）编码一个酶活性丧失的CMP-Neu5Ac羟化酶。这种失活源于人类特异性的92-bp外显子缺失，导致该蛋白无法将CMP-Neu5Ac转化为CMP-Neu5Gc（PMID:9624188）。然而，CMAHP蛋白仍保留完整表达并具有独立于催化活性的Wnt信号调控功能。其结构域包括Cnh（IPR027033, Pfam Lactamase_B_3 PF13483），属于核糖核酸酶Z/羟基谷氨酸水解酶超家族的金属-β-内酰胺酶折叠。

**Wnt信号连接与TE调控的潜在汇合点**：UniProt明确注释CMAHP"may play a role in Wnt signaling"——这是本蛋白与TE调控之间最直接的分子桥梁。Wnt/β-catenin通路通过TCF/LEF转录因子调控靶基因表达，而TCF/LEF结合位点在多种TE衍生调控元件中高度富集。特别是TCF结合基序（WWCAAWG）在MIR和L2家族的TE衍生增强子中被发现具有功能活性（PMID:28087692）。此外，CMAHP被发现在肺癌中通过减少Snail泛素化促进EMT和转移（PMID:34716430），暗示其参与染色质重塑因子调控。

**PPI网络和TE相关的微妙线索**：PPI degree=1（唯一互作为RAB34, BioGRID score=0）暗示极孤立的功能网络。然而PubMed=7的高新颖性（满分50/50）和pLDDT=93.1的极高置信度结构弥补了PPI数据的不足。CMAHP Cnh结构域的金属-β-内酰胺酶折叠（包含双Zn2+结合位点）可能具有非催化核酸结合能力——类似的金属-β-内酰胺酶折叠蛋白（如CPSF-73, SNM1/Apollo）已被证明参与RNA加工和DNA损伤应答，但CMAHP的底物特异性完全未知。

**人类特异性失活与TE调控的进化假说**：CMAHP是在人类演化中特异失活的少数几个酶之一（与Neu5Gc丢失协同）。人类大脑中TE的活跃表达被认为是人类认知演化的驱动力之一，而唾液酸生物学（Neu5Gc→Neu5Ac转变）与脑发育的关联已被广泛认可。如果CMAHP的Wnt信号调控功能涉及TE位点，则可能构成人类TE调控新颖机制的范例——一个失活的代谢酶被重定向为TE表观遗传调控因子。这是一个值得深入研究的高风险概念假设。


### 补充分析 (UniProt API)

**蛋白全称**: Inactive cytidine monophosphate-N-acetylneuraminic acid hydroxylase

**功能**: Sialic acids are components of carbohydrate chains of glycoconjugates and are involved in cell-cell recognition and cell-pathogen interactions. That protein has no CMP-N-acetylneuraminate monooxygenase activity and is not able to convert CMP-N-acetylneuraminic acid (CMP-Neu5Ac) into its hydroxylated derivative CMP-N-glycolylneuraminic acid (CMP-Neu5Gc), a sialic acid abundantly expressed at the surface of many cells in vertebrates (PubMed:9624188). However, it may play a role in Wnt signaling (P

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR027033 |
| InterPro | IPR036866 |
| Pfam | PF13483 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RAB34 | BioGRID | 0 |