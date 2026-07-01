---
type: protein-evaluation
gene: "TNFRSF25"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TNFRSF25 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TNFRSF25 |
| 蛋白名称 | Tumor necrosis factor receptor superfamily member 25 |
| 蛋白大小 | 417 aa / 45.4 kDa |
| UniProt ID | Q93038 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Actin filaments; Focal adhesion sites; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 417 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=97 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=72.3; PDB=3 |
| 调控结构域 | 4/10 | x2 | 8.0 | DEATH-like_dom_sf; Death_dom; TNFR/NGFR_Cys_rich_reg |
| PPI | 5/10 | x3 | 15.0 | PPI degree=35 |
| **加权总分** | | | **121/180** | |
| **归一化总分** | | | **67.2/100** | 互证: +2 |

### 3. 分析
- Actin filaments; Focal adhesion sites; Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=97 broad=343
- AF pLDDT=72.3 PDB=3
- InterPro: DEATH-like_dom_sf; Death_dom; TNFR/NGFR_Cys_rich_reg
- Pfam: Death; TNFR_c6
- PPI degree=35 ChIP: None
40749165: Pretransplant targeting of TNFRSF25 and CD25 stimulates recipient Tregs in targe | 35018112: Long Non-Coding RNA Signatures Associated with Ferroptosis Predict Prognosis in  | 40428348: Whole-Genome DNA Methylation Analysis in Age-Related Hearing Loss.

### 4. 总体评价
**67.2/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Tumor necrosis factor receptor superfamily member 25

**功能**: Receptor for TNFSF12/APO3L/TWEAK. Interacts directly with the adapter TRADD. Mediates activation of NF-kappa-B and induces apoptosis. May play a role in regulating lymphocyte homeostasis

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011029 |
| InterPro | IPR000488 |
| InterPro | IPR001368 |
| InterPro | IPR022329 |
| InterPro | IPR034050 |
| Pfam | PF00531 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TNFSF15 | STRING | 999 |
| TRADD | STRING | 994 |
| TNFSF6 | STRING | 991 |
| FASLG | STRING | 991 |
| WDR11 | STRING | 774 |
| NUDT10 | STRING | 755 |
| DAP3 | BioGRID | 1 |
| NOL3 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q93038-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TNFRSF25

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000215788-TNFRSF25

![](https://images.proteinatlas.org/69834/1324_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/69834/1324_B9_9_red_green.jpg)
![](https://images.proteinatlas.org/69834/1356_F11_3_red_green.jpg)
![](https://images.proteinatlas.org/69834/1356_F11_5_red_green.jpg)
![](https://images.proteinatlas.org/69834/1325_B9_4_red_green.jpg)
![](https://images.proteinatlas.org/69834/1325_B9_5_red_green.jpg)

### 深度机制分析

**结构域架构**：TNFRSF25（Tumor necrosis factor receptor superfamily member 25, 417 aa / 45.4 kDa）的主要结构域注释为IPR011029（Death-like domain superfamily）、IPR000488（Death domain）、IPR001368（TNFR/NGFR cysteine-rich region）和IPR022329（TNFR25-specific cysteine-rich domain）、IPR034050（TNFR25 Death domain）。Pfam识别到PF00531（Death domain）和TNFR_c6。该蛋白的pLDDT=72.3（高置信度），已有3个实验PDB结构（Death domain单独解析），但full-length extracellular domain + transmembrane + intracellular domain的全长结构仍待确定。PubMed=97（丰富文献量），研究集中于immune regulation（Treg biology）和inflammatory bowel disease。Actin filaments/Focal adhesion sites/Nucleoplasm (Approved)的三定位模式提示该蛋白具有alternative intracellular trafficking and moonlighting functions beyond classical plasma membrane receptor role。

**PPI互作网络解读**：PPI network（degree=35）——STRING记录的高分互作partner包括TNFSF15（score=999, TL1A, primary ligand）、TRADD（score=994, TNFR1-associated death domain protein, primary adaptor）、TNFSF6/FASLG（score=991, death ligands, cross-talk with CD95 pathway）、WDR11（score=774, WD repeat domain 11, ciliopathy protein）和NUDT10（score=755, nudix hydrolase 10, nucleotide metabolism）。BioGRID记录到DAP3（death associated protein 3, mitochondrial apoptosis）和NOL3（nucleolar protein 3, anti-apoptotic）。TRADD作为primary adaptor是key finding——TRADD bridges TNFRSF25 to downstream NF-kappaB and apoptosis signaling cascades（TRAF2, RIPK1, FADD）。WDR11 interaction linkage to ciliopathy pathway值得关注——可能反映TNFRSF25在primary cilium assembly/function中的作用。

**结构解读**：TNFRSF25的architectural signature为extracellular cysteine-rich domains (CRDs) + intracellular Death domain的双模块：(1) Extracellular CRDs——ligand-binding module, mediate specific recognition of TL1A (TNFSF15) through cysteine-stabilized β-sandwich fold；(2) Intracellular Death domain (DD)——signaling module, upon ligand-induced receptor trimerization, DD recruits TRADD via homotypic DD-DD interaction, initiating two competing outcomes: NF-kappaB activation (pro-survival, via TRAF2/RIPK1) or caspase-8 activation (pro-apoptosis, via FADD)。pLDDT=72.3 with PDB=3 provides high-confidence Death domain structure, but CRD-transmembrane-DD spatial arrangement in the full receptor context remains speculative。

**机制模型**：TNFRSF25的canonical mechanism为plasma membrane receptor-ligand signaling：(1) TL1A binding→receptor trimerization→TRADD recruitment→NF-kappaB or apoptosis。Nucleoplasm localization (Approved)提示alternative mechanism：(2) Nuclear translocation of full-length receptor or proteolytic fragments——similar to NOTCH and other receptors that undergo regulated intramembrane proteolysis (RIP) upon ligand activation releasing intracellular domain (ICD) that translocates to nucleus；(3) TNFRSF25-ICD may function as transcriptional co-regulator——Death domain in nuclear context could interact with nuclear factors through non-classical interfaces。TRADD自身也可在特定条件下translocate到核内参与transcriptional regulation；(4) Actin filament localization提示TNFRSF25可能参与actin dynamics调控，通过cytoskeletal changes间接影响nuclear shape and chromatin organization。

**TE调控展望**：TNFRSF25的TE regulation潜力为indirect inference through NF-kappaB pathway。TE调控关联性取决于：(1) NF-kappaB is a well-characterized transcriptional activator of specific ERV families (HERV-K, HERV-W)——inflammatory signaling through TNFRSF25 could indirectly modulate TE expression via NF-kappaB；(2) TL1A/TNFRSF25 signaling in Treg cells may influence global chromatin landscape including TE silencing through cytokine-mediated epigenetic remodeling；(3) The potential nuclear ICD fragment of TNFRSF25 could directly participate in chromatin-level regulation if the cleavage-and-translocation hypothesis is correct。建议通过：(a) fractionation/IF验证TNFRSF25的nuclear pool是否为full-length or cleaved fragment；(b) TNFRSF25 activation (TL1A stimulation)条件下检测NF-kappaB-dependent ERV expression changes；(c) ChIP-seq with TNFRSF25 antibody评估其genomic binding pattern with annotation to TE loci。

### PubMed

**Count: 344**

| PMID | Title |
|---|---|
| 42364076 | Preclinical development of SL-325, a novel high-affinity DR3-blocking antibody for durable inhibition of the DR3/TL1A axis in inflammatory bowel disea |
| 42313929 | TL1A/DR3 signaling deletion attenuates mucosal inflammation and alveolar bone loss in a murine model of spontaneous periodontitis. |
| 42225083 | Lactylation of lysine396 in TNFRSF25 by lysine acetyltransferase 6B aggravates ferroptosis in metabolic dysfunction-associated steatohepatitis. |
| 42097330 | A high throughput assay to identify modulators of Death Receptor 3 (DR3). |
| 42079644 | Ribosome biogenesis programs define a three-gene RBscore with prognostic relevance in bladder cancer. |


