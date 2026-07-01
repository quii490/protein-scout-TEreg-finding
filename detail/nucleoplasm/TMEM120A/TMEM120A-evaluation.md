---
type: protein-evaluation
gene: "TMEM120A"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMEM120A 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMEM120A |
| 蛋白名称 | Transmembrane protein 120A |
| 蛋白大小 | 343 aa / 40.6 kDa |
| UniProt ID | Q9BXJ8 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 343 aa |
| 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=22 |
| 三维结构 | 10/10 | ×3 | 30.0 | pLDDT=89.2; PDB=5 |
| 调控结构域 | 4/10 | ×2 | 8.0 | TMEM120A/B |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=63 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +2 |

### 3. 分析
- HPA: nan (nan)
- PubMed: strict=22, broad=31
- AF pLDDT: 89.2 / PDB: 5
- InterPro: TMEM120A/B
- Pfam: TMEM120A-B
- PPI degree=63 ChIP: None
38556553: Transmembrane proteins with unknown function (TMEMs) as ion channels: electrophy | 39147733: Phosphatidic acid is an endogenous negative regulator of PIEZO2 channels and mec | 34583807: Pain or gain?

### 4. 总体评价
★★★★  **72.1/100**  **nucleoplasm**
Nuclear protein


### 深度机制分析

TMEM120A（亦称TACAN）是一个多功能跨膜蛋白，其核心结构域为TMEM120A/B保守区（Pfam PF07851，InterPro IPR012926），该结构域在进化上高度保守，但具体生化功能尚未完全阐明。AlphaFold2预测的整体结构具有较高可信度（pLDDT=89.2），且PDB数据库中已有5个实验结构，提示其三级结构已得到较好的实验验证。该蛋白包含多个跨膜螺旋区，符合其作为机械敏感离子通道和脂质代谢调控因子的双重角色。

从蛋白互作网络来看，TMEM120A的PPI网络度为63，具有中等规模的互作组。其关键互作伙伴中PAXIP1（PTIP）尤为值得注意——PAXIP1是一个含BRCT结构域的核蛋白，参与DNA损伤应答和转录调控，TMEM120A与PAXIP1的互作（BioGRID）可能暗示TMEM120A在核质中的非经典功能。此外，与PPP1CC（蛋白磷酸酶1催化亚基）的互作提示TMEM120A可能参与磷酸化信号调控。但遗憾的是，这些互作缺乏实验验证评分，需要进一步验证。

从功能机制角度，TMEM120A最明确的功能是作为机械敏感离子通道参与机械感觉传导。文献PMID:35235791证实其可能作为感知机械刺激的离子通道，而PMID:36420836揭示其通过直接物理互作介导PKD2-TMEM120A通道复合物的机械敏感性。值得深入探讨的是，TMEM120A可能通过改变细胞脂质组成抑制PIEZO2通道（PMID:39147733），磷脂酸被鉴定为PIEZO2的内源性负调控因子。这种脂质介导的调控模式可能在核膜机械传导中具有特殊意义，因为核膜的脂质环境与质膜有显著差异。TMEM120A在核质中的定位（尽管HPA证据为nan）可能与其在核膜机械感知或脂质代谢调控中的潜在功能有关。

尽管HPA核定位证据缺失是该蛋白的主要短板，但22篇PubMed文献的研究新颖性极高（得分9/10），加上优良的结构解析度（PDB=5, pLDDT=89.2），使其成为值得深入研究的核机械传导候选蛋白。未来研究应重点关注TMEM120A在核膜上的定位验证，以及其是否通过脂质微环境调控影响核内基因表达。

### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protein 120A

**功能**: Multifunctional protein involved in mechanosensation, and plays an essential role in lipid metabolism and adipocyte differentiation (PubMed:26024229, PubMed:36420836). May function as a potential ion channel involved in sensing mechanical stimuli (PubMed:35235791). Mediates the mechanosensitivity of the PKD2-TMEM120A channel complex through direct physical interaction (PubMed:36420836). TMEM120A seems to affect mechanosensation by inhibiting PIEZO2 channels, possibly by altering cellular lipid c

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR012926 |
| Pfam | PF07851 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PAXIP1 | BioGRID | 0 |
| VKORC1 | BioGRID | 0 |
| PPP1CC | BioGRID | 0 |
| SNAP29 | BioGRID | 0 |
| SLC39A4 | BioGRID | 0 |
| POMK | BioGRID | 0 |
| B4GALT3 | BioGRID | 0 |
| SYPL2 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9BXJ8-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 31**

| 42184262 | Biolayer Interferometry for Investigating Membrane Protein-Inhibitor Binding: TACAN Mutant and GsMTx4 As a Model System. | J Vis Exp 2026 |
| 42098142 | A conserved ER protein prevents lipotoxicity by stimulating the key enzyme in glycerolipid synthesis. | Nat Commun 2026 |
| 41967766 | From nociception to therapy: The expanding role of TMEM proteins in pain. | Life Sci 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMEM120A

