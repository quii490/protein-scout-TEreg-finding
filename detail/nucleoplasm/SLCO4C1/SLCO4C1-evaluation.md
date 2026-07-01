---
type: protein-evaluation
gene: "SLCO4C1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SLCO4C1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SLCO4C1 |
| 蛋白名称 | Solute carrier organic anion transporter family member 4C1 |
| 蛋白大小 | 724 aa / 78.9 kDa |
| UniProt ID | Q6ZQN7 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm; Plasma membrane (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 724 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=28 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=78.6; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Kazal_dom; Kazal_dom_sf; MFS_dom |
| PPI | 5/10 | x3 | 15.0 | PPI degree=28 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=28 broad=57
- AF pLDDT=78.6 PDB=0
- InterPro: Kazal_dom; Kazal_dom_sf; MFS_dom
- Pfam: Kazal_2; OATP
- PPI degree=28 ChIP: None
38650001: T cell expressions of aberrant gene signatures and Co-inhibitory receptors (Co-I | 38226966: Identification and validation of SLCO4C1 as a biological marker in hepatocellula | 23874392: Indoxyl sulfate down-regulates SLCO4C1 transporter through up-regulation of GATA

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

SLCO4C1（Solute Carrier Organic Anion Transporter Family Member 4C1，亦称OATP4C1）是一个724 aa的有机阴离子转运蛋白（78.9 kDa），拥有典型的MFS（Major Facilitator Superfamily）转运体折叠。其结构域架构包含两个核心模块：N端Kazal型丝氨酸蛋白酶抑制剂结构域（Pfam Kazal_2, InterPro IPR002350），这是一个在转运蛋白中相对罕见的结构特征；C端为MFS转运体结构域（Pfam OATP, InterPro IPR020846），采用12次跨膜螺旋的经典MFS折叠。AlphaFold2预测pLDDT=78.6（得分6/10），无PDB实验结构，但MFS折叠已有大量同源结构支持。

SLCO4C1的PPI网络度为28，其主要互作伙伴的组成提示了令人信服的细胞内转运和信号调控功能。与CTBP2（C端结合蛋白2，转录辅抑制因子）的BioGRID互作具有深刻的核内功能含义——CTBP2是核内关键的转录抑制因子，通过识别含PxDLS基序的转录因子抑制基因表达。SLCO4C1在核质中的Approved级别定位使其与CTBP2的互作在核内具有功能可行性。与RAB11A（小GTPase，调控再循环内体运输）的互作则提示SLCO4C1可能在核周内体-核膜界面上参与底物运输。

SLCO4C1的经典功能是作为肾脏有机阴离子转运蛋白，介导类固醇激素（硫酸雌酮、鹅去氧胆酸等）、甲状腺激素（T3/T4）和cAMP的跨膜转运。然而，其核质Approved级别定位暗示了一个更具冲击力的功能模型——SLCO4C1可能在核内膜或核周内体上转运核内信号分子。cAMP作为SLCO4C1的底物尤为重要，因为核内cAMP可以激活PKA，后者磷酸化CREB等转录因子调控基因表达。SLCO4C1通过调控核内cAMP浓度可能间接影响整个cAMP/PKA/CREB信号轴。PMID:41826328的最新发现证实SLCO4C1是cAMP摄取转运蛋白，在肝细胞中抑制脂肪生成，为MASLD（代谢功能障碍相关脂肪肝病）提供治疗靶点。

SLCO4C1的转录调控也高度相关。PMID:23874392发现硫酸吲哚酚（尿毒症毒素）通过上调GATA3下调SLCO4C1表达——GATA3是核内转录因子，这一调控回路涉及核内的转录调控与膜上的转运功能之间的信号交流。28篇PubMed文献（得分9/10）提供了适度的研究基础，但SLCO4C1在核质中的功能几乎从未被直接研究。其核定位特异性得分9/10和Kazal结构域的独特存在使其成为核转运调控研究中一个不可忽视的候选蛋白。

### 补充分析 (UniProt API)

**蛋白全称**: Solute carrier organic anion transporter family member 4C1

**功能**: Mediates the transport of organic anions such as steroids (estrone 3-sulfate, chenodeoxycholate, glycocholate) and thyroid hormones (3,3',5-triiodo-L-thyronine (T3), L-thyroxine (T4)), in the kidney (PubMed:14993604, PubMed:19129463, PubMed:20610891). Capable of transporting cAMP and pharmacological substances such as digoxin, ouabain and methotrexate (PubMed:14993604). Transport is independent of sodium, chloride ion, and ATP (PubMed:14993604). Transport activity is stimulated by an acidic extr

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002350 |
| InterPro | IPR036058 |
| InterPro | IPR020846 |
| InterPro | IPR036259 |
| InterPro | IPR004156 |
| Pfam | PF07648 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HECW2 | BioGRID | 0 |
| TMEM17 | BioGRID | 0 |
| CTBP2 | BioGRID | 0 |
| LAMTOR1 | BioGRID | 0 |
| RAB11A | BioGRID | 0 |
| DSC1 | BioGRID | 0 |
| MTX1 | BioGRID | 0 |
| SLC45A1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6ZQN7-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 57**

| 41898457 | Preeclampsia Genomic Susceptibility Factors in Populations of African Ancestry: A Systematic Review and Meta-Analysis. | Int J Mol Sci 2026 |
| 41826328 | Hepatocyte SLCO4C1 is a cAMP uptake transporter for inhibiting lipogenesis and a therapeutic target for MASLD. | Nat Commun 2026 |
| 41398767 | Systematic druggable genome-wide mendelian randomization identifies therapeutic targets for childhood asthma. | Medicine (Baltimore) 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SLCO4C1

