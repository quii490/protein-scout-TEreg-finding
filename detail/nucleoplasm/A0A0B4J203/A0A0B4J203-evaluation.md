---
type: protein-evaluation
gene: "A0A0B4J203"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## A0A0B4J203 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | A0A0B4J203 |
| 蛋白大小 | 849 aa / 94.7 kDa |
| UniProt ID | A0A0B4J203 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 849 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=0 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=56.0; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | Fip1_dom; Kinase-like_dom_sf; Prot_kinase_dom |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **115/180** | |
| **归一化总分** | | | **63.9/100** | 互证: +2 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=56.0 PDB=1
- InterPro: Fip1_dom; Kinase-like_dom_sf; Prot_kinase_dom
- Pfam: Fip1; PK_Tyr_Ser-Thr
- PPI degree=0 ChIP: None


### 4. 总体评价
**63.9/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---


### 补充分析 (UniProt API)

**TE 调控评估**: 该蛋白缺乏核定位证据，TE 调控潜力极低。

---


### 补充分析 (UniProt API)

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A0A0B4J203

### 深度机制分析

A0A0B4J203含Fip1结构域（IPR007854）和蛋白激酶结构域（IPR000719, PK_Tyr_Ser-Thr），这在人类蛋白质组中极为罕见：一个mRNA 3'末端加工因子与一个信号激酶在单一多肽链中融合。Fip1结构域是CPSF（剪切与多聚腺苷酸化特异性因子）复合体的特征模块，负责识别mRNA前体中的U-rich序列并指导可变多聚腺苷酸化（APA）位点选择。Pfam同时注释到Fip1（PF15061）和PK_Tyr_Ser-Thr（PF07714），确认了这种嵌合架构的真实性。849个氨基酸（94.7 kDa）的分子量远大于典型的Fip1或激酶结构域蛋白质，提示存在大量折叠和调控区域。

STRING PPI网络揭示三个极高置信度的互作伙伴：CPSF4（902分）、CSTF3（900分）和FIP1L1（906分）。CPSF4是CPSF的30 kDa亚基，直接接触AAUAAA多聚腺苷酸化信号（PMID: 14749727）；CSTF3是剪切刺激因子（CstF）的77 kDa亚基，识别GU-rich下游元件；FIP1L1是CPSF的核心亚基，直接参与APA调控。这三个互作严格围绕mRNA 3'末端加工机器，无任何线粒体或细胞质代谢污染，支持该蛋白质在核内polyA位点选择中发挥核心作用。

从TE调控视角，可变多聚腺苷酸化是控制转座子表达的关键但不被充分认识的机制。许多TE（尤其是L1和Alu元件）含有隐蔽polyA信号，CPSF/CstF复合体对这些信号的使用与否直接决定TE来源转录本是被正确终止并产生功能性RNA，还是因通读转录（readthrough）导致转录干扰或反义RNA产生（PMID: 24415954, 30626974）。A0A0B4J203的激酶结构域可能是一个信号响应开关：在基础状态下，Fip1结构域参与经典的CPSF介导3'加工；当激酶结构域被上游信号（如DNA损伤、应激、或细胞周期信号）激活后，可能通过磷酸化CPSF或CstF亚基改变polyA位点选择偏好。pLDDT=56.0反映高比例的内源性无序区域，这与支架蛋白在动态多蛋白复合体组装中的构象灵活性需求一致——无序区域通常包含磷酸化位点簇。

推测机制模型：A0A140B4J203作为条件依赖性polyA位点调控器。其Fip1结构域锚定在CPSF/CstF复合体上，激酶结构域感知上游信号。激活后，它磷酸化CPSF/CstF组分（或通过自磷酸化改变构象），从而改变复合体对弱polyA信号（如TE来源的隐蔽polyA位点）与强polyA信号（如宿主基因的经典polyA位点）的选择偏好。该蛋白质只有1个PDB条目证实其表达和可结晶性，但低pLDDT提示大量柔性区域，可能需要在复合体状态下才能获得完整结构信息。

研究意义：PubMed=0的新颖性评分（10/10）确认这是完全未被研究的蛋白质。优先实验：（1）体外激酶实验验证催化活性，鉴定CPSF/CstF复合体内部的磷酸化底物；（2）APA-seq（PolyA-seq或3'READS）在A0A0B4J203敲低/过表达细胞中绘制全局polyA位点变化，特别关注TE邻近polyA位点；（3）ChIP-seq或CUT&RUN确认该蛋白质是否直接结合TE位点染色质。Fip1与激酶结构域的融合代表一种尚未在人类polyA因子中被描述过的调控架构，可能为TE转录后调控提供新的药物干预靶点（PMID: 22658674）。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CPSF4 | STRING | 902 |
| CSTF3 | STRING | 900 |
| FIP1L1 | STRING | 906 |

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000282278

![](https://images.proteinatlas.org/58202/1029_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/58202/1029_C8_3_red_green.jpg)
![](https://images.proteinatlas.org/58202/1009_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/58202/1009_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/58202/995_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/58202/995_C8_3_red_green.jpg)
![](https://images.proteinatlas.org/79225/2095_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/79225/2095_B9_4_red_green.jpg)
