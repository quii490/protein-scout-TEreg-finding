---
type: protein-evaluation
gene: "LYPD5"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## LYPD5 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | LYPD5 |
| 蛋白名称 | Ly6/PLAUR domain-containing protein 5 |
| 蛋白大小 | 251 aa / 26.9 kDa |
| UniProt ID | Q6UWN5 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 251 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=4 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=84.0; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | CD59_antigen_CS; LY6_UPA_recep-like; Snake_toxin-like_sf |
| PPI | 5/10 | x3 | 15.0 | PPI degree=14 |
| **加权总分** | | | **134/180** | |
| **归一化总分** | | | **73.8/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=4 broad=7
- AF pLDDT=84.0 PDB=0
- InterPro: CD59_antigen_CS; LY6_UPA_recep-like; Snake_toxin-like_sf
- Pfam: UPAR_LY6
- PPI degree=14 ChIP: None
30558617: Circular RNA regulatory network reveals cell-cell crosstalk in acute myeloid leu | 23896969: The urokinase receptor homolog Haldisin is a novel differentiation marker of str | 29377892: Network-based co-expression analysis for exploring the potential diagnostic biom

### 4. 总体评价
**73.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Ly6/PLAUR domain-containing protein 5

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR018363 |
| InterPro | IPR016054 |
| InterPro | IPR045860 |
| Pfam | PF00021 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CLSTN1 | BioGRID | 0 |
| ERMP1 | BioGRID | 0 |
| TSPO | BioGRID | 0 |
| LPPR2 | BioGRID | 0 |
| BET1 | BioGRID | 0 |
| EHHADH | BioGRID | 0 |
| C14orf1 | BioGRID | 0 |
| IFITM3 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：LYPD5（251 aa，26.9 kDa）属于Ly6/urokinase-type plasminogen activator receptor（uPAR）蛋白超家族，含有标志性的LU结构域（LY6_UPA_recep-like，IPR045860）和CD59抗原保守序列（CD59_antigen_CS，IPR018363）。LU结构域采用三指毒素折叠（Snake_toxin-like_sf，IPR016054）——以高度保守的二硫键网络（8-10个Cys残基）稳定3个β-发夹环从中央疏水核心向外延伸，形成刚性的蛋白-蛋白互作界面。C端含GPI锚定信号，将LYPD5锚定于细胞膜外叶。Pfam注释为UPAR_LY6（PF00021），与尿激酶受体同源。

**PPI互作网络解读**：PPI degree仅14，且所有互作评分均为0（BioGRID低通量筛选）。互作伙伴包括CLSTN1（Calsyntenin-1，突触后膜货物转运受体）、TSPO（线粒体外膜转位蛋白18kDa）、IFITM3（干扰素诱导跨膜抗病毒蛋白3）和BET1（ER-Golgi SNARE蛋白）。这些互作的生物学相关性存疑——GPI锚定蛋白的互作瞬时性强（低亲和力细胞外互作），在酵母双杂交（BioGRID主要数据来源）中难以真实捕获。PPI度低与GPI锚定蛋白的生化特性一致。

**结构解读**：AlphaFold pLDDT=84.0，LU结构域核心区域预测质量良好（pLDDT >90）。三指拓扑结构由N端α-螺旋和C端延伸区约束5条反平行β-链形成疏水核心，三个延伸环（Loop1-3）暴露于溶剂，构成潜在的配体结合表面。GPI锚定位点（ω位点）的预测在AlphaFold中未被建模（IDR区域）。值得注意的是，Pfam PF00021（UPAR_LY6）结构域对应uPAR的多配体结合面——在人uPAR中该结构域同时结合尿激酶（uPA）、玻连蛋白和整合素，但LYPD5是否保留这一多功能结合面需实验验证。

**机制模型**：LYPD5/Haldisin最初被鉴定为角质形成细胞终末分化标志物（PMID:23896969），定位于表皮颗粒层（stratum granulosum）。作为GPI锚定细胞表面蛋白，LYPD5的功能机制可能包括：（1）顺式调控相邻跨膜信号受体（如整合素或生长因子受体）的活性——这是uPAR家族成员的经典功能模式；（2）作为可溶性配体的诱饵受体，经GPI锚定磷脂酶（如GPI-PLD）切割后释放至细胞外间质；（3）参与角质形成细胞间粘附和分层。其在核质中的HPA阳性信号极可能是ER/Golgi运输途中沿核膜的GPI锚定蛋白转运中间体造成的免疫荧光假象——GPI锚定蛋白在ER腔面合成后经COPII囊泡→Golgi→细胞膜的路径不涉及核质分布。

**TE调控展望**：LYPD5的TE调控潜力为0。GPI锚定的拓扑限制使其永远无法接触染色质或核内调控因子。其在鳞状细胞分化和角质形成细胞生物学中的角色局限于细胞表面信号传导——与TE沉默机制无任何已知交叉。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6UWN5-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000159871-LYPD5

![](https://images.proteinatlas.org/42511/460_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/42511/460_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/42511/467_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/42511/467_G6_3_red_green.jpg)
![](https://images.proteinatlas.org/42511/465_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/42511/465_G6_2_red_green.jpg)

### PubMed 文献

**PubMed count: 7**

| 41074104 | Saliva as a potential and non-invasive approach to identify upregulated genes associated with comorbidities of T1DM: a b | Eur J Med Res 2025 |
| 32140067 | Crystal Structures of Human C4.4A Reveal the Unique Association of Ly6/uPAR/α-neurotoxin Domain. | Int J Biol Sci 2020 |
| 30558617 | Circular RNA regulatory network reveals cell-cell crosstalk in acute myeloid leukemia extramedullary infiltration. | J Transl Med 2018 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/LYPD5

