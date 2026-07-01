---
type: protein-evaluation
gene: "BCAM"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## BCAM (Basal cell adhesion molecule) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | BCAM |
| 蛋白全称 | Basal cell adhesion molecule |
| UniProt ID | P50895 |
| 蛋白大小 | 628 aa / 69.1 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 628 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR013162; InterPro:IPR007110; InterPro:IPR036179; InterPro:IPR013783; InterPro:IPR003599; InterPro:IPR003598 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Transmembrane glycoprotein that functions as both a receptor and an adhesion molecule playing a crucial role in cell adhesion, motility, migration and invasion (PubMed:9616226, PubMed:31413112). Extracellular domain enables binding to extracellular matrix proteins, such as laminin, integrin and other ligands while its intracellular domain interacts with cytoskeletal proteins like hemoglobin, facil

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR013162 |
| InterPro | IPR007110 |
| InterPro | IPR036179 |
| InterPro | IPR013783 |
| InterPro | IPR003599 |
| InterPro | IPR003598 |
| InterPro | IPR013106 |
| InterPro | IPR051116 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。


### 深度机制分析

**结构域架构**：BCAM（628 aa, 69.1 kDa, P50895, Basal cell adhesion molecule，别名LU/Lutheran blood group antigen, CD239）是免疫球蛋白超家族（IgSF）细胞粘附分子。胞外域含5个immunoglobulin-like（Ig-like）domains——2个V-type（IPR013106, Ig-like V-type 1: residues 32-142; V-type 2: residues 147-257）和3个C2-type（IPR013162, C2-type 1: residues 274-355; C2-type 2: residues 363-441; C2-type 3: residues 448-541）——V-type Ig domain为~110 aa的Greek-key beta-sandwich（2层anti-parallel beta-sheet, BED/A'GFCC' topology），C2-type为较小的beta-sandwich（D-E and A-B-E-D topology）。胞内域（residues 542-628, ~87 aa）——较短但功能关键——含conserved basic motif（KxK/R motif）结合ankyrin和spectrin——介导BCAM与actin cytoskeleton的连接。AlphaFold结构可用——Ig domains因高度保守pLDDT高（>85），胞内tail disordered（pLDDT <50）。IgSF蛋白因大量glycosylation和disulfide bonds使X-ray crystallography和NMR均有一定困难——BCAM尚无实验PDB结构。BCAM在红细胞（作为LU blood group antigen）、多种上皮细胞和内皮细胞表面表达——Lutheran null phenotype（Lu(a-b-)）由KLF1 transcription factor变异导致BCAM表达丧失。

**PPI互作网络解读**：PPI degree有限。LAMA5（Laminin subunit alpha-5, STRING 946, high confidence）是BCAM的关键extracellular ligand——laminin-511/521（alpha5-beta1/beta2-gamma1）是basement membrane的主要组件——BCAM-LAMA5 interaction经BCAM的V-type Ig domains介导epithelial/endothelial cell adhesion to basement membrane——应力下维持组织integrity。GCLC（Glutamate-cysteine ligase catalytic subunit, STRING 905）是谷胱甘肽（GSH）生物合成的rate-limiting enzyme——催化glutamate + cysteine→gamma-glutamylcysteine——GCLC互作暗示BCAM可能参与oxidative stress response signaling。GRHPR（Glyoxylate reductase/hydroxypyruvate reductase, STRING 874）催化glyoxylate→glycolate和hydroxypyruvate→D-glycerate——oxalate metabolism的关键酶。UBE2I（SUMO-conjugating enzyme UBC9, BioGRID）是SUMOylation pathway的核心E2 enzyme——将SUMO moiety共价连接至substrate lysine——调控protein localization, stability and interaction。KLHL2（Kelch-like protein 2, BioGRID）是cullin3-RING E3 ligase adaptor——识别specific substrate进行泛素化降解。ARNTL（Aryl hydrocarbon receptor nuclear translocator-like/BMAL1, BioGRID）是circadian clock核心transcription factor——与CLOCK形成heterodimer→结合E-box→驱动circadian gene expression。PRCC（Papillary renal cell carcinoma translocation-associated protein, BioGRID）是transcription co-regulator。

**结构解读**：BCAM的5个Ig-like domains形成extended "beads-on-a-string"构型——总extracellular span约35-40 nm——将配体结合位点（V-type Ig domains的A'CFG sheet）投射至远离细胞表面的位置——利于结合大分子laminin polymers in basement membrane。V-type Ig domain的conserved inter-sheet disulfide bond（Cys23-Cys104 pattern）稳定Ig fold——C2-type Ig domain通常缺乏此disulfide。胞内tail KxK/R motif识别ankyrin-B/G的ZU5 domain——ankyrin作为adaptor连接BCAM和beta-spectrin/actin cytoskeleton——BCAM-ankyrin-spectrin complex在red blood cell membrane skeleton中维持bi-concave shape和mechanical elasticity。Lutheran blood group antigen Lu(a)/Lu(b) polymorphism由BCAM胞外域的单氨基酸变异（His77/Arg77）导致——影响anti-Lu antibody recognition but不影响laminin binding。

**机制模型**：（1）Cell adhesion to laminin——BCAM识别laminin alpha5 chain的LG domain（laminin G-like domain）——经BCAM-LAMA5 adhesion维持epithelium对basement membrane的anchoring——在血管内皮中，BCAM-laminin-511/521 interaction在血管壁shear stress resistance中重要（尤其在skeletal muscle capillary, placenta, kidney glomerulus）。（2）Sickle cell disease——BCAM在sickle RBC中的上调和phosphorylation（经PKA）增加RBC adhesion to laminin→促进vaso-occlusive crisis——异常RBC adhesion至血管内皮基底膜laminin→blocking microvasculature→ischemia and pain。（3）Prostate cancer（PMID:42374482）——ELFN1-AS1（lncRNA）作为ceRNA通过sponging miR-28-5p上调BCAM——BCAM overexpression促进prostate cancer cell proliferation and migration via enhanced cell-matrix adhesion signaling。（4）Circadian connection——BCAM-ARNTL/BMAL1互作暗示BCAM可能参与circadian rhythm-dependent cell adhesion——细胞粘附分子表达在许多组织中有circadian oscillation→影响组织通透性和免疫细胞trafficking随时间的变化。

**TE调控展望**：BCAM的TE调控关联极弱。作为classical cell adhesion molecule，BCAM的主要功能在胞外和质膜——通过UBE2I（SUMOylation）、KLHL2（E3 ligase adaptor）和PRCC（transcriptional co-regulator）间接连接至核内调控。UBE2I-SUMOylation system在TE silencing中的作用已有多项研究——SUMO modification of TRIM28/KAP1 and KRAB-ZFPs is required for SETDB1 recruitment and H3K9me3 deposition on ERV/LINE-1 loci——BCAM-UBE2I互作如果影响UBE2I在核内的availability→可能间接干扰TE silencing。ARNTL/BMAL1作为circadian transcription factor结合E-box（CACGTG）——该motif在LINE-1和ERV LTR中存在——circadian regulation of TE expression在文献中有初步报道——BCAM-BMAL1互作提示BCAM可能参与TE expression的circadian modulation。但这些均为高度推测性路径，缺乏BCAM与TE直接function的experimental support。

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000187244-BCAM

![](https://images.proteinatlas.org/5654/609_G4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/5654/609_G4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/5654/604_G4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/5654/604_G4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/5654/607_G4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/5654/607_G4_3_blue_red_green.jpg)

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00409;SM00408; |
| InterPro | IPR013162;IPR007110;IPR036179;IPR013783;IPR003599;IPR003598;IPR013106;IPR051116; |
| Pfam | PF08205;PF13895;PF13927;PF07686; |
| UniProt Domain | DOMAIN 32..142; /note="Ig-like V-type 1"; DOMAIN 147..257; /note="Ig-like V-type 2"; DOMAIN 274..355; /note="Ig-like C2-type 1"; DOMAIN 363..441; /note="Ig-like C2-type 2"; DOMAIN 448..541; /note="Ig-like C2-type 3" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| LAMA5 | STRING | 946 |
| GCLC | STRING | 905 |
| GRHPR | STRING | 874 |
| HACL1 | STRING | 758 |
| UBE2I | BioGRID | 1 |
| KLHL2 | BioGRID | 1 |
| ARNTL | BioGRID | 1 |
| PRCC | BioGRID | 1 |


### PubMed 文献

**PubMed count: 571**

| 42374482 | Silencing of ELFN1-AS1 induces prostate cancer cell apoptosis and autophagy by regulating miR-28-5p/BCAM axis. | World J Surg Oncol 2026 |
| 42351768 | Live Imaging of Nitric Oxide Dynamics Reveals Cell Type-Specific NO Signaling in Air-Liquid Interface Cultures of Human  | Biomedicines 2026 |
| 42311766 | Personalized polygenic profiling based on the genetic architecture of lipid metabolism in the Russian population. | Front Cardiovasc Med 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/BCAM

