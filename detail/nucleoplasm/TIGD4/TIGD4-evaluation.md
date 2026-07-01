---
type: protein-evaluation
gene: "TIGD4"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## TIGD4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TIGD4 |
| 蛋白名称 | Tigger transposable element-derived protein 4 |
| 蛋白大小 | 512 aa / 57.5 kDa |
| UniProt ID | Q8IY51 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 512 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=3 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=78.1; PDB=0 |
| 调控结构域 | 6/10 | ×2 | 12.0 | CenT-Element_Derived; DDE_SF_endonuclease_dom; Homeodomain-like_sf |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=5 |
| **加权总分** | | | **140/180** | |
| **归一化总分** | | | **77.0/100** | 互证: +1 |

### 3. 分析
- HPA: Cytosol; Nucleoplasm (Approved)
- PubMed: strict=3, broad=4
- AF pLDDT: 78.1 / PDB: 0
- InterPro: CenT-Element_Derived; DDE_SF_endonuclease_dom; Homeodomain-like_sf
- Pfam: CENP-B_N; DDE_1; HTH_Tnp_Tc5
- PPI degree: 5 / ChIP: None
**Papers**: 29315579: Muscle molecular adaptations to endurance exercise training are conditioned by g | 32742312: Evolution of pogo, a separate superfamily of IS630-Tc1-mariner transposons, reve | 41775084: Single-cell analysis of TIGD genes in hepatocellular carcinoma: Prognostic value

### 4. 总体评价
★★★★  **77.0/100**  |  **nucleoplasm**
**TE candidate**: CenT-Element_Derived; DDE_SF_endonuclease_dom; Homeodomain-like_sf


### 深度机制分析

**结构域架构**: TIGD4是目前报告中最独特的结构域组合——由转座子驯化（domestication）事件产生的三层DNA结合模块。N端结构域为CENP-B_N（Pfam），这是一个螺旋-转角-螺旋（HTH）DNA结合模块，源自着丝粒蛋白CENP-B，能特异性识别着丝粒区域的CENP-B盒DNA基序。中间为DDE_1（Pfam），属于DDE-转座酶/整合酶催化结构域（IS630-Tc1-mariner超家族），核心为RNase H-like折叠，含保守的DDE催化三联体——但驯化后这些催化残基可能已失活。C端为HTH_Tnp_Tc5（Pfam）和Homeodomain-like_sf（InterPro），提供第二个序列特异性DNA识别表面。InterPro标注"CenT-Element_Derived"将此蛋白明确归类为着丝粒转座元件衍生蛋白。这三个结构域按线性排列，形成了一个罕见的"串联DNA结合—催化样—串联DNA结合"架构。

**PPI网络解读**: TIGD4的PPI网络（degree=5）虽小但信息密集。HOXD4（BioGRID评分1）是同源异型盒转录因子——TIGD4的C端homeodomain-like折叠可能与HOXD4共用或竞争相似的DNA结合位点，暗示TIGD4可能作为转录调控的辅助因子。TRAF2（BioGRID评分1）是TNF受体信号通路的关键接头蛋白，直接参与NF-κB和JNK的激活——这是唯一一个将TIGD4与炎症信号通路联系起来的线索，具有重大意义：TIGD4可能作为TE来源的免疫调控蛋白，在进化上被招募来整合转座子沉默与先天免疫信号。RNF123（BioGRID）是E3泛素连接酶，S100B（BioGRID）是钙结合蛋白。缺乏STRING高评分互作提示TIGD4主要以DNA为底物而非蛋白网络运作。

**结构诠释**: AlphaFold pLDDT=78.1为中等置信度，反映了多结构域蛋白的结构复杂性。三个结构域间的柔性连接区（linker）导致整体折叠的可变性。CENP-B_N结构域通常采用经典的HTH折叠（3个α螺旋），以第二个螺旋（识别螺旋）插入DNA大沟；DDE结构域采用RNase H-like的β1-β2-β3-α1-β4-β5-α2折叠（含5条β链形成的混合β片层）；homeodomain-like结构域以HTH二聚体形式结合DNA。PMID 32742312（Mob DNA 2020）对pogo超家族的进化分析揭示了Tc1-mariner转座子通过多次独立的驯化事件进入宿主基因组——TIGD4代表了其中一个驯化事件，其祖先转座酶可能捕获了一个CENP-B_N结构域作为DNA结合模块。

**分子机制模型**: TIGD4是一个被驯化的转座子来源的染色质组织蛋白：(1) 它的CENP-B_N结构域将其靶向着丝粒/中心粒周围区域的CENP-B盒序列——这是宿主着丝粒功能与转座子驯化之间的一个迷人联系；(2) DDE结构域虽已失去催化活性，但保留了识别和弯曲转座子末端反向重复序列（TIR）的结构能力，可能作为DNA弯曲/成环因子辅助染色质三维组织；(3) C端的homeodomain-like结构域提供了第二层DNA序列识别能力，可能识别与Tigger转座子相关的内部DNA基序。这三层DNA结合能力使TIGD4有潜力将分散在基因组中的Tigger家族转座子拷贝组织为高级染色质结构域。HPA核质定位（Approved）与这一模型一致。

**研究/治疗意义**: PMID 41775084（Transl Oncol 2026）的单细胞分析表明TIGD基因家族在肝细胞癌中具有预后价值——TIGD4可能在肝癌的染色质重塑中发挥作用，影响癌基因或抑癌基因附近TE元件的表观遗传状态。TRAF2互作（BioGRID）开辟了一个全新方向：TIGD4可能参与连接转座子感应与炎症信号——类似于cGAS-STING通路感应细胞质DNA，TIGD4可能在核内感应TE激活并通过TRAF2→NF-κB触发炎症反应。作为pogo超家族的驯化成员，TIGD4代表了一类新的药物靶点——针对驯化转座酶的特异性抑制可能影响肿瘤细胞的染色质组织而不影响正常细胞的着丝粒功能（因为CENP-B本身具有功能冗余性）。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HOXD4 | BioGRID | 1 |
| TRAF2 | BioGRID | 1 |
| KIAA1279 | BioGRID | 0 |
| RNF123 | BioGRID | 0 |
| S100B | BioGRID | 0 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000169989-TIGD4

![](https://images.proteinatlas.org/35649/393_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/35649/393_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/35649/396_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/35649/396_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/35649/392_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/35649/392_H8_2_red_green.jpg)

### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8IY51-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 4**

| 42352890 | Novel Potential Risk Loci for Migraine in the Portuguese Population. | Int J Mol Sci 2026 |
| 41775084 | Single-cell analysis of TIGD genes in hepatocellular carcinoma: Prognostic value and functional characterization. | Transl Oncol 2026 |
| 32742312 | Evolution of pogo, a separate superfamily of IS630-Tc1-mariner transposons, revealing recurrent domestication events in  | Mob DNA 2020 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TIGD4

