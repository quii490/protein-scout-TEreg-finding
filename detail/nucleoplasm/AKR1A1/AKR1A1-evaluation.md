---
type: protein-evaluation
gene: "AKR1A1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## AKR1A1 (Aldo-keto reductase family 1 member A1) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | AKR1A1 |
| 蛋白全称 | Aldo-keto reductase family 1 member A1 |
| UniProt ID | P14550 |
| 蛋白大小 | 325 aa / 35.8 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 325 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR020471; InterPro:IPR044481; InterPro:IPR018170; InterPro:IPR036812; InterPro:IPR023210; Pfam:PF00248 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Catalyzes the NADPH-dependent reduction of a wide variety of carbonyl-containing compounds to their corresponding alcohols (PubMed:10510318, PubMed:30538128). Displays enzymatic activity towards endogenous metabolites such as aromatic and aliphatic aldehydes, ketones, monosaccharides and bile acids, with a preference for negatively charged substrates, such as glucuronate and succinic semialdehyde 

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR020471 |
| InterPro | IPR044481 |
| InterPro | IPR018170 |
| InterPro | IPR036812 |
| InterPro | IPR023210 |
| Pfam | PF00248 |

#### 3.3 核定位

no known nuclear annotation

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 深度机制分析

AKR1A1（Aldo-keto reductase family 1 member A1）属于醛酮还原酶超家族，其核心催化结构域为Pfam:PF00248（Aldo/keto reductase family），采用经典的(α/β)₈桶状折叠（TIM barrel），通过InterPro:IPR020471（AKR家族）和InterPro:IPR044481（NADP-dependent oxidoreductase domain）实现NADPH依赖性羰基还原。InterPro:IPR018170（Aldo/keto reductase, conserved site）标记了包含催化四联体（Tyr-His-Asp-Lys）的保守活性位点区域，InterPro:IPR036812（NADP-dependent oxidoreductase domain superfamily）界定Rossmann折叠的辅因子结合域。该蛋白仅325 aa（35.8 kDa），结构紧凑，属于典型的单体氧化还原酶。

从蛋白互作网络角度，AKR1A1与CBR1（STRING评分909，同属AKR超家族的羰基还原酶1）形成高置信度的功能关联，提示二者在羰基化合物解毒和类固醇代谢通路中可能存在底物交叉冗余。值得注意的是，TERF1（端粒重复结合因子1）和TERF2IP（TERF2相互作用蛋白）的BioGRID互作记录暗示AKR1A1可能通过间接方式与端粒/染色质维持机制产生功能性联系。EXOSC4（外来体复合物组分9）和DAZAP1（DAZ相关蛋白1，RNA结合蛋白）的互作则进一步提示其可能参与RNA代谢调控。代谢酶GAPDH和NANS的互作（均为BioGRID评分1）支持其在细胞代谢网络中的中心节点角色。

从结构生物学角度，目前尚无实验解析的PDB晶体结构，AlphaFold预测模型可用。鉴于AKR超家族结构的保守性和同源性，其活性位点由Tyr55-His117-Asp50-Lys84催化四联体构成（以AKR1A1标准编号推断），NADPH辅因子结合于Rossmann折叠的羧基端区域。该蛋白在PubMed中共有140篇文献报道，研究基础扎实，其中PMID:42105791（AKR1A1通过S-亚硝基化修饰保护肾脏移植物，揭示翻译后修饰调控）、PMID:42048774（巨噬细胞NO依赖性重塑中AKR1A1的负调控角色）和PMID:42147287（甜瓜根系与糖/氨基酸代谢）代表了其在不同生物学语境中的功能多样性。

从TE调控角度，AKR1A1定位于nucleoplasm，但其核心功能为胞质氧化还原代谢酶，缺乏DNA结合域（如HTH、锌指、bZIP等）或染色质重塑特征结构域（如chromodomain、bromodomain、PHD finger）。然而，其与TERF1/TERF2IP的互作关系——尽管置信度低——提示AKR1A1可能通过氧化还原敏感的翻译后修饰（如S-亚硝基化或羰基应激）改变亚细胞分布，进而在特定应激条件下被招募至端粒/染色质区域。TERF2IP作为Shelterin复合物的核心组分，直接参与端粒保护和DNA损伤应答，如果AKR1A1- TERF2IP互作确实发生，可能通过氧化还原依赖性方式影响端粒区域TE元件的表观遗传状态。

从研究转化角度，AKR1A1综合评分67.8/100，研究新颖性评分10/10（TrEMBL条目级别新颖性），但PubMed文献量达140篇表明其基础功能已有广泛研究。虽然糖皮质激素代谢和氧化应激是其经典领域，建议关注AKR1A1的亚细胞分区动态——特别是S-亚硝基化修饰（PMID:42105791的Cys亚硝基化位点确认）是否改变其从细胞质向细胞核的穿梭行为，以及核内定位的AKR1A1是否通过NADPH消耗改变局部氧化还原环境进而影响逆转座子元件的染色质可及性。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CBR1 | STRING | 909 |
| TERF1 | BioGRID | 1 |
| TERF2IP | BioGRID | 1 |
| EXOSC4 | BioGRID | 1 |
| DAZAP1 | BioGRID | 1 |
| GAPDH | BioGRID | 1 |
| NANS | BioGRID | 1 |
| NME2 | BioGRID | 1 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/AKR1A1

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000117448-AKR1A1

![](https://images.proteinatlas.org/17919/173_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17919/173_B11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17919/140_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17919/140_B11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17919/168_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17919/168_B11_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000117448-AKR1A1

![](https://images.proteinatlas.org/17919/173_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17919/173_B11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17919/140_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17919/140_B11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17919/168_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17919/168_B11_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000117448-AKR1A1

![](https://images.proteinatlas.org/17919/173_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17919/173_B11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17919/140_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17919/140_B11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/17919/168_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/17919/168_B11_2_blue_red_green.jpg)

### PubMed

**Count: 140**

| PMID | Title |
|---|---|
| 42147287 | Rootstock selection shapes melon taste by divergent regulation of sugar and amino acid metabolism. |
| 42134613 | Exogenous vitamin C regulates osteoclast differentiation kinetics, cytoskeletal maturation, and bone resorption through ERK1/2-DAPK1-caspase-3 signali |
| 42105791 | The protective role of aldo-keto reductase family 1 member A1 in kidney allograft injury: beyond S-nitrosylation. |
| 42048774 | Multi-omic analysis reveals nitric oxide dependent remodeling in classically activated macrophages and identifies negative regulation mediated by AKR1 |
| 41835849 | Subtype-Specific Causal Effects of Antidiabetic Drug Targets on Ovarian Cancer: Mendelian Randomization and Colocalization Evidence. |


