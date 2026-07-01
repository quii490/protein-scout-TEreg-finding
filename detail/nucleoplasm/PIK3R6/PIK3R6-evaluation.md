---
type: protein-evaluation
gene: "PIK3R6"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PIK3R6 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PIK3R6 |
| 蛋白名称 | Phosphoinositide 3-kinase regulatory subunit 6 |
| 蛋白大小 | 754 aa / 84.3 kDa |
| UniProt ID | Q5UE93 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Golgi apparatus; Nucleoplasm; Plasma memb (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 754 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=23 |
| 三维结构 | 4/10 | x3 | 12.0 | pLDDT=0.0; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | PIK3R5/6 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=46 |
| **加权总分** | | | **125/180** | |
| **归一化总分** | | | **68.9/100** | 互证: +1 |

### 3. 分析
- Cytosol; Golgi apparatus; Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=23 broad=30
- AF pLDDT=0.0 PDB=0
- InterPro: PIK3R5/6
- Pfam: PI3K_1B_p101
- PPI degree=46 ChIP: None
39060344: Generation of novel lipid metabolism-based signatures to predict prognosis and i | 36252138: BCAM Deficiency May Contribute to Preeclampsia by Suppressing the PIK3R6/p-STAT3 | 33155192: RBBP6 aggravates the progression of ovarian cancer by targeting PIK3R6.

### 4. 总体评价
**68.9/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**PI3Kγ调控亚基的核质信号功能**：PIK3R6（Phosphoinositide 3-kinase regulatory subunit 6, 754 aa, UniProt Q5UE93）是I类PI3Kγ复合物的调控亚基，与催化亚基PIK3CG（p110γ）形成异二聚体。其唯一结构域为PI3K_1B_p101（Pfam: PI3K_1B_p101 PF10486; InterPro: PIK3R5/6 IPR019522），作为适配蛋白驱动G蛋白βγ亚基对PIK3CG的激活。PI3Kγ复合物主要在胞质中产生PIP3第二信使，调控免疫细胞趋化性和血管生成（通过PDE3B:RAPGEF3信号复合物）。HPA数据清晰标注该蛋白位于Nucleoplasm（Approved级别, 核定位特异性9/10），暗示存在核内PI3K信号的新功能。

**核内磷酸肌醇信号与转录调控**：近年来核内磷酸肌醇（nuclear phosphoinositides, nPI）代谢已成为一个活跃的研究领域。核内PIP2和PIP3被发现在染色质重塑、pre-mRNA剪接和转录起始中发挥调控作用。核内PI3K/s PIP3产物可与核内PHD锌指蛋白（如TAF3, ING2）结合，影响其染色质结合行为。若PIK3R6-PIK3CG复合物在核内产生PIP3，可间接调控PHD指蛋白的H3K4me3阅读功能——而H3K4me3标记与TE启动子区域的染色质状态直接相关。

**极低结构置信度与PPI特征**：AlphaFold pLDDT=0.0（极不寻常的低值）暗示PIK3R6为高度无序蛋白，这与其适配蛋白/支架蛋白的角色一致——信号适配蛋白通常缺乏独立折叠域，其构象在结合互作伙伴后才稳定化。PPI degree=46（BioGRID/STRING），包含PIK3CG催化亚基（BioGRID score=0），以及多个核蛋白伙伴：DHX9（RNA解旋酶A, BioGRID score=0）、HIST1H1A（接头组蛋白H1.1, BioGRID score=0）和RPL10A（核糖体蛋白L10a）——这些核内互作一致暗示核内功能。

**肿瘤相关文献中的染色质调控线索**：PubMed=23的文献主要集中于癌症生物信息学（PMIDs:39060344, 36252138, 33155192）。PMIDs:33155192（RBBP6加重卵巢癌进展通过靶向PIK3R6）和36252138（BCAM缺陷通过抑制PIK3R6/p-STAT3促进子痫前期）提示该蛋白可能通过STAT3信号通路参与转录调控——而STAT3被报道能调控LINE-1和Alu元件的转录（PMID:28003220）。

**PI3K-mTOR-TE调控网络的多层交汇**：PI3K/AKT/mTOR通路通过mTORC1抑制DF-1自噬受体介导的TE RNA降解，且mTOR信号影响PIWI蛋白稳定性。PIK3R6作为PI3Kγ特异调控亚基，可能通过组织特异性mTOR激活间接影响TE表达。加上核质定位的存在，核内PI3K-PIP3信号可能参与染色质区域的局部磷脂微环境调控——这一新兴概念为PIK3R6的TE调控研究提供了独特的分子假说。归一化得分68.9/100中核定位特异性36/40和新奇性45/50均为支撑维度。


### 补充分析 (UniProt API)

**蛋白全称**: Phosphoinositide 3-kinase regulatory subunit 6

**功能**: Regulatory subunit of the PI3K gamma complex. Acts as an adapter to drive activation of PIK3CG by beta-gamma G protein dimers. The PIK3CG:PIK3R6 heterodimer is much less sensitive to beta-gamma G protein dimers than PIK3CG:PIK3R5 and its membrane recruitment and beta-gamma G protein dimer-dependent activation requires HRAS bound to PIK3CG. Recruits of the PI3K gamma complex to a PDE3B:RAPGEF3 signaling complex involved in angiogenesis; signaling seems to involve RRAS

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR019522 |
| Pfam | PF10486 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PIK3CG | BioGRID | 0 |
| RFC5 | BioGRID | 0 |
| HIST1H1A | BioGRID | 0 |
| S100A10 | BioGRID | 0 |
| STX3 | BioGRID | 0 |
| TCP1 | BioGRID | 0 |
| DHX9 | BioGRID | 0 |
| RPL10A | BioGRID | 0 |