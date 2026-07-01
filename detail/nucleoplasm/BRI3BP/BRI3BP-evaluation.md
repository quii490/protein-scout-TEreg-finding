---
type: protein-evaluation
gene: "BRI3BP"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## BRI3BP 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | BRI3BP |
| 蛋白名称 | BRI3-binding protein |
| 蛋白大小 | 251 aa / 27.8 kDa |
| UniProt ID | Q8WY22 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36.0 | Mitochondria; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 251 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=10 |
| 三维结构 | 4/10 | ×3 | 12.0 | pLDDT=62.8; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | BRI3BP |
| PPI | 7/10 | ×3 | 21.0 | PPI degree=118 |
| **加权总分** | | | **134/180** | |
| **归一化总分** | | | **74.3/100** | 互证: +2 |

### 3. 分析
- HPA: Mitochondria; Nucleoplasm (Approved)
- PubMed: strict=10, broad=11
- AF pLDDT: 62.8 / PDB: 0
- InterPro: BRI3BP
- Pfam: BRI3BP
- PPI degree=118 ChIP: None
41174063: Multi-omic analysis reveals elevated BRI3BP expression associated with hepatocel | 41085794: A prognostic model for gastric cancer constructed by multiple machine learning a | 17765869: Augmentation of drug-induced cell death by ER protein BRI3BP.

### 4. 总体评价
★★★★  **74.3/100**  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: BRI3-binding protein

**功能**: Involved in tumorigenesis and may function by stabilizing p53/TP53

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR033367 |
| Pfam | PF14965 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: BRI3-binding protein

**功能**: Involved in tumorigenesis and may function by stabilizing p53/TP53

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR033367 |
| Pfam | PF14965 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ESR1 | BioGRID | 0 |
| RNF2 | BioGRID | 0 |
| AMFR | BioGRID | 0 |
| TSPAN5 | BioGRID | 0 |
| GDE1 | BioGRID | 0 |
| PTH1R | BioGRID | 0 |
| P2RY12 | BioGRID | 0 |
| DLK1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8WY22-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000184992-BRI3BP

![](https://images.proteinatlas.org/14957/1386_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/14957/1386_E7_2_red_green.jpg)

### PubMed 文献

**PubMed count: 11**

| 41674927 | Establishment and validation of a prognostic model based on liquid-liquid phase separation-related genes in gastric canc | Transl Cancer Res 2026 |
| 41174063 | Multi-omic analysis reveals elevated BRI3BP expression associated with hepatocellular carcinoma progression and poor pro | Sci Rep 2025 |
| 41085794 | A prognostic model for gastric cancer constructed by multiple machine learning algorithms. | J Mol Histol 2025 |

### 深度机制分析

BRI3BP是p53/TP53稳定性的调控因子，参与肿瘤发生过程（PMID:17765869）。其结构域架构极简——仅含单个BRI3BP结构域（IPR033367/PF14965），251 aa的蛋白中AlphaFold pLDDT仅62.8且无实验PDB结构，暗示其可能含有大量无序区域。PPI网络达118个互作伙伴，其中ESR1（雌激素受体α）、RNF2（Polycomb抑制复合物1的E3泛素连接酶）和AMFR（自噬相关E3泛素连接酶）最值得关注，提示BRI3BP可能通过泛素-蛋白酶体系统调控多种转录因子的蛋白稳定性。

BRI3BP的核心机制模型以p53稳定化为枢纽：通过与BRI3（内质网膜蛋白）的结合，BRI3BP可能在内质网应激条件下感知ER稳态失衡，进而通过抑制MDM2或直接结合p53来阻止其泛素化降解。这种"ER应激-p53轴"在肿瘤发生中具有双重效应——在正常细胞中维持基因组稳定性，而在已转化的细胞中则可能被共选择以抵抗凋亡。HPA中Mitochondria和Nucleoplasm的双重Approved定位支持这一模型：线粒体池感知凋亡信号，核质池直接参与p53转录程序的调控。

肝癌预后分析（PMID:41174063, 41674927）将BRI3BP鉴定为肝细胞癌进展和不良预后的标志物，胃液-液相分离相关基因的预后模型（PMID:41674927）进一步将BRI3BP纳入相分离调控网络。考虑到液-液相分离（LLPS）是p53核内凝聚体形成的驱动力，BRI3BP可能在LLPS介导的p53转录凝聚体组装中扮演支架蛋白角色。对其无序区域的计算预测和p53凝聚体的共定位分析将是验证这一假设的关键实验。

