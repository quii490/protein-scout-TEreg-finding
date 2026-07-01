---
type: protein-evaluation
gene: "PAM16"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PAM16 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PAM16 |
| 蛋白名称 | Mitochondrial import inner membrane translocase subunit TIM16 |
| 蛋白大小 | 125 aa / 13.8 kDa |
| UniProt ID | Q9Y3D7 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Microtubules; Mitochondria; Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 125 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=33 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=89.3; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | J_dom_sf; Tim16 |
| PPI | 7/10 | x3 | 21.0 | PPI degree=131 |
| **加权总分** | | | **132/180** | |
| **归一化总分** | | | **73.2/100** | 互证: +2 |

### 3. 分析
- Microtubules; Mitochondria; Nucleoplasm (Approved)
- PubMed strict=33 broad=52
- AF pLDDT=89.3 PDB=0
- InterPro: J_dom_sf; Tim16
- Pfam: Pam16
- PPI degree=131 ChIP: None
37403271: Heart failure in patients is associated with downregulation of mitochondrial qua | 27829973: Common functions of the chloroplast and mitochondrial co-chaperones cpDnaJL (CDF | 19564938: The mitochondrial protein translocation motor: structural conservation between t

### 4. 总体评价
**73.2/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Mitochondrial import inner membrane translocase subunit TIM16

**功能**: Regulates ATP-dependent protein translocation into the mitochondrial matrix. Inhibits DNAJC19 stimulation of HSPA9/Mortalin ATPase activity

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR036869 |
| InterPro | IPR005341 |
| Pfam | PF03656 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| FEZ1 | BioGRID | 0 |
| DNAJC19 | BioGRID | 0 |
| TIMM17A | BioGRID | 0 |
| MRFAP1 | BioGRID | 0 |
| GPM6A | BioGRID | 0 |
| CEP70 | BioGRID | 0 |
| BLOC1S2 | BioGRID | 0 |
| DNMT3B | BioGRID | 0 |


### 深度机制分析

**结构域架构**：PAM16（125 aa，13.8 kDa）是线粒体内膜蛋白输入马达的核心调控亚基，含两个保守结构域——J_dom_sf（IPR036869）和Tim16（IPR005341，PF03656 Pam16）。J_dom_sf属于分子伴侣DnaJ超家族的类J结构域折叠，但PAM16的J-like结构域缺乏经典的HPD（His-Pro-Asp）三肽基序，取而代之的是非经典的类J折叠——这一"失活"的J结构域使其无法像典型DnaJ蛋白那样刺激Hsp70 ATPase活性，反而通过与DNAJC19（Tim14/PAM18）的竞争性结合**抑制**HSPA9/Mortalin的ATPase活性（UniProt功能注释）。Tim16结构域形成紧凑的螺旋束折叠，作为与TIMM17A等转位酶亚基的结合平台。

**PPI互作网络解读**：PPI degree=131，核心互作包括：DNAJC19（线粒体内膜转位酶J蛋白，PAM16的直接抑制靶标）、TIMM17A（线粒体内膜蛋白转位酶Tim17/Tim22/Tim23复合物的核心亚基，与PAM16共同构成PAM复合物的膜锚定点）、DNMT3B（DNA甲基转移酶3B，催化CpG位点的从头甲基化——此互作在非线粒体环境中提示PAM16可能通过调控线粒体代谢影响甲基供体SAM的产生）。FEZ1（Fasciculation and Elongation Protein Zeta 1，微管结合蛋白）和CEP70（中心体蛋白70）的互作进一步支持PAM16在微管和中心体相关过程中的非经典功能。

**结构解读**：AlphaFold pLDDT=89.3，预测质量极佳。J-like结构域（残基约1-70）形成经典的DnaJ折叠——4股α-螺旋束（helix I-IV），其中helix II和III之间的loop区在原核/线粒体DnaJ蛋白中负责与Hsp70的ATPase域互作。PAM16在此区域缺乏HPD基序（被替代为HDD或类似序列），结构上表现为更窄的loop构象，无法有效激活Hsp70。Tim16域（残基约70-125）为α-螺旋结构，pLDDT >90，形成与TIMM17A的跨膜α-螺旋互补的结合界面。

**机制模型**：PAM16的经典功能是作为线粒体蛋白输入马达（PAM复合物）的抑制性调控亚基：（1）在膜间隙侧，PAM16通过J-like结构域与DNAJC19竞争HSPA9/Mortalin的结合位点，调控ATP驱动的蛋白转位进入线粒体基质的速率；（2）PAM16与TIMM17A和TIMM23共同构成内膜转位酶的完整性——PAM16的Tim16域直接结合TIMM17A，稳定内膜转位通道；（3）PAM16的核质定位（Microtubules; Mitochondria; Nucleoplasm Approved）的来源推测为：新生PAM16在胞质核糖体合成后至线粒体输入的中间状态（precursor pool），在此过程中部分PAM16可能结合微管并被HPA检测到核周信号。DNMT3B的互作是否为检测假象还是有生物学意义（如通过SAM代谢连接线粒体和核内甲基化）尚需验证。

**TE调控展望**：PAM16的TE调控潜力极低。其作为线粒体特异性蛋白的功能框架完全定位于线粒体蛋白稳态维持。唯一潜在的间接联系为：线粒体功能障碍（如PAM16缺失导致的蛋白输入缺陷）可激活线粒体未折叠蛋白应答（UPR^mt），该应激信号可通过ATF5-CHOP轴影响核基因表达——但这一通路与TE调控之间的关系非常间接，目前无任何实验证据支持。



![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9Y3D7-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000217930-PAM16

![](https://images.proteinatlas.org/62721/1261_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/62721/1261_H8_3_red_green.jpg)
![](https://images.proteinatlas.org/62721/1232_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/62721/1232_B9_2_red_green.jpg)
![](https://images.proteinatlas.org/62721/1199_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/62721/1199_B9_6_red_green.jpg)

### PubMed 文献

**PubMed count: 52**

| 42090721 | MAGMAS Inhibition Enhances Temozolomide Efficacy in Chemotherapy-Resistant Glioblastoma Models. | Cancer Res Commun 2026 |
| 41099349 | Lon/Pim1-mediated degradation of presequence translocase-associated motor components Pam16 and Pam18 in Saccharomyces ce | Biochem J 2025 |
| 40508044 | Identification of Genomic Structural Variations in Xinjiang Brown Cattle by Deep Sequencing and Their Association with B | Int J Mol Sci 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PAM16

