---
type: protein-evaluation
gene: "CASQ1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CASQ1

### 1. Basic Info
| Item | Value |
|---|---|
| Gene | CASQ1 |
| Protein Name | Calsequestrin-1 |
| Size | 396 aa / 45.2 kDa |
| UniProt | P31415 |
| Date | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | Mitochondria; Nucleoplasm (Approved) |
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 396 aa |
| 🆕 研究新颖性 | 7/10 | ×5 | 35.0 | PubMed=90 |
| 🏗️ 三维结构 | 10/10 | ×3 | 30.0 | pLDDT=90.0; PDB=6 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | Calsequestrin; Calsequestrin_C; Calsequestrin_CS |
| 🔗 PPI | 5/10 | ×3 | 15.0 | PPI degree=20 |
| **加权总分** | | | **133.0/180** | |
| **归一化总分 (÷1.83)** | | | **72.7/100** | 互证: +2.0 |

### 3. Analysis
- HPA: Mitochondria; Nucleoplasm (Approved)
- PubMed: strict=90, broad=172
- AF pLDDT: 90.0 / PDB: 6
- InterPro: Calsequestrin; Calsequestrin_C; Calsequestrin_CS
- Pfam: Calsequestrin
- PPI degree=20 ChIP: None
32488451: Calsequestrin, a key protein in striated muscle health and disease. | 24887214: An association study of CASQ1 gene polymorphisms and heat stroke. | 40707202: Calsequestrin-1 Deficiency Induced Malignant Hyperthermia-Like Skeletal Injury t

### 4. Assessment
★★★★  **73.8/100**  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Calsequestrin-1

**功能**: Calsequestrin is a high-capacity, moderate affinity, calcium-binding protein and thus acts as an internal calcium store in muscle (PubMed:28895244). Calcium ions are bound by clusters of acidic residues at the protein surface, often at the interface between subunits. Can bind around 80 Ca(2+) ions (PubMed:28895244). Regulates the release of lumenal Ca(2+) via the calcium release channel RYR1; this plays an important role in triggering muscle contraction. Negatively regulates store-operated Ca(2+

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR001393 |
| InterPro | IPR041860 |
| InterPro | IPR018233 |
| InterPro | IPR041858 |
| InterPro | IPR041859 |
| InterPro | IPR036249 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ILKAP | BioGRID | 0 |
| TRDN | BioGRID | 0 |
| CSK | BioGRID | 0 |
| DVL2 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：CASQ1/Calsequestrin-1（396 aa，45.2 kDa）是肌质网（SR）腔内的主要Ca^2+储存蛋白，属于Calsequestrin家族。含三个特征性结构域：（1）Calsequestrin（IPR001393，核心钙结合域）——由3个串联的硫氧还蛋白样结构域（Trx-like domains I/II/III）构成；（2）Calsequestrin_C（IPR041860，C端酸性尾域，含约50个Asp/Glu残基）——是Ca^2+低亲和力（Kd ~1 mM）、超高容量（~80 Ca^2+/单体）结合的决定簇；（3）Calsequestrin_CS（IPR018233，保守序列）。Thioredoxin-like fold（IPR036249）进一步支持域I/II/III的结构归类。Calsequestrin不采用EF-hand或其他典型Ca^2+结合基序——而是通过表面酸性残基簇和C端poly-Asp/Glu尾以静电方式螯合Ca^2+。

**PPI互作网络解读**：PPI degree=20，主要互作包括：TRDN（Triadin，SR跨膜蛋白，连接Calsequestrin与RyR1钙释放通道——TRDN-CASQ1-RyR1是骨骼肌兴奋-收缩耦合的核心三元复合物）和DVL2（Dishevelled 2，Wnt信号通路支架蛋白）。TRDN是CASQ1功能上最关键的伙伴——TRDN的腔域直接结合CASQ1的Domain II/III界面，并将CASQ1-Ca^2+复合物锚定于距RyR1通道口约10 nm的SR腔面区域，形成高浓度的局部Ca^2+储备池快速供应RyR1开放时的Ca^2+需求。ILKAP（整合素连接激酶相关磷酸酶，BioGRID 0分）和CSK的互作提示CASQ1可能通过非肌细胞中的亚型表达参与更广泛的信号通路。

**结构解读**：AlphaFold pLDDT=90.0，PDB=6——是本批次中结构信息最丰富的蛋白之一。三个Thioredoxin-like结构域（Domain I: 残基1-135, Domain II: 136-260, Domain III: 261-350）的pLDDT均>93，呈现出高度有序的α/β折叠。Trx样折叠由中央4股反平行β-片层被3个α-螺旋包围——Domain I的折叠典型性最高。C端酸性尾（残基351-396，pLDDT 65-80）在无Ca^2+时呈高度延伸的无规卷曲，在Ca^2+饱和时折叠为紧凑构象（已有NMR和SAXS实验证实此构象转变）。CASQ1以低聚物（二聚体/四聚体/更高阶聚合物）形式发挥功能——在Ca^2+浓度升高时，CASQ1通过Domain II-Domain II界面的疏水互作和C端尾的桥接形成线性聚合物，增大Ca^2+储存容量。

**机制模型**：CASQ1在骨骼肌快速收缩-舒张循环中作为Ca^2+缓冲器和RyR1调控器：（1）Ca^2+缓冲：每个CASQ1单体通过表面酸性残基和C端聚天冬氨酸尾螯合约80个Ca^2+离子（总容量~40 mM Ca^2+/SR腔），在SR Ca^2+-ATPase（SERCA1）泵入Ca^2+时防止SR腔内游离Ca^2+浓度过度升高（避免渗透压破坏和Ca^2+磷酸盐沉淀）；（2）Ca^2+释放调控：TRDN直接将CASQ1-RyR1耦合——SR腔Ca^2+浓度低时，CASQ1经TRDN抑制RyR1的开放（防止SR Ca^2+泄漏）；SR腔Ca^2+浓度高时，CASQ1-Ca^2+复合物解聚，解除其对TRDN-RyR1的抑制作用，促进RyR1开放——这一"Ca^2+传感器"功能确保RyR1仅在SR Ca^2+储备充足时被激活。CASQ1突变导致恶性高热（MH）和空泡性肌病（Vacuolar myopathy）——Asp244His突变（PMID:41699400）是亚洲人群中的复发致病位点。

**TE调控展望**：CASQ1的TE调控潜力为0。CASQ1的表达在生理条件下严格限定于骨骼肌纤维（fast-twitch type II fibers为主），其功能和定位完全局限于肌质网腔内的Ca^2+缓冲。即便在非肌细胞中的异位表达（如口腔鳞状细胞癌中，PMID:41613641），CASQ1也不具备任何核/染色质接触的可能性。SR腔蛋白与核TE调控之间的物理区隔过于绝对——多个膜屏障（SR膜、线粒体膜、核膜双层）+胞质宽度使因果联系不可能。

![PAE](https://alphafold.ebi.ac.uk/files/AF-P31415-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000143318-CASQ1

![](https://images.proteinatlas.org/7845/1529_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/7845/1529_H3_2_red_green.jpg)

### PubMed 文献

**PubMed count: 172**

| 41972723 | Tubular Aggregate Myopathies: Genetic Heterogeneity and Diverse Clinical Features Converging on Calcium Dysregulation. | Cells 2026 |
| 41699400 | Vacuolar myopathy caused by CASQ1 p.Asp244His: pathogenic evidence from two unrelated Chinese families. | J Hum Genet 2026 |
| 41613641 | Revealing CASQ1 as a potential target for oral squamous cell carcinoma through gene expression and functional analysis:  | In Silico Pharmacol 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CASQ1

