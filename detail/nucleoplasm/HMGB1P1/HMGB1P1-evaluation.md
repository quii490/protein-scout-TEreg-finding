---
type: protein-evaluation
gene: "HMGB1P1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## HMGB1P1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | HMGB1P1 |
| 蛋白名称 | High mobility group protein B1-like 1 |
| 蛋白大小 | 211 aa / 24.2 kDa |
| UniProt ID | B2RPK0 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | Nucleoplasm (Approved) |
| 📏 蛋白大小 | 7/10 | ×1 | 7.0 | 211 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=75.9; PDB=0 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | HMG_box_dom; HMG_box_dom_sf; HMGB |
| 🔗 PPI | 5/10 | ×3 | 15.0 | PPI degree=37 |
| **加权总分** | | | **134/180** | |
| **归一化总分 (÷1.83)** | | | **73.8/100** | 互证: +1 |

### 3. 详细分析

| 项目 | 详情 |
|---|---|
| HPA | Nucleoplasm (Approved) |
| PubMed | strict=0, broad=1 |
| AlphaFold | pLDDT=75.9 |
| PDB | 0 entries |
| InterPro | HMG_box_dom; HMG_box_dom_sf; HMGB |
| Pfam | HMG_box; HMG_box_2 |
| PPI | combined degree=37 |
| ChIP | None |

### 4. 总体评价
⭐⭐⭐⭐
**73.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: High mobility group protein B1-like 1

**功能**: Binds preferentially single-stranded DNA and unwinds double-stranded DNA

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR009071 |
| InterPro | IPR036910 |
| InterPro | IPR050342 |
| Pfam | PF00505 |
| Pfam | PF09011 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: High mobility group protein B1-like 1

**功能**: Binds preferentially single-stranded DNA and unwinds double-stranded DNA

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR009071 |
| InterPro | IPR036910 |
| InterPro | IPR050342 |
| Pfam | PF00505 |
| Pfam | PF09011 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

HMGB1P1是HMGB1(High Mobility Group Box 1)蛋白的假基因编码同源物，含211 aa且携带两个HMG_box功能域(HMG_box_dom IPR009071和HMG_box_dom_sf IPR036910)。HMG box是经典的DNA结合/弯曲结构域，由3个α-螺旋组成L形折叠，嵌入DNA小沟并诱导急剧的DNA弯曲(>90°)。与脊椎动物HMGB1的串联双HMG-box不同，HMGB1P1仅含211 aa，是否编码完整的双HMG盒有待进一步序列比对确认。

HPA定位为Nucleoplasm(Approved)，这是HMG-box超家族的经典定位类型。在核质中，HMGB1P1通过HMG box结合并弯曲DNA，这种DNA弯曲活性在以下生物过程中发挥核心作用：核小体滑移与染色质重塑(V(D)J重组中的RAG1/2增强因子)、基因转录调控(作为多种转录因子的辅助激活因子)和DNA修复(识别顺铂加合物等扭曲DNA结构)。PPI互作证据显示HMGB1P1与EP300(组蛋白乙酰转移酶p300)和RAC1(小G蛋白)存在BioGRID互作，暗示其在染色质修饰和细胞骨架信号间的桥接功能。

需要注意的是，HMGB1P1是假基因产物——其表达的蛋白可能具有与HMGB1功能冗余但不完全等同的角色。与母本HMGB1(pLDDT未知，但结构已有PF00505和PF09011的双HMG-box高置信度预测)相比，HMGB1P1的pLDDT仅75.9，表明折叠完整性可能有所下降。进一步研究的核心问题是：HMGB1P1是否拮抗或协同HMGB1的DNA结合活性？还是作为竞争性内源RNA翻译产物以非HMG依赖方式发挥功能？PubMed count=0(仅有1篇非直接相关文献)使该蛋白成为"已知结构域、未知功能"的研究领域蓝海，CRISPR-i敲低实验可揭示其细胞必需性与HMGB1的功能差异性。




![PAE](https://alphafold.ebi.ac.uk/files/AF-B2RPK0-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000124097-HMGB1P1

![](https://images.proteinatlas.org/73663/2007_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/73663/2007_F11_2_red_green.jpg)
![](https://images.proteinatlas.org/73663/2043_F12_31_red_green.jpg)
![](https://images.proteinatlas.org/73663/2043_F12_32_red_green.jpg)
![](https://images.proteinatlas.org/73663/1935_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/73663/1935_A6_2_red_green.jpg)

### PubMed 文献

**PubMed count: 1**

| 27655316 | A comparative analysis of genetic diversity of candidate genes associated with type 2 diabetes in worldwide populations. | Yi Chuan 2016 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/HMGB1P1

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ABCE1 | physical | Kaerblane K (2015) |
| HMGB1 | physical | Huttlin EL (2017) |
| RPTOR | physical | Fonseca BD (2015) |
| LARP7 | physical | Faust TB (2018) |
| METTL14 | physical | Yue Y (2018) |
| EP300 | physical | Raisner R (2018) |
| CASP9 | physical | Kennedy SA (2020) |
| RAC1 | physical | Kennedy SA (2020) |
| RALBP1 | physical | Kennedy SA (2020) |
| SH3GL3 | physical | Kennedy SA (2020) |

