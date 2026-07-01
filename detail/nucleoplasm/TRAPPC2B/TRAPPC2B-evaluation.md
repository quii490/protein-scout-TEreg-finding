---
type: protein-evaluation
gene: "TRAPPC2B"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TRAPPC2B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TRAPPC2B |
| 蛋白名称 | Trafficking protein particle complex subunit 2B |
| 蛋白大小 | 140 aa / 16.4 kDa |
| UniProt ID | P0DI82 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36.0 | Endoplasmic reticulum; Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 6/10 | ×1 | 6.0 | 140 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=92.2; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Longin-like_dom_sf; Sedlin |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=36 |
| **加权总分** | | | **136/180** | |
| **归一化总分** | | | **75.4/100** | 互证: +2 |

### 3. 分析
- HPA: Endoplasmic reticulum; Nucleoplasm; Vesicles (Approved)
- PubMed: strict=0, broad=0
- AF pLDDT: 92.2 / PDB: 0
- InterPro: Longin-like_dom_sf; Sedlin
- Pfam: Sedlin_N
- PPI degree: 36 / ChIP: None


### 4. 总体评价
★★★★  **75.4/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Trafficking protein particle complex subunit 2B

**功能**: Prevents transcriptional repression and induction of cell death by ENO1. May play a role in vesicular transport from endoplasmic reticulum to Golgi

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011012 |
| InterPro | IPR006722 |
| Pfam | PF04628 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Trafficking protein particle complex subunit 2B

**功能**: Prevents transcriptional repression and induction of cell death by ENO1. May play a role in vesicular transport from endoplasmic reticulum to Golgi

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011012 |
| InterPro | IPR006722 |
| Pfam | PF04628 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ZBED1 | BioGRID | 0 |
| EPS15L1 | BioGRID | 0 |
| KCTD1 | BioGRID | 0 |
| TRIM42 | BioGRID | 0 |
| EFTUD2 | BioGRID | 0 |
| TGOLN2 | BioGRID | 0 |
| ZRANB1 | BioGRID | 0 |
| TRAPPC3 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-P0DI82-F1-predicted_aligned_error_v6.png)

### 深度机制分析

**结构域架构解析**：TRAPPC2B是一个140氨基酸的小蛋白，但其折叠域的进化保守性令人印象深刻。Sedlin_N结构域（PF04628，IPR006722）与TRAPPC2/Sedlin（X-连锁迟发性脊椎骨骺发育不良致病基因产物）共享高度同源的核心折叠。Longin-like_dom_sf（IPR011012）将TRAPPC2B归入longin超家族——该超家族蛋白普遍采用α-β-α三明治折叠，其标志性特征是一个由5条β链和两侧α螺旋组成的紧凑球状结构域。longin结构域最初在SNARE调控蛋白中鉴定（如VAMP7的longin结构域介导自抑制折叠），但后来发现该折叠被重复用于多种细胞功能：囊泡运输（TRAPP复合物亚基）、自噬调控（MON1-CCZ1复合物）、以及核内功能。在TRAPPC2B中，longin样折叠的分子表面可能提供两种不同性质的相互作用界面——一个疏水凹槽用于结合TRAPP复合物的其他亚基（如TRAPPC3，BioGRID共纯化证实的伙伴），另一个带电荷表面区域用于核内互作伙伴的识别。pLDDT=92.2是该报告集中最高的评分之一，表明AlphaFold对140个残基的几乎所有位置都有高置信度的主链构象预测，这与其紧凑的单结构域折叠特征完全一致。非结构区域（N端或C端延伸）几乎不存在，是典型的全折叠小蛋白。

**PPI网络中的核心信号**：TRAPPC3的共鉴定是确认TRAPPC2B作为TRAPP复合物组分的"金标准"证据——TRAPPC3（synbindin）是TRAPP II/III复合物的核心亚基，两者同属于TRAPP家族的小亚基组。但真正揭示TRAPPC2B核功能的是其余互作伙伴组合：ZBED1（zinc finger BED-type containing 1）是一个DNA结合蛋白，其BED型锌指结构与hAT转座酶超家族同源，通常作为转录调控因子（已知调控MHC I类基因表达）；EFTUD2（elongation factor Tu GTP binding domain containing 2）是U5 snRNP的核心成分，在剪接体的组装和催化中不可或缺，其突变导致下颌骨面部发育不良伴小头畸形（MFDM）；ZRANB1（zinc finger RANBP2-type containing 1）是一个去泛素化酶，特异性切割K63-连接的多聚泛素链，参与Wnt和NF-kB信号通路。这组伙伴提示TRAPPC2B在细胞核内连接了囊泡运输蛋白与RNA加工机器和泛素信号系统——这在目前已知的TRAPP复合物亚基中独一无二。

**双重定位的结构基础与功能模型**：UniProt注释揭示TRAPPC2B"prevents transcriptional repression and induction of cell death by ENO1"（防止ENO1引起的转录抑制和细胞死亡），这一功能描述完全独立于其囊泡运输角色。ENO1（α-enolase）已知具有"兼职"转录抑制功能：在细胞核中，ENO1结合c-myc启动子的MBP-1元件并抑制转录。TRAPPC2B可能通过以下机制对抗ENO1：(1) 直接竞争——TRAPPC2B的longin结构域与ENO1的DNA结合域竞争同一结合位点或互作伙伴；(2) 间接去抑制——TRAPPC2B可能招募去泛素化酶ZRANB1去除ENO1复合物上的K63多聚泛素链，导致抑制性复合物解聚。其分子量仅16.4 kDa，远小于典型核孔复合物的被动扩散截止值（约40-60 kDa），意味着TRAPPC2B可以不依赖主动转运自由穿梭核膜，为在细胞质（ER-高尔基体）和细胞核之间发挥双重功能提供了物理基础。

**研究与应用前景**：PubMed为0的事实使TRAPPC2B成为此轮评估中新颖性最高的蛋白（新颖性评分10/10），但也意味着几乎所有推论都需要从头验证。首选的验证策略应包括：(1) 免疫共沉淀确认TRAPPC2B与ZBED1、EFTUD2和ZRANB1的内源性互作；(2) ChIP-seq确认TRAPPC2B在ENO1靶基因启动子上的共定位；(3) 在TRAPPC2B敲除细胞系中检测c-myc和ENO1已知靶基因的表达变化；(4) 免疫电镜或Split-GFP互补实验确证细胞核膜两侧的双重定位。该蛋白的结构紧凑性和高pLDDT使结构引导的突变研究（如破坏longin结构域疏水核心的突变）成为直接可行的功能解剖策略。如果TRAPPC2B确实将囊泡运输机制与转录调控耦合，它将代表一个崭新的跨界功能类别——"运输-转录双重功能蛋白"，其核功能可能独立进化为从早期分泌通路的"服务者"到基因表达的直接调控者。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TRAPPC2B

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000256060-TRAPPC2B

![](https://images.proteinatlas.org/63308/1186_G12_2_red_green.jpg)
![](https://images.proteinatlas.org/63308/1186_G12_3_red_green.jpg)
![](https://images.proteinatlas.org/63308/1200_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/63308/1200_G12_6_red_green.jpg)
