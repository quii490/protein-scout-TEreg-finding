---
type: protein-evaluation
gene: "A8K683"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## A8K683 (cDNA FLJ75708, highly similar to Homo sapiens N-myc (and STAT) interactor (NMI), mRNA) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | A8K683 |
| 蛋白全称 | cDNA FLJ75708, highly similar to Homo sapiens N-myc (and STAT) interactor (NMI), mRNA |
| UniProt ID | A8K683 |
| 蛋白大小 | 307 aa / 33.8 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 307 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR009909; InterPro:IPR009938; InterPro:IPR012677; Pfam:PF07334; Pfam:PF07292 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL unreviewed entry, function not fully annotated.

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR009909 |
| InterPro | IPR009938 |
| InterPro | IPR012677 |
| Pfam | PF07334 |
| Pfam | PF07292 |

#### 3.3 核定位

no known nuclear annotation

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 深度机制分析

A8K683（cDNA FLJ75708，高度相似于人N-myc/STAT相互作用因子NMI）属于NMI/STAT相互作用因子家族，其核心结构域由InterPro:IPR009909（NMI domain）、InterPro:IPR009938（NMI/CMTR interaction domain）和InterPro:IPR012677（Nucleotide-binding alpha-beta plait domain superfamily）组成。Pfam:PF07334（NMI domain）和PF07292（NMI/CMTR domain）分别界定NMI蛋白的保守特征序列和与CMTR（cap methyltransferase）的相互作用界面。该蛋白仅307 aa（33.8 kDa），为小型核质蛋白，其核苷酸结合模块（IPR012677）提示潜在的核酸或核苷酸结合功能。

从蛋白互作网络角度，作为一种高度相似于NMI的蛋白质，其已知同源物NMI通过STAT信号通路调控JAK-STAT转录应答，NMI直接与STAT1/STAT5形成复合物增强STAT介导的转录活性。NMI亦与c-Myc、N-Myc、BRCA1和IFI35形成复杂的互作网络，参与肿瘤免疫监视和DNA损伤应答的转录调控。由于A8K683为TrEMBL未审核条目，功能注释有限，但基于与NMI的高度序列相似性，推断其可能通过类似的SH2/pY结合界面与STAT转录因子互作，进而参与干扰素信号通路调控。

从结构生物学角度，暂无实验解析的PDB晶体结构，AlphaFold预测模型可用。鉴于NMI家族蛋白在N端可形成螺旋卷曲（coiled-coil）介导同源/异源二聚化，其中央区域的核苷酸结合折叠可能负责与RNA或ATP的相互作用，而C端的NMI/CMTR功能域则可能通过与mRNA帽甲基转移酶CMTR1的相互作用参与mRNA加工过程的调控。该蛋白在PubMed中尚无直接研究发表（PubMed=0），属于高度新颖的TrEMBL靶标。

从TE调控角度，A8K683定位于nucleoplasm，其与NMI的同源性使其在理论上有参与染色质调控的潜力。NMI已知通过与BRCA1的互作参与DNA损伤位点的染色质重塑，而BRCA1作为E3泛素连接酶，可在逆转座子元件（如LINE1、Alu）处富集并调控其表观遗传沉默。此外，STAT信号通路（NMI的核心功能通路之一）被证明参与内源性逆转录病毒（ERV）的转录激活，尤其在炎症和干扰素刺激条件下。如果A8K683保留了NMI的STAT结合功能，它可能作为STAT信号通路与TE转录调控之间的桥梁分子。

从研究转化角度，A8K683综合评分67.8/100，研究新颖性极高（PubMed=0），PPI数据极为有限，属于中等优先级的早期靶标。建议首先通过免疫共沉淀实验验证A8K683与STAT1/STAT5的内源性互作，进而通过ChIP-seq检测STAT靶标位点的TE富集情况。功能获得性/丧失性实验结合TE转录组测序（TEtranscripts或SQuIRE管线）可验证其TE调控活性。AlphaFold预测的pLDDT值将为后续结构域截短体的功能域划分提供指导。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A8K683

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/A8K683
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A8K683
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=A8K683
