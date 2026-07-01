---
type: protein-evaluation
gene: "SLC39A11"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SLC39A11 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SLC39A11 |
| 蛋白名称 | Zinc transporter ZIP11 |
| 蛋白大小 | 342 aa / 35.4 kDa |
| UniProt ID | Q8N1S5 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 342 aa |
| 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=17 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=76.5; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | ZIP |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=72 |
| **加权总分** | | | **134/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +1 |

### 3. 分析
- HPA: Nucleoplasm (Approved)
- PubMed: strict=17, broad=28
- AF pLDDT: 76.5 / PDB: 0
- InterPro: ZIP
- Pfam: Zip
- PPI degree: 72 / ChIP: None
**Papers**: 36388803: Role of methylation-related genes CRYAB and SLC39A11 in the occurrence and devel | 39114488: A Novel Role for the Longevity-Associated Protein SLC39A11 as a Manganese Transp | 36155972: Prostaglandins and calprotectin are genetically and functionally linked to the I

### 4. 总体评价
★★★★  **73.8/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Zinc transporter ZIP11

**功能**: Zinc importer that regulates cytosolic zinc concentrations either via zinc influx from the extracellular compartment or efflux from intracellular organelles such as Golgi apparatus. May transport copper ions as well. The transport mechanism remains to be elucidated

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR003689 |
| Pfam | PF02535 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

SLC39A11(ZIP11)是ZIP(SLC39)锌转运蛋白家族成员，编码一个具有8次跨膜螺旋结构的膜整合蛋白。其核心功能域为ZIP结构域(IPR003689/PF02535)，该结构域在进化上高度保守，从原核ZupT到真核ZIP家族均保留核心锌/锰离子转运功能。AlphaFold预测其跨膜螺旋束结构的pLDDT仅76.5且无PDB实验结构，提示其胞外环区及膜内柔性区域存在较高的构象不确定性，这与膜蛋白固有结晶困难的特征一致。

HPA定位数据显示SLC39A11在核质(Nucleoplasm, Approved)中有明确信号。这一发现挑战了传统上认为ZIP蛋白仅位于质膜或细胞器膜上的认知。核质定位可能通过以下机制实现：ZIP11在核膜上发挥离子通道功能，调节核内锌离子([Zn²⁺]nuc)浓度稳态。核内游离Zn²⁺作为第二信使，在转录因子结构中参与锌指蛋白(ZFP)的锌配位组装，直接影响数百种锌指转录因子与DNA的结合活性。

PPI互作证据显示SLC39A11与ELAVL1(HuR，RNA结合蛋白)和EGFR(表皮生长因子受体)存在物理互作(BioGRID)。HuR结合提示ZIP11可能通过调控核质Zn²⁺浓度间接影响HuR对ARE含mRNA的剪接与稳定性。EGFR互作则暗示了一条核Zn²⁺信号—EGFR—MAPK信号通路之间的耦合调控。

近年研究表明SLC39A11除转运锌离子外，也是一类功能性的锰离子转运蛋白(PMID:39114488)。核锰的蓄积可通过激活MnSOD启动子区域的氧化应激响应元件而影响核基因转录。此外，SLC39A11启动子区域的DNA甲基化状态与肿瘤发生密切相关(PMID:36388803)，这为该核定位转运蛋白的表观遗传调控提供了直接线索。综合而言，SLC39A11作为核质定位明确的离子转运蛋白(PubMed仅17篇)，是探索核内金属离子信号与转录调控交叉机制的理想研究对象。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8N1S5-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000133195-SLC39A11

![](https://images.proteinatlas.org/21455/1584_C8_4_red_green.jpg)
![](https://images.proteinatlas.org/21455/1584_C8_5_red_green.jpg)
![](https://images.proteinatlas.org/21455/1601_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/21455/1601_A10_3_red_green.jpg)
![](https://images.proteinatlas.org/21455/1732_A10_7_cr580611b3405d6_red_green.jpg)
![](https://images.proteinatlas.org/21455/1732_A10_13_cr580611bc44ecf_red_green.jpg)

### PubMed 文献

**PubMed count: 28**

| 42303625 | Manganese: biology, physiology and role in disease. | Cell Discov 2026 |
| 42089960 | In vitro and in silico analysis of three variants associated with type 2 diabetes. | Acta Diabetol 2026 |
| 41966325 | Sex-specific regulation of SLC39A11 in the murine liver. | J Genet Genomics 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SLC39A11

