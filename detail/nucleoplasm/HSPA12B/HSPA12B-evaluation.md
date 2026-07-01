---
type: protein-evaluation
gene: "HSPA12B"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## HSPA12B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | HSPA12B |
| 蛋白名称 | Heat shock 70 kDa protein 12B |
| 蛋白大小 | 686 aa / 75.7 kDa |
| UniProt ID | Q96MM6 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 686 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=54 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=82.4; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | ATPase_NBD |
| PPI | 6/10 | x3 | 18.0 | PPI degree=77 |
| **加权总分** | | | **124/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=54 broad=65
- AF pLDDT=82.4 PDB=0
- InterPro: ATPase_NBD
- Pfam: 
- PPI degree=77 ChIP: None
34221864: Extracellular vesicle activities regulating macrophage- and tissue-mediated inju | 40443679: Endothelial HSPA12B regulates myocardial monocyte infiltration and inflammatory  | 32790647: Endothelial cell HSPA12B and yes-associated protein cooperatively regulate angio

### 4. 总体评价
**68.3/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**非典型HSP70家族蛋白的核质定位与内皮功能**：HSPA12B（Heat shock 70 kDa protein 12B, 686 aa, UniProt Q96MM6）是HSP70超家族的非典型成员——其序列仅包含ATPase核苷酸结合域（ATPase_NBD IPR043129），完全缺乏经典HSP70的底物结合域（SBD）和C端盖状结构域。这种"半截HSP70"的架构暗示其可能作为ATP依赖性构象调控因子而非经典蛋白质折叠分子伴侣发挥功能。HPA核质定位为Approved级别（核定位特异性9/10），与HSPA14（5/10, 核定位不明）形成对比——HSPA12B似乎是HSP70家族中少有的明确核质定位成员。

**内皮HSPA12B对心肌巨噬细胞浸润的旁分泌TE调控假说**：PubMed=54的文献全部集中于HSPA12B在内皮细胞和心血管疾病中的功能。关键发现包括：(1) "Endothelial HSPA12B regulates myocardial monocyte infiltration and inflammatory" (PMID:40443679)；(2) "Endothelial cell HSPA12B and yes-associated protein cooperatively regulate angiogenesis" (PMID:32790647)；(3) "Extracellular vesicle activities regulating macrophage- and tissue-mediated injury" (PMID:34221864)。这些数据提示HSPA12B可能通过胞外囊泡（EVs）介导内皮细胞-巨噬细胞交叉对话。从TE调控角度，HSPA12B-EVs可能携带TE衍生RNA（如Alu或LINE-1 RNA片段）至受体细胞，通过TLR或RIG-I模式识别受体激活炎症体——这是衰老相关无菌炎症中TE的致病机制之一（PMID:32032505）。反之，HSPA12B在核质中可能通过与YAP（Yes-associated protein）的协作影响染色质——YAP/TEAD转录因子通过识别ERV/MaLR中的TEAD结合基序调控基因表达。

**HSP70互作网络的节点角色**：PPI degree=77（STRING/BioGRID），HSPA1B（STRING 901）、HSPA1A（STRING 901）和HSPA4（STRING 884）的超高互作评分表明HSPA12B是HSP70互作网络的功能枢纽。HSPA1A/B（HSP72）已被证实直接结合L1 ORF2p逆转录酶域并促进其正确折叠，支持L1蛋白的合成（PMID:28070091）。若HSPA12B通过同源互作影响HSPA72的L1 ORF2p折叠功能，则可间接调控L1逆转座效率。AlphaFold pLDDT=82.4的ATPase域暗示核苷酸结合功能完整。实验上建议CRISPR敲除HSPA12B的内皮细胞后进行胞外囊泡small RNA测序，检查TE衍生RNA的富集情况。


### 补充分析 (UniProt API)

**蛋白全称**: Heat shock 70 kDa protein 12B

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR043129 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Heat shock 70 kDa protein 12B

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR043129 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HSPA1B | STRING | 901 |
| HSPA1A | STRING | 901 |
| HSPA4 | STRING | 884 |
| HSPA12A | STRING | 867 |
| HSPA13 | STRING | 838 |
| HSPA14 | STRING | 803 |
| HSPA4L | STRING | 779 |
| HSPA6 | STRING | 757 |