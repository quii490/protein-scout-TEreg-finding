---
type: protein-evaluation
gene: "PSMC3IP"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PSMC3IP 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PSMC3IP |
| 蛋白名称 | Homologous-pairing protein 2 homolog |
| 蛋白大小 | 217 aa / 24.9 kDa |
| UniProt ID | Q9P2W1 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm (Supported) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 217 aa |
| 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=28 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=92.1; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Hop2_WH_dom; LZ3wCH; WH-like_DNA-bd_sf |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=38 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **71.0/100** | 互证: +2 |

### 3. 分析
| 项目 | 详情 |
|---|---|
| HPA | Nucleoplasm (Supported) |
| PubMed | strict=28, broad=46 |
| AF pLDDT | 92.1 |
| PDB | 0 |
| InterPro | Hop2_WH_dom; LZ3wCH; WH-like_DNA-bd_sf |
| Pfam | LZ3wCH; WHD_TBPIP |
| PPI degree | 38 |
| ChIP | None |

**Papers**: 30362169: Knockdown of PSMC3IP suppresses the proliferation and xenografted tumorigenesis  | 33170803: Meiosis interrupted: the genetics of female infertility via meiotic failure. | 24481226: No mutations in the PSMC3IP gene identified in a Swedish cohort of women with pr

### 4. 总体评价
★★★★  **71.0/100**  |  **nucleoplasm**
Nuclear protein


### 深度机制分析

PSMC3IP（HOP2/TBPIP）是一个217个氨基酸的减数分裂特异性同源配对因子，其核心结构域组合为翼螺旋（Winged-Helix, WH）DNA结合结构域（IPR040661/WHD_TBPIP）与亮氨酸拉链三螺旋束（IPR010776/LZ3wCH）。WH结构域采用经典的α/β折叠——三个α-螺旋构成疏水核心，C端的"翼"环作为DNA磷酸骨架的辅助识别元件。LZ3wCH形成左手三股卷曲螺旋超二级结构，介导PSMC3IP与MND1形成稳定的异二聚体——这是其所有的减数分裂功能的前提。AlphaFold预测pLDDT高达92.1，结合0个PDB条目的矛盾（高预测置信度但无实验结构），使该蛋白成为结构生物学中极具吸引力的靶标。

PSMC3IP的核心机制模型为：PSMC3IP-MND1异二聚体作为RAD51和DMC1重组酶的辅因子，促进减数分裂中同源染色体配对和链交换（strand exchange）过程。具体而言，该异二聚体结合DNA后稳定RAD51/DMC1在ssDNA上形成的核蛋白丝（presynaptic filament），并促进其对dsDNA的捕获（synaptic complex formation），从而催化同源重组中的关键步骤——链侵入（strand invasion）和D-loop形成。缺乏PSMC3IP的小鼠/人类模型中减数分裂完全停滞，导致不育（PMID:33170803）。

HPA Supported的核质定位（Nucleoplasm）完全符合其在减数分裂同源重组中的核功能——该蛋白必须在染色质水平上发挥功能。PPI网络（degree=38）中与NR3C1（糖皮质激素受体）和BCAR3（乳腺癌抗雌激素耐药蛋白3）的核内互作（BioGRID=0）提示PSMC3IP可能具有减数分裂之外的、发生在体细胞中的DNA修复功能。事实上，PSMC3IP在胶质瘤中已被鉴定为预后生物标志物和免疫调节因子（PMID:40684322），其表达水平与患者生存期显著相关——这一观察如果反映的是PSMC3IP在体细胞同源重组修复中的角色，将具有重要的药物基因组学意义。

尽管ChIP结果为None，PSMC3IP作为WH结构域蛋白在理论上具备直接结合DNA的能力。WH超折叠是转录因子中第二常见的DNA结合基序（仅次于HTH），包括FOX、ETS和HNF3等经典转录因子家族。PSMC3IP的WH结构域可能在进化上保留了对特定DNA序列（如减数分裂重组热点）的识别能力——这一假说若获证实，将使PSMC3IP从"纯重组辅因子"升级为"位点特异的染色质调控因子"。从TE调控角度看，PSMC3IP通过同源重组机制可能参与维持着丝粒和端粒附近的基因组稳定性——这些区域富含转座子衍生的重复序列——间接影响TE元件的维持与清除的平衡。

**蛋白全称**: Homologous-pairing protein 2 homolog

**功能**: Plays an important role in meiotic recombination. Stimulates DMC1-mediated strand exchange required for pairing homologous chromosomes during meiosis. The complex PSMC3IP/MND1 binds DNA, stimulates the recombinase activity of DMC1 as well as DMC1 D-loop formation from double-strand DNA. This complex stabilizes presynaptic RAD51 and DMC1 filaments formed on single strand DNA to capture double-strand DNA. This complex stimulates both synaptic and presynaptic critical steps in RAD51 and DMC1-promot

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR010776 |
| InterPro | IPR040661 |
| InterPro | IPR036388 |
| Pfam | PF18517 |
| Pfam | PF07106 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| NR3C1 | BioGRID | 0 |
| PSMC3 | BioGRID | 0 |
| MND1 | BioGRID | 0 |
| AURKA | BioGRID | 0 |
| BCAR3 | BioGRID | 0 |
| BRMS1 | BioGRID | 0 |
| CASP8 | BioGRID | 0 |
| FZR1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9P2W1-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000131470-PSMC3IP

![](https://images.proteinatlas.org/44439/519_A8_2_red_green.jpg)
![](https://images.proteinatlas.org/44439/519_A8_3_red_green.jpg)

### PubMed 文献

**PubMed count: 46**

| 41681894 | Comprehensive Characterization of Stem Cell Landscape Identifies Novel Stemness-Relevant Genes for Nasopharyngeal Carcin | Cancers (Basel) 2026 |
| 41644825 | Disruption of meiotic double-strand break dynamics provokes germline human infertility in both sexes. | J Assist Reprod Genet 2026 |
| 40684322 | PSMC3IP as a prognostic biomarker and immunomodulatory regulator in low-grade glioma: insights from multi-omics and meth | Neurol Res 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PSMC3IP

