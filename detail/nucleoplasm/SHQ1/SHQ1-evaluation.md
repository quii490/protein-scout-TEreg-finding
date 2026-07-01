---
type: protein-evaluation
gene: "SHQ1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SHQ1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SHQ1 |
| 蛋白名称 | Protein SHQ1 homolog |
| 蛋白大小 | 577 aa / 65.1 kDa |
| UniProt ID | Q6PI26 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 577 aa |
| 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=28 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=72.5; PDB=3 |
| 调控结构域 | 4/10 | ×2 | 8.0 | CS_dom; HSP20-like_chaperone; Shq1 |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=36 |
| **加权总分** | | | **127/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +2 |

### 3. 分析
- HPA: Nucleoplasm (Supported)
- PubMed: strict=28, broad=43
- AF pLDDT: 72.5 / PDB: 3
- InterPro: CS_dom; HSP20-like_chaperone; Shq1
- Pfam: SHQ1; SHQ1-like_CS
- PPI degree: 36 / ChIP: None
**Papers**: 41132854: VIRMA-mediated SHQ1 m6A modification enhances liver regeneration through an HNRN | 25553844: Structure and interactions of the CS domain of human H/ACA RNP assembly protein  | 36869663: Proteomic analyses reveal new features of the box H/ACA RNP biogenesis.

### 4. 总体评价
★★★★  **70.5/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Protein SHQ1 homolog

**功能**: Required for the quantitative accumulation of H/ACA ribonucleoproteins (RNPs), including telomerase, probably through the stabilization of DKC1, from the time of its synthesis until its association with NOP10, NHP2, and NAF1 at the nascent H/ACA RNA

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR007052 |
| InterPro | IPR008978 |
| InterPro | IPR039742 |
| InterPro | IPR048696 |
| InterPro | IPR007009 |
| Pfam | PF04925 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DKC1 | STRING | 999 |
| GAR1 | STRING | 995 |
| NOP10 | STRING | 994 |
| NHP2 | STRING | 983 |
| NAF1 | STRING | 878 |
| RUVBL1 | STRING | 861 |
| RUVBL2 | STRING | 829 |
| WRAP53 | STRING | 813 |



### 深度机制分析

SHQ1（Protein SHQ1 homolog，577 aa）是H/ACA核糖核蛋白（RNP）生物合成和端粒酶组装的关键伴侣蛋白。结构域包含CS结构域（IPR007052）、HSP20样伴侣域（IPR008978）和Shq1特异区域（IPR039742, PF04925）。CS（CHORD-SGT1）结构域与Hsp90共伴侣蛋白同源，提示其作为分子伴侣的功能。AF pLDDT=72.5，PDB=3。PPI网络极度富集H/ACA RNP组分：DKC1（999，dyskerin假尿苷合酶）、GAR1（995）、NOP10（994）、NHP2（983）和RUVBL1/RUVBL2（861/829）——后者为染色质重塑相关的AAA+ ATP酶。关键文献41132854揭示VIRMA介导的SHQ1 m6A修饰通过HNRNPA2B1依赖机制增强肝再生（Acta Pharm Sin B 2025），这是SHQ1与表观转录组学的直接联系。41885709报道SHQ1相关神经发育障碍扩展基因型和表型前沿。核质定位为Supported。SHQ1作为H/ACA snoRNP伴侣，通过稳定DKC1确保假尿苷修饰的正常进行，这一修饰发生于rRNA、snRNA甚至mRNA，直接影响翻译和剪接精度。m6A修饰SHQ1自身mRNA则构成了表观转录组调控的反馈环路，TE调控可能性高。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6PI26-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000144736-SHQ1

![](https://images.proteinatlas.org/42792/558_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/42792/558_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/42792/518_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/42792/518_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/42792/530_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/42792/530_F8_3_red_green.jpg)

### PubMed 文献

**PubMed count: 43**

| 41885709 | A Revealing Case of SHQ1-Related Neurodevelopmental Disorder: Expanding the Genotypic and Phenotypic Frontier. | J Child Neurol 2026 |
| 41132854 | VIRMA-mediated SHQ1 m6A modification enhances liver regeneration through an HNRNPA2B1-dependent mechanism. | Acta Pharm Sin B 2025 |
| 41132644 | Ribosome biogenesis-related gene signature predicts prognosis and immune landscape in glioma and identifies UTP20 as a t | Front Immunol 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SHQ1

