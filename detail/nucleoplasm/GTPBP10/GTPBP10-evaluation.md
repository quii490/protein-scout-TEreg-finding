---
type: protein-evaluation
gene: "GTPBP10"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## GTPBP10 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | GTPBP10 |
| 蛋白名称 | GTP-binding protein 10 |
| 蛋白大小 | 387 aa / 42.9 kDa |
| UniProt ID | A4D1E9 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 387 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=6 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=80.4; PDB=2 |
| 调控结构域 | 4/10 | ×2 | 8.0 | G_OBG; GTP-bd; GTP-bd_Obg/CgtA |
| PPI | 7/10 | ×3 | 21.0 | PPI degree=181 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +2 |

### 3. 分析
- HPA: nan (nan)
- PubMed: strict=6, broad=13
- AF pLDDT: 80.4 / PDB: 2
- InterPro: G_OBG; GTP-bd; GTP-bd_Obg/CgtA
- Pfam: GTP1_OBG; MMR_HSR1
- PPI degree=181 ChIP: None
36595475: A comprehensive landscape of transcription profiles and data resources for human | 30321378: Human GTPBP10 is required for mitoribosome maturation. | 30085210: The human Obg protein GTPBP10 is involved in mitoribosomal biogenesis.

### 4. 总体评价
★★★★  **71.6/100**  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: GTP-binding protein 10

**功能**: May be involved in the ribosome maturation process. Complements an ObgE(CgtA) function in E.coli ribosome maturation. Plays a role of GTPase in vitro. When missing, disorganization of the nucleolar architecture is observed

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR031167 |
| InterPro | IPR006073 |
| InterPro | IPR014100 |
| InterPro | IPR006169 |
| InterPro | IPR036726 |
| InterPro | IPR045086 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DDX28 | STRING | 955 |
| MRPL58 | STRING | 933 |
| MRPL19 | STRING | 902 |
| RPL13 | STRING | 898 |
| MRPL2 | STRING | 888 |
| MRPL44 | STRING | 860 |
| MTG1 | STRING | 852 |
| MRPL15 | STRING | 846 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-A4D1E9-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 13**

| 38042949 | Structural insights into the role of GTPBP10 in the RNA maturation of the mitoribosome. | Nat Commun 2023 |
| 36595475 | A comprehensive landscape of transcription profiles and data resources for human leukemia. | Blood Adv 2023 |
| 35320117 | Pan-cancer analysis revealed the significance of the GTPBP family in cancer. | Aging (Albany NY) 2022 |

### 深度机制分析

GTPBP10（387 aa, 42.9 kDa）是保守的Obg/CgtA GTPase家族成员，该家族从细菌到人类均高度保守，参与核糖体成熟这一核心细胞过程。其结构域架构由G_OBG GTPase结构域（IPR031167）组成，该结构域包含经典的GTP结合基序（G1-G5），并与一个独特的Obg折叠（IPR014100）融合。AlphaFold预测pLDDT=80.4，已有2个PDB条目提供实验结构验证，使其成为结构信息较为完善的候选者。

GTPBP10的功能已有明确生化验证：作为线粒体核糖体（mitoribosome）成熟所必需的GTPase（PMID:30321378；PMID:30085210），它在线粒体大亚基（mtLSU）组装后期发挥关键作用。近期结构研究（PMID:38042949）揭示了GTPBP10在mitoribosome的RNA成熟过程中的精确结构角色——它结合在rRNA加工中间体上，利用GTP水解的能量驱动构象重排以释放组装因子并完成成熟过程。当GTPBP10缺失时，可观察到核仁结构的紊乱（UniProt注释），它将线粒体功能与核仁完整性联系起来。

PPI网络极为丰富（BioGRID degree=181），几乎全部为线粒体核糖体蛋白（MRPL系列、DDX28、MTG1），STRING评分普遍高于850，证实GTPBP10整合入线粒体翻译机器的核心网络中。与RPL13（胞质核糖体大亚基蛋白）的互作则暗示线粒体-胞质核糖体之间存在协作调控。

尽管HPA未能提供GTPBP10的有效定位数据（nan, nan），但核仁结构紊乱的表型强烈指示其功能与核仁存在间接联系——可能通过线粒体逆行信号（mitochondrial retrograde signaling）影响核仁。核仁作为核糖体生物合成中心，对线粒体功能状态十分敏感。

在TE调控方面，GTPBP10主要通过线粒体-核逆行信号通路（mito-nuclear crosstalk）间接参与：线粒体应激→改变GTPBP10活性→mitoribosome组装异常→线粒体未折叠蛋白应答（UPRmt）激活→染色质重塑因子和转录因子（如ATFS-1/ATF5）核转位→可能影响核内TE位点的表观遗传状态。线粒体功能障碍与转座子去抑制之间的关联是新兴领域，因mtDNA损伤和线粒体应激可导致SIRT1下调和H3K9me3丢失。GTPBP10位于这一通路的早期节点，使其成为连接线粒体稳态和核内TE抑制的潜在桥梁。Pan-cancer分析提示GTPBP家族在肿瘤中的重要地位（PMID:35320117）。建议实验用mtDNA缺失细胞（rho0细胞）检查TE表达变化与GTPBP10表达的相关性。

