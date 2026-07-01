---
type: protein-evaluation
gene: "NPIPB2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## NPIPB2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | NPIPB2 |
| 蛋白名称 | Nuclear pore complex-interacting protein family member B2 |
| 蛋白大小 | 397 aa / 45.6 kDa |
| UniProt ID | A6NJ64 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 9/10 | ×4 | 36.0 | Nucleoplasm (Approved) |
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 397 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=1 |
| 🏗️ 三维结构 | 4/10 | ×3 | 12.0 | pLDDT=56.0; PDB=0 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | NPIP; NPIP_N |
| 🔗 PPI | 4/10 | ×3 | 12.0 | PPI degree=0 |
| **加权总分** | | | **127/180** | |
| **归一化总分 (÷1.83)** | | | **69.9/100** | 互证: +1 |

### 3. 详细分析

#### 3.1 核定位证据
HPA: Nucleoplasm (Approved)
UniProt: SUBCELLULAR LOCATION: Nucleus {ECO:0000250}.

IF 图像: [Protein Atlas](https://www.proteinatlas.org/)

#### 3.2 蛋白大小
397 aa / 45.6 kDa

#### 3.3 研究现状
PubMed strict=1, broad=1
- PMID 39975192: Structural variation, selection, and diversification of the NPIP gene family from the human pangenome. *bioRxiv : the preprint server for biology*

#### 3.4 三维结构
AF pLDDT=56.0, PDB=0

#### 3.5 结构域
InterPro: NPIP; NPIP_N
Pfam: NPIP
Standard nuclear protein domains

#### 3.6 PPI 互作网络
Combined degree=0

### 4. 总体评价
⭐⭐⭐⭐
**69.9/100** | **nucleoplasm**
Nuclear protein with standard evaluation


### 补充分析 (UniProt API)

**蛋白全称**: Nuclear pore complex-interacting protein family member B2

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR009443 |
| InterPro | IPR054697 |
| Pfam | PF06409 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

### 深度机制分析

**结构域架构**：NPIPB2（397 aa, 45.6 kDa, A6NJ64）是Nuclear Pore Complex-Interacting Protein family member B2——蛋白名称即指示其与核孔复合体（NPC）的功能关联。结构域包含NPIP_N（IPR054697, N端保守域）和NPIP（IPR009443, Pfam PF06409）两个特征domain——两者均为NPIP家族（约20个人类paralog）的保守模块。AlphaFold pLDDT=56.0——中等偏低，无PDB实验结构，暗示蛋白含大量柔性区域。NPIP_N域（~120 aa N-terminal）在序列上高度保守（NPIP家族成员间的amino acid identity >80%）——预测形成mixed a/b globular fold——可能作为NPC结合模块或蛋白-蛋白互作平台。NPIP域（~200 aa）功能未知但高度保守，pLDDT约55-65——暗示其可能处于折叠-无序过渡状态或需要结合partner后发生coupled folding。NPIP家族通过基因复制和结构变异形成了human-specific expanded gene family（PMID:39975192），具有species-specific功能。

**PPI互作网络解读**：PPI degree=0——无检测到的蛋白互作伙伴，但这更可能反映了NPIPB2是高度understudied的黑暗蛋白，而非无互作。NPIP家族的名称直接来自其最初的Y2H筛查中发现与NPC组分（NUP62, NUP98, NUP153等含FG-repeat的nucleoporin）的互作。NPC中约30种nucleoporins——其FG-repeat区域含Phe-Gly dipeptide repeats（如FxFG, GLFG）——形成phase-separated hydrogel-like barrier（选择性通透屏障）——仅允许小于约40 kDa的分子自由扩散；大于此阈值的分子需通过karyopherin-mediated active transport。NPIP家族蛋白可能通过NPIP_N域识别特定的FG-repeat nucleoporin→被tether至NPC cytoplasmic face或nuclear basket→参与核-质转运调控。

**结构解读**：pLDDT=56.0的结构欠佳。NPIP_N域（~aa 1-120）pLDDT中等（60-70），fold为small globular domain（预测为a+beta roll），表面暴露conserved hydrophobic + basic patch——可能是FG-repeat binding site。NPIP域（~aa 130-330）pLDDT低（40-55）——预测为高度无序区域——富含charged残基（Arg/Lys/Glu/Asp）和Ser/Thr——典型IDR组成——可能在NPC中通过multivalent weak interaction与FG-repeat hydrogel互作，影响NPC通透性屏障的局部特性。

**机制模型**：（1）NPC功能调控——NPIPB2定位在NPC（根据UniProt Nucleus annotation）——通过NPIP_N域识别特定FG-repeat nucleoporin（如NUP62在central channel或NUP153在nuclear basket）→插入其IDR domain至FG hydrogel mesh→膨胀或收缩局部FG mesh→改变NPC的通透性和选择性→调控特定cargo（RNA, protein, ribonucleoprotein）的nucleocytoplasmic transport速率。（2）Pangenome结构变异与选择（PMID:39975192）——NPIP基因家族在人类pangenome中的显著结构变异（CNV, segmental duplication, inversion）提示NPIP家族经历了快速的适应性演化——可能与人类特异性的发育、认知或免疫功能相关——NPIPB2的拷贝数变异可能影响NPC运输效率→影响神经或免疫细胞中关键转录因子/RNA的核质分配。

**TE调控展望**：NPIPB2通过NPC功能间接参与TE调控。LINE-1 and ERV RNA需经NPC从核内export至胞质以进行翻译（ORF1p/ORF2p/Gag/Pol/Env）和逆转录转座——NPC export效率直接影响TE RNA的胞质可用性→TE蛋白产量和转座率。NPIPB2可能作为NPC运输的facilitator或restrictor——通过调节FG hydrogel permeability选择性地pass或block TE RNA-核糖核蛋白复合体（RNP）的出核。若NPIPB2限制TE RNP export→TE RNA核内累积→核内TE RNA degradation（exosome/or RNA editing by ADAR）→转座减少。此外，Many antiviral restriction factors（如MX2/MxB, TRIM5a, APOBEC3G）需经NPC进入核内行使功能——NPIPB2可能影响这些restriction factor的nuclear import→间接调控TE defense。NPIP家族作为human-specific expanded gene family可能在人类TE control and genome defense中发挥了species-specific fine-tuning功能。


![PAE](https://alphafold.ebi.ac.uk/files/AF-A6NJ64-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000234719-NPIPB2

![](https://images.proteinatlas.org/53611/826_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/53611/826_D8_2_red_green.jpg)
![](https://images.proteinatlas.org/53611/819_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/53611/819_D8_2_red_green.jpg)
![](https://images.proteinatlas.org/53611/809_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/53611/809_D8_2_red_green.jpg)

### PubMed

**Count: 1**

| PMID | Title |
|---|---|
| 39975192 | Structural variation, selection, and diversification of the NPIP gene family from the human pangenome. |


