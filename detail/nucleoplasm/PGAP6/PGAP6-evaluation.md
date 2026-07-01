---
type: protein-evaluation
gene: "PGAP6"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PGAP6 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PGAP6 |
| 蛋白名称 | Post-GPI attachment to proteins factor 6 |
| 蛋白大小 | 771 aa / 84.8 kDa |
| UniProt ID | Q9HCN3 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Cytokinetic bridge; Nucleoplasm (Supported) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 771 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=2 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=80.9; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | EGF; NGX6/PGAP6/MYMK |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **132/180** | |
| **归一化总分** | | | **73.2/100** | 互证: +2 |

### 3. 分析
- Cytokinetic bridge; Nucleoplasm (Supported)
- PubMed strict=2 broad=5
- AF pLDDT=80.9 PDB=0
- InterPro: EGF; NGX6/PGAP6/MYMK
- Pfam: DUF3522
- PPI degree=0 ChIP: None
37414151: Identification of the glycosylphosphatidylinositol-specific phospholipase A2 (GP | 41180236: Analysis of transcriptome and metabolome characteristics of blood in yaks at dif

### 4. 总体评价
**73.2/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Post-GPI attachment to proteins factor 6

**功能**: Involved in the lipid remodeling steps of GPI-anchor maturation. Lipid remodeling steps consist in the generation of 2 saturated fatty chains at the sn-2 position of GPI-anchor proteins (GPI-AP). Has phospholipase A2 activity that removes an acyl-chain at the sn-2 position of GPI-anchors during the remodeling of GPI. Required for the shedding of the GPI-AP CRIPTO, but not CFC1, at the cell surface. Shedding of CRIPTO modulates Nodal signaling by allowing soluble CRIPTO to act as a Nodal corecept

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000742 |
| InterPro | IPR021910 |
| Pfam | PF12036 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

### 深度机制分析

**结构域架构**：PGAP6（771 aa，84.8 kDa）含有两个特征结构域：EGF样结构域（IPR000742）和NGX6/PGAP6/MYMK家族结构域（IPR021910，PF12036 DUF3522）。EGF结构域含保守的半胱氨酸骨架形成三对二硫键，常见于分泌蛋白和膜蛋白的胞外区；而DUF3522是该蛋白的催化核心，编码GPI-磷脂酶A2（GPI-PLA2）活性——这是GPI锚定蛋白脂质重塑的关键酶活。多个Cytokinetic bridge定位（Supported）表明PGAP6在细胞分裂末期的膜重塑中发挥功能。

**PPI互作网络解读**：PPI degree=0（BioGRID未收录直接互作），但STRING共表达网络揭示PGAP6与GPI锚定生物合成通路的蛋白高度共表达——PIGB（415）、PGAP2（474）、PGAP3（455）、PGAP1（472），所有评分均为中高水平（>400）。这种"无直接互作但共表达网络完整"的模式符合内质网/高尔基体定位的酶学特征：GPI重塑酶不形成稳定复合物，而是作为独立酶成员在同一亚细胞区室（ER）中顺序作用。自身互作评分536提示可能形成同源二聚体或寡聚体。

**结构解读**：AlphaFold pLDDT=80.9，整体折叠质量较高。EGF结构域形成紧凑的β-折叠核心（pLDDT >85），三对二硫键提供了高度稳定性。DUF3522催化域预测为α/β水解酶折叠（pLDDT 70-85），含有推测的催化三联体Ser-His-Asp，通过亲核攻击机制水解GPI锚的sn-2酰基链。PMID:37414151为唯一的功能验证文献，鉴定PGAP6为GPI-PLA2活性并提供CRIPTO剪切的功能证据。

**机制模型**：PGAP6的核心功能集中于GPI锚定蛋白的脂质重塑步骤（ER→高尔基体运输途中），但核质定位（Supported）暗示存在非经典功能：（1）在细胞分裂的cytokinetic bridge阶段，PGAP6可能参与分裂沟的GPI锚定蛋白重塑，其核膜重新组装期间的一过性核质信号可能是分裂相关转运的结果而非真正的核内功能；（2）EGF结构域使得PGAP6易被蛋白酶（如ADAM家族金属蛋白酶）从膜上剪切释放，可溶性胞内片段可能扩散至核质参与信号传导。

**TE调控展望**：PGAP6的TE调控潜力极低。其主要功能锚定于膜脂代谢和蛋白质翻译后修饰，缺乏任何DNA/RNA结合或染色质修饰结构域。核质信号更可能反映其在高尔基体-ER-核膜连续体中运输或细胞分裂过程中的瞬时再分布。若需排除其TE调控潜力，可在GPI-PLA2活性抑制后检测TE表达水平——鉴于无直接核内机制证据，预期不产生显著变化。


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9HCN3-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000129925-PGAP6

![](https://images.proteinatlas.org/51281/1240_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/51281/1240_A3_3_red_green.jpg)
![](https://images.proteinatlas.org/51281/840_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/51281/840_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/51281/781_B5_1_red_green.jpg)
![](https://images.proteinatlas.org/51281/781_B5_2_red_green.jpg)
![](https://images.proteinatlas.org/64673/1258_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/64673/1258_C2_2_red_green.jpg)

### PubMed 文献

**PubMed count: 5**

| 41180236 | Analysis of transcriptome and metabolome characteristics of blood in yaks at different reproductive stages. | Front Vet Sci 2025 |
| 40618286 | Dual Functions and Therapeutic Potential of FZD6 in Biliary Atresia. | Dig Dis Sci 2025 |
| 37414151 | Identification of the glycosylphosphatidylinositol-specific phospholipase A2 (GPI-PLA2) that mediates GPI fatty acid rem | J Biol Chem 2023 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PGAP6

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PIGB | STRING | 415 |
| ATP1B4 | STRING | 615 |
| PGAP2 | STRING | 474 |
| PGAP3 | STRING | 455 |
| ACER1 | STRING | 539 |
| ANKRD27 | STRING | 456 |
| IGDCC4 | STRING | 453 |
| ACER2 | STRING | 489 |
| PGAP1 | STRING | 472 |
| SIDT1 | STRING | 448 |
| TIMM17B | STRING | 459 |
| FAM234A | STRING | 410 |
| TTC21A | STRING | 479 |
| PGAP6 | STRING | 536 |
