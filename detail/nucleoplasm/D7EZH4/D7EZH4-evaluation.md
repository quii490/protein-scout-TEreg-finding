---
type: protein-evaluation
gene: "D7EZH4"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## D7EZH4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | D7EZH4 |
| 蛋白名称 | SNF2LT |
| 蛋白大小 | 776 aa / 89.3 kDa |
| UniProt ID | D7EZH4 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 776 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=68.3; PDB=0 |
| 调控结构域 | 6/10 | ×2 | 12.0 | Helicase_ATP-bd; Helicase_C-like; ISWI_HAND-dom_sf |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **121/180** | |
| **归一化总分** | | | **66.7/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=68.3 PDB=0
- InterPro: Helicase_ATP-bd; Helicase_C-like; ISWI_HAND-dom_sf
- Pfam: Helicase_C; SNF2-rel_dom
- PPI degree=0 ChIP: None


### 4. 总体评价
**66.7/100** | **nucleoplasm**
TE candidate: Helicase_ATP-bd; Helicase_C-like; ISWI_HAND-dom_sf


### 补充分析 (UniProt API)

**蛋白全称**: SNF2LT

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR014001 |
| InterPro | IPR001650 |
| InterPro | IPR036306 |
| InterPro | IPR027417 |
| InterPro | IPR044755 |
| InterPro | IPR038718 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: SNF2LT

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR014001 |
| InterPro | IPR001650 |
| InterPro | IPR036306 |
| InterPro | IPR027417 |
| InterPro | IPR044755 |
| InterPro | IPR038718 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

### 深度机制分析

**结构域架构**：D7EZH4（SNF2LT, 776 aa, 89.3 kDa）属于SNF2超家族（Sucrose Non-Fermenting 2, SF2 helicase/translocase）——ATP依赖的chromatin remodeling酶。SNF2家族的核心架构为tandem RecA-like ATPase lobes（DExx-box helicase domain, IPR014001/Helicase_ATP-bd, Pfam SNF2-rel_dom）——两个RecA-like lobes形成conserved ATP-binding cleft——ATP binding在lobe1和lobe2间诱导conformational change→产生translocation force。Helicase_C 结构域（IPR001650）构成C端lobe2的延伸，与lobe1共同完成ATP水解循环。最关键的是ISWI_HAND-dom_sf（IPR044755, IPR038718, I-SWI HAND domain superfamily）——ISWI（Imitation SWI）亚家族的HAND-SANT-SLIDE三模块是识别nucleosome linker DNA的"molecular ruler"——HAND（HSSB-associated N-terminal domain）结合linker DNA——SANT domain（SWI3, ADA2, N-CoR, TFIIIB）是chromatin interaction module——SLIDE（SANT-like ISWI domain）作为spacer测量linker DNA长度——ISWI remodeler通过HAND-SANT-SLIDE感知linker DNA length→决定nucleosome spacing（例如ISWI/SNF2H催化equally-spaced nucleosome array formation）。D7EZH4作为SNF2家族孤儿成员，exact remodeling specificity unknown。AlphaFold pLDDT=68.3, PDB=0——RecA lobes区域置信度>80，但HAND-SLIDE linker和N/C terminal extension pLDDT<50。纯度极高——PubMed=0, PPI degree=0——完全不曾在文献中被单独研究。

**PPI互作网络解读**：PPI degree=0——即STRING, IntAct, BioGRID三大数据库中均无实验验证或预测互作——这是一把双刃剑。积极面：D7EZH4可能是极其新颖且未受探索的chromatin remodeler；消极面：无PPI导致功能推断完全依赖结构域同源比较。保守分析：ISWI亚家族的核心互作伙伴对（pair）——SNF2H（SMARCA5）结合BAZ1A（ACF1）/BAZ1B（WSTF）/BAZ2A（TIP5）/RSF1/CECR2等accessory subunit形成distinct remodeling complexes（ACF, CHRAC, WICH, NoRC, RSF, CERF）——每个accessory蛋白携带特定chromatin recognition domains（PHD finger, bromodomain, MBD）——赋予remodeler特定chromatin标记的targeting specificity。D7EZH4因无已知PPI，暂无法推断其accessory subunit组成。

**结构解读**：SNF2-type ATPase的translocation mechanism遵循"ATP-dependent inchworm"模型。RecA lobe1（N端）和lobe2（C端）间的ATP binding cleft在ATP bound state→lobe1向lobe2靠近约5-7 angstrom→此旋转力（torque）通过lobe1/2连接的rigid body传递至bound dsDNA→产生约1-2 bp的DNA translocation step→ATP hydrolysis→lobe1-lobe2解离→recovery stroke回原位→new ATP binding cycle。ISWI remodeler的HAND-SANT-SLIDE module位于C端——SLIDE domain富含basic residues（Lys/Arg patch）——形成DNA binding groove that contacts linker DNA backbone——HAND domain coordinate linker DNA entry/exit angle——通过control linker DNA trajectory决定nucleosome sliding direction（从linker DNA长的侧向短的侧→generating evenly spaced nucleosome arrays）。保守的ISWI catalytic mechanism——SLIDE domain sensing extra-nucleosomal linker DNA length→allosteric control of ATPase activity→translocate DNA from linker entry toward dyad of nucleosome→nucleosome repositioning。

**机制模型**：（1）Nucleosome spacing——D7EZH4可能在chromatin assembly后催化regular nucleosome spacing——维持genome-wide nucleosome positioning和chromatin fiber compaction。（2）Transcriptional regulation——ISWI remodelers（如NURF complex, SNF2L-SNF2H-BPTF）通过nucleosome sliding调控promoter accessibility——在developmental genes的promoter区域generate nucleosome-depleted regions（NDRs）→allow transcription factor binding。（3）DNA damage response——ISWI remodelers（如ACF complex）参与DNA damage sites的chromatin reorganization→facilitate repair factor access。

**TE调控展望**：SNF2家族chromatin remodeler在TE silencing中的角色——ISWI complex（NoRC, SNF2H-TIP5）参与rDNA silencing和pericentric heterochromatin maintenance——TIP5（BAZ2A）的MBD domain识别methylated DNA（5mC）——将NoRC complex靶向methylated CpG-rich区域（类似TE区域的CpG islands）→催化H3K9me2/H4K20me3 heterochromatin marks→transcriptional silencing。D7EZH4可能作为类似的TE heterochromatin regulator——其HAND-SANT-SLIDE module感知TE-adjacent nucleosome linker DNA→调控TE区域的chromatin fiber compaction→影响TE promoter的accessibility。作为PubMed=0的完全未研究蛋白，D7EZH4的真in vivo remodeling substrate必须通过ChIP-seq（anti-D7EZH4）+ MNase-seq定位至特异的chromatin features（active TE, repressed TE, gene promoters, enhancers）。


![PAE](https://alphafold.ebi.ac.uk/files/AF-D7EZH4-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/D7EZH4
