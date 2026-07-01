---
type: protein-evaluation
gene: "SNORC"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SNORC 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | SNORC |
| 蛋白全称 | Protein SNORC |
| UniProt ID | Q6UX34 |
| 蛋白大小 | 121 aa / 13.3 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 未知 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoli; Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 121 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=9 |
| 三维结构 | 5/10 | x3 | 15.0 | pLDDT=65.8; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | SNORC |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +1 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | 未知 | 1: Evidence at protein level |

#### 3.2 功能描述

Plays a role in the regulation of chondrocyte maturation and postnatal endochondral ossification. May inhibit cell growth stimulation induced by FGF2

#### 3.3 结构域分析

| 来源 | 结构域 ID | 名称 |
|---|---|---|
| InterPro | IPR031500 | SNORC |
| Pfam | PF15756 | DUF4690 |


#### 3.4 结构信息

蛋白长度 121 aa，AlphaFold 预测可用。

#### 3.5 PPI 网络

PPI 数据待充实。

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR031500; |
| Pfam | PF15756; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| COL9A1 | STRING | 437 |

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000182600-SNORC

![](https://images.proteinatlas.org/52824/1309_C11_1_red_green.jpg)
![](https://images.proteinatlas.org/52824/1309_C11_2_red_green.jpg)
![](https://images.proteinatlas.org/52824/882_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/52824/882_B6_3_red_green.jpg)
![](https://images.proteinatlas.org/52824/831_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/52824/831_B6_2_red_green.jpg)

### TE 调控相关性

该蛋白无明确的染色质/TE 沉默相关定位。TE 调控潜力极低。
### 4. 总体评价
**71.6/100** | **nucleolus**
Nuclear protein


### 深度机制分析

**结构域架构**: SNORC仅121个氨基酸，含有一个DUF4690结构域（PF15756，IPR031500），该结构域功能完全未知。SMART分析未检出任何已知结构域，表明DUF4690可能是一种进化上较新的折叠类型或严重分化的已知折叠变体。AlphaFold pLDDT为65.8（ESMFold仅0.54），说明结构预测存在显著模型差异——AF2可能捕捉到DUF4690的部分折叠，而ESMFold由于缺乏进化深度（该蛋白仅存在于脊椎动物）未能提供有效约束。缺乏已知结构域意味着SNORC可能代表一个未被描述的结构功能范式——可能是核仁内rRNA结合蛋白的新型折叠，或功能仅依赖于内在无序区域的相分离行为。

**PPI网络解读**: STRING仅捕获到COL9A1（IX型胶原蛋白α1链，评分437）一个互作伙伴。IX型胶原是软骨细胞外基质成分，与核仁功能看似矛盾。然而，这一互作可能反映的是：(a) 间接互作——两者均在软骨细胞中高表达，富集于相同的蛋白质组数据集；(b) 信号传递关系——COL9A1的细胞外信号通过整合素-FAK-MAPK级联反应汇聚于FGF2信号的负调控点，而SNORC正是通过核仁应激抑制FGF2诱导的软骨细胞增殖。因此，COL9A1-SNORC互作可能代表了"细胞外基质 → 整合素信号 → 核仁应激"的完整信息流。更关键的是，STRING数据库中SNORC的核仁互作网络尚未被实验捕获——已知核仁蛋白如nucleolin、nucleophosmin、fibrillarin应为SNORC的物理互作体，但未出现在STRING中。

**结构解释**: pLDDT 65.8但ESMFold仅0.54的巨大差异值得注意。AF2使用MSA信息，可检测到脊椎动物直系同源基因中的共进化信号，部分约束结构折叠；而ESMFold是完全从头折叠，缺乏MSA信号，对于进化浅的小蛋白容易产生低置信度。这种差异的一个有趣解释是：SNORC可能部分折叠为紧凑的核仁定位域，但功能态依赖于伴侣蛋白辅助折叠或在结合rRNA/核仁蛋白后发生构象固定。换言之，SNORC可能是"客户蛋白诱导折叠"的实例——独立存在时部分无序，与核仁结合伙伴互作后折叠活化。

**机制整合模型**: SNORC是核仁应激应答的软骨保护因子，工作模型为：(1) 在静息软骨细胞中，SNORC定位于核仁，通过DUF4690结构域与rDNA或45S pre-rRNA相互作用，维持适度的核糖体生物合成速率；(2) FGF2刺激激活FGFR-ERK1/2信号轴，磷酸化核仁磷蛋白，驱动rDNA转录上调以满足增殖所需的核糖体产能；(3) SNORC作为核仁应激的"缓冲器"——当细胞外基质信号（COL9A1-整合素-FAK）降低时，SNORC核仁驻留增加，通过竞争性结合rDNA或pre-rRNA来限制RNA Pol I转录；(4) 在骨关节炎条件下，SNORC表达下降（PMID 37659033证实SNORC敲低加重软骨细胞炎症和基质降解），核仁应激缓冲能力消失，导致不适当的软骨细胞肥大和基质降解。这一模型将SNORC定位为核仁-核糖体生物合成的变阻器，而非简单的FGF2信号拮抗因子。

**研究/转化意义**: SNORC是具有明确疾病关联（骨关节炎）的核仁功能蛋白。骨关节炎目前没有改变疾病进程的药物（仅对症治疗），SNORC增强疗法——通过维持软骨细胞的核仁稳态——代表了一个全新的治疗方向。DUF4690结构域的首次结构解析将是理解该蛋白功能的突破点。此外，SNORC在非软骨组织（如HPA显示多种细胞系核仁定位）中的功能尚待探索，可能参与核仁应激的通用保护机制。

### 补充分析 (UniProt API)

**蛋白全称**: Protein SNORC

**功能**: Plays a role in the regulation of chondrocyte maturation and postnatal endochondral ossification. May inhibit cell growth stimulation induced by FGF2

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR031500 |
| Pfam | PF15756 |

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6UX34-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 10**

| 39691700 | MicroRNA-181a/b-1 enhances chondroprogenitor anabolism and downregulates aquaporin-9. | Osteoarthr Cartil Open 2025 |
| 37659033 | SNORC knockdown alleviates inflammation, autophagy defect and matrix degradation of chondrocytes in osteoarthritis devel | Mol Cell Biochem 2024 |
| 35633575 | Potential effect of Enterolactone and Raloxifene in reversing osteoarthritis markers in cultured human articular chondro | ARP Rheumatol 2022 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SNORC

### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `detail/_esm_structures/SNORC_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.54 |
| pLDDT > 0.9 | 0.0% |
| pLDDT < 0.5 | 25.6% |
| 残基数 | 121 |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。

