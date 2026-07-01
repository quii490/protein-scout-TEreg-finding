---
type: protein-evaluation
gene: "FAM72A"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## FAM72A 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | FAM72A |
| 蛋白名称 | Protein FAM72A |
| 蛋白大小 | 149 aa / 16.6 kDa |
| UniProt ID | Q5TYM5 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | nan (Approved) |
| 📏 蛋白大小 | 6/10 | ×1 | 6.0 | 149 aa |
| 🆕 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=22 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=86.1; PDB=0 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | YPEH2ZP |
| 🔗 PPI | 5/10 | ×3 | 15.0 | PPI degree=2 |
| **加权总分** | | | **131/180** | |
| **归一化总分 (÷1.83)** | | | **72.1/100** | 互证: +1 |

### 3. 详细分析

| 项目 | 详情 |
|---|---|
| HPA | nan (Approved) |
| PubMed | strict=22, broad=36 |
| AlphaFold | pLDDT=86.1 |
| PDB | 0 entries |
| InterPro | YPEH2ZP |
| Pfam | YPEH2ZP |
| PPI | combined degree=2 |
| ChIP | None |

### 4. 总体评价
⭐⭐⭐⭐
**72.1/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

FAM72A（Protein FAM72A）是一个仅149 aa的小蛋白（16.6 kDa），其唯一已知的结构域为YPEH2ZP保守区（Pfam PF14976, InterPro IPR026768），这是一个功能未知的脊椎动物特异性结构域家族。AlphaFold2预测pLDDT=86.1（得分7/10），无PDB实验结构，提示该蛋白虽小但具有明确的折叠核心。分子量仅16.6 kDa使FAM72A可能通过被动扩散穿越核孔复合物进入核质（HPA Approved级别定位），无需经典的核定位信号（NLS）。

FAM72A的PPI网络极为有限（degree=2），仅与MPPED2（金属磷酸酯酶结构域蛋白2）和WDYHV1（含WDYHV基序蛋白1）存在BioGRID互作。这种低度的PPI网络既可能是真实的功能特征（FAM72A可能作为独立的功能单元而非复合物亚基发挥作用），也可能反映研究覆盖度低。MPPED2在神经发育中具有功能，WDYHV1可能参与蛋白去乙酰化或类泛素化修饰，这两条线索都指向FAM72A在细胞增殖和分化调控中的潜在角色。

从功能机制角度，FAM72A在肿瘤生物学中正成为一个备受关注的分子。UniProt注释提示其参与细胞活性氧代谢调控和细胞生长调控。最新文献提供了关键的肿瘤机制证据：PMID:42174281发现FAM72A通过NF-κB信号通路促进肺癌增殖和迁移，NF-κB是炎症-癌症转化的核心核内转录因子，FAM72A在核质中可能直接或间接调控NF-κB的转录活性。PMID:42159844揭示了FAM72A在卵巢癌中通过PINK1/Parkin通路驱动线粒体自噬和细胞焦亡的功能，提示FAM72A在核-线粒体交叉通讯中的协调作用。

尤为关键的是，PMID:41414706发现FAM72A的表达受细胞周期调控，来自Srgap2-Fam72a主基因座，其产物导致Mis18a下调。Mis18a是着丝粒染色质装配的关键因子，负责CENP-A的着丝粒沉积。这一发现直接将FAM72A与核内着丝粒功能和染色体精确分离相连接。FAM72A在核质中的Approved级别定位与这一功能高度一致。作为22篇PubMed文献（得分9/10）的蛋白，FAM72A在肿瘤生物学中的重要性已初见端倪，但其在正常核质中的分子功能仍有待系统性阐明。

### 补充分析 (UniProt API)

**蛋白全称**: Protein FAM72A

**功能**: May play a role in the regulation of cellular reactive oxygen species metabolism. May participate in cell growth regulation

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR026768 |
| Pfam | PF14976 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MPPED2 | BioGRID | 0 |
| WDYHV1 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q5TYM5-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000196550-FAM72A

![](https://images.proteinatlas.org/43271/748_A6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43271/748_A6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43271/896_A6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43271/896_A6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43271/728_A6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43271/728_A6_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000196550-FAM72A

![](https://images.proteinatlas.org/43271/748_A6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43271/748_A6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43271/896_A6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43271/896_A6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43271/728_A6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43271/728_A6_2_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000196550-FAM72A

![](https://images.proteinatlas.org/43271/748_A6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43271/748_A6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43271/896_A6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43271/896_A6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43271/728_A6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43271/728_A6_2_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 36**

| 42174281 | FAM72A is associated with lung cancer proliferation and migration via the NF‑κB signaling pathway. | Mol Genet Genomics 2026 |
| 42159844 | FAM72A Knockdown Drives Cell Mitophagy and Pyroptosis in Ovarian Cancer Via the PINK1/Parkin Pathway. | Appl Biochem Biotechnol 2026 |
| 41414706 | Cell cycle-regulated expression of Fam72a from the |Srgap2-Fam72a| master gene leads to Mis18a downregulation. | Cell Cycle 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/FAM72A

