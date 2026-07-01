---
type: protein-evaluation
gene: "C11orf24"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## C11orf24

### 1. Basic Info
| Item | Value |
|---|---|
| Gene | C11orf24 |
| Protein Name | Uncharacterized protein C11orf24 |
| Size | 449 aa / 46.1 kDa |
| UniProt | Q96F05 |
| Date | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | Golgi apparatus; Nucleoplasm; Vesicles (Approved) |
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 449 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=3 |
| 🏗️ 三维结构 | 4/10 | ×3 | 12.0 | pLDDT=51.5; PDB=0 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | DUF5585; Erythrocyte_Invasion_ImmMod |
| 🔗 PPI | 5/10 | ×3 | 15.0 | PPI degree=14 |
| **加权总分** | | | **130.0/180** | |
| **归一化总分 (÷1.83)** | | | **71.0/100** | 互证: +2.0 |

### 3. Analysis
- HPA: Golgi apparatus; Nucleoplasm; Vesicles (Approved)
- PubMed: strict=3, broad=3
- AF pLDDT: 51.5 / PDB: 0
- InterPro: DUF5585; Erythrocyte_Invasion_ImmMod
- Pfam: DUF5585
- PPI degree=14 ChIP: None
24312644: C11ORF24 is a novel type I membrane protein that cycles between the Golgi appara | 40285634: The C11orf24 Gene as a Useful Biomarker for Predicting Severe Neutropenia in Mod | 11401438: The sequence and gene characterization of a 400-kb candidate region for IDDM4 on

### 4. Assessment
★★★★  **72.1/100**  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Uncharacterized protein C11orf24

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR041056 |
| InterPro | IPR052660 |
| Pfam | PF17823 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| VAT1L | BioGRID | 0 |
| RNF166 | BioGRID | 0 |
| NME2P1 | BioGRID | 0 |
| VWA1 | BioGRID | 0 |
| LMNA | BioGRID | 0 |
| RNF123 | BioGRID | 0 |
| APEX1 | BioGRID | 0 |
| FAM209A | BioGRID | 0 |


### 深度机制分析

**结构域架构**：C11orf24（449 aa, 46.1 kDa）含DUF5585（Pfam PF17823, IPR041056）和Erythrocyte_Invasion_ImmMod（IPR052660）两个结构域。AlphaFold pLDDT=51.5，约70%残基pLDDT<70，表明蛋白整体处于折叠-无序过渡区。DUF5585域（domain of unknown function 5585）为约120 aa的预测球形折叠单元，但其低pLDDT提示在生理条件下以动态"熔球态"（molten globule）存在而非刚性折叠。Erythrocyte_Invasion_ImmMod域在恶性疟原虫（Plasmodium falciparum）裂殖子入侵红细胞阶段被注释为免疫调节模块（PfEMP1-like），但在人类蛋白中的功能完全未知。蛋白序列富含Leu（~12%）和Ser（~10%），Isoelectric point（pI）~6.5，两亲性特征提示膜结合倾向——与PMID 24312644报道的I型跨膜蛋白定位一致。

**PPI互作网络解读**：PPI network（degree=14, BioGRID）指示C11orf24参与核质-高尔基体膜交通调控。LMNA（lamin A/C, BioGRID）为核纤层（nuclear lamina）中间丝蛋白——通过其coiled-coil rod domain和Ig-fold尾部形成核膜下层的10 nm纤维网络，维持核膜机械稳定性和染色质锚定。C11orf24-LMNA互作暗示C11orf24在核膜-Golgi膜接触位点（membrane contact sites, MCS）参与ER-Golgi-核膜的膜系统连续性维持。APEX1（AP endonuclease 1, BioGRID, DNA修复酶）参与碱基切除修复（BER）——作为apurinic/apyrimidinic endonuclease在无嘌呤/无嘧啶位点裂解DNA主链——C11orf24可能作为APEX1的核内支架辅助其染色质招募。RNF166和RNF123（RING finger E3 ubiquitin ligases, BioGRID）为泛素化酶——提示C11orf24经泛素-蛋白酶体系统（UPS）调控其稳定性和亚细胞定位，尤其在Golgi-核膜间循环中。

**机制模型**：C11orf24为Rab6阳性高尔基体后囊泡的膜蛋白（PMID 24312644），在Golgi apparatus和plasma membrane之间以Rab6 GTPase依赖的方式循环。在核质中，C11orf24可能通过其DUF5585域与LMNA核纤层相互作用→锚定Golgi来源囊泡在核膜外侧→促进膜脂质/胆固醇向内核膜的运输→影响核膜脂筏（lipid raft）组织和核孔复合体（NPC）功能。在化疗诱导的中性粒细胞减少症中（PMID 40285634），C11orf24表达作为mFOLFIRINOX方案（胰腺癌）的严重中性粒细胞减少症的生物标志物——提示其在造血细胞（中性粒前体）的Golgi应激和分泌颗粒形成中的潜在角色。

**TE调控展望**：C11orf24对TE调控的关联较弱且间接。LMNA在核膜下形成转录沉默区（lamin-associated domains, LADs）——富含LINE-1/LTR逆转录转座子的基因组区域优先锚定在核纤层LAD上以维持转录沉默。C11orf24-LMNA互作可能影响LAD区域的染色质组织和TE沉默——C11orf24在高尔基体-核膜接触位点的膜运输功能调控核纤层脂质环境和LAD完整性→间接影响TE的核内空间定位和转录沉默状态。APEX1在DNA修复中通过BER处理逆转录转座介导的单链断裂（SSB）和脱嘌呤位点——C11orf24作为APEX1的核支架可能影响TE转座产生的DNA损伤修复效率。不过C11orf24的低研究度和DUF5585的未知功能使这些推论高度投机。



### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000171067-C11orf24

![](https://images.proteinatlas.org/12411/1966_A11_1_red_green.jpg)
![](https://images.proteinatlas.org/12411/1966_A11_2_red_green.jpg)
![](https://images.proteinatlas.org/12411/1898_A5_31_red_green.jpg)
![](https://images.proteinatlas.org/12411/1898_A5_32_red_green.jpg)
![](https://images.proteinatlas.org/12411/1901_C14_1_red_green.jpg)
![](https://images.proteinatlas.org/12411/1901_C14_4_red_green.jpg)

### PubMed 文献

**PubMed count: 3**

| 40285634 | The C11orf24 Gene as a Useful Biomarker for Predicting Severe Neutropenia in Modified FOLFIRINOX for Pancreatic Cancer. | Cancer Sci 2025 |
| 24312644 | C11ORF24 is a novel type I membrane protein that cycles between the Golgi apparatus and the plasma membrane in Rab6-posi | PLoS One 2013 |
| 11401438 | The sequence and gene characterization of a 400-kb candidate region for IDDM4 on chromosome 11q13. | Genomics 2001 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/C11orf24

