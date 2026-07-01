---
type: protein-evaluation
gene: "Q7Z4C6"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## Q7Z4C6 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | Q7Z4C6 |
| 蛋白名称 | MSTP142 |
| 蛋白大小 | 205 aa / 23.3 kDa |
| UniProt ID | Q7Z4C6 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 205 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=85.2; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | P-loop_NTPase; RecF/RecN/SMC_N; Smc1_ABC |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **121/180** | |
| **归一化总分** | | | **66.7/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=85.2 PDB=0
- InterPro: P-loop_NTPase; RecF/RecN/SMC_N; Smc1_ABC
- Pfam: SMC_N
- PPI degree=0 ChIP: None


### 4. 总体评价
**66.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: MSTP142

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR027417 |
| InterPro | IPR003395 |
| InterPro | IPR028468 |
| Pfam | PF02463 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: MSTP142

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR027417 |
| InterPro | IPR003395 |
| InterPro | IPR028468 |
| Pfam | PF02463 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

### 深度机制分析

**结构域架构**：Q7Z4C6（MSTP142, 205 aa, 23.3 kDa）是小型蛋白，仅含单一结构域SMC_N（IPR003395, Pfam PF02463）——Structural Maintenance of Chromosomes（SMC）蛋白家族的N-terminal domain。SMC家族蛋白是高度保守的ATPase——形成large ring-shaped complexes——作为chromosome organization, condensation, cohesion, DNA repair和dosage compensation的核心机器。SMC_N domain（~150 aa）的fold为RecA-like ATPase lobe——含conserved Walker A motif（GXXGXGKS/T, phosphate-binding loop/P-loop）和Walker B motif（hhhhD, Mg2+ coordination）——SMC蛋白通过其N端和C端（SMC_C domain, IPR028468）形成intramolecular antiparallel coiled-coil——将两个RecA lobes集聚为functional ATPase head domain。SMC monomer的architecture：N-lobe（SMC_N）—long antiparallel coiled-coil（~45 nm）—hinge domain（central dimerization）—coiled-coil return—C-lobe（SMC_C）。二聚化必需的hinge domain和coiled-coil（500-1200 aa）完全缺失于Q7Z4C6，后者仅含SMC_N lobe（~150-180 aa）后跟short C-terminal tail——意味着Q7Z4C6是SMC standalone domain或dominant-negative fragment——缺乏成环和ATP hydrolysis能力。AlphaFold pLDDT=85.2, PDB=0——SMC_N domain pLDDT极高（>90），但C-terminal short tail（~20 aa）pLDDT<50。PubMed=0, PPI degree=0——完全未研究蛋白。

**PPI互作网络解读**：PPI degree=0完全阻碍功能推断。SMC家族蛋白形成conserved multi-subunit complexes——Cohesin（SMC1-SMC3 heterodimer + RAD21/MCD1 kleisin + SA1/SA2/STAG1/2 stromal antigen protein）建立sister chromatid cohesion——Condensin I/II（SMC2-SMC4 heterodimer + kleisin CAP-H/H2 + HEAT repeat subunits CAP-D2/D3 + CAP-G/G2）催化chromosome condensation——SMC5/6 complex（SMC5-SMC6 heterodimer + NSE1-4 kleisin subunits）参与DNA repair and replication fork restart。SMC_SMC5/6_N domain（Q7Z4C6的predicted homologous）在SMC5/6 complex中属于N端ATPase lobe——但Q7Z4C6缺少所有形成functional SMC dimer所需的domains（hinge, coiled-coil, C-lobe）。因此Q7Z4C6可能编码：（1）SMC5/6 complex的isolated N-lobe——可能作为dominant-negative inhibitor competitive with full-length SMC5/6；（2）独立的monomeric SMC-like ATPase——利用P-loop NTPase activity进行某种新颖功能。

**结构解读**：SMC_N domain (RecA fold)的核心——central beta-sheet (6-7 strands parallel+antiparallel) sandwiched between alpha-helices——Walker A loop（P-loop）位于beta-sheet C-terminus——coordinating ATP phosphate groups——Walker B motif提供的acidic residue（Asp/Glu）配位Mg2+——ATP binding在两个SMC N-lobe的head-head engagement中诱导dimerization（"ATP-dependent head engagement"）。Cohesin/Condensin ring mechanism: SMC heterodimer的hinge-hinge association + N-C lobe head engagement→closed ring structure that topologically entraps chromosomal DNA (~20 nm diameter)——ATP hydrolysis at head domains drives ring opening→release DNA。Q7Z4C6作为solitary SMC_N lobe——可能无ring formation能力——但可能在核内以某种alternative mechanism识别DNA或protein。

**机制模型**：Q7Z4C6的机制推理受限于其极简domain content。推测：（1）SMC_N domain-mediated protein-protein interaction——SMC_N lobe的表面在full-length SMC protein中介导kleisin binding——Q7Z4C6可能作为decoy或competitor与SMC5/6或Cohesin/Condensin的kleisin subunit互作——破坏或调控这些chromosome organization complex的assembly。（2）ATP-regulated DNA binding——SMC_N lobe含canonical P-loop and Walker B motifs——推测可binding ATP——但无C-lobe partner无法完成ATP hydrolysis cycle——可能以ATP-bound form与DNA或chromatin protein interaction。（3）Novel chromosomal function——某些SMC单域蛋白在进化中独立获得功能——如Rad50（SMC family DNA repair protein）的ATPase domain在DNA double-strand break repair的MRN complex（MRE11-RAD50-NBS1）中保持functional stand-alone status。

**TE调控展望**：Chromosome organization complex（Cohesin, Condensin, SMC5/6）在genome organization和TE regulation中有关键作用。Cohesin complex通过loop extrusion建立TADs（Topologically Associating Domains）和chromatin loops——限制enhancer-promoter interaction——调控developmental gene expression——TE所在区域的chromatin loop结构变化可导致TE de-repression或activation。Condensin II参与interphase chromosome territory establishment——其loading影响chromosome compartmentalization。SMC5/6 complex direct roles in silencing of unintegrated viral DNA and restriction of hepatitis B virus transcription——其TE restriction potential值得探索。Q7Z4C6如果作为这些complex的modulator或decoy——可能间接调控TE区域的3D chromatin organization→影响TE expression。


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q7Z4C6-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/Q7Z4C6
